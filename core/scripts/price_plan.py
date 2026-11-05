#!/usr/bin/env python3
"""Price-headline plan: bible Standards 03, "Pricing & CTA mix" (bible 1793919328-c260, 5 Nov 2026):

  Rule 1  Daily pricing, 10% of ALL creatives: the HEADLINE reads "[Product Name] for only $X.XX/day" (the product's accurate daily price).
  Rule 2  Sermorelin monthly pricing, 5% of Sermorelin creatives (Men and Women): the HEADLINE reads "Starting at $95/month".
  Rule 3  Every other creative: a varied mix of the product's approved CTAs.

    price_plan.py --product sermorelin --n 10             which of the next 10 ads carry a price headline, and the exact text
    price_plan.py --product sermorelin --n 1 --kind video   the next VIDEO: does its header / end-card headline carry one?  (add --log once approved)
    price_plan.py --product sermorelin --n 10 --log       record the batch (deal_worlds.py --log does this for images)

The shares are kept over time, per computer, like the proof split: ~/Everlife-Creative/price-ledger.jsonl holds ads made and price ads made per
product. A batch gets round(share x (ads so far + this batch)) minus the price ads already made, so a batch of 10 gets 1 daily-price ad and
batches of 4 get 0, 1, 0 ... : small batches still average the bible's share instead of never carrying one. The shares and the monthly headline are
READ FROM THE BIBLE TEXT (core/claude/creative-bible.md), so a change by Justin carries through on the next sync; the daily price comes from
each product's bible `cta_price` ("Sermorelin for $3.00/day" -> "Sermorelin for only $3.00/day"). A product with no daily price on its bible page,
or one on HOLD, gets none. The hook (core/hooks/batch_hook.py) enforces the plan: a price slot must carry its headline, no other slot may,
and a price slot never doubles it with a $ CTA.
"""
import argparse, json, math, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.dirname(HERE)
SKILLS = os.path.join(os.path.dirname(CORE), "skills")
BIBLE = os.path.join(CORE, "claude", "creative-bible.md")
LEDGER = os.path.expanduser(os.environ.get("EVERLIFE_PRICE_LEDGER") or os.path.join(os.environ.get("EVERLIFE_CREATIVE", "~/Everlife-Creative"), "price-ledger.jsonl"))

# Used only when the bible text cannot be parsed (the test fails then, so the rule gets looked at, not silently forgotten).
FALLBACK = {"daily_share": 0.10, "monthly": {"product": "sermorelin", "share": 0.05, "headline": "Starting at $95/month"}}

# Products whose daily price must not run yet (CLAUDE.md gates, §3 Price CTAs). Remove the line when the hold is lifted.
HOLD = {
    "titan-rx": "Titan-Rx's offer is [VERIFY CURRENT]: its $/day line is held until the offer is verified (Priestley, 4 Nov 2026)",
    "spark": "Spark's CTA list is Pending approval: its $/day line needs Priestley's OK first",
}

DAILY_CTA = re.compile(r"^(?P<name>.+?) for \$(?P<amount>\d+(?:\.\d\d)?)/day$")


def rules():
    """{daily_share, monthly:{product, share, headline} | None, source}: the shares and the monthly headline, read from the bible text."""
    out = {"daily_share": FALLBACK["daily_share"], "monthly": dict(FALLBACK["monthly"]), "source": "fallback"}
    try:
        with open(BIBLE, encoding="utf-8") as f:
            txt = f.read()
    except OSError:
        return out
    m1 = re.search(r"Rule 1 [^\n]*?\((\d+)% of all creatives\)", txt)
    m2 = re.search(r"Rule 2 · (?P<p>[A-Za-z0-9+ -]+?) monthly pricing \((?P<s>\d+)% of [^)]*\)[^\n]*?headline “(?P<h>[^”]+?)\.?”", txt)
    if m1 and m2:
        out = {"daily_share": int(m1.group(1)) / 100.0,
               "monthly": {"product": m2.group("p").strip().lower().replace(" ", "-"), "share": int(m2.group("s")) / 100.0, "headline": m2.group("h").strip()},
               "source": "bible"}
    return out


def bible(pid):
    p = os.path.join(SKILLS, f"everlife-{pid}", "references", "bible.json")
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def daily_headline(pid):
    """(headline, why_not): "<Product> for only $X.XX/day" from the bible's own price CTA, or '' with the reason there is none."""
    if pid in HOLD:
        return "", HOLD[pid]
    m = DAILY_CTA.match((bible(pid).get("cta_price") or "").strip())
    if not m:
        return "", "no daily price on this product's bible page"
    return f"{m.group('name')} for only ${m.group('amount')}/day", ""


def monthly_headline(pid):
    m = rules()["monthly"]
    return m["headline"] if m and m["product"] == pid else ""


def state(pid):
    ads = daily = monthly = 0
    try:
        with open(LEDGER, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("product") == pid:
                    ads += int(r.get("ads", 0))
                    daily += int(r.get("price", 0))          # "price" = daily-price ads (rows written by the CTA version of this plan count too)
                    monthly += int(r.get("monthly", 0))
    except OSError:
        pass
    return ads, daily, monthly


def owed(share, ads, n, made):
    return max(0, min(n, math.floor(share * (ads + n) + 0.5) - made))


def plan(pid, n):
    """{daily:{headline,count,why_not}, monthly:{headline,count}|None, ads_before, ...}: how many of the next n ads carry each price headline."""
    r = rules()
    head, why = daily_headline(pid)
    ads, daily_before, monthly_before = state(pid)
    d = owed(r["daily_share"], ads, n, daily_before) if head else 0
    mh = monthly_headline(pid)
    m = owed(r["monthly"]["share"], ads, n, monthly_before) if mh else 0
    if d + m > n:                                  # tiny batches: the monthly line yields, the bible's 10% is the main rule
        m = max(0, n - d)
    return {"product": pid, "n": n, "ads_before": ads, "daily_before": daily_before, "monthly_before": monthly_before,
            "daily": {"headline": head, "count": d, "why_not": why},
            "monthly": {"headline": mh, "count": m} if mh else None}


def assign(p, rng):
    """A list of p['n'] entries: 'daily' / 'monthly' on the slots that carry a price headline (never both on one slot), 'free' elsewhere."""
    kinds = ["free"] * p["n"]
    d, m = p["daily"]["count"], (p["monthly"] or {}).get("count", 0)
    picks = rng.sample(range(p["n"]), d + m) if d + m else []
    for i in picks[:d]:
        kinds[i] = "daily"
    for i in picks[d:]:
        kinds[i] = "monthly"
    return kinds


def log(pid, n, daily, monthly=0, kind="image", tag=""):
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "product": pid, "ads": n, "price": daily, "monthly": monthly, "kind": kind, "tag": tag}) + "\n")


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
        log(a.product, a.n, p["daily"]["count"], (p["monthly"] or {}).get("count", 0), a.kind, a.tag)
    if a.json:
        print(json.dumps(p, indent=1))
        return
    d, m = p["daily"], p["monthly"]
    if not d["headline"] and not m:
        print(f"{a.product}: no price headline for these {a.n} ad(s): {d['why_not']}.")
        return
    if d["headline"]:
        print(f"{a.product}: {d['count']} of the next {a.n} ad(s) carry the daily-price headline \"{d['headline']}\" "
              f"({p['daily_before']} so far in {p['ads_before']} made; the bible's share is {int(rules()['daily_share'] * 100)}%)." + ("  Logged." if a.log else ""))
    else:
        print(f"{a.product}: no daily-price headline ({d['why_not']}).")
    if m:
        print(f"{a.product}: {m['count']} of the next {a.n} ad(s) carry the monthly headline \"{m['headline']}\" "
              f"({p['monthly_before']} so far; the bible's share is {int(rules()['monthly']['share'] * 100)}%).")
    if a.kind == "video" and a.n == 1:
        if d["count"]:
            print(f"→ THIS VIDEO's header / end-card headline is \"{d['headline']}\".")
        elif m and m["count"]:
            print(f"→ THIS VIDEO's header / end-card headline is \"{m['headline']}\".")
        else:
            print("→ this video uses its normal headline.")


if __name__ == "__main__":
    sys.exit(main())
