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
  - **product correctness:** the tablet matches the tablet render exactly (shape, colour, markings) and the bottle label
    matches its render; not mirrored (`--mirror-until <cut>`); exactly one tablet; **no injection vial** (the past ads
    always paired the bottle with one: models will add it back)
  - people: real-looking, the right age, fit but NOT bodybuilders, fully clothed; no bedroom; palette right (women: no
    orange or green in the scene)
  - no needles/syringes/vials, no gym-mirror body shots, no garbled text on props, no second phone (`--zoom 1.2`)
  - "growth hormone" said in full; never "GH"; product name pronounced clearly; no "GHK" anywhere
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "sermorelin", "style": "house|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["LINE 1", "LINE 2"], "sub": "subline (house only)",
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "<✅ bible>"],
 "cta": "<bible CTA in caps>", "vocab": "Sermorelin."}
```
`"product"` is required: the tools take everything product-specific from `product.json` in this skill (verbatim
disclaimer, renders, name casing, review highlight and reviews file) and refuse a job without it. **Never** `"product":
"sermorelin-ghk"` for this skill: that prints the other product's renders. Don't type the disclaimer into copy.json; if
it's there, it must match product.json exactly. The default bottle is 1000 mcg; 500 mcg jobs set
`"bottle": "sermorelin500_bottle.png"` (once it's in assets/).

Single-ingredient product, but the `tiktok` and `editorial` end cards **require** `ingredients_label` + `ingredients`
(`core/tools/styles.py`; `house` doesn't). Fill them with the three ✅ benefits, never a made-up ingredient claim:
```json
 "ingredients_label": "DOCTOR-PRESCRIBED SERMORELIN",
 "ingredients": [["ENERGY","Supports Energy + Stamina"],["STRENGTH","Supports Strength + Vitality"],
                 ["GROWTH HORMONE","Supports Natural Growth Hormone Activity"]]
```
**`tiktok` look:** the third row collides at that length ("Growth Hormone" runs into its claim; seen in the 2026-10-28
smoke test), so use `["DELIVERY","Easy sublingual delivery"]` as the third row and carry growth hormone in the VO or
the header. Its CTA button fits ≈ 20 characters: "EXPLORE SERMORELIN", "GET STARTED NOW", "BUILD YOUR PLAN" fit;
"SUPPORT NATURAL GROWTH HORMONE" overflows (use it in `house`/`editorial` only, and check the frame). Check the end card renders without "3-in-1" wording and nothing overlaps.
The round tablet is drawn at `pill_end_scale` (product.json, 0.62) of the default end-card pill size so it doesn't cover
the label line or dwarf the bottle.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` (Sermorelin, growth hormone, sublingual), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `house` · `tiktok` · `editorial`; vary across a batch. Women: prefer `tiktok`/`editorial` (the `house` navy/gold
is fine; check nothing in the scene reads orange besides the product).

## 3. Image finishing
Batch Mode: `finish_batch.py --product sermorelin` (see `image-batch.md`). `finish_modern.py` refuses this product until
its `product_zones` (the colours that let it find the bottle and tablet in a photo; orange label + orange tablet, so
both zones will sit in the same hue band) are calibrated in product.json. Legacy `core/scripts/finish_image.py` layouts
work (`standard`, `checklist`, `article`, `letter`, `split`, `frame`) with `"product"` in copy.json (article kicker
defaults to "STRENGTH · LONGEVITY"); `compare` is refused (no approved comparison for this product).

## 4. Report to the user
One block per asset: path, what it is (audience, hook, look), cost, any known issue in plain words.
