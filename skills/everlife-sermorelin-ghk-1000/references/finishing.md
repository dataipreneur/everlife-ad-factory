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
{"style": "house|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["LINE 1", "LINE 2"], "sub": "subline (house only)",
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<bible>", "<bible>", "<bible>"],
 "ingredients_label": "3-IN-1 PEPTIDE SUPPORT",
 "ingredients": [["SERMORELIN","<✅ Sermorelin claim>"],["GHK","<✅ GHK claim>"],["L-CITRULLINE MALATE","<✅ Citrulline claim>"]],
 "cta": "<bible CTA in caps>",
 "disclaimer": "AI-generated depictions and simulated portrayals used for illustrative advertising purposes. Not actual patients or medical providers. Disclaimer: Individual results may vary. Doctor-prescribed compounded prescription.",
 "bottle": "sghk1000_bottle.png", "pill": "sghk1000_tablet.png", "vocab": "Sermorelin GHK.",
 "keep_case": ["Sermorelin GHK", "Sermorelin", "GHK", "L-Citrulline Malate", "IGF-1", "3-in-1"],
 "highlight": "Sermorelin(\\s*\\+?\\s*GHK)?",
 "reviews_json": "~/.claude/skills/everlife-sermorelin-ghk-1000/references/reviews.json"}
```
`keep_case` stops the tiktok/editorial looks from printing "Ghk"; `highlight` and `reviews_json` point the review burst at
this product (keep them even while the burst is gated, so it can never fall back to Restora-Z reviews).

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` (Sermorelin, GHK, growth hormone, Citrulline), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `house` · `tiktok` · `editorial`; vary across a batch. Women: prefer `tiktok`/`editorial` (the `house` navy/gold
is fine; check nothing reads orange).

## 3. Image finishing
Batch Mode: `finish_batch.py` (see `image-batch.md`). Don't use `finish_modern.py` for this product yet: its
"keep type off the product" detector is tuned to Restora-Z's teal bottle and blue capsule, so it can't see this bottle.
Legacy `core/scripts/finish_image.py` layouts work (`standard`, `checklist`, `article`, `letter`, `split`, `frame`) if
copy.json sets every key (e.g. `kicker`, otherwise it defaults to Restora's "SLEEP NOTES"); never `compare`.

## 4. Report to the user
One block per asset: path, what it is (audience, hook, look), cost, any known issue in plain words.
