#!/usr/bin/env python3
"""Both-sizes + layout gate for image batches (Claude Code hooks; installed by install.sh). Mitansh 2026-11-05:
"how is it guaranteed that for every skill Claude will one-shot 10 images in 1 batch, 5 for each side?" → this file.

  batch_hook.py gate    PreToolUse on image-generation tools: an Everlife image prompt is REFUSED unless it carries the
                        STRICT LAYOUT block and the batch reference line the template adds at the end:
                          Reference only, never render: everlife slot=3 ratio=9:16 product=pt-141 job=<batch folder>
                        (ratio must match the layout block). Other generations (video, avatars, non-Everlife) pass untouched.
  batch_hook.py fired   PostToolUse: records every fired (slot, ratio) in <job>/renders.jsonl.
  batch_hook.py stop    Stop: for every batch touched today, compares deal.json (slots × ratios owed) with renders fired and
                        FINAL_<slot>_*_1080x1920 / _1080x1350 files finished. Anything owed → Claude is sent back once
                        (decision "block") with the exact list; the second time it lets the turn end and warns the user.
                        A batch the user abandoned is released with `batch_check.py <job> --release "<reason>"`.
                        Then the NEXT-BATCH QUESTIONNAIRE (Mitansh 2026-11-05: "Compulsory requestionnaire after 1 batch of
                        images is done, for that same product; not a memory, do it by code"): once every slot of a batch is
                        finished in both sizes, the turn cannot end until Claude has asked the product's setup question again
                        (one AskUserQuestion whose first question has the header "Next batch"; image-flow.md §9).
  batch_hook.py fired   also on AskUserQuestion: a question headed "Next batch" writes <job>/next_asked.json (questions +
                        answers) for every finished batch that was still owed one. That file is what the Stop check reads.

Independent of the team-log pause (a paused log never means half a batch). Local files only, no network.
"""
import datetime, glob, json, os, re, sys

HOME = os.path.expanduser(os.environ.get("EVERLIFE_CREATIVE", "~/Everlife-Creative"))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS_DIRS = [os.path.expanduser(os.environ.get("EVERLIFE_SKILLS_DIR", "")), os.path.join(REPO, "skills"), os.path.expanduser("~/.claude/skills")]
sys.path.insert(0, os.path.join(REPO, "core", "scripts"))
try:
    import hard_nos                     # the mechanical Hard NOs (one copy for the hook, teamlog and the generator)
except Exception:                        # a half-installed copy: the copy gate then checks only the bible lists
    hard_nos = None
OUT = os.path.join(HOME, "output")
REF = re.compile(r"Reference only, never render: everlife slot=(\d+) ratio=(9:16|4:5|1:1) product=([a-z0-9-]+) job=(\S+)")
IMAGE_TOOL = re.compile(r"model_playground_generate|edit_image|gpt[-_]image|image_generate|generate_image", re.I)
SIZES = {"9:16": "1080x1920", "4:5": "1080x1350", "1:1": "1080x1080"}
ASK_HEADER = "next batch"          # the questionnaire's first question carries this header (AskUserQuestion, max 12 chars)
ASKED = "next_asked.json"          # written into the job folder once the questionnaire has been asked
ASK_BLOCKS = 2                     # Stop sends Claude back this many times per session per batch, then warns the user


def strings(v, out=None):
    out = [] if out is None else out
    if isinstance(v, dict):
        for x in v.values(): strings(x, out)
    elif isinstance(v, list):
        for x in v: strings(x, out)
    elif isinstance(v, str): out.append(v)
    return out


def find_ref(tin):
    for s in strings(tin):
        m = REF.search(s)
        if m: return m.group(1), m.group(2), m.group(3), os.path.expanduser(m.group(4)), s
    return None


def is_everlife_image(tool, tin):
    if not IMAGE_TOOL.search(tool or ""): return False
    txt = "\n".join(strings(tin))
    return "Everlife" in txt or "STRICT LAYOUT" in txt or "everlife slot=" in txt


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": reason}}))


# ---- the copy gate (bible → prompt; Mitansh 2026-11-05: "the next batch of ads should have it done") ----
CTA_LINE = re.compile(r'^\s*CTA[^:\n"]*:\s*"([^"\n]+)"', re.M)
HEAD_LINE = re.compile(r'^\s*Headline:\s*"([^"\n]+)"', re.M)
SUPP_LINE = re.compile(r'^\s*Supporting[^:\n]*:\s*(.+)$', re.M)
SAVE_PCT = re.compile(r"save\s+up\s+to\s+(\d+)\s*%", re.I)


def bnorm(t):
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", t.replace("\u2014", "-").replace("\u2013", "-")).strip().lower()


def bible_of(product):
    for root in SKILLS_DIRS:
        if not root: continue
        bp = os.path.join(root, f"everlife-{product}", "references", "bible.json")
        if os.path.exists(bp):
            try: return json.load(open(bp, encoding="utf-8"))
            except Exception: return None
    return None


def repo_bible_version():
    for root in (REPO, os.path.join(os.path.expanduser("~/.claude/skills/everlife-ads"), "core", "..")):
        md = os.path.join(root, "core", "claude", "creative-bible.md")
        if os.path.exists(md):
            m = re.search(r"\(version ([^)]+)\)", open(md, encoding="utf-8").readline())
            if m: return m.group(1)
    return None


def copy_gate(product, txt):
    """→ a deny reason, or None. Checks only the TEXT block lines the template names (Headline / Supporting / CTA) plus any 'Save Up to N%'."""
    b = bible_of(product)
    if not b: return None                                   # no generated copy on this machine: lint/preflight report it, the gate never blocks
    name, ver = b.get("name", product), b.get("version", "?")
    rv = repo_bible_version()
    if rv and rv != ver:
        return (f"{name}'s skill copy is from bible version {ver} but the synced bible is {rv}: run `python3 core/scripts/bible_pipeline.py regen` "
                "(or update the tools) before generating, so the ad carries the current offer / CTAs.")
    ctas = {bnorm(c) for c in b.get("ctas", [])}
    retired = {bnorm(r["line"] if isinstance(r, dict) else r): (r.get("why", "") if isinstance(r, dict) else "") for r in b.get("retired", [])}
    offer = b.get("offer") or {}
    hint = f"Current {name} copy: `python3 core/scripts/product_copy.py {product}` (default CTA \"{b.get('cta_default')}\")."
    heads = HEAD_LINE.findall(txt); ctal = CTA_LINE.findall(txt)
    supp = [q for line in SUPP_LINE.findall(txt) for q in re.findall(r'"([^"\n]+)"', line)]
    if heads and not ctal:
        return f"No CTA line in the TEXT block: every ad has a CTA (bible Standards 03). Add `CTA (in a button): \"{b.get('cta_default')}\"`. {hint}"
    for c in ctal:
        n = bnorm(c)
        if n in retired:
            return f'CTA "{c}" was removed from the bible ({retired[n] or "retired"}). {hint}'
        if n not in ctas:
            return f'CTA "{c}" is not a {name} bible CTA (version {ver}): {" · ".join(b.get("ctas", []))}. {hint}'
    for n_ in SAVE_PCT.findall(txt):
        if offer.get("status") != "ok":
            return f"{name} has no verified offer in the bible ({offer.get('status', 'none')}): no \"Save Up to\" and no price on this product; use \"{b.get('cta_default')}\". {hint}"
        if int(n_) != int(offer.get("pct") or -1):
            return f"\"Save Up to {n_}%\" is not {name}'s featured discount: the bible says Save Up to {offer['pct']}% (rule 09: always the product's highest). {hint}"
    extra = [(pat.get("re", ""), pat.get("why", "")) for pat in b.get("patterns", []) if "❌" in pat.get("status", "❌")]
    for line in heads + supp + ctal:
        n = bnorm(line)
        if n in retired:
            return f'"{line}" was removed from the bible ({retired[n] or "retired"}): never use it. {hint}'
        if hard_nos:
            hits = hard_nos.check(line, extra=extra)
            if hits:
                return f'"{line}" breaks a Hard NO: {hits[0][1]}. Rewrite that line; the rest of the prompt is fine.'
    return None


def gate(p):
    tool, tin = p.get("tool_name", ""), p.get("tool_input", {}) or {}
    if not is_everlife_image(tool, tin): return
    ref = find_ref(tin)
    txt = "\n".join(strings(tin))
    if not ref:
        return deny("Everlife image prompt without its batch reference line. Every image prompt ends with: "
                    "'Reference only, never render: everlife slot=<n> ratio=<9:16|4:5> product=<id> job=<batch folder>' "
                    "(core/references/image-flow.md §4). Deal the batch first (deal_worlds.py → <job>/deal.json), then send both sizes.")
    slot, ratio, product, job, _ = ref
    if "STRICT LAYOUT" not in txt:
        return deny(f"Slot {slot} {ratio}: the prompt has no STRICT LAYOUT block (core/references/prompt-layout-zones.md). Add it and resend.")
    if f"STRICT LAYOUT ({ratio}" not in txt:
        return deny(f"Slot {slot}: the reference says ratio={ratio} but the STRICT LAYOUT block is for another ratio. One prompt per ratio, each with its own block.")
    deal = os.path.join(job, "deal.json")
    if not os.path.exists(deal):
        return deny(f"No deal.json in {job}. Run core/scripts/deal_worlds.py --product {product} --n N … --json > {deal} first; the batch is owed from that manifest.")
    try:
        slots = {str(s["slot"]) for s in json.load(open(deal))}
    except Exception:
        slots = set()
    if slots and slot not in slots:
        return deny(f"Slot {slot} is not in {deal} (slots {', '.join(sorted(slots, key=int))}). Re-roll an existing slot; never add a size-less extra.")
    why = copy_gate(product, txt)
    if why:
        return deny(f"Slot {slot} {ratio}: {why}")


def fired(p):
    tool, tin = p.get("tool_name", ""), p.get("tool_input", {}) or {}
    if tool == "AskUserQuestion": return asked(p)
    if not is_everlife_image(tool, tin): return
    ref = find_ref(tin)
    if not ref: return
    slot, ratio, product, job, _ = ref
    os.makedirs(job, exist_ok=True)
    with open(os.path.join(job, "renders.jsonl"), "a") as f:
        f.write(json.dumps({"ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "slot": int(slot),
                            "ratio": ratio, "product": product, "tool": tool, "session": p.get("session_id", "")}) + "\n")


def status(job):
    """→ dict(owed_fire=[(slot,ratio)], owed_finish=[(slot,ratio)], n, released)"""
    deal = os.path.join(job, "deal.json")
    if not os.path.exists(deal): return None
    try: slots = json.load(open(deal))
    except Exception: return None
    rel = os.path.join(job, ".batch-released")
    if os.path.exists(rel): return {"owed_fire": [], "owed_finish": [], "n": len(slots), "released": True}
    firedset = set()
    rp = os.path.join(job, "renders.jsonl")
    if os.path.exists(rp):
        for ln in open(rp):
            try: r = json.loads(ln); firedset.add((int(r["slot"]), r["ratio"]))
            except Exception: pass
    finals = set()
    for f in glob.glob(os.path.join(job, "**", "FINAL_*"), recursive=True):
        m = re.search(r"FINAL_(\d+)_.*_(1080x\d+)", os.path.basename(f))
        if m:
            for ratio, wh in SIZES.items():
                if m.group(2) == wh: finals.add((int(m.group(1)), ratio))
    owed_fire, owed_finish = [], []
    for s in slots:
        for ratio in s.get("ratios", ["9:16", "4:5"]):
            key = (int(s["slot"]), ratio)
            if key not in firedset and key not in finals: owed_fire.append(key)
            elif key not in finals: owed_finish.append(key)
    return {"owed_fire": owed_fire, "owed_finish": owed_finish, "n": len(slots), "released": False, "finals": len(finals)}


def product_of(job):
    """The product's name for messages: the output folder it lives in (…/output/PT-141/<job>)."""
    return os.path.basename(os.path.dirname(os.path.abspath(job)))


def finished(job, st=None):
    """Every slot of the batch exists in every owed size as a FINAL (and the batch was not released)."""
    st = st or status(job)
    return bool(st) and not st["released"] and st.get("finals", 0) > 0 and not st["owed_fire"] and not st["owed_finish"]


def sessions_of(job):
    """Session ids that fired renders for this batch (renders.jsonl, written by `fired`)."""
    out = set()
    rp = os.path.join(job, "renders.jsonl")
    if os.path.exists(rp):
        for ln in open(rp):
            try: out.add(json.loads(ln).get("session", ""))
            except Exception: pass
    out.discard("")
    return out


def questionnaire_owed(job, st=None, sid=""):
    """Only the session that generated the batch owes its questionnaire (another session's or teammate's batch on the same
    machine never blocks this one; found 2026-11-05 when a Lovara and a Sermorelin GHK batch from another session blocked a Titan-Rx run)."""
    if not sid or sid not in sessions_of(job): return False
    return finished(job, st) and not os.path.exists(os.path.join(job, ASKED))


def asked(p):
    tin = p.get("tool_input", {}) or {}
    qs = tin.get("questions") or []
    if not any(str(q.get("header", "")).strip().lower() == ASK_HEADER for q in qs if isinstance(q, dict)): return
    sid = p.get("session_id", "")
    for job in active_jobs():
        if not questionnaire_owed(job, sid=sid): continue
        with open(os.path.join(job, ASKED), "w") as f:
            json.dump({"ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "product": product_of(job),
                       "questions": qs, "answers": p.get("tool_response")}, f, indent=1)


def active_jobs(hours=14):
    cutoff = datetime.datetime.now().timestamp() - hours * 3600
    jobs = []
    for deal in glob.glob(os.path.join(OUT, "*", "*", "deal.json")):
        job = os.path.dirname(deal)
        newest = max(os.path.getmtime(x) for x in [deal] + glob.glob(os.path.join(job, "renders.jsonl")))
        if newest >= cutoff: jobs.append(job)
    return jobs


def fmt(pairs):
    by = {}
    for s, r in pairs: by.setdefault(r, []).append(str(s))
    return "; ".join(f"{r} for slot(s) {', '.join(sorted(v, key=int))}" for r, v in sorted(by.items()))


def stop(p):
    todo = []
    for job in active_jobs():
        st = status(job)
        if not st or st["released"]: continue
        rp = os.path.join(job, "renders.jsonl")
        if not os.path.exists(rp) and not st["owed_finish"]: continue   # dealt but never started: nothing owed yet
        parts = []
        if st["owed_fire"]: parts.append("not generated: " + fmt(st["owed_fire"]))
        if st["owed_finish"]: parts.append("generated but not finished (no FINAL file): " + fmt(st["owed_finish"]))
        if parts: todo.append(f"{os.path.basename(job)}: " + " · ".join(parts))
    if not todo: return ask_stop(p)
    nag = os.path.join(HOME, ".batch-stop-nag")
    sid = p.get("session_id", "")
    seen = open(nag).read() if os.path.exists(nag) else ""
    if sid and sid in seen:
        print(json.dumps({"systemMessage": "⚠ Batch incomplete: " + " | ".join(todo) + ". Every ad needs both sizes, finished. "
                          "Finish it next turn, or release it with core/scripts/batch_check.py <job> --release '<reason>'."}))
        return
    open(nag, "a").write(sid + "\n")
    print(json.dumps({"decision": "block", "reason": "Both-sizes gate: " + " | ".join(todo) + ". Every ad is owed in 9:16 AND 4:5, "
                      "finished with finish_batch.py (FINAL_<slot>_<world>_1080x1920 / _1080x1350). Generate / finish what is missing now "
                      "(same slots, same worlds). If the user stopped the batch on purpose: core/scripts/batch_check.py <job> --release '<their words>'."}))


def ask_stop(p):
    """Both sizes are done everywhere: a finished batch whose next-batch questionnaire was never asked blocks the turn's end."""
    sid = p.get("session_id", "")
    owed = [job for job in active_jobs() if questionnaire_owed(job, sid=sid)]
    if not owed: return
    nag = os.path.join(HOME, ".batch-ask-nag")
    seen = open(nag).read().splitlines() if os.path.exists(nag) else []
    names = ", ".join(f"{os.path.basename(j)} ({product_of(j)})" for j in owed)
    if sid and all(seen.count(f"{sid} {j}") >= ASK_BLOCKS for j in owed):
        print(json.dumps({"systemMessage": f"⚠ Next-batch questionnaire not asked for: {names}. Ask it at the start of the next turn "
                          "(image-flow.md §9), or release the batch with core/scripts/batch_check.py <job> --release '<reason>'."}))
        return
    with open(nag, "a") as f:
        for j in owed: f.write(f"{sid} {j}\n")
    prods = sorted({product_of(j) for j in owed})
    print(json.dumps({"decision": "block", "reason":
        f"Next-batch questionnaire owed (compulsory, image-flow.md §9): {names} is finished in both sizes. Before ending the turn, "
        f"show the contact sheet, then ask ONE AskUserQuestion for the SAME product ({', '.join(prods)}). Its FIRST question has "
        "header exactly 'Next batch' (\"Next batch of <Product> images?\": 'Another 8, new worlds (Recommended)' / 'Another 4' / "
        "'Variations of one ad' / 'Done for now'), then Direction (🎲 Surprise me first + three NEW pitches, never last batch's), "
        "Who's in them, and Form or Strength if the product has them. Asking it records <job>/next_asked.json and releases this check."}))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        p = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    except Exception:
        p = {}
    try:
        {"gate": gate, "fired": fired, "stop": stop}.get(cmd, lambda p: None)(p)
    except Exception as e:   # a hook must never break the session
        print(json.dumps({"systemMessage": f"batch hook skipped: {e}"}))


if __name__ == "__main__":
    main()
