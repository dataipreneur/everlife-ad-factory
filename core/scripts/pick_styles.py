#!/usr/bin/env python3
"""Pick random ad styles from the shared Everlife style library ("Surprise me").

  pick_styles.py --product pt-141 --n 5            # draw 5 different styles, avoiding the product's last batch
  pick_styles.py --product pt-141 --n 5 --allow S12   # also allow gated styles (Testimonial needs screened reviews)
  pick_styles.py --log --product pt-141 --codes S02,S09,S13   # record what the batch used

Ledger: ~/Everlife-Creative/style-ledger.jsonl (one JSON line per batch).
"""
import argparse, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.normpath(os.path.join(HERE, '..', 'references', 'style-library'))
LEDGER = os.path.expanduser('~/Everlife-Creative/style-ledger.jsonl')


def load_styles():
    with open(os.path.join(LIB, 'styles.json')) as f:
        return json.load(f)['styles']


def last_batch(product):
    if not os.path.exists(LEDGER):
        return []
    rows = []
    with open(LEDGER) as f:
        for line in f:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if row.get('product') == product:
                rows.append(row.get('codes', []))
    return [c for r in rows[-2:] for c in r]      # avoid the last TWO batches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--product', required=True)
    ap.add_argument('--n', type=int, default=4)
    ap.add_argument('--allow', default='', help='comma-separated gated codes to allow, e.g. S12')
    ap.add_argument('--log', action='store_true')
    ap.add_argument('--codes', default='')
    a = ap.parse_args()

    styles = load_styles()
    if a.log:
        codes = [c.strip() for c in a.codes.split(',') if c.strip()]
        known = {s['code'] for s in styles}
        bad = [c for c in codes if c not in known]
        if bad:
            sys.exit(f'unknown codes: {bad}')
        os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
        with open(LEDGER, 'a') as f:
            f.write(json.dumps({'ts': time.strftime('%Y-%m-%dT%H:%M:%S'), 'product': a.product, 'codes': codes}) + '\n')
        print(f'logged {a.product}: {",".join(codes)}')
        return

    allow = {c.strip() for c in a.allow.split(',') if c.strip()}
    pool = [s for s in styles if s['gate'] == 'open' or s['code'] in allow]
    recent = set(last_batch(a.product))
    fresh = [s for s in pool if s['code'] not in recent]
    random.shuffle(fresh)
    stale = [s for s in pool if s['code'] in recent]
    random.shuffle(stale)
    order = fresh + stale                       # fresh first, then reuse only if N > fresh styles
    picks = [order[i % len(order)] for i in range(a.n)]
    for i, s in enumerate(picks, 1):
        board = os.path.join(LIB, 'boards', f"{s['code']}_{s['slug']}.jpg")
        print(f"slot {i}: {s['code']} {s['name']}  [{s['group']}]  board: {board}")


if __name__ == '__main__':
    main()
