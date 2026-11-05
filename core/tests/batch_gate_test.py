#!/usr/bin/env python3
"""Regression test for the both-sizes gate (core/hooks/batch_hook.py + core/scripts/batch_check.py). No credits, no network.

    python3 core/tests/batch_gate_test.py      # prints ✅ per check, exits 1 on any failure

Proves, with fake prompts in a temp batch folder:
  gate   refuses an Everlife image prompt without the reference line · refuses a ratio mismatch · refuses a slot not in deal.json
         · allows a correct prompt · ignores a video / non-Everlife prompt
  fired  counts (slot, ratio) once per call
  stop   blocks while a size or a FINAL is owed, names exactly what is owed, stays silent once both sizes of every slot are finished
"""
import json, os, shutil, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOOK = os.path.join(REPO, 'core', 'hooks', 'batch_hook.py')
CHECK = os.path.join(REPO, 'core', 'scripts', 'batch_check.py')
DEAL = os.path.join(REPO, 'core', 'scripts', 'deal_worlds.py')
TOOL = 'mcp__creatify__model_playground_generate'
fails = []


def ok(name, cond):
    print(('✅ ' if cond else '❌ ') + name)
    if not cond: fails.append(name)


def hook(cmd, payload, env):
    r = subprocess.run([sys.executable, HOOK, cmd], input=json.dumps(payload), capture_output=True, text=True, env=env)
    return json.loads(r.stdout) if r.stdout.strip() else {}


def prompt(slot, ratio, job, ref=True, layout_ratio=None):
    lr = layout_ratio or ratio
    body = f"Design a finished, premium static social ad for PT-141 by Everlife … STRICT LAYOUT ({lr}, 1152x2048), follow exactly: …"
    if ref: body += f"\n\nReference only, never render: everlife slot={slot} ratio={ratio} product=pt-141 job={job}"
    return {'tool_name': TOOL, 'tool_input': {'prompt': body}}


def main():
    home = tempfile.mkdtemp(prefix='everlife-gate-test-')
    env = dict(os.environ, EVERLIFE_CREATIVE=home)
    job = os.path.join(home, 'output', 'PT-141', 'test_batch-1'); os.makedirs(job)
    deal = subprocess.run([sys.executable, DEAL, '--product', 'pt-141', '--n', '2', '--seed', '9', '--json'], capture_output=True, text=True, env=env).stdout
    open(os.path.join(job, 'deal.json'), 'w').write(deal)
    slots = json.loads(deal); ok('deal.json has 2 slots × 2 ratios', len(slots) == 2 and all(s['ratios'] == ['9:16', '4:5'] for s in slots))

    d = hook('gate', prompt(1, '9:16', job, ref=False), env).get('hookSpecificOutput', {})
    ok('gate refuses a prompt without the reference line', d.get('permissionDecision') == 'deny' and 'reference line' in d.get('permissionDecisionReason', ''))
    d = hook('gate', prompt(1, '4:5', job, layout_ratio='9:16'), env).get('hookSpecificOutput', {})
    ok('gate refuses a ratio mismatch', d.get('permissionDecision') == 'deny' and 'another ratio' in d.get('permissionDecisionReason', ''))
    d = hook('gate', prompt(7, '9:16', job), env).get('hookSpecificOutput', {})
    ok('gate refuses a slot that is not in deal.json', d.get('permissionDecision') == 'deny' and 'not in' in d.get('permissionDecisionReason', ''))
    ok('gate allows a correct prompt (silent)', hook('gate', prompt(1, '9:16', job), env) == {})
    ok('gate ignores a video prompt', hook('gate', {'tool_name': TOOL, 'tool_input': {'prompt': 'HOOK 0.0–1.5 s: a bottle flies across the gym'}}, env) == {})

    for s, r in [(1, '9:16'), (2, '9:16'), (1, '4:5')]:
        hook('fired', prompt(s, r, job), env)
    rp = os.path.join(job, 'renders.jsonl')
    ok('fired counts 3 renders', os.path.exists(rp) and len(open(rp).read().splitlines()) == 3)

    chk = subprocess.run([sys.executable, CHECK, job], capture_output=True, text=True, env=env)
    ok('batch_check reports 4:5 for slot 2 owed', chk.returncode == 1 and '4:5 for slot(s) 2' in chk.stdout and 'not finished' in chk.stdout)
    d = hook('stop', {'session_id': 'sess-A'}, env)
    ok('stop hook BLOCKS while a size is owed', d.get('decision') == 'block' and '4:5 for slot(s) 2' in d.get('reason', ''))
    d = hook('stop', {'session_id': 'sess-A'}, env)
    ok('stop hook warns (not blocks) the second time in the same session', 'systemMessage' in d and 'decision' not in d)

    hook('fired', prompt(2, '4:5', job), env)
    for n, wh in [(1, '1080x1920'), (1, '1080x1350'), (2, '1080x1920'), (2, '1080x1350')]:
        open(os.path.join(job, f'FINAL_{n}_world_{wh}.png'), 'w').close()
    chk = subprocess.run([sys.executable, CHECK, job], capture_output=True, text=True, env=env)
    ok('batch_check ✅ once both sizes of both slots are finished', chk.returncode == 0 and '2 ads × 2 sizes = 4' in chk.stdout)
    ok('stop hook silent when nothing is owed', hook('stop', {'session_id': 'sess-B'}, env) == {})

    shutil.rmtree(home)
    print(f"\n{len(fails)} failures" if fails else "\nall checks passed")
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
