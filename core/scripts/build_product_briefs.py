#!/usr/bin/env python3
"""Generate every skill's references/product-brief.md (the ONLY product file the image engine reads) and shrink
references/image-batch.md to a stub. Re-run after a bible sync or a product.json change.

    build_product_briefs.py [--only pt-141,nad] [--dry]

Brief = who it's for + creative direction + what it is (references/bible.json, generated from the bible) · variations (product.json) ·
product facts (renders, forms, hero) · hard stops (references/hard-stops.md, hand) + the bible facts block (offer, CTAs, benefits,
retired lines from bible.json) · this product's own references. Everything else is global (core/references/ENGINE.md).
"""
import argparse, json, os, re, shutil, time

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))
SKILLS = os.path.join(REPO, 'skills'); ORIG = os.path.join(REPO, '_originals', time.strftime('%Y-%m-%d'), 'product-briefs')
VARIATION_FILES = {
    'hardcore-men': 'core/references/hardcore-men.md', 'ultra-premium': 'core/references/ultra-premium.md',
    'vial-product': 'core/references/variations/vial-product.md', 'intimacy-tasteful': 'core/references/variations/intimacy-tasteful.md',
    'womens-palette': 'core/references/variations/womens-palette.md', 'peptide-stack': 'core/references/variations/peptide-stack.md',
    'two-forms': 'core/references/variations/two-forms.md', 'compounded-glp1': 'core/references/variations/compounded-glp1.md',
    'two-strengths': 'core/references/variations/two-strengths.md',
}


def section(text, start_pat, end_pat=r'^## '):
    out, on = [], False
    for ln in text.splitlines():
        if not on and re.match(start_pat, ln): on = True; out.append(ln); continue
        if on:
            if re.match(end_pat, ln): break
            out.append(ln)
    return '\n'.join(out).rstrip() + ('\n' if out else '')


def bible_json(skill_dir):
    """The product's generated copy (references/bible.json, written by build_product_bibles.py from the bible)."""
    p = os.path.join(skill_dir, 'references', 'bible.json')
    if not os.path.exists(p):
        raise SystemExit(f"❌ {p} missing: run build_product_bibles.py first (bible_pipeline.py regen)")
    return json.load(open(p, encoding='utf-8'))


def hard_stops(skill_dir):
    """references/hard-stops.md (hand: the product's own rules) + the bible facts block generated from bible.json."""
    p = os.path.join(skill_dir, 'references', 'hard-stops.md')
    if not os.path.exists(p):
        raise SystemExit(f"❌ {p} missing: run migrate_bible_extracts.py once, then keep it by hand")
    hand = '\n'.join(ln for ln in open(p, encoding='utf-8').read().splitlines() if not ln.startswith('# ')).strip()
    return hand


def bible_facts(bj):
    o = bj.get('offer') or {}
    out = [f"## Offer, CTAs and claims (from the bible, version {bj.get('version')}; generated, never edit)"]
    if o.get('status') == 'ok':
        out.append(f"- **Offer:** \"{o['cta']}\" is the product's highest discount (bible rule 09; source: {o.get('source')}). It is the default CTA. "
                   "Always \"Save Up to N%\", never a fixed discount, never another product's %.")
    else:
        out.append(f"- **Offer: none usable** ({o.get('status')}: {', '.join(o.get('lines') or []) or 'no offer line in the bible'}). "
                   "No %, no price, no \"Save Up to\" on this product until the bible carries a verified offer.")
    out.append(f"- **Default CTA:** \"{bj.get('cta_default')}\". **All bible CTAs:** " + ' · '.join(f'"{c}"' for c in bj.get('ctas', [])) +
               ". The gate refuses any other CTA string.")
    if bj.get('cta_price'):
        out.append(f"- **Price CTA (approved alternative; the only $ amount allowed):** \"{bj['cta_price']}\".")
    if o.get('variants'):
        out.append("- **Variant maximums (reference only, never shown as a lower %):** " + ', '.join(f"{k} {v}%" for k, v in o['variants'].items()) + '.')
    out.append("- **Quick-hit benefits (word for word, the only benefit lines):** " + ' · '.join(bj.get('benefits_quick', [])) + '.')
    more = [b['text'] for b in bj.get('benefits_more', []) if not b.get('badges')]
    if more:
        out.append("- **More approved benefits:** " + ' · '.join(more) + '.')
    if bj.get('hard_nos'):
        out.append("- **Product Hard NOs (bible):** " + ' · '.join(bj['hard_nos']))
    ret = [r['line'] if isinstance(r, dict) else r for r in bj.get('retired', [])]
    if ret:
        out.append("- **Retired, never use (left the bible or banned):** " + ' · '.join(ret) + '.')
    out.append("- **Disclaimer:** verbatim in `product.json` (= the bible's); the finisher lays it. Exact strings for pasting: `python3 core/scripts/product_copy.py <id>`.")
    return '\n'.join(out)


def build(skill_dir, pid, prod):
    name = prod.get('name', pid)
    bj = bible_json(skill_dir)
    who, direction = bj.get('who', ''), bj.get('direction', [])
    variations = prod.get('variations', [])
    renders = prod.get('renders', {}) or {}; forms = prod.get('forms', {}) or {}; hero = prod.get('hero', {}) or {}
    about = (prod.get('_about') or '').strip()

    out = [f"# {name}: product brief (generated by `core/scripts/build_product_briefs.py` from `product.json`, `references/bible.json` "
           f"(bible version {bj.get('version')}) and `references/hard-stops.md`; never edit this file: run `python3 core/scripts/bible_pipeline.py regen`)", "",
           f"The image engine is global: `core/references/image-flow.md` (flow), `core/references/world-deck/` (variety), "
           f"`core/references/global-rules.md` + the gates (compliance), `core/tools/` (finishing). This brief is everything that is specific to {name}.", ""]
    out += ["## Who it's for", who or "(the bible page has no 'Who it's for' line)", ""]
    if bj.get('truth'): out += ["## What it is (bible, one line)", bj['truth'], ""]
    if direction:
        out += ["## Creative direction (bible)"] + [f"- {d}" for d in direction] + [""]
    out += ["## Variations this product opts into"]
    out += [f"- `{v}` → `{VARIATION_FILES.get(v, '?')}`" for v in variations] or ["- none (global defaults only)"]
    out += ["", "## Product facts for the prompt"]
    if about: out.append(f"- **Settings note:** {about[:400]}")
    if renders: out.append("- **Renders (assets/):** " + ", ".join(f"{k}: `{v}`" for k, v in renders.items() if v) + ". Use them exactly; never describe the pill's shape or markings in text.")
    if forms and len(forms) > 1:
        out.append("- **Forms (one per ad):** " + "; ".join(f"**{k}** = {v.get('label', k)} (bottle `{v.get('bottle')}`{', pill `' + v['pill'] + '`' if v.get('pill') else ''})" for k, v in forms.items() if isinstance(v, dict)))
    strengths = {k: v for k, v in (prod.get('strengths') or {}).items() if isinstance(v, dict)}
    if len(strengths) > 1:
        out.append("- **Strengths (the image question asks; 'Either' = never mentioned, default bottle):** " + "; ".join(
            f"**{k} mcg** = bottle `{v.get('bottle')}` (label: {v.get('label', '')})" for k, v in sorted(strengths.items())) +
            ". \"Double Strength\" wording only with the 1000 mcg bottle in frame.")
    if hero: out.append(f"- **Hero:** {hero.get('element', '')}; min width {hero.get('min_width', 0.35)} of canvas; never: {hero.get('never', 'covered, blurred, mirrored')}.")
    out.append(f"- **Disclaimer:** verbatim in `product.json` (the finisher lays it). **Copy log:** `~/Everlife-Creative/{pid}-copy-log.md`. **Output:** `~/Everlife-Creative/output/{name}/`.")
    hs = hard_stops(skill_dir)
    out += ["", "## Headlines: references, not limits",
            "The bible's headlines, hooks and benefits in `references/product-bible.md` are inspiration for what this product does and how the brand talks. "
            "Write bold, fresh lines in each world's own voice. **The only fence is the Hard NOs** (global section 2 + the product's, below); Jeremy signs off on wording before anything goes live. No tiers, no per-line approvals (Mitansh 2026-11-05).", "",
            "## Hard stops (this product)", "- Lines the screening table marks ❌ / Hard NO conflict: never. Everything that is not a Hard NO is wording, and wording is free.",
            hs or "", "", bible_facts(bj), ""]
    refs = [(rel, why) for rel, why in [
        ('references/product-bible.md', 'the bible extract (generated): copy, screening table, verbatim section'),
        ('references/bible.json', 'the same as data (offer, CTAs, benefits, retired); `product_copy.py <id>` prints it'),
        ('references/product-notes.md', 'hand notes on the product'),
        ('references/winners/winners.md', 'reference level 1: our own winners, open first'),
        ('references/team-refs', "the team's approved statics for this product"),
        ('references/pinterest', 'category references (idea + layout only)'),
        ('references/personas.md', 'the critique pass per ad'),
        ('references/mens-direction.md', "men's ads"),
        ('references/lessons.md', 'paid-for mistakes; read before writing'),
        ('references/reviews.md', 'review worlds (verbatim ✅ reviews only)'),
        ('assets/RENDERS.md', 'what each render is')] if os.path.exists(os.path.join(skill_dir, rel))]
    out += ["## This product's references", "| File | Read for |", "|---|---|"] + [f"| `{r}` | {w} |" for r, w in refs] + [""]
    return "\n".join(out)


STUB = """# {name} IMAGE ads

Everything is in the engine: **`core/references/image-flow.md`** (one question → `deal_worlds.py --product {pid}` → write every ad
from its slot → 9:16 AND 4:5 in one run → `finish_batch.py --product {pid}` → QA → show). This product's facts, hard stops and
references: **`references/product-brief.md`**. Map of what is global vs per product: `core/references/ENGINE.md`.
"""


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--only', default=''); ap.add_argument('--dry', action='store_true'); a = ap.parse_args()
    only = {s for s in a.only.split(',') if s}
    for d in sorted(os.listdir(SKILLS)):
        if not d.startswith('everlife-') or d in ('everlife-new-product', 'everlife-ads'): continue
        pid = d[len('everlife-'):]
        if only and pid not in only: continue
        sd = os.path.join(SKILLS, d); pj = os.path.join(sd, 'product.json')
        prod = json.load(open(pj)) if os.path.exists(pj) else {'name': pid}
        brief = build(sd, pid, prod)
        if a.dry: print(f"{d}: brief {len(brief.splitlines())} lines, variations {prod.get('variations', [])}"); continue
        ib = os.path.join(sd, 'references', 'image-batch.md')
        if os.path.exists(ib):
            dst = os.path.join(ORIG, d, 'references', 'image-batch.md'); os.makedirs(os.path.dirname(dst), exist_ok=True)
            if not os.path.exists(dst): shutil.copy2(ib, dst)
        open(os.path.join(sd, 'references', 'product-brief.md'), 'w').write(brief)
        open(ib, 'w').write(STUB.format(name=prod.get('name', pid), pid=pid))
        print(f"✅ {d}: product-brief.md {len(brief.splitlines())} lines · image-batch.md → stub · variations {prod.get('variations', [])}")


if __name__ == '__main__':
    main()
