#!/usr/bin/env python3
"""One-time migration (2026-11-05) from hand-written references/product-bible.md to the generated pipeline.

    migrate_bible_extracts.py [--only pt-141] [--dry]

Per product skill:
  1. backs up references/product-bible.md and product-brief.md to _originals/<date>/bible-pipeline/<skill>/references/
  2. references/bible-screen.json  ← the hand pre-screen table: ❌ / ⚠ rows become "lines" overrides (with their why);
     "❌ removed" rows and 'Any "…"' rows become "retired" / "patterns" (patterns are printed for hand review);
     ✅ / ⏳ / Weak / label-only rows are dropped (derived from the bible from now on)
  3. references/product-notes.md   ← the hand prose (Product facts, The angle, how-to notes), offer/CTA/price lines replaced by a pointer
  4. references/hard-stops.md      ← the brief's "## Hard stops (this product)" minus the generic first bullet and offer/CTA/price bullets
  5. product.json                  ← "bible_sections" (the page headings), "bible_section" removed
  6. retired seeds: old verbatim list items that are no longer in the bible (printed; "Get Started Now" on every product)
Run build_product_bibles.py + build_product_briefs.py afterwards (bible_pipeline.py regen does both).
"""
import argparse, json, os, re, shutil, sys, time
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import bible_model as bm  # noqa: E402

SKILLS = os.path.join(REPO, "skills")
ORIG = os.path.join(REPO, "_originals", time.strftime("%Y-%m-%d"), "bible-pipeline")
SECTIONS = {"bpc-157": ["BPC-157"], "epithalon": ["Epithalon"], "ghk-cream": ["GHK-Cu Cream"], "glp-1": ["GLP1"], "lovara": ["Lovara"],
            "mots-c": ["MOTS-c"], "nad": ["NAD+"], "pt-141": ["PT-141"], "restora-z": ["Restora-Z"],
            "sermorelin": ["Sermorelin — Men", "Sermorelin — Women"], "sermorelin-ghk": ["Sermorelin GHK — Men", "Sermorelin GHK — Women"],
            "spark": ["Spark"], "spartan": ["Spartan Stack (BPC-157/KPV/TB500)"], "titan-rx": ["Titan-Rx"], "wolverine": ["Wolverine Stack (BPC-157/TB500)"]}
OFFER_LINE = re.compile(r"Save [Uu]p to \d+%|\$\d+\.\d\d/day|\$\d+/month|^\s*-\s*\*{0,2}(Offer|CTA|Default CTA|Price CTA)\b|Get Started Now|\[VERIFY CURRENT\]", re.I)


def read(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def table_rows(md):
    for row in md.splitlines():
        if row.startswith("|") and not row.startswith("|---") and not re.match(r"^\|\s*Line", row):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if len(cells) >= 3:
                yield cells


def screen_from(md, current):
    lines, patterns, retired = OrderedDict(), [], []
    for cells in table_rows(md):
        line, status = cells[0].strip(" *`"), next((c for c in cells[1:] if any(s in c for s in ("❌", "⚠", "⏳", "✅", "Weak", "label"))), "")
        why = cells[-1] if cells[-1] is not status else ""
        if not status:
            continue
        if line.startswith('Any "') or line.lower().startswith("any ") or "anywhere" in " ".join(cells[1:2]).lower():
            words = re.findall(r'"([^"]+)"', line) or re.findall(r"“([^”]+)”", line)
            if words:
                patterns.append(OrderedDict([("re", r"\b(" + "|".join(re.escape(w.lower()) for w in words) + r")\b"), ("status", "❌"),
                                             ("why", why or "product rule (migrated)"), ("_review", "regex built from the old row: check it")]))
            continue
        for item in re.split(r"\s·\s|\s•\s", line):
            item = re.sub(r"^CTA:\s*", "", item).strip(' "*')
            if len(item.split()) < 2:
                continue
            if "❌ removed" in status or ("❌" in status and "removed" in why.lower()):
                retired.append(OrderedDict([("line", item), ("why", why or "removed from the bible")])); continue
            if "❌" in status and bm.norm(item) in current:
                lines[item] = OrderedDict([("status", "❌"), ("why", why)])
            elif "⚠" in status and bm.norm(item) in current:
                st = "⚠ Jeremy" if "Jeremy" in status else "⚠ Justin" if "Justin" in status else "⚠"
                if "Jeremy" in status and "Justin" in status: st = "⚠ Jeremy + Justin"
                lines[item] = OrderedDict([("status", st), ("why", why)])
    return lines, patterns, retired


def notes_from(md):
    """Hand prose between the banners and the pre-screen / VERBATIM markers (tables and banners dropped)."""
    out, skipping = [], False
    for ln in md.splitlines():
        if re.match(r"^#{1,2} .*(VERBATIM|Verbatim)", ln) or ln.startswith("# VERBATIM"):
            break
        if ln.startswith("> **") or ln.startswith("> Source") or ln.startswith(">"):
            continue
        if re.match(r"^## Compliance pre-screen", ln):
            skipping = True; continue
        if skipping and ln.startswith("## "):
            skipping = False
        if skipping or ln.startswith("|") or ln.startswith("# "):
            continue
        if OFFER_LINE.search(ln) and not ln.startswith("#"):
            out.append("- (offer / CTA / price facts: see `references/bible.json`, regenerated from the bible on every sync)")
            continue
        out.append(ln)
    text = re.sub(r"(- \(offer / CTA / price facts[^\n]*\n)(?:\s*\1)+", r"\1", "\n".join(out))
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def hard_stops_from(brief):
    body, on = [], False
    for ln in brief.splitlines():
        if ln.startswith("## Hard stops"):
            on = True; continue
        if on and ln.startswith("## "):
            break
        if on:
            body.append(ln)
    bullets, cur = [], []
    for ln in body:
        if ln.startswith("- "):
            if cur: bullets.append(cur)
            cur = [ln]
        elif cur and ln.strip():
            cur.append(ln)
    if cur: bullets.append(cur)
    keep = []
    for b in bullets:
        first = b[0]
        if "Lines the bible pre-screen marks" in first:
            continue
        if OFFER_LINE.search(" ".join(b)) and re.match(r"^- \*{0,2}(Offer|CTA|Default CTA)", first):
            continue
        keep.append("\n".join(b))
    return "\n".join(keep).strip()


def old_verbatim_items(md):
    on, items = False, []
    for ln in md.splitlines():
        if re.match(r"^#{1,2} .*(VERBATIM|Verbatim)", ln):
            on = True; continue
        if on and (ln.startswith("- ") or re.match(r"^\d+\.\s", ln)):
            t = re.sub(r"^(\d+\.|-)\s*", "", ln).lstrip("—-• ").strip()
            t = re.sub(r"^CTA:\s*", "", t)
            t, _ = bm.split_badges(t)
            if 2 <= len(t.split()) <= 12 and not t.startswith("*") and not re.search(r"\bX%|current % savings|PLACEHOLDER", t, re.I):
                items.append(t)
    return items


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--only", default=""); ap.add_argument("--dry", action="store_true"); a = ap.parse_args()
    only = {s for s in a.only.split(",") if s}
    model = bm.load()
    for d in sorted(os.listdir(SKILLS)):
        pj_p = os.path.join(SKILLS, d, "product.json")
        if not d.startswith("everlife-") or not os.path.exists(pj_p):
            continue
        prod = json.load(open(pj_p), object_pairs_hook=OrderedDict); pid = prod.get("id")
        if only and pid not in only and d not in only:
            continue
        refs = os.path.join(SKILLS, d, "references")
        secs = SECTIONS.get(pid) or bm.sections_of(prod)
        prod2 = OrderedDict()
        for k, v in prod.items():
            if k == "bible_section":
                continue
            prod2[k] = v
            if k == "name":
                prod2["bible_sections"] = secs
        if "bible_sections" not in prod2:
            prod2["bible_sections"] = secs
        merged = bm.merge(bm.pages_for(model, prod2))
        current = set()
        for f in ("headlines", "quick_hits", "more_benefits", "ctas", "offers", "proof", "hard_nos", "direction"):
            current |= {bm.norm(i["text"] if isinstance(i, dict) else i) for i in merged[f]}
        for items in merged["ingredient_claims"].values():
            current |= {bm.norm(i["text"]) for i in items}
        old = read(os.path.join(refs, "product-bible.md")); brief = read(os.path.join(refs, "product-brief.md"))
        lines, patterns, retired = screen_from(old, current)
        for t in old_verbatim_items(old):
            if bm.norm(t) not in current and bm.norm(t) not in {bm.norm(r["line"]) for r in retired}:
                retired.append(OrderedDict([("line", t), ("why", "was in the skill's old verbatim copy, no longer in the bible")]))
        screen = OrderedDict([
            ("_about", "Hand overrides only (migrated 2026-11-05 from the old pre-screen table). lines: {bible line: {status ❌|⚠ …, why}}; "
                       "patterns: product regexes [{re, status, why}]; retired: lines gone from the bible that stay refused. Everything else is derived "
                       "from the bible's badges and core/scripts/hard_nos.py by build_product_bibles.py."),
            ("lines", lines), ("patterns", patterns), ("retired", retired)])
        notes = notes_from(old); hs = hard_stops_from(brief)
        print(f"== {d}: sections {secs} · overrides {len(lines)} · patterns {len(patterns)} (review) · retired {len(retired)} · notes {len(notes.splitlines())} lines · hard stops {len(hs.splitlines())} lines")
        for r in retired: print(f"     retired: {r['line']}")
        for p in patterns: print(f"     pattern: {p['re']}  ({p['why'][:50]})")
        if a.dry:
            continue
        bk = os.path.join(ORIG, d, "references"); os.makedirs(bk, exist_ok=True)
        for f in ("product-bible.md", "product-brief.md"):
            if os.path.exists(os.path.join(refs, f)): shutil.copy2(os.path.join(refs, f), os.path.join(bk, f))
        shutil.copy2(pj_p, os.path.join(ORIG, d, "product.json"))
        open(os.path.join(refs, "bible-screen.json"), "w", encoding="utf-8").write(json.dumps(screen, indent=1, ensure_ascii=False) + "\n")
        open(os.path.join(refs, "product-notes.md"), "w", encoding="utf-8").write(
            f"# {prod.get('name', pid)}: hand notes (kept by hand; appended to the generated product-bible.md)\n\n"
            "Offer, CTAs, benefits, headlines and the disclaimer come from `references/bible.json` (generated from the bible); never restate them here.\n\n" + notes + "\n")
        open(os.path.join(refs, "hard-stops.md"), "w", encoding="utf-8").write(
            f"# {prod.get('name', pid)}: product hard stops (hand; the brief adds the bible facts from bible.json)\n\n" + hs + "\n")
        open(pj_p, "w", encoding="utf-8").write(json.dumps(prod2, indent=1, ensure_ascii=False) + "\n")
    print("\nbackups in", ORIG)


if __name__ == "__main__":
    main()
