# QA + finishing (zero manual editing)

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

**Disclaimer:** `product.json` carries the standard ad disclaimer, now on the bible page too (sync 2026-11-03).
The finishers add it verbatim.

## 0. Safe zones (every 9:16 image and video)
Logo, headline, offer, CTA, captions and proof live only inside **x 156–924, y 144–1385, minus the Reels profile notch 156–375 ×
1216–1385** (`tools/safezones.py`); the disclaimer sits alone at the very bottom (`"disclaimer_at": "bottom"` in product.json). The
finishers refuse to export on a violation (exit 3 video, 2 image): never override; fix the layout or re-roll.
Feed (4:5, 1:1): 60 px margin.

## 1. QA the raw output (always, before the user sees it)
- Contact sheet: `$FF -v error -y -i raw.mp4 -vf "fps=2,scale=180:-1,tile=10x3" -frames:v 1 sheet.jpg`, then Read it.
- Transcript: faster-whisper from `$T/venv` (`vad_filter=True`, no prompt hint, to check for stray speech); compare with the script.
- Pass/fail (tell the user every fail):
  - **product correctness:** the pump bottle matches the render (navy label, champagne-gold cap and base, EVERLIFE / GHK / Peptide
    Cream / RX ONLY / 30G); **no strength or percentage invented on the label**; not mirrored (`--mirror-until <cut>`); exactly one
    bottle; **no tablet, capsule, dropper, jar, tube or any other product**
  - people: real-looking women 30–55, candid, sun-lit, an ordinary face (**no celebrity likeness**); lean and fit, **never a
    bodybuilder or "huge" physique**; no body-shape, waist or weight cues
  - **no before/after, no side-by-side skin, no skin-condition close-ups** (wrinkles, blemishes, scars); no mirror "transformation"
  - **no oranges or greens** anywhere (props, plants, clothes, light grade); gold stays champagne
  - no needles/syringes/vials, no garbled text on props, no second phone (`--zoom 1.2`)
  - product name said as "G-H-K Peptide Cream" (H2: "GHK-Cu Cream"); **never "copper"**; nothing said that isn't on the bible page
  - speech starts in the first second and ends by ~10.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product ghk-cream --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** log each generated clip to the Prompt & Outcome Log, the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log. Unreachable → the pending file, never block.

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "ghk-cream", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["GHK PEPTIDE CREAM BY EVERLIFE"], "head_always": true,
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "<✅ bible>"],
 "ingredients_label": "PEPTIDE SKIN SUPPORT",
 "ingredients": [["COLLAGEN","Supports Collagen + Elastin"],["TEXTURE","Supports Smoother-Looking Texture"],["TONE","Supports a Brighter, More Even-Looking Tone"]],
 "cta": "<✅ bible CTA in caps>", "vocab": "GHK Peptide Cream by Everlife."}
```
`"product"` is required: the tools take everything product-specific from `product.json` (verbatim disclaimer, render, name casing,
review highlight) and refuse a job without it. Don't type the disclaimer into copy.json. The "ingredients" rows are ✅ benefit
pillars (GHK is the only named ingredient; no other ingredient is on the bible page). `kicker` defaults to "PEPTIDE SKIN SUPPORT"
(`product.json` `kicker_default`). The `tiktok` CTA button fits ≈ 20 characters ("GET STARTED NOW", "SUPPORT FIRMER SKIN" fit;
"UPGRADE YOUR SKIN ROUTINE" and "EXPLORE GHK PEPTIDE CREAM" need `default`/`editorial`). H2 jobs: head "GHK-CU CREAM BY EVERLIFE",
vocab "GHK-Cu Cream by Everlife.", and no line that says "GHK Peptide Cream". The end card has no tablet: the bottle stands alone.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw_vo.mp4 <Tag> --end 11 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("GHK Peptide Cream", never "GHK cu" / "copper"), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.
**End card (looked at in the smoke test, 2026-11-02):** the headline stays clear, but the slim pump renders small (300 px tall,
~70 px wide on 1080 × 1920): the bottle reads, its label does not. Always give the raw video a product beat with the label large
(beat 3). The `default` look's benefit cards cut lines longer than ~25 characters ("Supports Smoother-Looking…", "Supports a Brighter,
More Even-Looking…" lost their last word): with those benefits use `tiktok` or `editorial`, or pick lines that fit; LOOK at the
end-card frame every time. The `default` look also carries a teal glow and teal dots (house style), and `tiktok` teal check icons:
teal is outside this product's pinks/tans/beige; prefer `tiktok`/`editorial` and flag the teal in SESSION.md until Justin says
whether house elements are exempt.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `tiktok` (beige/cream field: closest to the palette) · `editorial` · `default` (house navy/gold matches the bottle, but see
the teal and line-length notes above); vary across a batch; keep every look in pinks, tans and beige where colour is chosen (no
orange, no green).

## 3. Image finishing
Batch Mode: `finish_batch.py --product ghk-cream` (see `image-batch.md`). 9:16 from the approved 4:5 (`compose916.py`), or a 9:16
raw via `reposition_916.py` + `--fit trusted`. `finish_modern.py` refuses this product until its `product_zones` are calibrated in
product.json. `compare` is refused (no approved comparison); the `split` layout is never a before/after or a skin comparison.

## 4. Report to the user
One block per asset: path, what it is (hook, look, channel/name), cost, any known issue in plain words. Close with "provisional
disclaimer: Jeremy to confirm".
