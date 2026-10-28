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
    matches its render; not mirrored (`--mirror-until <cut>`); exactly one tablet
  - people: real-looking, the right age, fit but NOT bodybuilders, fully clothed; no bedroom (men); palette right (women)
  - no needles/syringes/vials, no gym-mirror body shots, no garbled text on props, no second phone (`--zoom 1.2`)
  - "growth hormone" said in full; product name pronounced clearly
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "sermorelin-ghk", "style": "house|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["LINE 1", "LINE 2"], "sub": "subline (house only)",
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<bible>", "<bible>", "<bible>"],
 "ingredients_label": "3-IN-1 PEPTIDE SUPPORT",
 "ingredients": [["SERMORELIN","<✅ Sermorelin claim>"],["GHK","<✅ GHK claim>"],["L-CITRULLINE MALATE","<✅ Citrulline claim>"]],
 "cta": "<bible CTA in caps>", "vocab": "Sermorelin GHK."}
```
`"product"` is required: the tools take everything product-specific from `product.json` in this skill (verbatim
disclaimer, renders, name casing so nothing prints "Ghk", review highlight and reviews file) and refuse a job without it.
Don't type the disclaimer into copy.json; if it's there, it must match product.json exactly. Until the transparent
bottle exists, add `"bottle": "sghk1000_bottle_ref.jpg"` (shows its black background on the end card: preview only).
500 mcg jobs set `"bottle": "sghk500_bottle.png"` (once it's in assets/); the tablet is the same for both strengths.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` (Sermorelin, GHK, growth hormone, Citrulline), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

**`tiktok` end card:** Sermorelin GHK's ingredient names and claims are too long for its name + claim rows (they overlap).
Set `"end_rows": "benefits"` and `"ingredients_label": "SERMORELIN + GHK + CITRULLINE"`: the rows then show the 3 bible
benefits. **Clip shorter than its speech + end card?** Marketing Studio fills the whole clip with speech, so hold the last
frame (`ffmpeg -vf tpad=stop_mode=clone:stop_duration=2.5 -af apad=pad_dur=2.5`) and start the end card after the last word.

Looks: `house` · `tiktok` · `editorial`; vary across a batch. Women: prefer `tiktok`/`editorial` (the `house` navy/gold
is fine; check nothing reads orange).

## 3. Image finishing
Batch Mode: `finish_batch.py --product sermorelin-ghk` (see `image-batch.md`). `finish_modern.py` refuses this
product until its `product_zones` (the colours that let it find the bottle and tablet in a photo) are calibrated in
product.json. Legacy `core/scripts/finish_image.py` layouts work (`standard`, `checklist`, `article`, `letter`, `split`,
`frame`) with `"product"` in copy.json (article kicker defaults to "STRENGTH · LONGEVITY"); `compare` is refused
(no approved comparison for this product).

## 4. Report to the user
One block per asset: path, what it is (audience, hook, look), cost, any known issue in plain words.
