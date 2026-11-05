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
  * BIBLE PIPELINE (2026-11-05): references/bible.json + product-bible.md + product-brief.md are generated from the synced bible
    and carry its version; no hand "Bible sync" banners; product.json disclaimer == the bible's; bible_sections resolve;
    bible-screen.json is valid and names only current lines; hard-stops.md carries no offer/CTA; no prose file quotes a % or a
    CTA that is not the product's current one or quotes a retired line; the gates' numbers match the bible
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SKILLS = os.path.join(REPO, 'skills')
CORE = os.path.join(REPO, 'core')
sys.path.insert(0, HERE)
import bible_model as bm  # noqa: E402

BANNER = re.compile(r'^> \*\*(Bible sync|CTA update|Price CTA|APPROVED UPDATE)', re.M)
PROSE_FILES = ['SKILL.md', 'references/product-notes.md', 'references/personas.md', 'references/video-prompting.md', 'references/image-batch.md',
               'references/reference-guide.md', 'references/hook-bank.md', 'references/finishing.md', 'references/image-prompting.md']   # lessons.md / reviews / winners are history
EXEMPT = re.compile(r'never|banned|removed|retired|left the bible|not |no |was |old |previous|used to|history|reference only|maximum', re.I)


def bible_checks(sd, pj, repo_version, model, errs, warns):
    """The bible pipeline's per-skill rules (all errors: the generators are the fix, `bible_pipeline.py regen`)."""
    bj_p = os.path.join(sd, 'references', 'bible.json'); pb_p = os.path.join(sd, 'references', 'product-bible.md')
    br_p = os.path.join(sd, 'references', 'product-brief.md'); sc_p = os.path.join(sd, 'references', 'bible-screen.json')
    hs_p = os.path.join(sd, 'references', 'hard-stops.md')
    if not pj.get('bible_sections'):
        errs.append('product.json: no "bible_sections" (the bible page headings this product is generated from)'); return
    try:
        bm.pages_for(model, pj)
    except SystemExit as e:
        errs.append(str(e)); return
    if not os.path.exists(bj_p):
        errs.append('no references/bible.json: run bible_pipeline.py regen'); return
    try:
        bj = json.load(open(bj_p, encoding='utf-8'))
    except ValueError:
        errs.append('references/bible.json is not valid JSON'); return
    if bj.get('version') != repo_version:
        errs.append(f'references/bible.json is from bible version {bj.get("version")}, the synced bible is {repo_version}: run bible_pipeline.py regen')
    for p_, label in ((pb_p, 'product-bible.md'), (br_p, 'product-brief.md')):
        if not os.path.exists(p_): errs.append(f'no references/{label}: run bible_pipeline.py regen'); continue
        head = open(p_, encoding='utf-8').readline()
        if 'GENERATED' not in head and 'generated' not in head: errs.append(f'references/{label} is not the generated file (line 1)')
        elif repo_version not in head: errs.append(f'references/{label} carries another bible version than {repo_version}: run bible_pipeline.py regen')
    if bm.norm(pj.get('disclaimer', '')) != bm.norm(bj.get('disclaimer', '')):
        errs.append('product.json disclaimer differs from the bible (bible.json): run bible_pipeline.py regen')
    if bj.get('cta_default') and bm.norm(bj['cta_default']) not in {bm.norm(c) for c in bj.get('ctas', [])}:
        errs.append(f'bible.json cta_default "{bj["cta_default"]}" is not one of its ctas')
    current = {bm.norm(x) for x in bj.get('ctas', []) + bj.get('benefits_quick', []) + bj.get('proof', []) + bj.get('offer_lines', [])}
    current |= {bm.norm(x['text']) for x in bj.get('benefits_more', []) + bj.get('headlines', [])}
    for items in (bj.get('ingredient_claims') or {}).values(): current |= {bm.norm(x) for x in items}
    if os.path.exists(sc_p):
        try:
            sc = json.load(open(sc_p, encoding='utf-8'))
            for k in (sc.get('lines') or {}):
                if bm.norm(k) not in current: errs.append(f'bible-screen.json "lines" names "{k}", which is no longer in the bible: move it to "retired"')
            for pat in (sc.get('patterns') or []):
                try: re.compile(pat.get('re', ''))
                except re.error as e: errs.append(f'bible-screen.json pattern {pat.get("re")!r} does not compile: {e}')
        except ValueError:
            errs.append('references/bible-screen.json is not valid JSON')
    if not os.path.exists(hs_p): errs.append('no references/hard-stops.md (hand product hard stops; migrate_bible_extracts.py creates it)')
    elif re.search(r'Save [Uu]p to \d+%|\$\d+\.\d\d/day|^- \*{0,2}CTA', open(hs_p, encoding='utf-8').read(), re.M):
        errs.append('hard-stops.md restates an offer / CTA / price: those come from bible.json only')
    for rel in ['references/product-bible.md', 'references/product-brief.md', 'SKILL.md'] + PROSE_FILES:
        p_ = os.path.join(sd, rel)
        if not os.path.exists(p_): continue
        txt = open(p_, encoding='utf-8').read()
        if BANNER.search(txt): errs.append(f'{rel} carries a hand "Bible sync" banner: generated / hand notes never do (the bible is synced by regeneration)')
    offer = bj.get('offer') or {}; pct = offer.get('pct') if offer.get('status') == 'ok' else None
    retired = {bm.norm(r['line'] if isinstance(r, dict) else r): (r['line'] if isinstance(r, dict) else r) for r in bj.get('retired', [])}
    for rel in PROSE_FILES:
        p_ = os.path.join(sd, rel)
        if not os.path.exists(p_): continue
        for i, ln in enumerate(open(p_, encoding='utf-8').read().splitlines(), 1):
            low = bm.norm(ln)
            if EXEMPT.search(ln): continue
            for m in re.finditer(r'save up to (\d+)\s*%', low):
                if pct is None: errs.append(f'{rel}:{i} quotes "Save Up to {m.group(1)}%" but the bible has no usable offer for this product ({offer.get("status")})')
                elif int(m.group(1)) != pct: errs.append(f'{rel}:{i} quotes "Save Up to {m.group(1)}%": the bible says {pct}% (read it from bible.json)')
            for n, orig in retired.items():
                if len(n.split()) >= 2 and n in low: errs.append(f'{rel}:{i} quotes the retired line "{orig}"')


def global_checks(model, errs):
    """The numbers the gates and global rules copy from the bible must still match it."""
    g = model['globals']
    gates = open(os.path.join(CORE, 'claude', 'everlife-gates.md'), encoding='utf-8').read()
    for prod, pct in g.get('discount_to_feature', {}).items():
        if not re.search(re.escape(prod) + r'\s+' + str(pct) + r'%', gates):
            errs.append(f'everlife-gates.md discount table: "{prod} {pct}%" (bible) not found')
    if g.get('proof_split') and not re.search(r'%s%% trust.*%s%%.*%s%%' % tuple(g['proof_split']), gates, re.S):
        errs.append(f'everlife-gates.md proof split differs from the bible {g["proof_split"]}')
    if g.get('focal') and not re.search(r'%s%% pill.*%s%% bottle.*%s%% person' % tuple(g['focal']), gates, re.S):
        errs.append(f'everlife-gates.md focal mix differs from the bible {g["focal"]}')
    if g.get('logo') and not re.search(r'9:16 = %s%% .* 4:5 = %s%%' % (g['logo'].get('9:16'), g['logo'].get('4:5')), gates):
        errs.append(f'everlife-gates.md logo widths differ from the bible {g["logo"]}')
    if g.get('min_text_px') and f'{g["min_text_px"]} px' not in gates:
        errs.append(f'everlife-gates.md minimum text size differs from the bible ({g["min_text_px"]} px)')
    if g.get('shirtless_cap') and f'{g["shirtless_cap"]}%' not in gates:
        errs.append(f'everlife-gates.md shirtless cap differs from the bible ({g["shirtless_cap"]}%)')

STALE = {
    r'reposition_916': 'banned tool (smeared edges, Mitansh 2026-11-02)',
    r'top 12%': 'old layout number (zones file: top 16%)',
    r'\b76%': 'old layout number',
    r'Unlimited[- ]mode': 'expired temporary route (Oct 29 + 4 days)',
    r'Round 2 \(images\)': 'old two-round image setup',
    r'GHK-Cu(?![ -]Cream)': 'naming Hard NO (GHK, never GHK-Cu) outside the cream product name',
    r'Provider-Guided From Home': 'unapproved line the team QA keeps flagging',
    r'Tier [AB]\b': 'headline tiers are gone: bible headlines are references, wording is free (Mitansh 2026-11-05)',
    r'Get Started Now': 'banned CTA (bible 2026-11-03)',
}
IMAGE_BANNERS = ('PROMPT LAYOUT ZONES', 'BOTH SIZES AT ONCE', 'NEVER `reposition_916', 'SHOW FIRST, THEN RE-ROLL', 'MOOD =', 'FOCAL-POINT MIX')
SHARED = ['core/references/image-flow.md', 'core/references/world-deck/worlds.json', 'core/scripts/deal_worlds.py',
          'core/scripts/bible_model.py', 'core/scripts/hard_nos.py', 'core/scripts/build_product_bibles.py', 'core/scripts/bible_pipeline.py',
          'core/scripts/product_copy.py', 'core/claude/creative-bible.md',
          'core/references/world-deck/INSPIRATIONS.md', 'core/references/ENGINE.md', 'core/references/variations/README.md',
          'core/references/prompt-layout-zones.md', 'core/references/global-rules.md']


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--strict', action='store_true'); a = ap.parse_args()
    missing = [s for s in SHARED if not os.path.exists(os.path.join(REPO, s))]
    if missing:
        print('❌ shared files missing: ' + ', '.join(missing)); sys.exit(1)
    # the run contract: the shared flow must keep every bare-minimum step (Mitansh 2026-11-05)
    flow = open(os.path.join(REPO, 'core/references/image-flow.md')).read()
    CONTRACT = ['9:16 AND 4:5', 'finish_batch.py', '--proof-plan', '--proof-check', '--proof <slot proof>', 'teamlog.py gens', 'teamlog.py qa',
                'teamlog.py copy', 'teamlog.py proof', 'teamlog.py run', 'teamlog.py close', 'teamlog.py sent', 'teamlog.py posted',
                'teamlog.py summary', 'Ad Review', 'SESSION.md', 'lessons.md', 'STRICT LAYOUT', '1385', 'AI disclosure', 'copy-log',
                'deal_worlds.py', 'preflight.sh', 'free-fix', 'contact sheet', 'includes one re-make', 'batch_check.py', 'never render: everlife slot=', 'deal.json', 'Strength', 'Next batch', 'next_asked.json']
    lost = [t for t in CONTRACT if t not in flow]
    if lost:
        print('❌ image-flow.md lost bare-minimum step(s): ' + ', '.join(lost)); sys.exit(1)
    print('✅ image-flow.md run contract: all %d bare-minimum steps present' % len(CONTRACT))
    model = bm.load(); repo_version = model['version']
    gerrs = []; global_checks(model, gerrs)
    for e in gerrs: print('❌ global: ' + e)
    bad_total = len(gerrs); warn_total = 0
    for d in sorted(os.listdir(SKILLS)):
        if not d.startswith('everlife-') or d in ('everlife-new-product', 'everlife-ads'): continue
        sd = os.path.join(SKILLS, d); errs, warns = [], []
        ib_p = os.path.join(sd, 'references', 'image-batch.md'); sk_p = os.path.join(sd, 'SKILL.md'); pj_p = os.path.join(sd, 'product.json')
        ib = open(ib_p).read() if os.path.exists(ib_p) else ''
        sk = open(sk_p).read() if os.path.exists(sk_p) else ''
        if not ib: errs.append('no references/image-batch.md')
        else:
            for needle, why in [('core/references/image-flow.md', 'does not follow the shared image flow'),
                                ('deal_worlds.py', 'does not deal worlds'),
                                ('9:16 AND 4:5', 'both sizes not stated'),
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
                    if re.search(r'never|banned|not |no |OVERRIDES|retired|removed', ctx, flags=re.I) and pat in (r'reposition_916', r'Unlimited[- ]mode', r'GHK-Cu(?![ -]Cream)', r'Provider-Guided From Home', r'Get Started Now'):
                        continue  # a line that forbids it is fine
                    errs.append(f'{name}:{line} {why}: "{ctx.strip()[:70]}"')
        if not os.path.exists(pj_p): errs.append('no product.json')
        else:
            pj = json.load(open(pj_p))
            if not pj.get('disclaimer') or len(pj['disclaimer']) < 40: errs.append('product.json: no verbatim disclaimer')
            if not pj.get('name'): errs.append('product.json: no name')
            if not any((pj.get('renders') or {}).values()): errs.append('product.json: no renders')
            if 'variations' not in pj: errs.append('product.json: no "variations" list (ENGINE.md)')
            if pj.get('audience') not in ('men', 'women', 'both'): errs.append('product.json: "audience" must be men / women / both (the dealer\'s default; ENGINE.md)')
            for v in pj.get('variations', []):
                if not os.path.exists(os.path.join(REPO, 'core', 'references', 'variations', v + '.md')) and not os.path.exists(os.path.join(REPO, 'core', 'references', v + '.md')):
                    errs.append(f'product.json: unknown variation "{v}"')
        pb_p = os.path.join(sd, 'references', 'product-brief.md')
        if not os.path.exists(pb_p): errs.append('no references/product-brief.md (run build_product_briefs.py)')
        elif '## Hard stops' not in open(pb_p).read(): errs.append('product-brief.md: no hard stops section')
        if os.path.exists(pj_p): bible_checks(sd, pj, repo_version, model, errs, warns)
        banners = re.findall(r'^> \*\*(?!Engine)', sk, flags=re.M)
        if banners: errs.append(f'SKILL.md carries {len(banners)} rule banner(s); only the Engine block is allowed')
        if 'core/references/golden-rules.md' not in sk: errs.append('SKILL.md does not point at golden-rules.md')
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
