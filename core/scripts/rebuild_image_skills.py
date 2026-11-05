#!/usr/bin/env python3
"""Rebuild every product skill's IMAGE side from the shared golden flow (core/references/image-flow.md).

    rebuild_image_skills.py [--only pt-141,nad] [--dry]

Per skill (never everlife-new-product):
  * references/image-batch.md  -> rewritten: pointer to image-flow.md + this product's §0 copy rules (kept verbatim) +
    product facts from product.json + its own reference files. Everything duplicated from the shared flow is removed.
  * SKILL.md -> image-only banners removed (layout zones, both sizes, reposition, show-first, mood, focal: all enforced by
    the gates + code), the "IMAGE ADS → Batch Mode" section replaced by one pointer, Step 1 = one question for images;
    the old Step 1 is kept verbatim below it as the VIDEO setup (videos untouched, Mitansh 2026-11-05), minus its
    image-only rounds.
Originals go to _originals/<date>/image-skill-rebuild/<skill>/ (repo convention).
"""
import argparse, json, os, re, shutil, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SKILLS = os.path.join(REPO, 'skills')
DATE = time.strftime('%Y-%m-%d')
ORIG = os.path.join(REPO, '_originals', DATE, 'image-skill-rebuild')

IMAGE_BANNER_KEYS = ('PROMPT LAYOUT ZONES', 'BOTH SIZES AT ONCE', 'NEVER `reposition_916.py`', 'SHOW FIRST, THEN RE-ROLL',
                     'MOOD =', 'FOCAL-POINT MIX', 'Both sizes at once', 'FOCAL MIX', 'IMAGE STYLE LIBRARY', 'STYLE LIBRARY')
INTIMACY = {'pt-141', 'lovara', 'spark', 'titan-rx'}
HARDCORE = {'sermorelin', 'sermorelin-ghk', 'bpc-157', 'wolverine', 'spartan'}
METABOLIC = {'glp-1', 'nad', 'mots-c', 'epithalon'}
SKIN = {'ghk-cream'}


def fam(pid):
    return ('intimacy' if pid in INTIMACY else 'men' if pid in HARDCORE else 'metabolic' if pid in METABOLIC
            else 'skin' if pid in SKIN else 'generic')


def section(text, start_pat, end_pat=r'^## '):
    """Return the block from the heading matching start_pat up to the next heading matching end_pat."""
    lines = text.splitlines()
    out, on = [], False
    for ln in lines:
        if not on and re.match(start_pat, ln):
            on = True; out.append(ln); continue
        if on:
            if re.match(end_pat, ln): break
            out.append(ln)
    return '\n'.join(out).rstrip() + ('\n' if out else '')


def backup(skill_dir, rel):
    src = os.path.join(skill_dir, rel)
    if not os.path.exists(src): return
    dst = os.path.join(ORIG, os.path.basename(skill_dir), rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if not os.path.exists(dst): shutil.copy2(src, dst)


def build_image_batch(skill_dir, pid, prod, old):
    name = prod.get('name', pid)
    copy_rules = section(old, r'^## 0\. ') if old else ''
    if not copy_rules:
        copy_rules = ("## 0. Copy rules (product-specific)\nClaims, headlines, CTAs and offers only from `references/product-bible.md` "
                      "(its pre-screen table: ✅ use · ⚠ explicit OK + Jeremy · ❌ never) and `core/references/global-rules.md`.\n")
    else:
        copy_rules = re.sub(r'^## 0\. .*$', '## 0. Copy rules (product-specific; kept from the original skill)', copy_rules, count=1, flags=re.M)

    renders = prod.get('renders', {}) or {}
    forms = prod.get('forms', {}) or {}
    hero = prod.get('hero', {}) or {}
    facts = [f"- **Product:** {name} (`{pid}`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`."]
    if renders:
        facts.append("- **Renders to attach (assets/):** " + ", ".join(f"{k}: `{v}`" for k, v in renders.items() if v) + ". Use them exactly; never describe the pill's shape or markings in text.")
    if forms and len(forms) > 1:
        facts.append("- **Forms (one per ad; the image question asks which):** " + "; ".join(f"**{k}** = {v.get('label', k)} (bottle `{v.get('bottle')}`{', pill `' + v['pill'] + '`' if v.get('pill') else ''})" for k, v in forms.items() if isinstance(v, dict)))
    if hero:
        facts.append(f"- **Hero:** {hero.get('element', '')}; min width {hero.get('min_width', 0.35)} of canvas; never: {hero.get('never', 'covered, blurred, mirrored')}.")
    f = fam(pid)
    fam_line = {
        'men': "- **Cast & mood:** men's slots follow `core/references/hardcore-men.md` (the dealer tags 40% HARDCORE); women's slots pinks, tans, beige. Copy never ties the body to the product.",
        'intimacy': "- **Cast & mood:** tasteful, product-led; people clothed, shoulder-up/waist-up, daylight; never a bed or bedroom; no body shots. The dealer filters those worlds out.",
        'metabolic': "- **Cast & mood:** active adults 30–65, bright real rooms; no body-composition or targeted fat-loss claims, no before/after.",
        'skin': "- **Cast & mood:** women's palette (pinks, tans, beige, cream); no oranges or greens; 'glow' is a mood, never a skin promise.",
        'generic': "- **Cast & mood:** real people 45–65, warm sun-lit candid rooms.",
    }[f]
    facts.append(fam_line)
    facts.append(f"- **World translation family for the dealer:** `{f}` (each world card's `translate.{f}` line, else `translate.generic`).")

    refs = []
    for rel, why in [('references/product-bible.md', 'every claim, headline, CTA, offer'),
                     ('references/winners/winners.md', 'reference level 1: our own winners, open first'),
                     ('references/team-refs', 'the team\'s own approved statics for this product'),
                     ('references/pinterest', 'category references (layout + idea only)'),
                     ('references/personas.md', 'the critique pass per ad'),
                     ('references/mens-direction.md', "men's ads"),
                     ('references/lessons.md', 'paid-for mistakes; read before writing'),
                     ('references/reviews.md', 'any review world (verbatim ✅ reviews only)'),
                     ('assets/RENDERS.md', 'what each render is')]:
        if os.path.exists(os.path.join(skill_dir, rel)):
            refs.append(f"| `{rel}` | {why} |")
    refs_tbl = "| File | Read for |\n|---|---|\n" + "\n".join(refs) if refs else "(no product reference files yet: run the reference harvest)"

    return f"""# {name} IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product {pid}`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to {name}.

{copy_rules}
## 1. Product facts for the prompt
{chr(10).join(facts)}

## 2. This product's references
{refs_tbl}

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product {pid} --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/{name}/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/{pid}-copy-log.md`;
`deal_worlds.py --product {pid} --n <N> --log` once approved.
"""


NEW_STEP1 = """## Step 1 — Setup (one question for images; video setup unchanged below)
**Question A, alone:** "What are we making?" → "🖼️ Image ads: 8 in both sizes (Recommended)" / "🎬 Video ad" / "🧑‍💼 AI Avatar Video" / "🔁 Remake one of ours".
- **Images** → `core/references/image-flow.md` §1: ONE AskUserQuestion (how many · **direction: 🎲 Surprise me first, then three
  inspirations you pitch for this product from `core/references/world-deck/INSPIRATIONS.md`** · who's in them: men / women / mix
  only for products made for both · form or strength, only if the product has several), then `deal_worlds.py` deals the mix (following the chosen direction) and you write every ad from its slot.
  Never ask for mood, palette, copy density, boldness, hook angle, placement or framework. This product's facts, hard stops and
  references: `references/product-brief.md`.
- **Video / Avatar** → the video setup below, unchanged.

"""


def rebuild_skill_md(text):
    lines = text.splitlines(keepends=True)
    out, i = [], 0
    # 1. drop image-only banners (single-line "> **…**" paragraphs near the top)
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('> **') and any(k in ln for k in IMAGE_BANNER_KEYS):
            i += 1
            while i < len(lines) and lines[i].strip() == '': i += 1
            continue
        out.append(ln); i += 1
    text = ''.join(out)
    # 2. replace "## 🖼️ IMAGE ADS → Batch Mode" section with a pointer
    text = re.sub(r'^## 🖼️ IMAGE ADS → Batch Mode\n(?:(?!^## ).*\n?)*',
                  '## 🖼️ Image ads\nFollow `core/references/image-flow.md` with this product\'s `references/image-batch.md`. Both sizes every run; finishing in code.\n\n',
                  text, flags=re.M)
    # 3. Step 1: insert the new one and demote the old to the video setup, minus its image rounds
    m = re.search(r'^## Step 1 — .*\n', text, flags=re.M)
    if m:
        start = m.start()
        nxt = re.search(r'^## ', text[m.end():], flags=re.M)
        end = m.end() + nxt.start() if nxt else len(text)
        old = text[m.end():end]
        # strip image-only rounds and mood banners inside the old step
        old = re.sub(r'^\*\*Round 2 \(images\).*?(?=^\*\*Round 2 \(video\)|^## |\Z)', '', old, flags=re.M | re.S)
        old = re.sub(r'^> \*\*🎨 MOOD.*\n', '', old, flags=re.M)
        old = re.sub(r'^- \*\*Images\*\* → .*\n', '', old, flags=re.M)
        old = re.sub(r'^\d+\. \*\*What are we making\?\*\*.*\n', '', old, flags=re.M)
        old = re.sub(r'^\*\*Never asked:\*\*.*?\n\n', '', old, flags=re.M | re.S)
        old = re.sub(r'^\*\*Question A, alone:\*\*.*\n', '', old, flags=re.M)
        video = '### Video setup (unchanged; images never use these questions)\n' + old.lstrip('\n')
        text = text[:start] + NEW_STEP1 + video + text[end:]
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', default='')
    ap.add_argument('--dry', action='store_true')
    a = ap.parse_args()
    only = {s.strip() for s in a.only.split(',') if s.strip()}
    done = []
    for d in sorted(os.listdir(SKILLS)):
        if not d.startswith('everlife-') or d == 'everlife-new-product': continue
        pid = d[len('everlife-'):]
        if only and pid not in only: continue
        skill_dir = os.path.join(SKILLS, d)
        pj = os.path.join(skill_dir, 'product.json')
        prod = json.load(open(pj)) if os.path.exists(pj) else {'name': pid}
        ib = os.path.join(skill_dir, 'references', 'image-batch.md')
        old = open(ib).read() if os.path.exists(ib) else ''
        new_ib = build_image_batch(skill_dir, pid, prod, old)
        sk = os.path.join(skill_dir, 'SKILL.md')
        new_sk = rebuild_skill_md(open(sk).read())
        if a.dry:
            print(f"{d}: image-batch {len(old.splitlines())} → {len(new_ib.splitlines())} lines; SKILL.md {len(open(sk).read().splitlines())} → {len(new_sk.splitlines())}")
            continue
        backup(skill_dir, 'references/image-batch.md'); backup(skill_dir, 'SKILL.md')
        os.makedirs(os.path.dirname(ib), exist_ok=True)
        open(ib, 'w').write(new_ib); open(sk, 'w').write(new_sk)
        done.append(d)
        print(f"✅ {d}: image-batch.md {len(old.splitlines())} → {len(new_ib.splitlines())} lines · SKILL.md rebuilt")
    if done: print(f"\n{len(done)} skills rebuilt; originals in {ORIG}")


if __name__ == '__main__':
    main()
