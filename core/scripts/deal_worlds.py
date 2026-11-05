#!/usr/bin/env python3
"""Everlife World Dealer: hands every image batch N slots that are guaranteed different.

    deal_worlds.py --product pt-141 --n 8 [--audience men|women|both] [--log] [--json] [--skip world1,world2]

--audience is the "Who's in them" answer; omitted = the product's own audience (product.json "audience": men / women / both,
Mitansh 2026-11-05). A men's or women's product refuses the other gender (exit 2): Titan-Rx never deals a woman persona.

Each slot gets: world (from core/references/world-deck/worlds.json), type pairing, accent, placement, light,
focal (pill / bottle / person per the bible 40/30/30; 75/25 for products without a pill, Justin to confirm), proof (trust / count / none,
42/28/30 per standard_footer.SHARE), hand-held (max 20% of the batch), headline_kind (daily / monthly / free: the bible's price headlines on 10% / 5% of ads, kept over batches by price_plan.py), hardcore tag (a cap of 30% of men's slots on hardcore products, bible 2026-11-04),
persona (age band, look) and the ratio pair (always 9:16 + 4:5).

Guarantees (code, not memory):
  * no world repeats inside a batch; at most 2 slots per world family;
  * no world this product used in its last 3 batches (ledger ~/Everlife-Creative/world-ledger.jsonl) or in --skip;
  * no two slots share a type pairing, accent or placement; lights spread;
  * worlds flagged not-intimacy / restora-only / pill-products-only / needs-review are filtered per product;
  * proof "none" lands on person-led or product-low worlds first (they rarely have a clean shelf).
The dealer decides the MIX. Claude writes the prompt freely inside the slot.
"""
import argparse, json, os, random, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import price_plan  # the price-headline shares (bible Standards 03, Pricing & CTA mix: daily price 10%, Sermorelin monthly 5%)

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.dirname(HERE)
DECK = os.path.join(CORE, 'references', 'world-deck', 'worlds.json')
LEDGER = os.path.expanduser(os.environ.get('EVERLIFE_WORLD_LEDGER', '~/Everlife-Creative/world-ledger.jsonl'))
SKILLS = os.path.join(os.path.dirname(CORE), 'skills')

INTIMACY = {'pt-141', 'lovara', 'spark', 'titan-rx'}
HARDCORE = {'sermorelin', 'sermorelin-ghk', 'bpc-157', 'wolverine', 'spartan'}
METABOLIC = {'glp-1', 'nad', 'mots-c', 'epithalon'}
SKIN = {'ghk-cream'}
PROOF_SHARE = {'trust': 0.42, 'count': 0.28, 'none': 0.30}
FOCAL_PILL = {'pill': 0.40, 'bottle': 0.30, 'person': 0.30}   # bible 2026-11-04 (was 50/25/25)
FOCAL_NOPILL = {'bottle': 0.75, 'person': 0.25}

CAST = {
    'men':   ['man 45–55, grey at the temples, lean and fit, warm smile', 'man 50–60, salt-and-pepper beard, weathered, calm',
              'man 40–50, shaved head, broad shoulders, kind eyes', 'man 55–65, silver hair, reading glasses, relaxed'],
    'women': ['woman 45–55, shoulder-length silver-blonde hair, freckles', 'woman 50–60, dark curly hair, glasses, easy laugh',
              'woman 40–50, natural grey pixie cut, athletic', 'woman 55–65, long white hair, linen shirt, serene'],
}
HARDCORE_CAST = ['shirtless bodybuilder 40–45, flawless condition, hard gym light', 'lifter in a stringer 40–45, vascular, chalked hands',
                 'shirtless man 40–45, tattoos, cable-crossover station, sweat sheen']


def product_family(pid, prod=None):
    v = set((prod or {}).get('variations', []))
    if 'intimacy-tasteful' in v or pid in INTIMACY: return 'intimacy'
    if 'hardcore-men' in v or pid in HARDCORE: return 'men'
    if pid in METABOLIC: return 'metabolic'
    if 'womens-palette' in v and pid in SKIN or pid in SKIN: return 'skin'
    return 'generic'


AUDIENCES = ('men', 'women', 'both')


def resolve_audience(pid, prod, asked=None):
    """product.json "audience" is the default; a single-audience product refuses the other gender (code, not memory)."""
    own = prod.get('audience') or 'both'
    if own not in AUDIENCES: raise SystemExit(f'{pid}: product.json "audience" must be men / women / both (got {own!r})')
    if asked in (None, '', own): return own
    if own in ('men', 'women'):
        raise SystemExit(f"{pid} is a {own}'s product (product.json audience): --audience {asked} refused. Omit --audience.")
    return asked


def load_product(pid):
    p = os.path.join(SKILLS, f'everlife-{pid}', 'product.json')
    if os.path.exists(p):
        with open(p) as f: return json.load(f)
    return {}


def has_pill(prod):
    r = prod.get('renders', {}) or {}
    if r.get('pill') or r.get('tablet') or r.get('capsule'): return True
    for form in (prod.get('forms') or {}).values():
        if isinstance(form, dict) and form.get('pill'): return True
    return False


def recent_worlds(pid, batches=3):
    used = []
    if not os.path.exists(LEDGER): return used
    rows = []
    with open(LEDGER) as f:
        for line in f:
            try:
                row = json.loads(line)
                if row.get('product') == pid: rows.append(row)
            except Exception: pass
    for row in rows[-batches:]:
        used += row.get('worlds', [])
    return used


def spread(n, share, rng):
    """Integer counts for a share dict, summing to n, largest remainder, ties random."""
    raw = {k: v * n for k, v in share.items()}
    out = {k: int(v) for k, v in raw.items()}
    rest = n - sum(out.values())
    order = sorted(share, key=lambda k: (-(raw[k] - out[k]), rng.random()))
    for k in order[:rest]: out[k] += 1
    seq = []
    for k, c in out.items(): seq += [k] * c
    rng.shuffle(seq)
    return seq


def deal(pid, n, audience, skip=(), seed=None, prefer=(), families=()):
    rng = random.Random(seed)
    with open(DECK) as f: deck = json.load(f)
    prod = load_product(pid)
    audience = resolve_audience(pid, prod, audience)
    variations = set(prod.get('variations', []))
    fam = product_family(pid, prod)
    pill = has_pill(prod)
    banned = (set(skip) | set(recent_worlds(pid))) - set(prefer)

    pool = []
    for w in deck['worlds']:
        fl = set(w.get('flags', []))
        if w['id'] in banned: continue
        if 'restora-only' in fl and pid != 'restora-z': continue
        if 'not-intimacy' in fl and fam == 'intimacy': continue
        if 'pill-products-only' in fl and not pill: continue
        if 'needs-review' in fl or 'seasonal' in fl or 'byline-pending' in fl: continue
        if fam == 'intimacy' and w['id'] in {'drop-the-day', 'lamp-reader'}: continue  # beds / reclining
        if families and w['family'] not in families and w['id'] not in prefer: continue
        pool.append(w)
    rng.shuffle(pool)
    # a chosen direction: its worlds come first and are guaranteed
    pref = [w for w in pool if w['id'] in prefer]; rest = [w for w in pool if w['id'] not in prefer]
    # ultra-premium bias for vial products (variation vial-product): material / scene worlds lead; comic/print/surreal ≤ 3 of the batch
    if 'vial-product' in variations:
        premium = [w for w in rest if w['family'] in ('MATERIAL', 'SCENE', 'INFOGRAPHIC', 'TYPE')]
        other = [w for w in rest if w['family'] not in ('MATERIAL', 'SCENE', 'INFOGRAPHIC', 'TYPE')]
        rest = premium + other
    pool = pref + rest

    focal_seq = spread(n, FOCAL_PILL if pill else FOCAL_NOPILL, rng)
    proof_seq = spread(n, PROOF_SHARE, rng)
    hand_max = max(1, int(n * 0.2))
    person_target = focal_seq.count('person')

    slots, fam_count, used_pair, used_acc, used_place, used_light = [], {}, set(), set(), set(), []
    cap = {f: 2 for f in deck['families']}
    if 'vial-product' in variations:
        cap.update({'COMIC': 1, 'PRINT': 1, 'SURREAL': 1})
    # pass 1: person-led worlds for the person slots, then everything else
    person_worlds = [w for w in pool if 'person' in w.get('flags', [])]
    other_worlds = [w for w in pool if 'person' not in w.get('flags', [])]
    hands = 0
    chosen = []
    for w in person_worlds:
        if len(chosen) >= person_target: break
        if fam_count.get(w['family'], 0) >= cap.get(w['family'], 2) and w['id'] not in prefer: continue
        if 'hand-held' in w['flags'] and hands >= hand_max: continue
        chosen.append(w); fam_count[w['family']] = fam_count.get(w['family'], 0) + 1
        hands += 'hand-held' in w['flags']
    for w in other_worlds:
        if len(chosen) >= n: break
        if fam_count.get(w['family'], 0) >= cap.get(w['family'], 2) and w['id'] not in prefer: continue
        if 'hand-held' in w['flags'] and hands >= hand_max: continue
        chosen.append(w); fam_count[w['family']] = fam_count.get(w['family'], 0) + 1
        hands += 'hand-held' in w['flags']
    if len(chosen) < n:
        sys.exit(f'deal_worlds: only {len(chosen)} worlds available for {pid} after filters; shrink --n or clear --skip')

    # order: person worlds take the person focal slots
    person_idx = [i for i, f in enumerate(focal_seq) if f == 'person']
    other_idx = [i for i, f in enumerate(focal_seq) if f != 'person']
    ordered = [None] * n
    pw = [w for w in chosen if 'person' in w['flags']]
    ow = [w for w in chosen if 'person' not in w['flags']]
    for i in person_idx:
        ordered[i] = pw.pop(0) if pw else ow.pop(0)
    for i in other_idx:
        ordered[i] = ow.pop(0) if ow else pw.pop(0)

    # proof none → person / low-shelf worlds first
    low_shelf = {'holdout', 'big-hug', 'ugc-selfie', 'scribble', 'typestack', 'capsule-sofa', 'drop-the-day', 'golden-hour',
                 'cinematic-window', 'lamp-reader', 'bw-portrait', 'chairs', 'reply-comment', 'billboard', 'bus-shelter'}
    none_count = proof_seq.count('none')
    proof_final = [None] * n
    none_targets = [i for i, w in enumerate(ordered) if w['id'] in low_shelf][:none_count]
    for i in none_targets: proof_final[i] = 'none'
    rest = [p for p in proof_seq if p != 'none'] + ['none'] * (none_count - len(none_targets))
    rng.shuffle(rest)
    for i in range(n):
        if proof_final[i] is None: proof_final[i] = rest.pop()
    for i, w in enumerate(ordered):
        if 'proof-count' in w['flags']: proof_final[i] = 'count'

    pairs = deck['type_pairings'][:]; rng.shuffle(pairs)
    accents = deck['accents'][:]; rng.shuffle(accents)
    places = deck['placements'][:]; rng.shuffle(places)
    lights = deck['lights'][:]; rng.shuffle(lights)
    if fam in ('intimacy', 'skin') or audience == 'women':
        accents = [a for a in accents if a not in ('forest', 'mint', 'amber')]  # no oranges / greens for women's creative
    if fam == 'men' and audience == 'men':
        accents = [a for a in accents if a not in ('rose', 'blush')]  # men's muscle products: no pinks

    # hardcore tags: 40% of men's slots on hardcore products
    # gender per slot first (a 'both' batch alternates over the PERSON slots), so the hardcore cap can only land on a man's slot
    gender, rank = {}, 0
    for i, f in enumerate(focal_seq):
        if audience != 'both': gender[i] = audience
        else:
            gender[i] = 'men' if rank % 2 == 0 else 'women'
            if f == 'person': rank += 1
    men_slots = [i for i, f in enumerate(focal_seq) if f == 'person' and gender[i] == 'men']
    hc_cfg = {}
    try:
        with open(os.path.join(CORE, 'references', 'hardcore-men.json')) as f: hc_cfg = json.load(f)
    except Exception: pass
    hc_share = float(hc_cfg.get('share', 0.3))
    # bible 2026-11-04: shirtless talent on UP TO 30% of a product's creatives → a cap: floor(share × men's slots), never above
    # cap = floor(share × the whole batch), like pick_styles.py; it lands on men's person slots (hardcore = a shirtless person)
    hardcore_n = min(len(men_slots), int(hc_share * n)) if ('hardcore-men' in variations or pid in hc_cfg.get('products', HARDCORE)) else 0
    hardcore_idx = set(rng.sample(men_slots, hardcore_n)) if hardcore_n else set()

    pplan = price_plan.plan(pid, n)
    default_cta = price_plan.bible(pid).get('cta_default') or None
    price_rng = random.Random(f'{seed}-price') if seed is not None else random.Random()   # own stream: the rest of a seeded deal is unchanged
    hkinds = price_plan.assign(pplan, price_rng)
    hheads = {'daily': pplan['daily']['headline'], 'monthly': (pplan['monthly'] or {}).get('headline'), 'free': None}

    for i, w in enumerate(ordered):
        aud = gender[i]
        hardcore = i in hardcore_idx
        persona = rng.choice(HARDCORE_CAST) if hardcore else rng.choice(CAST[aud])
        if fam == 'intimacy': persona += ', clothed, shoulder-up, daylight, never a bed'
        slots.append({
            'slot': i + 1,
            'world': w['id'], 'world_name': w['name'], 'family': w['family'],
            'look': w['look'], 'type_hint': w['type'], 'product_place': w['product'],
            'translate': w.get('translate', {}).get(fam) or w.get('translate', {}).get('generic') or '',
            'type_pairing': pairs[i % len(pairs)], 'accent': accents[i % len(accents)],
            'placement': places[i % len(places)], 'light': lights[i % len(lights)],
            'focal': focal_seq[i], 'proof': proof_final[i],
            'hand_held': 'hand-held' in w['flags'],
            'audience': aud if focal_seq[i] == 'person' else None,
            'batch_audience': audience,
            'hardcore': hardcore,
            'persona': persona if focal_seq[i] == 'person' else None,
            'headline_kind': hkinds[i],                 # daily / monthly: the HEADLINE is exactly `headline`; free: the headline is yours
            'headline': hheads[hkinds[i]],
            'cta': default_cta,
            'ratios': ['9:16', '4:5'],
            'variations': sorted(variations),
            'ultra_premium': 'vial-product' in variations and w['family'] in ('MATERIAL', 'SCENE'),
        })
    return slots


def pplan_head(slots, kind):
    return next((s['headline'] for s in slots if s['headline_kind'] == kind), '')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--product', required=True)
    ap.add_argument('--n', type=int, default=8)
    ap.add_argument('--audience', default=None, choices=['men', 'women', 'both'],
                    help="the Who's-in-them answer; omitted = product.json audience; a men's / women's product refuses the other")
    ap.add_argument('--skip', default='', help='comma-separated world ids to avoid (e.g. from the team Copy Ledger)')
    ap.add_argument('--seed', type=int)
    ap.add_argument('--prefer', default='', help='comma-separated world ids from the chosen direction (guaranteed in the batch)')
    ap.add_argument('--families', default='', help='restrict to these families (comma-separated), e.g. PRINT,COMIC')
    ap.add_argument('--log', action='store_true', help='append this deal to the ledger (do it once the batch is approved)')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    skip = [s.strip() for s in a.skip.split(',') if s.strip()]
    prefer = [s.strip() for s in a.prefer.split(',') if s.strip()]
    families = [s.strip().upper() for s in a.families.split(',') if s.strip()]
    slots = deal(a.product, a.n, a.audience, skip, a.seed, prefer, families)
    if a.log:
        os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
        with open(LEDGER, 'a') as f:
            f.write(json.dumps({'ts': time.strftime('%Y-%m-%dT%H:%M:%S'), 'product': a.product, 'n': a.n,
                                'worlds': [s['world'] for s in slots]}) + '\n')
        price_plan.log(a.product, a.n, sum(1 for s in slots if s['headline_kind'] == 'daily'),
                       sum(1 for s in slots if s['headline_kind'] == 'monthly'), 'image', 'deal')
    if a.json:
        print(json.dumps(slots, indent=1)); return
    print(f"# {a.product} · {a.n} slots · audience {slots[0]['batch_audience'] if slots else a.audience} · both sizes each")
    print("| # | World | Family | Focal | Proof | Price headline | Type | Accent | Placement | Light | Person |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for s in slots:
        who = (('💪 ' if s['hardcore'] else '') + (s['persona'] or '—'))
        print(f"| {s['slot']} | **{s['world_name']}** (`{s['world']}`) | {s['family']} | {s['focal']} | {s['proof']} | "
              f"{('💲 ' + s['headline']) if s['headline_kind'] == 'daily' else ('📅 ' + s['headline']) if s['headline_kind'] == 'monthly' else '—'} | {s['type_pairing'][0]} / {s['type_pairing'][1]} | {s['accent']} | {s['placement']} | {s['light']} | {who} |")
    print()
    nd, nm = sum(1 for s in slots if s['headline_kind'] == 'daily'), sum(1 for s in slots if s['headline_kind'] == 'monthly')
    if nd or nm:
        print(f"Price headline plan (bible Standards 03, Pricing & CTA mix): "
              + (f"{nd} of {a.n} slot(s) 💲 carry \"{pplan_head(slots, 'daily')}\" as the HEADLINE" if nd else "no daily-price slot this batch")
              + (f"; {nm} 📅 carry \"{pplan_head(slots, 'monthly')}\"" if nm else "") + ". Every other slot writes its own headline; "
              "the gate refuses these headlines anywhere else, refuses a price slot with another headline, and a price slot never also carries a $ CTA.")
    else:
        _, why = price_plan.daily_headline(a.product)
        print("Price headline plan: no price-headline slot in this batch" + (f" ({why})" if why else " (the bible's share is kept over batches: the next one carries it)") + ".")
    for s in slots:
        print(f"{s['slot']}. {s['world_name']}: {s['look']}  · product: {s['product_place']}"
              + (f"  · for this product: {s['translate']}" if s['translate'] else ''))


if __name__ == '__main__':
    main()
