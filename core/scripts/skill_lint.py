#!/usr/bin/env python3
"""Everlife skill lint: every product skill must have the same image flow and none of the known rot.

    skill_lint.py            # prints ✅ / ❌ per skill, exits 1 on any ❌
    skill_lint.py --strict   # warnings count as failures too

Checks (image side only; video text is not touched, Mitansh 2026-11-05):
  * references/image-batch.md points at core/references/image-flow.md and deal_worlds.py, names both sizes, has §0 copy rules
  * SKILL.md Step 1 is the one-question image flow; no image-only banners; no "Round 2 (images)" leftovers
  * no stale layout numbers / banned tool names / expired routes anywhere in the skill's image files
  * product.json has a verbatim disclaimer, a name and at least one render
  * the shared files the skill points at exist
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SKILLS = os.path.join(REPO, 'skills')
CORE = os.path.join(REPO, 'core')

STALE = {
    r'reposition_916': 'banned tool (smeared edges, Mitansh 2026-11-02)',
    r'top 12%': 'old layout number (zones file: top 16%)',
    r'\b76%': 'old layout number',
    r'Unlimited[- ]mode': 'expired temporary route (Oct 29 + 4 days)',
    r'Round 2 \(images\)': 'old two-round image setup',
    r'GHK-Cu(?![ -]Cream)': 'naming Hard NO (GHK, never GHK-Cu) outside the cream product name',
    r'Provider-Guided From Home': 'unapproved line the team QA keeps flagging',
}
IMAGE_BANNERS = ('PROMPT LAYOUT ZONES', 'BOTH SIZES AT ONCE', 'NEVER `reposition_916', 'SHOW FIRST, THEN RE-ROLL', 'MOOD =', 'FOCAL-POINT MIX')
SHARED = ['core/references/image-flow.md', 'core/references/world-deck/worlds.json', 'core/scripts/deal_worlds.py',
          'core/references/world-deck/INSPIRATIONS.md', 'core/references/ENGINE.md', 'core/references/variations/README.md',
          'core/references/prompt-layout-zones.md', 'core/references/global-rules.md']


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--strict', action='store_true'); a = ap.parse_args()
    missing = [s for s in SHARED if not os.path.exists(os.path.join(REPO, s))]
    if missing:
        print('❌ shared files missing: ' + ', '.join(missing)); sys.exit(1)
    bad_total = warn_total = 0
    for d in sorted(os.listdir(SKILLS)):
        if not d.startswith('everlife-') or d == 'everlife-new-product': continue
        sd = os.path.join(SKILLS, d); errs, warns = [], []
        ib_p = os.path.join(sd, 'references', 'image-batch.md'); sk_p = os.path.join(sd, 'SKILL.md'); pj_p = os.path.join(sd, 'product.json')
        ib = open(ib_p).read() if os.path.exists(ib_p) else ''
        sk = open(sk_p).read() if os.path.exists(sk_p) else ''
        if not ib: errs.append('no references/image-batch.md')
        else:
            for needle, why in [('core/references/image-flow.md', 'does not follow the shared image flow'),
                                ('deal_worlds.py', 'does not deal worlds'),
                                ('9:16 AND 4:5', 'both sizes not stated'),
                                ('## 0. Copy rules', 'no product copy rules section'),
                                ('finish_batch.py', 'no finishing command')]:
                if needle not in ib: errs.append(f'image-batch.md: {why}')
            if len(ib.splitlines()) > 120: warns.append(f'image-batch.md is {len(ib.splitlines())} lines (should hold product facts only)')
        if not sk: errs.append('no SKILL.md')
        else:
            if 'core/references/image-flow.md' not in sk: errs.append('SKILL.md Step 1 does not route images to image-flow.md')
            for b in IMAGE_BANNERS:
                if re.search(r'^> \*\*[^\n]*' + re.escape(b), sk, flags=re.M): errs.append(f'SKILL.md still carries the image banner "{b}"')
        for pat, why in STALE.items():
            for name, txt in (('image-batch.md', ib), ('SKILL.md', sk)):
                for m in re.finditer(pat, txt):
                    line = txt[:m.start()].count('\n') + 1
                    ctx = txt.splitlines()[line - 1]
                    if re.search(r'never|banned|not |no |OVERRIDES', ctx, flags=re.I) and pat in (r'reposition_916', r'Unlimited[- ]mode', r'GHK-Cu(?![ -]Cream)', r'Provider-Guided From Home'):
                        continue  # a line that forbids it is fine
                    errs.append(f'{name}:{line} {why}: "{ctx.strip()[:70]}"')
        if not os.path.exists(pj_p): errs.append('no product.json')
        else:
            pj = json.load(open(pj_p))
            if not pj.get('disclaimer') or len(pj['disclaimer']) < 40: errs.append('product.json: no verbatim disclaimer')
            if not pj.get('name'): errs.append('product.json: no name')
            if not any((pj.get('renders') or {}).values()): errs.append('product.json: no renders')
            if 'variations' not in pj: errs.append('product.json: no "variations" list (ENGINE.md)')
            for v in pj.get('variations', []):
                if not os.path.exists(os.path.join(REPO, 'core', 'references', 'variations', v + '.md')) and not os.path.exists(os.path.join(REPO, 'core', 'references', v + '.md')):
                    errs.append(f'product.json: unknown variation "{v}"')
        if not os.path.exists(os.path.join(sd, 'references', 'product-brief.md')): errs.append('no references/product-brief.md (run build_product_briefs.py)')
        if 'INSPIRATIONS.md' not in sk: errs.append('SKILL.md Step 1 does not offer the inspiration directions')
        for rel in ['references/product-bible.md']:
            if not os.path.exists(os.path.join(sd, rel)): errs.append(f'missing {rel}')
        if not os.path.isdir(os.path.join(sd, 'references', 'winners')) and not os.path.isdir(os.path.join(sd, 'references', 'team-refs')):
            warns.append('no winners/ or team-refs/: run the reference harvest')
        bad_total += len(errs); warn_total += len(warns)
        mark = '❌' if errs else ('⚠️ ' if warns else '✅')
        print(f'{mark} {d}' + (': ' + ' · '.join(errs + warns) if errs or warns else ''))
    print(f'\n{bad_total} errors, {warn_total} warnings')
    sys.exit(1 if bad_total or (a.strict and warn_total) else 0)


if __name__ == '__main__':
    main()
