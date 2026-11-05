#!/usr/bin/env python3
"""Generate every product skill's bible extract FROM the synced bible (core/claude/creative-bible.md), so a bible change
reaches the skill by regeneration, never by hand (Mitansh 2026-11-05: "a small update in the bible about a single product
→ that product's skill has it updated and the next batch of ads has it done").

    build_product_bibles.py [--only pt-141,nad] [--dry] [--out DIR]

Per skill it writes (GENERATED, committed, never edited):
  references/bible.json          the product's current copy as data: offer, cta_default, ctas, benefits, headlines, hard NOs,
                                 disclaimer, screening statuses, retired lines  ← read by the hook, lint, briefs, product_copy.py
  references/product-bible.md    the same as a page: product copy, screening table, the verbatim section(s), hand notes
and updates product.json "disclaimer" when the bible's differs (verbatim rule).
Hand inputs (small, optional): references/bible-screen.json (overrides: ❌/⚠ lines with a why, product regex patterns, retired lines),
references/product-notes.md (prose), product.json "bible_sections".
Statuses: hand ❌/⚠ > auto ❌ (core/scripts/hard_nos.py) > product patterns > bible badges (Hard NO conflict / PLACEHOLDER → ❌,
Pending approval / VERIFY CURRENT → ⏳, Weak → Weak) > "✅ NEW in <version>" (first seen this version) > ✅.
Retired = hand retired ∪ lines that were in the previous bible.json but left the bible ∪ "Get Started Now". Never pitched, refused by the gate.
"""
import argparse, json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import bible_model as bm  # noqa: E402
import hard_nos  # noqa: E402

SKILLS = os.path.join(REPO, "skills")
STATUS_BADGE = {"Hard NO conflict": "❌ (bible: Hard NO conflict)", "PLACEHOLDER": "❌ placeholder (bible)",
                "VERIFY CURRENT": "⏳ VERIFY CURRENT (bible)", "Pending approval": "⏳ Pending approval (bible)",
                "Weak headline": "Weak (bible)", "Weak benefit": "Weak (bible)"}
ALWAYS_RETIRED = [{"line": "Get Started Now", "why": "banned CTA (bible 2026-11-03): lead with the offer"}]


def read_json(p, default):
    if not os.path.exists(p):
        return default
    try:
        return json.load(open(p, encoding="utf-8"), object_pairs_hook=OrderedDict)
    except ValueError as e:
        raise SystemExit(f"❌ {p}: not valid JSON ({e})")


def write_json(p, obj):
    open(p, "w", encoding="utf-8").write(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")


def product_skills(only=()):
    for d in sorted(os.listdir(SKILLS)):
        pj = os.path.join(SKILLS, d, "product.json")
        if d.startswith("everlife-") and os.path.exists(pj):
            prod = read_json(pj, None)
            if not only or prod.get("id") in only or d in only:
                yield d, os.path.join(SKILLS, d), prod


def screen_of(skill_dir):
    s = read_json(os.path.join(skill_dir, "references", "bible-screen.json"), OrderedDict())
    lines = {bm.norm(k): v for k, v in (s.get("lines") or {}).items()}
    pats = [(p.get("re", ""), p.get("status", "❌"), p.get("why", "")) for p in (s.get("patterns") or [])]
    retired = [r if isinstance(r, dict) else {"line": r, "why": "retired (bible-screen.json)"} for r in (s.get("retired") or [])]
    return lines, pats, retired


def status_of(text, badges, field_badges, screen_lines, patterns, first_seen, version, baseline=False):
    n = bm.norm(text)
    if n in screen_lines:
        o = screen_lines[n]
        return o.get("status", "⚠"), o.get("why", "") + (f" ({o['who']})" if o.get("who") else "")
    hits = hard_nos.check(text)
    if hits:
        return "❌ auto", "; ".join(w for _, w in hits)
    for pat, st, why in patterns:
        try:
            if re.search(pat, text, re.I):
                return st, why
        except re.error:
            return "❌ auto", f"bad pattern in bible-screen.json: {pat}"
    for b in list(badges) + list(field_badges):
        if b in STATUS_BADGE:
            return STATUS_BADGE[b], f"bible badge [{b}]"
    if first_seen.get(n) == version and not baseline:
        return f"✅ NEW in {version}", "new or reworded in this sync: not yet reviewed by Jeremy"
    return "✅", ""


_VERB = {}
def verbatim_lines(heading):
    if not _VERB:
        for head, badges, lines, cat in bm.sections(open(bm.BIBLE, encoding="utf-8").read()):
            _VERB[head] = list(lines)
    out = _VERB.get(heading, [])
    while out and not out[-1].strip():
        out = out[:-1]
    return out


def build_one(model, skill, skill_dir, prod, out_dir=None):
    pages = bm.pages_for(model, prod)
    merged = bm.merge(pages)
    g = model["globals"]; version = model["version"]
    name = prod.get("name") or merged["headings"][0]
    offer = bm.offer_of(merged, g, name)
    cta_default = bm.cta_default_of(merged, offer)
    cta_price = bm.cta_price_of(merged)
    refs = os.path.join(out_dir or skill_dir, "references"); os.makedirs(refs, exist_ok=True)
    prev = read_json(os.path.join(skill_dir, "references", "bible.json"), OrderedDict())
    screen_lines, patterns, hand_retired = screen_of(skill_dir)

    page_of = {}
    for p in pages:
        for f in ("headlines", "quick_hits", "more_benefits", "ctas", "offers", "proof", "hard_nos"):
            for it in p[f]:
                page_of.setdefault(bm.norm(it["text"]), p["heading"])
    kinds = [("headlines", "headlines"), ("quick_hits", "quick-hit benefits"), ("more_benefits", "more approved benefits"),
             ("ctas", "CTAs"), ("offers", "offers"), ("proof", "proof")]
    current = {bm.norm(it["text"]) for f, _ in kinds for it in merged[f]}
    for ing, items in merged["ingredient_claims"].items():
        current |= {bm.norm(it["text"]) for it in items}

    baseline = not prev          # first generation ever for this skill: every line is "known", nothing is flagged NEW
    first_seen = OrderedDict((k, v) for k, v in (prev.get("first_seen") or {}).items() if k in current)
    for n in sorted(current):
        first_seen.setdefault(n, "baseline" if baseline else version)   # baseline = known before the pipeline; never NEW

    retired, seen = [], set()
    def add_retired(line, why):
        n = bm.norm(line)
        if n and n not in seen and n not in current:
            seen.add(n); retired.append(OrderedDict([("line", line), ("why", why)]))
    for r in ALWAYS_RETIRED + hand_retired:
        add_retired(r["line"], r.get("why", ""))
    for r in prev.get("retired") or []:
        add_retired(r["line"] if isinstance(r, dict) else r, (r.get("why") if isinstance(r, dict) else None) or "left the bible")
    prev_keys = {"headlines": "headlines", "quick_hits": "benefits_quick", "more_benefits": "benefits_more", "ctas": "ctas",
                 "offers": "offer_lines", "proof": "proof"}
    for f, _ in kinds:
        for it in prev.get(prev_keys[f]) or []:
            add_retired(it["text"] if isinstance(it, dict) else it, f"left the bible in {version}")
    for n in screen_lines:
        if n not in current:
            add_retired(n, "listed in bible-screen.json but no longer in the bible")

    rows, screen_out = [], OrderedDict()
    for f, where in kinds:
        fb = merged["field_badges"].get(f, [])
        for it in merged[f]:
            st, why = status_of(it["text"], it["badges"], fb, screen_lines, patterns, first_seen, version, baseline)
            rows.append((it["text"], where, st, why))
            if not st.startswith("✅") or "NEW" in st:
                screen_out[bm.norm(it["text"])] = OrderedDict([("status", st), ("why", why)])
    for ing, items in merged["ingredient_claims"].items():
        for it in items:
            st, why = status_of(it["text"], it["badges"], [], screen_lines, patterns, first_seen, version, baseline)
            if st.startswith("✅"):
                st, why = "⚠ ingredient claim", f"only on its own ingredient ({ing}); never attributed to the product" + (f"; {why}" if why else "")
            rows.append((f"{ing}: {it['text']}", "ingredient claims", st, why))
            screen_out[bm.norm(it["text"])] = OrderedDict([("status", st), ("why", why)])
    for r in retired:
        rows.append((r["line"], "retired", "❌ retired", r["why"]))

    bj = OrderedDict([
        ("_generated", "core/scripts/build_product_bibles.py from core/claude/creative-bible.md; never edit, run `python3 core/scripts/bible_pipeline.py regen`"),
        ("version", version), ("id", prod.get("id")), ("name", name), ("sections", merged["headings"]), ("category", merged["category"]),
        ("who", merged["who"]), ("truth", merged["truth"]), ("direction", merged["direction"]),
        ("offer", offer), ("cta_default", cta_default), ("cta_price", cta_price),
        ("ctas", [c["text"] for c in merged["ctas"]]),
        ("benefits_quick", [c["text"] for c in merged["quick_hits"]]),
        ("benefits_more", [OrderedDict([("text", c["text"]), ("badges", c["badges"])]) for c in merged["more_benefits"]]),
        ("headlines", [OrderedDict([("text", c["text"]), ("badges", c["badges"]), ("page", page_of.get(bm.norm(c["text"]), ""))]) for c in merged["headlines"]]),
        ("offer_lines", [c["text"] for c in merged["offers"]]),
        ("proof", [c["text"] for c in merged["proof"]]),
        ("hard_nos", [c["text"] for c in merged["hard_nos"]]),
        ("ingredient_claims", OrderedDict((k, [i["text"] for i in v]) for k, v in merged["ingredient_claims"].items())),
        ("disclaimer", merged["disclaimer"]), ("landing_page", merged["landing_page"]), ("last_verified", merged["last_verified"]),
        ("field_badges", merged["field_badges"]), ("screen", screen_out), ("first_seen", first_seen), ("retired", retired),
        ("patterns", [OrderedDict([("re", r_), ("status", st), ("why", why)]) for r_, st, why in patterns]),
        ("extra", merged["extra"]),
    ])
    write_json(os.path.join(refs, "bible.json"), bj)

    md = [f"# {name} — creative bible extract (GENERATED from `core/claude/creative-bible.md` version {version} by "
          f"`core/scripts/build_product_bibles.py`; never edit this file: run `python3 core/scripts/bible_pipeline.py regen`)", "",
          "> Hand inputs: `references/product-notes.md` (notes), `references/bible-screen.json` (screening overrides), "
          "`references/hard-stops.md` (product hard stops). Rules: the gates + `core/references/global-rules.md`. "
          "Headlines are references, the only fence is the Hard NOs; Jeremy signs off before anything goes live.", "",
          f"## Product copy (bible version {version})"]
    if offer["status"] == "ok":
        md.append(f"- **Offer:** {offer['cta']} (the product's highest; source: {offer['source']}). Always \"Save Up to N%\", never a fixed discount.")
    else:
        md.append(f"- **Offer:** none usable ({offer['status']}: {', '.join(offer['lines']) or 'no offer line'}). No % and no price in ads until the bible carries a verified offer.")
    md.append(f"- **Default CTA:** {cta_default}")
    md.append("- **CTAs (bible):** " + " · ".join(bj["ctas"]))
    if cta_price: md.append(f"- **Price CTA (approved alternative, the only $ amount allowed):** {cta_price}")
    if offer.get("variants"): md.append("- **Variant maximums (reference only, never shown as a lower %):** " + ", ".join(f"{k} {v}%" for k, v in offer["variants"].items()))
    md.append("- **Quick-hit benefits (word for word):** " + " · ".join(bj["benefits_quick"]))
    if bj["benefits_more"]: md.append("- **More approved benefits:** " + " · ".join(c["text"] + (f" [{', '.join(c['badges'])}]" if c["badges"] else "") for c in bj["benefits_more"]))
    md.append("- **Proof:** " + " · ".join(bj["proof"]))
    md.append("- **Product Hard NOs:** " + " · ".join(bj["hard_nos"]))
    md.append(f"- **Disclaimer (verbatim, in product.json):** {merged['disclaimer']}")
    md.append(f"- **Landing page:** {merged['landing_page']}" + (f" (last verified {merged['last_verified']})" if merged['last_verified'] else ""))
    if retired: md.append("- **Retired, never use:** " + " · ".join(r["line"] for r in retired))
    md += ["", "## Screening (auto pre-screen + overrides; ✅ usable · ⏳ pending in the bible · ⚠ ask · ❌ never; NEW = first seen this sync)",
           "| Line (bible) | Where | Status | Why |", "|---|---|---|---|"]
    md += [f"| {t} | {w} | {s} | {y} |" for t, w, s, y in rows]
    for p in pages:
        md += ["", f"## Verbatim (bible section \"{p['heading']}\", version {version})", "```text"] + verbatim_lines(p["heading"]) + ["```"]
    notes_p = os.path.join(skill_dir, "references", "product-notes.md")
    if os.path.exists(notes_p):
        md += ["", "## Notes (hand, `references/product-notes.md`)", open(notes_p, encoding="utf-8").read().rstrip()]
    open(os.path.join(refs, "product-bible.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")

    changed_disc = False
    if merged["disclaimer"] and bm.norm(prod.get("disclaimer", "")) != bm.norm(merged["disclaimer"]) and not out_dir:
        prod["disclaimer"] = merged["disclaimer"]; write_json(os.path.join(skill_dir, "product.json"), prod); changed_disc = True
    return {"skill": skill, "offer": offer, "cta_default": cta_default, "new": [t for t, w, s, y in rows if "NEW" in s],
            "retired": retired, "disclaimer_changed": changed_disc, "prev_version": prev.get("version")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=""); ap.add_argument("--dry", action="store_true"); ap.add_argument("--out", default="")
    a = ap.parse_args()
    only = {s for s in a.only.split(",") if s}
    model = bm.load()
    if len(model["order"]) < 20:
        raise SystemExit(f"❌ the bible parsed into only {len(model['order'])} product sections: refusing to generate (bad sync?)")
    reports = []
    for skill, sd, prod in product_skills(only):
        if a.dry:
            mg = bm.merge(bm.pages_for(model, prod)); o = bm.offer_of(mg, model["globals"], prod.get("name", ""))
            print(f"{skill}: {', '.join(mg['headings'])} · offer {o['status']} {o['pct']} · default CTA {bm.cta_default_of(mg, o)}"); continue
        r = build_one(model, skill, sd, prod, os.path.join(a.out, skill) if a.out else None); reports.append(r)
        o = r["offer"]
        print(f"✅ {skill}: offer {o['status']}" + (f" {o['pct']}%" if o["pct"] else "") + f" · default CTA \"{r['cta_default']}\""
              + (f" · {len(r['new'])} NEW line(s) to screen" if r["new"] else "") + (f" · {len(r['retired'])} retired" if r["retired"] else "")
              + (" · product.json disclaimer updated" if r["disclaimer_changed"] else ""))
    if any(r["new"] for r in reports):
        print("\nNEW lines for Jeremy (usable now, not yet reviewed):")
        for r in reports:
            for t in r["new"]:
                print(f"  {r['skill']}: {t}")


if __name__ == "__main__":
    main()
