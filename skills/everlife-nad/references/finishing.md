# QA + finishing (zero manual editing)

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

Disclaimer: NAD+'s bible text, verbatim in `product.json`.

## 0. Safe zones (every 9:16 image and video)
Logo, headline, offer, CTA, captions, proof and disclaimer live only inside **x 156–924, y 144–1385** (`tools/safezones.py`); the
proof footer ends at y 1385 and may cross the lower-left profile notch (creative lead, 2026-10-29). The finishers refuse to export on
a violation (exit 3 video, 2 image): never override; fix the layout or re-roll. QA view:
`python -c "import safezones,PIL.Image as I; safezones.overlay(I.open('frame.png')).save('qa.png')"`. Feed (4:5, 1:1): 60 px margin.

## 1. QA the raw output (always, before the user sees it)
- Contact sheet: `$FF -v error -y -i raw.mp4 -vf "fps=2,scale=180:-1,tile=10x3" -frames:v 1 sheet.jpg`, then Read it.
- Cuts: `$FF -i raw.mp4 -vf scdet=threshold=12 -f null - 2>&1 | grep -oE 'scd.time: [0-9.]+'`
- Transcript: faster-whisper from `$T/venv`; compare with the approved script.
- Pass/fail (tell the user every fail):
  - **product correctness:** the label matches the form's render (green bottle 'NAD+ … SUBLINGUAL TABLET' + the green tablet, or the green vial 'NAD+ · RX ONLY · 5ML'); not mirrored (`--mirror-until <cut>`);
    **no syringe, needle, pen, dropper, droplets or injecting in any frame**; no capsules; no pill except the one NAD+ tablet
    (sublingual ads), none in injection ads
  - people: everyday adults 30–65, ordinary faces, clothed; no celebrity look-alikes; no IV drips or clinic chairs
  - no garbled text on props, no second phone (`--zoom 1.2`), no clinic/physio settings
  - product name pronounced clearly ("N-A-D plus", bible); nothing said that isn't on the bible page
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product nad --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "nad", "form": "sublingual|injection", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["NAD+ BY EVERLIFE"], "head_always": true,
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "<✅ bible>"],
 "ingredients_label": "SUBLINGUAL TABLET OR INJECTION",
 "ingredients": [["FOCUS", "Supports All-Day Energy + Focus"], ["BURNOUT", "Supports Bounce-Back From Burnout"], ["AGING", "Promotes Healthy Aging"]],
 "cta": "<✅ bible CTA in caps>", "vocab": "NAD+ by Everlife. N-A-D plus."}
```
`"product"` and `"form"` (sublingual | injection) are required; the end card shows that form (bottle + tablet, or the vial).
The rows are ✅ benefit pillars.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("NAD+"), merge one-word chunks, re-run. Check 4 frames (hook,
mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch. Women-only: prefer `tiktok`/`editorial`
(check nothing reads orange or green).

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product nad` (see `image-batch.md`). `finish_modern.py` refuses this product until its
`product_zones` are calibrated in product.json. Legacy `core/scripts/finish_image.py` layouts work (`standard`,
`checklist`, `article`, `letter`, `split`, `frame`) with `"product"` in copy.json (article kicker defaults to "CELLULAR ENERGY", product.json `kicker_default`);
`compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (audience, angle, look), cost, any known issue in plain words.
