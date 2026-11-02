"""Which proof this creative carries: the trust row or "Over 100,000 happy customers" (bible 2026-11-02, Standards 01 + 02 · 06:
trust callouts on ~60% of creatives, the customer count on ~40%, one per creative; images and videos).

  proof_next.py --product <id>               print the proof for the next VIDEO (keeps the product's running split near 60/40)
  proof_next.py --product <id> --log <tag>   ... and record it (run once the video is approved for finishing)
  proof_next.py --plan N                     the split for an N-ad IMAGE batch (same as finish_batch.py --proof-plan N)

Put the answer in the video's copy.json as "proof": "trust" | "count" (full_layout.py / premium_finish.py read it), or pass
--proof to finish_batch.py for images. The ledger is ~/Everlife-Creative/proof-ledger.jsonl (per computer).
"""
import argparse, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "tools"))
import standard_footer as sf  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--product"); ap.add_argument("--log", metavar="TAG"); ap.add_argument("--plan", type=int)
a = ap.parse_args()
if a.plan:
    for i, p in enumerate(sf.proof_plan(a.plan), 1):
        print(f"ad {i}: {p}")
    sys.exit()
if not a.product:
    sys.exit("❌ pass --product <id> (or --plan N)")
p = sf.next_proof(a.product)
rows = sf._ledger(a.product)
print(f"{a.product}: next video → \"proof\": \"{p}\"  (so far: {sum(r['proof'] == 'trust' for r in rows)} trust, "
      f"{sum(r['proof'] == 'count' for r in rows)} count)")
if a.log:
    sf.log_proof(a.product, p, a.log); print(f"logged {a.log} → {p}")
