#!/usr/bin/env python3
"""Remove the rule banners and the per-skill "Golden rules" restatements from every SKILL.md; replace both with one Engine block.

    strip_skill_banners.py [--dry]

Mitansh 2026-11-05: "the skills had 10 different IMPORTANT claims which made the system very non-deterministic … the skills
should not be having all the bullshit stuff across all the products". Rules now live once: core/references/golden-rules.md,
ENGINE.md, the gates, global-rules.md, the video rule files. Video flow steps (3–6) are not touched.
Originals: _originals/<date>/strip-banners/<skill>/SKILL.md
"""
import argparse, os, re, shutil, time

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))
SKILLS = os.path.join(REPO, 'skills'); ORIG = os.path.join(REPO, '_originals', time.strftime('%Y-%m-%d'), 'strip-banners')

ENGINE_BLOCK = """> **Engine (2026-11-05):** this skill is a product brief on top of the shared Everlife engine; rules are never restated here.
> Images: `core/references/image-flow.md` + `references/product-brief.md` (one question, worlds dealt, both sizes, finished in code).
> Videos: `core/references/video-team-rules.md` · `video-winners.md` · `on-camera-speech.md` · `seedance-on-creatify.md` ·
> `car-throw-review.md` (tablet / capsule products) · `hook-engine/`. Exceptions this product opts into: `product.json` →
> `variations` (`core/references/ENGINE.md`). Golden rules: `core/references/golden-rules.md`. Compliance: the gates + `global-rules.md`.

"""


def strip(text):
    lines = text.splitlines(keepends=True)
    out, i = [], 0
    # keep frontmatter + H1
    while i < len(lines):
        out.append(lines[i]); i += 1
        if lines[i - 1].startswith('# '): break
    # drop blank lines and every "> **…" banner paragraph that follows the H1 (continuation lines start with ">" or are blank)
    while i < len(lines) and (lines[i].strip() == '' or lines[i].startswith('>')):
        i += 1
    out.append('\n'); out.append(ENGINE_BLOCK)
    rest = ''.join(lines[i:])
    # replace the "Golden rules" block (from a line containing 'Golden rules' up to the 'Read these' table intro) with a pointer
    rest = re.sub(r'^Golden rules[^\n]*\n(?:(?!^Read these|^## |^\| File)[^\n]*\n)*',
                  'Golden rules: `core/references/golden-rules.md` (one copy for every product). Product facts and hard stops: `references/product-brief.md`.\n\n',
                  rest, count=1, flags=re.M)
    return ''.join(out) + rest


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--dry', action='store_true'); a = ap.parse_args()
    for d in sorted(os.listdir(SKILLS)):
        if not d.startswith('everlife-'): continue
        p = os.path.join(SKILLS, d, 'SKILL.md')
        if not os.path.exists(p): continue
        old = open(p).read(); new = strip(old)
        nb_old = len(re.findall(r'^> \*\*', old, flags=re.M)); nb_new = len(re.findall(r'^> \*\*', new, flags=re.M))
        if a.dry: print(f"{d}: banners {nb_old} → {nb_new}; lines {len(old.splitlines())} → {len(new.splitlines())}"); continue
        dst = os.path.join(ORIG, d, 'SKILL.md'); os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst): shutil.copy2(p, dst)
        open(p, 'w').write(new)
        print(f"✅ {d}: banners {nb_old} → {nb_new}; lines {len(old.splitlines())} → {len(new.splitlines())}")


if __name__ == '__main__':
    main()
