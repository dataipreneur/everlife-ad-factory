# QA + finishing (zero manual editing)

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

Disclaimer: GLP-1's own bible text, verbatim in `product.json` (ends "Compounded medications are not FDA-approved.").

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
  - **product correctness:** the label matches the form's vial render ('Compounded' box · SEMAGLUTIDE or TIRZEPATIDE · RX ONLY), one vial only; not mirrored (`--mirror-until <cut>`);
    **no syringe, needle, pen, dropper, droplets or injecting in any frame**; no capsules or pills anywhere
  - people: everyday adults 30–60, clothed, shoulder-up; never a body shot, scale, tape, waistline or mirror; no before/after
  - no garbled text on props, no second phone (`--zoom 1.2`), no clinic/physio settings
  - product name pronounced clearly ("G-L-P one"; "compounded semaglutide / tirzepatide" in full if spoken); nothing said that isn't on the bible page
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
**Proof split, videos too (bible 2026-11-02, Standards 02 · 06):** each video carries ONE proof in its footer, the trust row (~60%) or "Over 100,000 happy customers" (~40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product glp-1 --log <tag>` and put its answer in copy.json as `"proof": "trust"` or `"proof": "count"` (animated stills: `animate_still.py --proof …`).

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "glp-1", "form": "semaglutide|tirzepatide", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["GLP-1 BY EVERLIFE"], "head_always": true,
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "One Price, No Surprise Increases"],
 "ingredients_label": "PROVIDER-GUIDED FROM HOME",
 "ingredients": [["APPETITE", "Supports Appetite Regulation"], ["FOOD NOISE", "Helps Reduce Food Noise"], ["ONE PRICE", "No Surprise Increases"]],
 "cta": "<✅ bible CTA in caps>", "vocab": "GLP-1 by Everlife."}
```
`"product"` and `"form"` (semaglutide | tirzepatide) are required; the end card shows that vial alone. The rows are ✅ benefit
pillars; the price line is always one of them.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("GLP-1", "compounded"), merge one-word chunks, re-run. Check 4 frames (hook,
mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch. Women-only: prefer `tiktok`/`editorial`
(check nothing reads orange or green).

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product glp-1` (see `image-batch.md`). `finish_modern.py` refuses this product until its
`product_zones` are calibrated in product.json. Legacy `core/scripts/finish_image.py` layouts work (`standard`,
`checklist`, `article`, `letter`, `split`, `frame`) with `"product"` in copy.json (article kicker defaults to "WEIGHT MANAGEMENT", product.json `kicker_default`);
`compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (audience, angle, look), cost, any known issue in plain words.
