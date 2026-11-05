#!/usr/bin/env python3
"""Price-CTA plan: the bible asks for the product's price line ("Sermorelin for $3.00/day") on 10% of ALL ads
(Standards, "Show the lowest price or the price per day on 10% of all ads"; Sermorelin: "Starting at $95/month" on 10% too).

    price_plan.py --product sermorelin --n 8              how many of the next 8 ads carry the price CTA (and which text)
    price_plan.py --product sermorelin --n 1 --kind video   the next VIDEO: does it carry it?  (add --log once approved)
    price_plan.py --product sermorelin --n 8 --log        record the batch (deal_worlds.py --log does this for images)

The share is kept over time, per computer, like the proof split: ~/Everlife-Creative/price-ledger.jsonl holds ads made and price
ads made per product; a batch gets round(10% x (ads so far + this batch)) minus the price ads already made. A batch of 10 gets 1;
batches of 4 get 0, then 1, then 0 ... so small batches still average 10% instead of never carrying one.

The price line comes from the product's bible page (skills/everlife-<id>/references/bible.json -> cta_price), never typed by hand.
A product with no price CTA on its bible page, or one on HOLD, gets none. The hook (core/hooks/batch_hook.py) enforces the plan:
a price slot must carry the price CTA, and no other slot may.
"""
import argparse, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.join(os.path.dirname(os.path.dirname(HERE)), "skills")
LEDGER = os.path.expanduser(os.environ.get("EVERLIFE_PRICE_LEDGER") or os.path.join(os.environ.get("EVERLIFE_CREATIVE", "~/Everlife-Creative"), "price-ledger.jsonl"))
SHARE = 0.10

# Products whose price CTA must not run yet (CLAUDE.md gates, §3 Price CTAs). Remove the line when the hold is lifted.
HOLD = {
    "titan-rx": "Titan-Rx's offer is [VERIFY CURRENT]: its $/day CTA is held until the offer is verified (Priestley, 4 Nov 2026)",
    "spark": "Spark's CTA list is Pending approval: its $/day CTA needs Priestley's OK first",
}


def bible(pid):
    p = os.path.join(SKILLS, f"everlife-{pid}", "references", "bible.json")
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def price_cta(pid):
    """(text, why_not): the bible's price line for this product, or '' with the reason there is none."""
    if pid in HOLD:
        return "", HOLD[pid]
    text = (bible(pid).get("cta_price") or "").strip()
    return (text, "") if text else ("", "no price CTA on this product's bible page")


def state(pid):
    ads = price = 0
    try:
        with open(LEDGER, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("product") == pid:
                    ads += int(r.get("ads", 0))
                    price += int(r.get("price", 0))
    except OSError:
        pass
    return ads, price


def plan(pid, n):
    """{cta, count, why_not, ads_before, price_before}: how many of the next n ads carry the price CTA."""
    text, why = price_cta(pid)
    ads, price = state(pid)
    k = 0
    if text:
        k = max(0, math.floor(SHARE * (ads + n) + 0.5) - price)
        k = min(k, n)
    return {"product": pid, "cta": text, "count": k, "why_not": why, "ads_before": ads, "price_before": price, "n": n}


def log(pid, n, k, kind="image", tag=""):
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "product": pid, "ads": n, "price": k, "kind": kind, "tag": tag}) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--product", required=True)
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--kind", default="image", choices=["image", "video"])
    ap.add_argument("--log", action="store_true", help="record these ads in the ledger (once the batch / video is approved)")
    ap.add_argument("--tag", default="", help="a label for the ledger row (job folder, video name)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    p = plan(a.product, a.n)
    if a.log:
        log(a.product, a.n, p["count"], a.kind, a.tag)
    if a.json:
        print(json.dumps(p, indent=1))
        return
    if not p["cta"]:
        print(f"{a.product}: no price CTA for these {a.n} ad(s): {p['why_not']}.")
        return
    print(f"{a.product}: {p['count']} of the next {a.n} ad(s) carry the price CTA \"{p['cta']}\" "
          f"({p['price_before']} price ads in {p['ads_before']} made so far; target {int(SHARE * 100)}%)."
          + ("  Logged." if a.log else ""))
    if a.kind == "video" and a.n == 1:
        print("→ THIS VIDEO carries it." if p["count"] else "→ this video uses the default offer CTA.")


if __name__ == "__main__":
    sys.exit(main())
