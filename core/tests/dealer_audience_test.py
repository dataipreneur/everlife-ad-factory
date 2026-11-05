#!/usr/bin/env python3
"""Audience per product, in code (Mitansh 2026-11-05): product.json "audience" is the dealer's default; a men's / women's product
refuses the other gender; a 'both' batch alternates men / women over the person slots. Spends nothing; touches no ledger.

    python3 core/tests/dealer_audience_test.py
"""
import glob, json, os, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEALER = os.path.join(REPO, 'core', 'scripts', 'deal_worlds.py')
fails = []


def ok(name, cond):
    print(('✅ ' if cond else '❌ ') + name)
    if not cond: fails.append(name)


def deal(pid, n=8, audience=None, seed=7):
    cmd = [sys.executable, '-I', DEALER, '--product', pid, '--n', str(n), '--seed', str(seed), '--json']
    if audience: cmd += ['--audience', audience]
    env = dict(os.environ, EVERLIFE_WORLD_LEDGER='/nonexistent/world-ledger.jsonl')   # no ledger → no "recent worlds" skipping, no writes
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    return r.returncode, (json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip().startswith('[') else None), r.stderr + r.stdout


def persons(slots):
    return [s for s in slots if s['focal'] == 'person']


# 1. every product.json carries a valid audience
pjs = sorted(glob.glob(os.path.join(REPO, 'skills', 'everlife-*', 'product.json')))
bad = [os.path.basename(os.path.dirname(p)) for p in pjs if json.load(open(p, encoding='utf-8')).get('audience') not in ('men', 'women', 'both')]
ok(f'every product.json has audience men / women / both ({len(pjs)} products)', pjs and not bad)
if bad: print('   missing:', bad)

# 2. men's product: default casts men only; --audience women refused
rc, slots, out = deal('titan-rx')
ok('titan-rx default deal succeeds', rc == 0 and slots is not None)
if slots:
    ok('titan-rx: every person slot is a man', all(s['audience'] == 'men' and s['persona'].startswith(('man', 'shirtless', 'lifter')) for s in persons(slots)))
    ok('titan-rx: batch_audience = men', slots[0]['batch_audience'] == 'men')
rc, _, out = deal('titan-rx', audience='women')
ok('titan-rx --audience women is refused (exit ≠ 0, says "refused")', rc != 0 and 'refused' in out)

# 3. women's product: default casts women only; --audience men refused
rc, slots, out = deal('lovara')
ok('lovara default deal succeeds', rc == 0 and slots is not None)
if slots:
    ok('lovara: every person slot is a woman', all(s['audience'] == 'women' and s['persona'].startswith('woman') for s in persons(slots)))
rc, _, out = deal('lovara', audience='men')
ok('lovara --audience men is refused', rc != 0 and 'refused' in out)

# 4. both: default alternates over the PERSON slots, so a mix always shows both genders; explicit men / women honoured
for pid in ('pt-141', 'sermorelin', 'sermorelin-ghk'):
    rc, slots, out = deal(pid, n=8)
    ok(f'{pid} default deal succeeds', rc == 0 and slots is not None)
    if slots:
        ps = persons(slots)
        genders = {s['audience'] for s in ps}
        ok(f'{pid}: a Mix batch of 8 shows both men and women on its {len(ps)} person slots', len(ps) >= 2 and genders == {'men', 'women'})
        ok(f'{pid}: batch_audience = both', slots[0]['batch_audience'] == 'both')
    rc, slots, out = deal(pid, n=8, audience='women')
    ok(f'{pid} --audience women: women only', rc == 0 and slots and all(s['audience'] == 'women' for s in persons(slots)))
    rc, slots, out = deal(pid, n=8, audience='men')
    ok(f'{pid} --audience men: men only', rc == 0 and slots and all(s['audience'] == 'men' for s in persons(slots)))

# 5. hardcore (shirtless) only ever lands on a MAN's slot: across seeds, a Mix batch never pairs a woman with a hardcore persona,
#    and with 2+ person slots both genders still appear (the cap can't eat the woman's slot)
for pid in ('sermorelin', 'sermorelin-ghk', 'bpc-157'):
    bad, nomix = [], []
    for seed in range(1, 9):
        rc, slots, out = deal(pid, n=8, seed=seed)
        if rc != 0 or not slots: bad.append(seed); continue
        ps = persons(slots)
        if any(s['hardcore'] and s['audience'] != 'men' for s in slots): bad.append(seed)
        if len(ps) >= 2 and {s['audience'] for s in ps} != {'men', 'women'}: nomix.append(seed)
    ok(f'{pid}: 8 seeds × Mix of 8: hardcore only on men\'s slots', not bad)
    ok(f'{pid}: 8 seeds × Mix of 8: both genders on the person slots', not nomix)

# 6. hardcore cap still applies to the men's person slots only (never on a women-only batch)
rc, slots, out = deal('sermorelin', n=8, audience='women')
ok('sermorelin women-only batch: no hardcore (shirtless) slots', rc == 0 and slots and not any(s['hardcore'] for s in slots))

print(f"\n{len(fails)} failures" if fails else "\nall checks passed")
sys.exit(1 if fails else 0)
