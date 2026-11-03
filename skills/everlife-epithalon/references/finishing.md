# QA + finishing (zero manual editing)

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

Disclaimer: the standard text in product.json, now on the bible page too (sync 2026-11-03); the finishers render it.

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
  - **product correctness:** the label matches the Epithalon vial render (teal label: EVERLIFE · EPITALON · 10MG/ML · RX ONLY · 5ML;
    the label's EPITALON spelling is right, never "corrected"); not mirrored (`--mirror-until <cut>`);
    **no syringe, needle, pen, dropper, droplets or injecting in any frame**; no capsules, tablets or pills anywhere
  - people: adults 45–65 in calm daytime moments (`direction.md`); never a physique or a mirror; nobody in a before/after or
    side-by-side face/body comparison; **no bed, bedroom, night, alarm clock or anyone waking up** (product Hard NO)
  - no garbled text on props, no second phone (`--zoom 1.2`), no clinic/physio settings
  - product name pronounced clearly ("Epithalon", said "eh-PITH-uh-lon") with "by Everlife"; nothing said that isn't a ✅ line
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product epithalon --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** log each generated clip to the Prompt & Outcome Log, the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log. Unreachable → the pending file, never block.

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "epithalon", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["EPITHALON BY EVERLIFE"], "head_always": true,
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["Supports Healthy Aging", "Supports Oxidative Stress Defense", "Doctor Prescribed"],
 "ingredients_label": "HEALTHY AGING",
 "ingredients": [["AGING", "Supports Healthy Aging"], ["DEFENSE", "Supports Oxidative Stress Defense"], ["PHARMACY", "Doctor Prescribed"]],
 "cta": "<✅ bible CTA in caps, e.g. START LONGEVITY SUPPORT>", "vocab": "Epithalon by Everlife."}
```
`"product"` is required. The end card shows the vial alone, centred. The rows are the two ✅ benefits + "Doctor Prescribed" (a sourced
trust signal) unless the user OKs ⚠ "Supports DNA + Cellular Health" (flag for Jeremy). `end_head` = a ✅ benefit or a ⏳ headline with
an OK; never a sleep line.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("Epithalon"; whisper writes "Epitalon", "Epithelon"), merge one-word chunks, re-run. Check 4 frames (hook,
mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch. No palette limit for this product.

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product epithalon` (see `image-batch.md`). `finish_modern.py` refuses this product until its
`product_zones` are calibrated in product.json. Legacy `core/scripts/finish_image.py` layouts work (`standard`,
`checklist`, `article`, `letter`, `split`, `frame`) with `"product"` in copy.json (article kicker defaults to "HEALTHY AGING", product.json `kicker_default`);
`compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (audience, angle, look), cost, any known issue in plain words.
