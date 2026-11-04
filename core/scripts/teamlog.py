#!/usr/bin/env python3
"""Build, check and mirror team-log records (core/team-logs/TEAM-LOGS.md §6). Never calls the network: it writes JSON files
under <job>/teamlog/ that Claude then sends with ArtifactData (`file_path` = the printed path), so every record is checked
first and a local copy stays in the job folder.

  teamlog.py gen   <job> --run-id R --ad-id A --product P --model M --prompt-file F [--ref-type T --ref-id I] [--refs a,b]
                   [--cost-creatify N] [--cost-higgsfield N] [--ratio 9:16] [--resolution 720p] [--setup k=v ...] [--ask "..."]
                   [--retake-of <doc_id of the take it replaces>] [--edited-by-user]  (the operator rewrote the prompt themselves)
                   [--headline "..." (images) | --hook "<opening spoken line>" (videos)] [--cta "..."]   the copy this take carries
                   → copies the exact prompt to <job>/prompts/NN.txt, writes gen-<run>-NN.json (call it when the job is SUBMITTED)
  teamlog.py qa    <job> <doc_id> --pass | --fail [--reason "..."] [--result-file out/raw.mp4]
  teamlog.py tool  <job> <doc_id> --file F --source "<the read call>"   what the TOOL actually ran (an expanded prompt, a
                   script, concepts, a revised prompt), read back after the job; saved next to our prompt as prompts/NN_tool.txt
  teamlog.py note  <job> <doc_id> --ask "<the operator's own words>"   feedback or a change request on that generation
                   ("make it slower", "script makes 0 sense"); the next take is logged with --retake-of <doc_id> --ask "<same words>"
  teamlog.py copy  <job> --run-id R --ad-id A --product P --kind image|video [--ad "label"] [--audience men]
                   → builds the copy record from <job>/copy.json, premium.json (captions) and phrases.json, labels every line
                     against the product's bible pre-screen and the global Hard NOs; refuses a banned line
  teamlog.py proof <job> --run-id R --ad-id A --product P --kind image|video --proof trust|count|none
  teamlog.py run   <job> --run-id R --product P --format images|video|avatar|still --captions yes|no
                   (started_at = the run's first logged generation, automatically; never typed)
                   [--creatify-before N --creatify-after N] [--higgsfield-before N --higgsfield-after N] [--notes "..."]
                   → made / finished / rerolled / spent come from the gen records in <job>/teamlog/
  teamlog.py check <file.json> ...      validate records (exit 1 on an error)
  teamlog.py close <job>                closing check before SESSION.md: every gen has QA and a prompt file, every finished ad has
                                        copy + proof, a run record exists and agrees with the gens (exit 1 on an error)
"""
import argparse, datetime, glob, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = [os.path.expanduser(os.environ.get("EVERLIFE_SKILLS_DIR", "~/.claude/skills")),
          os.path.normpath(os.path.join(HERE, "..", "..", "skills"))]
# Routes that rewrite or expand what we send: their gen records should carry tool_prompt (TEAM-LOGS §6).
EXPANDS = re.compile(r"marketing[_ -]?studio|ads[_ -]?studio|composer|ad[_ -]?agent|ugc", re.I)
# The page each record type goes to (TEAM-LOGS.md table). Printed with every record so it is never sent to the wrong page.
PAGES = {"gen": ("Prompt & Outcome Log", "https://claude.ai/artifact/YALbdpQKrMMfZzA9mr32Y2"),
         "copy": ("Copy Ledger", "https://claude.ai/artifact/4acQzvt2mZ592jU45RLB9o"),
         "proof": ("Copy Ledger", "https://claude.ai/artifact/4acQzvt2mZ592jU45RLB9o"),
         "style": ("Copy Ledger", "https://claude.ai/artifact/4acQzvt2mZ592jU45RLB9o"),
         "run": ("Activity & Spend Log", "https://claude.ai/artifact/R2GqUTb8pKbSniNmjGqBre")}
REF_TYPES = {"board_winner", "meta_winner", "own_ad", "style_board", "hardcore_ref", "product_example", "outside", "hook_engine", "none"}
LINE_KINDS = {"headline", "hook", "vo", "caption", "benefit", "end_head", "cta", "offer"}
SPOKEN = {"hook", "vo", "caption"}
NO_REFS_OK = re.compile(r"lyria|music|voice|tts|animate_code", re.I)

# Global Hard NOs a line can be checked for mechanically (CLAUDE.md gates §2-3; bible 2026-11-03). (pattern, why, video_only)
BANNED = [
    (r"\bget started now\b", "\"Get Started Now\" is banned as a CTA (bible 2026-11-03): lead with the offer", False),
    (r"\b(i|i'm|i've|i'd|i'll|me|my|mine|myself)\b", "first person is a Hard NO (\"I tried\", \"my results\")", False),
    (r"\bneedles?\b|needle-free", "never mention needles, including \"needle-free\"", False),
    (r"\bGH\b", "spell out \"growth hormone\", never \"GH\"", False),
    (r"ghk-cu|copper peptide", "creative says \"GHK\", never \"GHK-Cu\" / \"copper peptide\" (H2 product name only)", False),
    (r"\b(melt\w*|burn\w*|ripped|shred\w*)\b", "no melt / burn / ripped / shred", False),
    (r"\barousal|aroused|arousing\b", "never \"arousal\" or any form of it", False),
    (r"\ball[- ]natural\b", "never \"all natural\" for a sublingual", False),
    (r"\bclinically (studied|backed|proven)\b", "\"clinically studied/backed\" only for a named ingredient", False),
    (r"\b(cure|cures|treats?|prevents?)\b", "no disease claims (cure / treat / prevent)", False),
    (r"trustpilot rating", "Trustpilot reads exactly \"Trustpilot rated 4.9 Excellent\"", False),
    (r"\bbreaking news\b", "no \"Breaking News\" framing", False),
    (r"\b(after|over|past|at|turning|under)\s+\d{2}\b|\b\d{2}\s*(\+|plus|years?|yrs?)\b|\b(twenty|thirty|forty|fifty|sixty|seventy)(-\w+)?\b",
     "no specific ages in video scripts or captions (team video rules, 2026-11-03)", True),
]
WARN = [
    (r"\bare you\b", "second-person health question with a pronoun? (pronoun-free questions are fine)"),
    (r"\bbuilds\b", "say \"supports\", never \"builds\""),
    (r"\bboosts?\b", "\"boost\" reads as an outcome claim: prefer \"supports\""),
    (r"\bguarantee", "no guaranteed outcomes"),
]


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return " ".join(re.sub(r"[^a-z0-9%+' ]+", " ", t.lower()).split())


def product_bible(product):
    for root in SKILLS:
        p = os.path.join(root, f"everlife-{product}", "references", "product-bible.md")
        if os.path.exists(p):
            return open(p, encoding="utf-8").read()
    return None


def screen(product):
    """{normalized line: status} from the product-bible pre-screen tables (❌ / ⚠ / ⏳ / ✅) plus the verbatim block."""
    md = product_bible(product)
    if md is None:
        return None, set()
    status = {}
    for row in md.splitlines():
        if not row.startswith("|") or row.startswith("|---"):
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        st = next((c for c in cells if any(m in c for m in ("❌", "⛔", "⚠", "⏳", "✅"))), None)
        if not st:
            continue
        s = "no" if ("❌" in st or "⛔" in st) else "hold" if ("⚠" in st or "⏳" in st) else "ok"
        for c in cells:
            if c is st or not c:
                continue
            for item in re.split(r"\s·\s|\s•\s", re.sub(r"^CTA:\s*", "", c)):
                n = norm(item.strip(' "*'))
                if len(n.split()) >= 2 and n not in status:
                    status[n] = s
    verbatim = set()   # any line of the extract (its verbatim bible copy); the pre-screen statuses above win over it
    for ln in md.splitlines():
        n = norm(re.sub(r"^[-—•\s]*(CTA:)?", "", ln))
        if len(n.split()) >= 2:
            verbatim.add(n)
    return status, verbatim


def label_line(text, kind, product, media):
    """→ (source label, [errors], [warnings]) for one line of copy."""
    errs, warns = [], []
    low = text.lower().replace("’", "'")
    for pat, why, video_only in BANNED:
        if video_only and not (media == "video" and kind in SPOKEN | {"headline", "end_head"}):
            continue
        if re.search(pat, text if pat == r"\bGH\b" else low):
            errs.append(why)
    if errs:
        return "❌ banned", errs, warns
    status, verbatim = screen(product)
    if status is None:
        warns.append(f"no product-bible.md found for '{product}': label unchecked")
        return "unchecked", errs, warns
    n = norm(text)
    hit = status.get(n) or next((s for k, s in status.items() if len(k.split()) >= 4 and (k in n or (len(n.split()) >= 4 and n in k))), None)
    if hit == "no":
        errs.append("marked ❌ in this product's pre-screen")
        return "❌ pre-screen", errs, warns
    if hit == "hold":
        warns.append("⚠/⏳ in the pre-screen: needs an explicit OK, flag for Jeremy")
        return "⏳ needs approval", errs, warns
    if hit == "ok" or n in verbatim:
        return "bible ✅", errs, warns
    warns += [why for pat, why in WARN if re.search(pat, low)]   # only fresh wording gets the softer warnings
    return "Tier B proposed", errs, warns


# ---------- record checks ----------
def is_iso(v):
    return isinstance(v, str) and bool(re.match(r"\d{4}-\d\d-\d\dT\d\d:\d\d", v))


def check(rec):
    """→ (errors, warnings) for one record."""
    E, W = [], []
    t = rec.get("type")
    need = {"run": ["run_id", "product", "format", "made", "finished", "rerolled", "credits", "started_at", "ended_at", "out_dir"],
            "gen": ["run_id", "ad_id", "product", "created_at", "model", "prompt", "ref", "qa", "cost"],
            "copy": ["run_id", "ad_id", "product", "date", "lines"],
            "proof": ["run_id", "ad_id", "product", "kind", "proof", "date"],
            "style": ["run_id", "product", "date", "styles"]}.get(t)
    if need is None:
        return [f"unknown type {t!r}"], W
    for k in need:
        if rec.get(k) in (None, "", [], {}):
            E.append(f"{t}: '{k}' is missing")
    bf = rec.get("backfill")
    if t == "run":
        for k in ("started_at", "ended_at"):
            if rec.get(k) and not is_iso(rec[k]):
                (W if bf else E).append(f"run: '{k}' must be an ISO time (2026-11-03T14:05:00-05:00), not {rec[k]!r}")
        if is_iso(rec.get("started_at")) and is_iso(rec.get("ended_at")):
            try:
                if datetime.datetime.fromisoformat(rec["started_at"]) > datetime.datetime.fromisoformat(rec["ended_at"]):
                    (W if bf else E).append(f"run: started_at {rec['started_at']} is after ended_at {rec['ended_at']}")
            except ValueError:
                pass
        if rec.get("format") in ("video", "avatar", "still") and rec.get("captions") is None:
            E.append("run: 'captions' (true/false) is required for video")
        if rec.get("captions") is False and rec.get("format") in ("video", "avatar"):
            W.append("run: captions = false: the bible requires on-screen captions on every video (Standards 02)")
        cr = rec.get("credits", {})
        for tool in ("creatify", "higgsfield"):
            c = cr.get(tool, {})
            if c.get("before") is None and c.get("spent"):
                W.append(f"run: {tool} balance before/after unknown (spent = sum of charges)")
    elif t == "gen":
        if rec.get("created_at") and not is_iso(rec["created_at"]):
            (W if bf else E).append(f"gen: 'created_at' must be an ISO time, not {rec['created_at']!r}")
        p = rec.get("prompt", "")
        if p.startswith("BACKFILL") or "not saved" in p:
            (W if bf else E).append("gen: 'prompt' is a summary, not the exact text sent")
        if not rec.get("prompt_file"):
            (W if bf else E).append("gen: 'prompt_file' missing (save the exact prompt with `teamlog.py gen`)")
        ref = rec.get("ref") or {}
        if ref.get("type") not in REF_TYPES:
            E.append(f"gen: ref.type {ref.get('type')!r} is not one of {sorted(REF_TYPES)}")
        if ref.get("type") == "outside" and re.search(r"everlife|sermorelin|restora|wolverine|spartan|base\d+|_video_|_static_", str(ref.get("id", "")), re.I):
            W.append("gen: ref looks like an earlier Everlife ad: use ref.type 'own_ad' (or 'meta_winner' if it is CPA-ranked)")
        if not rec.get("refs") and not NO_REFS_OK.search(rec.get("model", "")):
            W.append("gen: 'refs' is empty: list the product render / start frame / reference files attached")
        qa = rec.get("qa") or {}
        if EXPANDS.search(rec.get("model", "")) and qa.get("pass") is not None and not rec.get("tool_prompt"):
            W.append("gen: this tool writes its own prompt/script: read it back and save it (`teamlog.py tool`)")
        cp = rec.get("copy") or {}
        if not (cp.get("headline") or cp.get("hook")) and not NO_REFS_OK.search(rec.get("model", "")):
            W.append("gen: no headline / hook on this take (--headline for images, --hook for videos; `teamlog.py copy` fills it after the batch)")
        if qa.get("pass") is None:
            W.append("gen: QA not recorded yet (update it with `teamlog.py qa`)")
    elif t == "copy":
        kinds = set()
        for ln in rec.get("lines", []):
            kinds.add(ln.get("kind"))
            if ln.get("kind") not in LINE_KINDS:
                E.append(f"copy: line kind {ln.get('kind')!r} is not one of {sorted(LINE_KINDS)}")
            src, e, w = label_line(ln.get("text", ""), ln.get("kind"), rec.get("product", ""), rec.get("media", "image"))
            E += [f"copy: \"{ln.get('text')}\": {x}" for x in e]
            W += [f"copy: \"{ln.get('text')}\": {x}" for x in w]
            if ln.get("source") and src != "unchecked" and ln["source"] != src and not (src == "Tier B proposed" and "⏳" in ln["source"]):
                W.append(f"copy: \"{ln.get('text')}\" is labelled {ln['source']!r} but checks as {src!r}")
        if not kinds & {"cta", "offer"}:
            W.append("copy: no cta / offer line: every ad ends on a clear CTA")
    elif t == "proof":
        if rec.get("proof") not in ("trust", "count", "none"):
            E.append(f"proof: {rec.get('proof')!r} is not trust / count / none")
    return E, W


# ---------- files ----------
def tdir(job):
    d = os.path.join(job, "teamlog")
    os.makedirs(d, exist_ok=True)
    return d


def write(job, doc_id, rec):
    E, W = check(rec)
    path = os.path.join(tdir(job), doc_id + ".json")
    json.dump(rec, open(path, "w"), ensure_ascii=False, indent=1)
    for w in W:
        print("⚠", w)
    for e in E:
        print("❌", e)
    page = PAGES.get(rec.get("type"), ("?", "?"))
    print(("❌ NOT READY: fix the errors, then run again" if E else "✅ ready") + f"\n  doc_id: {doc_id}\n  file:   {path}"
          + f"\n  send to: {page[0]} ({page[1]}), collection data/users/me, doc_id {doc_id}")
    return 1 if E else 0


def records(job):
    return {os.path.basename(f)[:-5]: json.load(open(f)) for f in sorted(glob.glob(os.path.join(job, "teamlog", "*.json")))}


def kv(pairs):
    out = {}
    for p in pairs or []:
        k, _, v = p.partition("=")
        out[k.strip()] = v.strip()
    return out


def cmd_gen(a):
    pd = os.path.join(a.job, "prompts")
    os.makedirs(pd, exist_ok=True)
    n = len([r for r in records(a.job).values() if r.get("type") == "gen" and r.get("run_id") == a.run_id]) + 1
    text = open(a.prompt_file, encoding="utf-8").read()
    if not text.strip():
        sys.exit("❌ the prompt file is empty")
    pf = os.path.join(pd, f"{n:02d}_{re.sub(r'[^A-Za-z0-9.-]+', '-', a.model)[:40]}.txt")
    if os.path.abspath(a.prompt_file) != os.path.abspath(pf):
        shutil.copyfile(a.prompt_file, pf)
    rec = {"type": "gen", "run_id": a.run_id, "ad_id": a.ad_id, "product": a.product, "created_at": now(), "model": a.model,
           "prompt": text, "prompt_file": os.path.relpath(pf, a.job), "refs": [r for r in (a.refs or "").split(",") if r],
           "ref": {"type": a.ref_type, "id": a.ref_id or ""}, "reference": a.ref_id or "", "setup": kv(a.setup), "asks": a.ask or [],
           "settings": {"ratio": a.ratio, "resolution": a.resolution},
           "copy": {k: v for k, v in (("headline", a.headline), ("hook", a.hook), ("cta", a.cta)) if v}, "result_file": "",
           "qa": {"pass": None, "reasons": []}, "rerolls": 0, "retake_of": a.retake_of or "",
           "prompt_by": "operator" if a.edited_by_user else "claude", "feedback": [],
           "cost": {"creatify": a.cost_creatify, "higgsfield": a.cost_higgsfield}}
    rc = write(a.job, f"gen-{a.run_id}-{n:02d}", rec)
    # The Stop hook (core/hooks/teamlog_hook.py) compares this index with the paid calls it captured in the session.
    idx = os.path.expanduser(os.environ.get("EVERLIFE_CREATIVE", "~/Everlife-Creative"))
    os.makedirs(idx, exist_ok=True)
    with open(os.path.join(idx, "teamlog-index.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps({"at": now(), "doc_id": f"gen-{a.run_id}-{n:02d}", "job": os.path.abspath(a.job), "model": a.model}) + "\n")
    return rc


def cmd_note(a):
    path = os.path.join(a.job, "teamlog", a.doc_id + ".json")
    rec = json.load(open(path))
    rec.setdefault("feedback", []).extend({"at": now(), "text": t} for t in a.ask)
    return write(a.job, a.doc_id, rec)


def cmd_tool(a):
    path = os.path.join(a.job, "teamlog", a.doc_id + ".json")
    rec = json.load(open(path))
    text = open(a.file, encoding="utf-8").read()
    if not text.strip():
        sys.exit("❌ the file is empty: if the tool returned nothing, say so with --none instead")
    pf = os.path.join(a.job, rec.get("prompt_file") or f"prompts/{a.doc_id}.txt")
    tf = re.sub(r"\.txt$", "", pf) + "_tool.txt"
    os.makedirs(os.path.dirname(tf), exist_ok=True)
    if os.path.abspath(a.file) != os.path.abspath(tf):
        shutil.copyfile(a.file, tf)
    rec.update({"tool_prompt": text, "tool_prompt_file": os.path.relpath(tf, a.job), "tool_prompt_source": a.source or ""})
    return write(a.job, a.doc_id, rec)


def cmd_tool_none(a):
    path = os.path.join(a.job, "teamlog", a.doc_id + ".json")
    rec = json.load(open(path))
    rec.update({"tool_prompt": "(the tool returned no expanded prompt)", "tool_prompt_source": a.source or ""})
    return write(a.job, a.doc_id, rec)


def cmd_qa(a):
    path = os.path.join(a.job, "teamlog", a.doc_id + ".json")
    rec = json.load(open(path))
    rec["qa"] = {"pass": bool(a.ok), "reasons": a.reason or []}
    if a.result_file:
        rec["result_file"] = a.result_file
    rec["qa_at"] = now()
    return write(a.job, a.doc_id, rec)


def job_copy(job):
    """Lines from the finishing files: copy.json (head/sub/end_head/benefits/cta), premium.json captions, phrases.json."""
    lines = []
    add = lambda kind, t: t and t.strip() and lines.append({"kind": kind, "text": re.sub(r"\s+", " ", t).strip()})
    for name in ("copy.json", "premium.json"):
        p = os.path.join(job, name)
        if not os.path.exists(p):
            continue
        C = json.load(open(p))
        head = C.get("head") or C.get("header")
        if head:
            add("headline", " ".join(head) if isinstance(head, list) else head)
        add("headline", C.get("sub") if isinstance(C.get("sub"), str) else "")
        eh = C.get("end_head")
        if eh:
            add("end_head", " ".join(eh) if isinstance(eh, list) else eh)
        for b in C.get("benefits") or []:
            add("benefit", b)
        add("offer", C.get("offer", ""))
        add("cta", C.get("cta", ""))
        for c in C.get("caps") or []:
            add("caption", c[2] if isinstance(c, list) and len(c) > 2 else str(c))
    ph = os.path.join(job, "phrases.json")
    if os.path.exists(ph) and not any(l["kind"] == "caption" for l in lines):
        add("caption", " ".join(re.sub(r"\|\d+$", "", p) for p in json.load(open(ph))))
    seen, out = set(), []
    for l in lines:
        k = (l["kind"], norm(l["text"]))
        if k not in seen:
            seen.add(k)
            out.append(l)
    return out


def cmd_copy(a):
    lines = job_copy(a.job)
    if not lines:
        sys.exit("❌ no copy.json / premium.json / phrases.json in the job folder: nothing to log")
    for l in lines:
        l["source"] = label_line(l["text"], l["kind"], a.product, a.kind)[0]
    rec = {"type": "copy", "product": a.product, "ad_id": a.ad_id, "ad": a.ad or a.ad_id, "run_id": a.run_id, "audience": a.audience,
           "date": now()[:10], "media": a.kind, "lines": lines, "status": "draft"}
    rc = write(a.job, f"copy-{a.ad_id}", rec)
    # Fill the headline / hook / CTA on every take of this ad that has none, so the Prompt log never shows a blank (re-send those).
    first = lambda kinds: next((l["text"] for l in lines if l["kind"] in kinds), "")
    fill = {"headline": first(("headline",)), "hook": first(("hook", "vo", "caption")), "cta": first(("cta", "offer"))}
    for doc, g in records(a.job).items():
        if g.get("type") != "gen" or g.get("ad_id") != a.ad_id:
            continue
        cp = g.setdefault("copy", {})
        new = {k: v for k, v in fill.items() if v and not cp.get(k)}
        if new:
            cp.update(new)
            json.dump(g, open(os.path.join(a.job, "teamlog", doc + ".json"), "w"), ensure_ascii=False, indent=1)
            print(f"↻ {doc}: copy filled ({', '.join(new)}): re-send this gen record")
    return rc


def cmd_proof(a):
    rec = {"type": "proof", "product": a.product, "ad_id": a.ad_id, "kind": a.kind, "proof": a.proof, "date": now()[:10], "run_id": a.run_id}
    return write(a.job, f"proof-{a.ad_id}", rec)


def cmd_run(a):
    gens = [r for r in records(a.job).values() if r.get("type") == "gen" and r.get("run_id") == a.run_id]
    ads = {}
    for g in gens:
        ads.setdefault(g["ad_id"], []).append(g)
    finished = sum(1 for ad in ads.values() if any((g.get("qa") or {}).get("pass") for g in ad))
    rerolled = sum(1 for g in gens if (g.get("qa") or {}).get("pass") is False)
    def tool(name, before, after):
        spent = round(sum(float((g.get("cost") or {}).get(name) or 0) for g in gens), 2)
        if before is not None and after is not None:
            spent = round(before - after, 2)
        return {"before": before, "after": after, "spent": spent, "quoted": round(sum(float((g.get("cost") or {}).get(name) or 0) for g in gens), 2)}
    times = sorted(g["created_at"] for g in gens if is_iso(g.get("created_at")))
    started = times[0] if times else now()
    if not times:
        print("⚠ no generation logged for this run: started_at = now (log generations with `teamlog.py gen` when they are submitted)")
    rec = {"type": "run", "run_id": a.run_id, "product": a.product, "format": a.format, "made": len(ads), "finished": finished,
           "rerolled": rerolled, "captions": a.captions == "yes",
           "credits": {"creatify": tool("creatify", a.creatify_before, a.creatify_after),
                       "higgsfield": tool("higgsfield", a.higgsfield_before, a.higgsfield_after)},
           "out_dir": os.path.abspath(a.job), "on_board": False, "started_at": started, "ended_at": now(), "notes": a.notes or ""}
    return write(a.job, f"run-{a.run_id}", rec)


def cmd_check(a):
    bad = 0
    for f in a.files:
        rec = json.load(open(f))
        rec = rec.get("data", rec) if "type" not in rec else rec
        E, W = check(rec)
        print(f"{'❌' if E else '✅'} {os.path.basename(f)}")
        for x in E:
            print("   ❌", x)
        for x in W:
            print("   ⚠", x)
        bad += bool(E)
    return 1 if bad else 0


def cmd_close(a):
    R = records(a.job)
    E, W = [], []
    runs = {r["run_id"]: r for r in R.values() if r.get("type") == "run"}
    gens = [r for r in R.values() if r.get("type") == "gen"]
    if not gens:
        E.append("no gen records in teamlog/: every paid generation is logged when it is submitted (`teamlog.py gen`)")
    for doc, r in R.items():
        e, w = check(r)
        E += [f"{doc}: {x}" for x in e]
        W += [f"{doc}: {x}" for x in w]
    for g in gens:
        if g.get("prompt_file") and not os.path.exists(os.path.join(a.job, g["prompt_file"])):
            E.append(f"{g['ad_id']}: prompt file {g['prompt_file']} is missing")
    for g in gens:
        if g.get("retake_of") and g["retake_of"] not in R:
            W.append(f"{g['ad_id']}: retake_of {g['retake_of']} is not in this job's records")
        if g.get("retake_of") and not g.get("asks"):
            W.append(f"{g['ad_id']}: a re-take without the operator's words (--ask): what did they ask to change?")
    finished_ads = {g["ad_id"] for g in gens if (g.get("qa") or {}).get("pass")}
    for ad in sorted(finished_ads):
        for t in ("copy", "proof"):
            if not any(r.get("type") == t and r.get("ad_id") == ad for r in R.values()):
                E.append(f"{ad}: finished, but no {t} record (`teamlog.py {t}`)")
    for rid in sorted({g["run_id"] for g in gens}):
        r = runs.get(rid)
        if not r:
            E.append(f"{rid}: no run record (`teamlog.py run`)")
            continue
        fails = sum(1 for g in gens if g["run_id"] == rid and (g.get("qa") or {}).get("pass") is False)
        if r.get("rerolled") != fails:
            E.append(f"{rid}: run says rerolled {r.get('rerolled')}, but {fails} generation(s) failed QA")
    for x in W:
        print("⚠", x)
    for x in E:
        print("❌", x)
    n = {t: sum(1 for r in R.values() if r.get('type') == t) for t in ("gen", "copy", "proof", "run")}
    by_page = {}
    for doc, r in R.items():
        by_page.setdefault(PAGES.get(r.get("type"), ("?", "?")), []).append(doc)
    for (name, url), docs in by_page.items():
        print(f"  → {name} ({url}): {len(docs)} record(s)")
    print(("❌ NOT CLOSED" if E else "✅ closed") + f": {n['gen']} gen · {n['copy']} copy · {n['proof']} proof · {n['run']} run "
          f"in {os.path.join(a.job, 'teamlog')} (send any not yet sent: one ArtifactData batch per page)")
    return 1 if E else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    g = sp.add_parser("gen"); g.add_argument("job")
    for k in ("--run-id", "--ad-id", "--product", "--model", "--prompt-file"):
        g.add_argument(k, required=True)
    g.add_argument("--ref-type", default="none", choices=sorted(REF_TYPES)); g.add_argument("--ref-id")
    g.add_argument("--refs"); g.add_argument("--cost-creatify", type=float, default=0); g.add_argument("--cost-higgsfield", type=float, default=0)
    g.add_argument("--ratio", default=""); g.add_argument("--resolution", default="")
    g.add_argument("--setup", nargs="*"); g.add_argument("--ask", action="append")
    g.add_argument("--retake-of"); g.add_argument("--edited-by-user", action="store_true")
    g.add_argument("--headline"); g.add_argument("--hook"); g.add_argument("--cta")
    t = sp.add_parser("tool"); t.add_argument("job"); t.add_argument("doc_id"); t.add_argument("--source")
    tg = t.add_mutually_exclusive_group(required=True); tg.add_argument("--file"); tg.add_argument("--none", action="store_true")
    n = sp.add_parser("note"); n.add_argument("job"); n.add_argument("doc_id"); n.add_argument("--ask", action="append", required=True)
    q = sp.add_parser("qa"); q.add_argument("job"); q.add_argument("doc_id")
    m = q.add_mutually_exclusive_group(required=True); m.add_argument("--pass", dest="ok", action="store_true"); m.add_argument("--fail", dest="ok", action="store_false")
    q.add_argument("--reason", action="append"); q.add_argument("--result-file")
    c = sp.add_parser("copy"); c.add_argument("job")
    for k in ("--run-id", "--ad-id", "--product"):
        c.add_argument(k, required=True)
    c.add_argument("--kind", required=True, choices=["image", "video"]); c.add_argument("--ad"); c.add_argument("--audience", default="")
    p = sp.add_parser("proof"); p.add_argument("job")
    for k in ("--run-id", "--ad-id", "--product"):
        p.add_argument(k, required=True)
    p.add_argument("--kind", required=True, choices=["image", "video"]); p.add_argument("--proof", required=True, choices=["trust", "count", "none"])
    r = sp.add_parser("run"); r.add_argument("job")
    for k in ("--run-id", "--product"):
        r.add_argument(k, required=True)
    r.add_argument("--started", help=argparse.SUPPRESS)   # ignored: the start comes from the first logged generation
    r.add_argument("--format", required=True, choices=["images", "video", "avatar", "still"])
    r.add_argument("--captions", required=True, choices=["yes", "no"])
    for k in ("--creatify-before", "--creatify-after", "--higgsfield-before", "--higgsfield-after"):
        r.add_argument(k, type=float)
    r.add_argument("--notes")
    k = sp.add_parser("check"); k.add_argument("files", nargs="+")
    z = sp.add_parser("close"); z.add_argument("job")
    a = ap.parse_args()
    sys.exit({"gen": cmd_gen, "tool": lambda a: cmd_tool_none(a) if a.none else cmd_tool(a), "note": cmd_note, "qa": cmd_qa, "copy": cmd_copy, "proof": cmd_proof, "run": cmd_run, "check": cmd_check, "close": cmd_close}[a.cmd](a))


if __name__ == "__main__":
    main()
