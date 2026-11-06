#!/usr/bin/env python3
"""Regression test for the price-headline plan (core/scripts/price_plan.py, deal_worlds.py, the price rule in core/hooks/batch_hook.py).
Bible Standards 03, "Pricing & CTA mix": the daily price as a HEADLINE on 10% of creatives, Sermorelin's "Starting at $95/month" headline on 5%.
No credits, no network, never touches the real ledgers.

    python3 core/tests/price_plan_test.py      # prints ✅ per check, exits 1 on any failure

Proves: the shares and the monthly headline are read from the bible text (this test FAILS if Justin rewrites the rule, so it gets looked at) ·
the headline is built from each product's own bible price · a batch of 10 carries 1 daily + 1 monthly (Sermorelin) and small batches average
the share · held / price-less products get none · the dealer marks the slots and logs the batch · the gate refuses a price slot with another
headline, a price headline on any other slot, and a doubled price (headline + $ CTA), and stays silent on a correct prompt, on a bible CTA
elsewhere (rule 3) and on a deal.json from before the plan.
"""
import json, os, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, 'core', 'scripts'))
HOOK = os.path.join(REPO, 'core', 'hooks', 'batch_hook.py')
DEAL = os.path.join(REPO, 'core', 'scripts', 'deal_worlds.py')
PLAN = os.path.join(REPO, 'core', 'scripts', 'price_plan.py')
TOOL = 'mcp__plugin_creatify-ad-agent_creatify-ad-agent__composer_edit_image'
fails = []


def ok(name, cond):
    print(('✅ ' if cond else '❌ ') + name)
    if not cond: fails.append(name)


def run(args, env):
    return subprocess.run([sys.executable] + args, capture_output=True, text=True, env=env).stdout


def hook(cmd, payload, env):
    r = subprocess.run([sys.executable, HOOK, cmd], input=json.dumps(payload), capture_output=True, text=True, env=env)
    return json.loads(r.stdout) if r.stdout.strip() else {}


def prompt(slot, ratio, job, headline, cta):
    body = (f'Design a finished static ad for Sermorelin by Everlife … STRICT LAYOUT ({ratio}, 1152x2048), follow exactly: …\n'
            f'TEXT: render ONLY these strings, exactly as written:\n  Headline: "{headline}"\n  CTA (in a button): "{cta}"\n'
            f'Reference only, never render: everlife slot={slot} ratio={ratio} product=sermorelin job={job}')
    return {'tool_name': TOOL, 'tool_input': {'prompt': body}, 'session_id': 'sess-P'}


def denied(d):
    return d.get('hookSpecificOutput', {}).get('permissionDecision') == 'deny', d.get('hookSpecificOutput', {}).get('permissionDecisionReason', '')


def main():
    home = tempfile.mkdtemp(prefix='everlife-price-test-')
    env = dict(os.environ, EVERLIFE_CREATIVE=home, EVERLIFE_WORLD_LEDGER=os.path.join(home, 'world-ledger.jsonl'))
    env.pop('EVERLIFE_PRICE_LEDGER', None)
    os.environ.update(EVERLIFE_CREATIVE=home)
    import price_plan as pp
    ledger = pp.LEDGER
    ok('the test ledger sits in the temp folder', ledger.startswith(home))

    r = pp.rules()
    ok('the shares and the monthly headline are read from the bible text (not the fallback)', r['source'] == 'bible')
    ok('Rule 1: daily pricing on 10% of all creatives', abs(r['daily_share'] - 0.10) < 1e-9)
    ok('Rule 2: Sermorelin monthly on 5%, headline "Starting at $95/month"',
       r['monthly']['product'] == 'sermorelin' and abs(r['monthly']['share'] - 0.05) < 1e-9 and r['monthly']['headline'] == 'Starting at $95/month')

    for pid, want in [('sermorelin', 'Sermorelin for only $3.00/day'), ('sermorelin-ghk', 'Sermorelin GHK for only $4.25/day'),
                      ('ghk-cream', 'GHK Peptide Cream for only $1.50/day'), ('nad', 'NAD+ for only $3.25/day')]:
        ok(f"{pid}: the headline is built from the bible's own price", pp.daily_headline(pid)[0] == want)

    p = pp.plan('sermorelin', 10)
    ok('Sermorelin, a batch of 10: 1 daily-price ad and 1 monthly ad', p['daily']['count'] == 1 and p['monthly']['count'] == 1)
    q = pp.plan('pt-141', 10)
    ok('PT-141, a batch of 10: 1 daily-price ad and no monthly line', q['daily']['count'] == 1 and q['monthly'] is None)
    ok('the monthly line is Sermorelin only (not Sermorelin GHK)', pp.plan('sermorelin-ghk', 10)['monthly'] is None)
    ok('a batch of 4 carries none the first time', pp.plan('sermorelin', 4)['daily']['count'] == 0)

    tot_d = tot_m = 0
    for _ in range(5):                                  # five batches of 4 = 20 ads → 2 daily (10%) and 1 monthly (5%)
        k = pp.plan('sermorelin', 4)
        d, m = k['daily']['count'], k['monthly']['count']
        pp.log('sermorelin', 4, d, m)
        tot_d, tot_m = tot_d + d, tot_m + m
    ok('five batches of 4 (20 ads): 2 daily-price + 1 monthly in total', (tot_d, tot_m) == (2, 1))
    ok('another product is counted on its own', pp.plan('pt-141', 10)['ads_before'] == 0)

    for pid, word in [('titan-rx', 'VERIFY'), ('spark', 'Pending')]:
        k = pp.plan(pid, 10)
        ok(f'{pid} is on hold: no daily-price headline, and it says why', k['daily']['count'] == 0 and word in k['daily']['why_not'])
    k = pp.plan('spartan', 10)
    ok('Spartan has no daily price on its bible page: none', k['daily']['count'] == 0 and 'no daily price' in k['daily']['why_not'])

    os.remove(ledger)
    with open(ledger, 'w') as f:
        f.write(json.dumps({'product': 'sermorelin', 'ads': 10, 'price': 1}) + '\n')   # a row from the CTA version of this plan
    ok('rows written by the earlier CTA version still count as daily-price ads', pp.plan('sermorelin', 10)['daily']['count'] == 1)
    os.remove(ledger)

    deal = run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4', '--json'], env)
    slots = json.loads(deal)
    daily = [s for s in slots if s['headline_kind'] == 'daily']
    monthly = [s for s in slots if s['headline_kind'] == 'monthly']
    free = [s for s in slots if s['headline_kind'] == 'free']
    ok('the dealer marks 1 daily, 1 monthly and 8 free slots of 10', (len(daily), len(monthly), len(free)) == (1, 1, 8))
    ok('the price slots carry the exact headline, the free slots none',
       daily[0]['headline'] == 'Sermorelin for only $3.00/day' and monthly[0]['headline'] == 'Starting at $95/month' and all(s['headline'] is None for s in free))
    ok('every slot keeps the default offer CTA (no $ CTA is dealt)', all(s['cta'] == 'Save Up to 65%' for s in slots))
    ok('a dealing without --log leaves the ledger alone', not os.path.exists(ledger))
    again = json.loads(run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4', '--json'], env))
    ok('a seeded deal is repeatable, price slots included', [s['headline_kind'] for s in again] == [s['headline_kind'] for s in slots])

    table = run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4'], env)
    ok('the batch table has a Price headline column with both markers', '| Price headline |' in table and '💲 Sermorelin for only $3.00/day' in table and '📅 Starting at $95/month' in table)
    run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4', '--log'], env)
    rows = [json.loads(l) for l in open(ledger)]
    ok('--log records 10 ads, 1 daily and 1 monthly', len(rows) == 1 and (rows[0]['ads'], rows[0]['price'], rows[0]['monthly']) == (10, 1, 1))
    nxt = pp.plan('sermorelin', 10)
    ok('the next batch of 10: 1 daily again, no monthly yet (5% of 20 ads is 1)', nxt['daily']['count'] == 1 and nxt['monthly']['count'] == 0)

    out = run([PLAN, '--product', 'sermorelin', '--n', '1', '--kind', 'video'], env)
    ok('the video CLI answers for the next video', 'next 1 ad' in out and ('THIS VIDEO' in out or 'normal headline' in out))

    # the gate
    job = os.path.join(home, 'output', 'Sermorelin', 'price_batch-1'); os.makedirs(job)
    open(os.path.join(job, 'deal.json'), 'w').write(deal)
    ds, ms, fs = daily[0], monthly[0], free[0]
    DH, MH, OFFER, DCTA = 'Sermorelin for only $3.00/day', 'Starting at $95/month', 'Save Up to 65%', 'Sermorelin for $3.00/day'
    ok('gate: the daily slot with its exact headline passes', hook('gate', prompt(ds['slot'], '9:16', job, DH, OFFER), env) == {})
    ok('gate: a trailing full stop on the headline is fine', hook('gate', prompt(ds['slot'], '4:5', job, DH + '.', OFFER), env) == {})
    ok('gate: the monthly slot with its exact headline passes', hook('gate', prompt(ms['slot'], '9:16', job, MH, OFFER), env) == {})
    ok('gate: a free slot with its own headline and the offer CTA passes', hook('gate', prompt(fs['slot'], '9:16', job, 'Built for the long game', OFFER), env) == {})
    ok('gate: a free slot may use the bible price CTA (rule 3: any approved CTA)', hook('gate', prompt(fs['slot'], '4:5', job, 'Built for the long game', DCTA), env) == {})
    bad, why = denied(hook('gate', prompt(ds['slot'], '9:16', job, 'Built for the long game', OFFER), env))
    ok('gate: the daily slot with another headline is refused', bad and DH in why and 'daily-price' in why)
    bad, why = denied(hook('gate', prompt(ms['slot'], '9:16', job, DH, OFFER), env))
    ok('gate: the monthly slot with the daily headline is refused', bad and MH in why)
    bad, why = denied(hook('gate', prompt(ds['slot'], '9:16', job, DH, DCTA), env))
    ok('gate: a price headline plus a $ CTA is refused (the price twice)', bad and 'twice' in why)
    bad, why = denied(hook('gate', prompt(fs['slot'], '9:16', job, DH, OFFER), env))
    ok('gate: the daily-price headline on a free slot is refused', bad and 'price headline' in why)
    bad, why = denied(hook('gate', prompt(fs['slot'], '4:5', job, MH, OFFER), env))
    ok('gate: the monthly headline on a free slot is refused', bad and 'price headline' in why)

    old = [{k: v for k, v in s.items() if k not in ('headline_kind', 'headline')} for s in slots]
    open(os.path.join(job, 'deal.json'), 'w').write(json.dumps(old))
    ok('gate: a deal.json from before the plan (no headline_kind) is not blocked', hook('gate', prompt(fs['slot'], '9:16', job, DH, OFFER), env) == {})

    print('\nall checks passed' if not fails else f'\n{len(fails)} FAILED: ' + '; '.join(fails))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
