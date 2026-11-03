# QA + finishing (zero manual editing)

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

## 0. Safe zones (every 9:16 image and video)
Logo, headline, offer, CTA, captions, proof and disclaimer live only inside **x 156–924, y 144–1385, minus the Reels
profile notch 156–375 × 1216–1385** (`tools/safezones.py`). The finishers refuse to export on a violation (exit 3 video,
2 image): never override; fix the layout or re-roll. QA view: `python -c "import safezones,PIL.Image as I; safezones.overlay(I.open('frame.png')).save('qa.png')"`.
Feed (4:5, 1:1): 60 px margin.

## 1. QA the raw output (always, before the user sees it)
- Contact sheet: `$FF -v error -y -i raw.mp4 -vf "fps=2,scale=180:-1,tile=10x3" -frames:v 1 sheet.jpg`, then Read it.
- Cuts: `$FF -i raw.mp4 -vf scdet=threshold=12 -f null - 2>&1 | grep -oE 'scd.time: [0-9.]+'`
- Transcript: faster-whisper from `$T/venv`; compare with the approved script.
- Pass/fail (tell the user every fail):
  - **product correctness:** the Titan-Rx bottle (matte black, chrome TITAN-RX); the label matches its render; not mirrored
    (`--mirror-until <cut>`); the capsule matches the capsule render exactly (chrome, TITAN-RX print) and there is exactly one
  - people: a real-looking man 40–65 (rugged, strong, hardcore-training feel, not a bodybuilder caricature), clothed, shoulder-up/
    waist-up, candid, an ordinary non-famous face; **no bare torso, no bed or bedroom in any frame**
  - no needles/syringes/vials, no body shots, no garbled text on props, no second phone (`--zoom 1.2`)
  - product name pronounced clearly ("Titan-Rx", "TIE-tan R-X"; the formula, if spoken, as "tadalafil, vardenafil and
    L-arginine", all three together, no claim on one); no "arousal", "ED", timing words or offer; nothing said that isn't on the
    bible page
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product titan-rx --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** each clip is already in the Prompt & Outcome Log (logged when submitted, `video-prompting.md`); now log the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log. Unreachable → the pending file, never block.

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "titan-rx", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["TITAN-RX BY EVERLIFE"], "head_always": true,
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "<✅ bible>"],
 "ingredients_label": "3-IN-1 PERFORMANCE FORMULA",
 "ingredients": [["DAILY","Once-Daily, No Timing Required"],["CIRCULATION","Supports Circulation + Firmness"],["READINESS","Supports Everyday Readiness"]],
 "cta": "<the session's CTA in caps>", "vocab": "Titan-Rx by Everlife. Tadalafil, Vardenafil, L-Arginine."}
```
`"product"` is required: the tools take everything product-specific from `product.json` (verbatim disclaimer, renders, name casing,
review highlight) and refuse a job without it. Don't type the disclaimer into copy.json. **The "ingredients" rows are ✅ benefit
pillars, never one benefit per ingredient**: the bible allows ingredient claims only on their own ingredient, and all three are ⚠/❌
in the pre-screen, so none are used. No offer row ("Save up to 49%" unverified). Videos keep "Titan-Rx by Everlife"; images never
say "by Everlife". The `tiktok` CTA button fits ≈ 20 characters ("GET STARTED NOW", "FIND YOUR PLAN", "EXPLORE TITAN-RX",
"START DAILY SUPPORT" fit; "GET PERFORMANCE SUPPORT" is 23: use `default`/`editorial` for it).

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("Titan-Rx", "Tadalafil", "Vardenafil", "L-Arginine"), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch.

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product titan-rx` (see `image-batch.md`). At 4:5 it does not refuse text under the footer: look at
every final. `finish_modern.py` refuses this product until its `product_zones` (the colours that let it find the product in a
photo) are calibrated in product.json. Legacy
`core/scripts/finish_image.py` layouts work (`standard`, `checklist`, `article`, `letter`, `split`, `frame`) with `"product"`
in copy.json (article kicker defaults to "MEN'S PERFORMANCE"); `compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (audience, hook, look), cost, any known issue in plain words.
