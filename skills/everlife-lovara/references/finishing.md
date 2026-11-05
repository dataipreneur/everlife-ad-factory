# QA + finishing (zero manual editing)

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

## 0. Safe zones (every 9:16 image and video)
Logo, headline, offer, CTA, captions and proof live only inside **x 156–924, y 144–1385, minus the Reels profile notch 156–375 ×
1216–1385** (`tools/safezones.py`); the disclaimer sits alone at the very bottom (`"disclaimer_at": "bottom"` in product.json). The
finishers refuse to export on a violation (exit 3 video, 2 image): never override; fix the layout or re-roll.
Feed (4:5, 1:1): 60 px margin.

## 1. QA the raw output (always, before the user sees it)
- Contact sheet: `$FF -v error -y -i raw.mp4 -vf "fps=2,scale=180:-1,tile=10x3" -frames:v 1 sheet.jpg`, then Read it.
- Transcript: faster-whisper from `$T/venv` (`vad_filter=True`, no prompt hint, to check for stray speech); compare with the script.
- Pass/fail (tell the user every fail):
  - **product correctness:** the label matches the render; not mirrored (`--mirror-until <cut>`); the capsule matches the capsule render
    exactly and there is exactly one; no other product
  - people: real-looking women 30–55, clothed, shoulder-up/waist-up, candid, an ordinary face (**no celebrity likeness**); **no bed or
    bedroom in any frame**; no lingerie, lips close-ups or couples
  - no needles/syringes/vials, no body shots, no garbled text on props, no second phone (`--zoom 1.2`)
  - product name pronounced clearly; nothing said that isn't on the bible page
  - speech starts in the first second and ends by ~10.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product lovara --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** each clip is already in the Prompt & Outcome Log (logged when submitted, `video-prompting.md`); now log the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log (`teamlog.py copy / proof / run`, then `close` ✅ before SESSION.md). Unreachable → the pending file, never block. **Ad Review:** post each finished video as an `entry` with its preview (end card or best frame; no rating; then `teamlog.py posted`), and read the product's flagged losers before writing the next script (`core/ad-review/AD-REVIEW.md` §3–4).

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "lovara", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["LOVARA BY EVERLIFE"], "head_always": true,
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "<✅ bible>"],
 "ingredients_label": "3-IN-1 INTIMACY SUPPORT",
 "ingredients": [["DESIRE","Supports Desire + Sensitivity"],["COMFORT","Promotes Comfort + Responsiveness"],["READINESS","Supports Intimate Readiness"]],
 "cta": "<✅ bible CTA in caps>", "vocab": "Lovara by Everlife."}
```
`"product"` is required: the tools take everything product-specific from `product.json` (verbatim disclaimer, renders, name casing,
review highlight) and refuse a job without it. Don't type the disclaimer into copy.json. The "ingredients" rows are ✅ benefit
pillars, not ingredient claims, while the ingredient list is under review (Justin). The `tiktok` CTA button fits ≈ 20 characters
("EXPLORE LOVARA", "DISCOVER LOVARA", "SAVE UP TO 45%" all fit; the CTA is one of `references/bible.json` ctas).

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw_vo.mp4 <Tag> --end 11 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("Lovara"), merge one-word chunks, restore "?", re-run. Check
4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch. Lovara: prefer `tiktok`/`editorial` in the women's
colours.

## 3. Image finishing
Batch Mode: `finish_batch.py --product lovara` (see `image-batch.md`). 9:16 from the approved 4:5 (`compose916.py`), or a 9:16 raw
via `reposition_916.py` + `--fit trusted`. `finish_modern.py` refuses this product until its `product_zones` are calibrated in
product.json. `compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (hook, look), cost, any known issue in plain words.
