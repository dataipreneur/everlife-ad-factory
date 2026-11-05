#!/usr/bin/env python3
"""Regression test for the price-CTA plan (core/scripts/price_plan.py, deal_worlds.py, the price rule in core/hooks/batch_hook.py).
No credits, no network, never touches the real ledgers.

    python3 core/tests/price_plan_test.py      # prints ✅ per check, exits 1 on any failure

Proves: a batch of 10 carries exactly 1 price CTA and small batches average 10% over time · the price line is the bible's own text ·
held / price-less products get none · the dealer marks the slots and logs the batch · the gate refuses the price line on an offer
slot and an offer CTA on a price slot, and stays silent on a correct prompt or a deal.json from before the plan.
"""
import json, os, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, 'core', 'scripts'))
HOOK = os.path.join(REPO, 'core', 'hooks', 'batch_hook.py')
DEAL = os.path.join(REPO, 'core', 'scripts', 'deal_worlds.py')
PLAN = os.path.join(REPO, 'core', 'scripts', 'price_plan.py')
TOOL = 'mcp__creatify__model_playground_generate'
fails = []


def ok(name, cond):
    print(('✅ ' if cond else '❌ ') + name)
    if not cond: fails.append(name)


def run(args, env):
    return subprocess.run([sys.executable] + args, capture_output=True, text=True, env=env).stdout


def hook(cmd, payload, env):
    r = subprocess.run([sys.executable, HOOK, cmd], input=json.dumps(payload), capture_output=True, text=True, env=env)
    return json.loads(r.stdout) if r.stdout.strip() else {}


def prompt(slot, ratio, job, cta):
    body = (f'Design a finished static ad for Sermorelin by Everlife … STRICT LAYOUT ({ratio}, 1152x2048), follow exactly: …\n'
            f'TEXT: Headline: "Built for the long game"\n  CTA (in a button): "{cta}"\n'
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

    p = pp.plan('sermorelin', 10)
    ok('a batch of 10 carries exactly 1 price CTA', p['count'] == 1)
    ok("the price line is the bible's own text", p['cta'] == 'Sermorelin for $3.00/day')
    ok('a batch of 5 carries 1 (round half up: 10% of 5 = 0.5)', pp.plan('sermorelin', 5)['count'] == 1)
    ok('a batch of 4 carries none the first time', pp.plan('sermorelin', 4)['count'] == 0)

    total = 0
    for _ in range(5):                                  # five batches of 4 = 20 ads → 2 price ads, never a long run of none
        k = pp.plan('sermorelin', 4)['count']
        pp.log('sermorelin', 4, k)
        total += k
    ok('five batches of 4 (20 ads) carry 2 price CTAs in total (10%)', total == 2)
    ok('another product is counted on its own', pp.plan('pt-141', 10)['count'] == 1 and pp.plan('pt-141', 10)['ads_before'] == 0)

    for pid, word in [('titan-rx', 'VERIFY'), ('spark', 'Pending')]:
        q = pp.plan(pid, 10)
        ok(f'{pid} is on hold: no price CTA, and it says why', q['count'] == 0 and word in q['why_not'])
    q = pp.plan('spartan', 10)
    ok('Spartan has no price CTA on its bible page: none', q['count'] == 0 and 'no price CTA' in q['why_not'])

    for f in (ledger,):
        if os.path.exists(f): os.remove(f)

    deal = run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4', '--json'], env)
    slots = json.loads(deal)
    price = [s for s in slots if s['cta_kind'] == 'price']
    offer = [s for s in slots if s['cta_kind'] == 'offer']
    ok('the dealer marks exactly 1 of 10 slots as the price slot', len(price) == 1 and len(offer) == 9)
    ok('the price slot carries the price line, the others the default offer CTA',
       price[0]['cta'] == 'Sermorelin for $3.00/day' and all(s['cta'] == 'Save Up to 65%' for s in offer))
    ok('a dealing without --log leaves the ledger alone', not os.path.exists(ledger))
    again = json.loads(run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4', '--json'], env))
    ok('a seeded deal is repeatable, price slot included', [s['cta_kind'] for s in again] == [s['cta_kind'] for s in slots])

    table = run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4'], env)
    ok('the batch table has a CTA column and marks the price slot', '| CTA |' in table and '💲 Sermorelin for $3.00/day' in table)
    run([DEAL, '--product', 'sermorelin', '--n', '10', '--seed', '4', '--log'], env)
    rows = [json.loads(l) for l in open(ledger)]
    ok('--log records 10 ads and 1 price ad', len(rows) == 1 and rows[0]['ads'] == 10 and rows[0]['price'] == 1)
    ok('the next batch of 10 then carries 1 again (20 ads, 2 price)', pp.plan('sermorelin', 10)['count'] == 1)

    out = run([PLAN, '--product', 'sermorelin', '--n', '1', '--kind', 'video'], env)
    ok('the video CLI answers for the next video', 'next 1 ad' in out and ('THIS VIDEO' in out or 'default offer CTA' in out))

    # the gate
    job = os.path.join(home, 'output', 'Sermorelin', 'price_batch-1'); os.makedirs(job)
    open(os.path.join(job, 'deal.json'), 'w').write(deal)
    ps, os_ = price[0], offer[0]
    d_price, d_off = 'Sermorelin for $3.00/day', 'Save Up to 65%'
    ok('gate: the price slot with the price CTA passes', hook('gate', prompt(ps['slot'], '9:16', job, d_price), env) == {})
    ok('gate: an offer slot with the offer CTA passes', hook('gate', prompt(os_['slot'], '9:16', job, d_off), env) == {})
    bad, why = denied(hook('gate', prompt(ps['slot'], '9:16', job, d_off), env))
    ok('gate: the price slot with the offer CTA is refused', bad and 'PRICE CTA' in why and d_price in why)
    bad, why = denied(hook('gate', prompt(os_['slot'], '4:5', job, d_price), env))
    ok('gate: the price line on an offer slot is refused', bad and '10%' in why and d_off in why)

    old = [{k: v for k, v in s.items() if k not in ('cta_kind', 'cta')} for s in slots]
    open(os.path.join(job, 'deal.json'), 'w').write(json.dumps(old))
    ok('gate: a deal.json from before the plan (no cta_kind) is not blocked', hook('gate', prompt(os_['slot'], '9:16', job, d_price), env) == {})

    print('\nall checks passed' if not fails else f'\n{len(fails)} FAILED: ' + '; '.join(fails))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
