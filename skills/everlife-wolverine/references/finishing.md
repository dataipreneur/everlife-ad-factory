# QA + finishing (zero manual editing)

> **💪 HARDCORE MEN = `core/references/hardcore-men.md` (Jeremy via Mitansh, 2026-11-02; OVERRIDES every "fully clothed / no bare torso / never shirtless / no flexing / not a bodybuilder / natural build" line and every winner's "Don't copy: shirtless" note in this skill):** men's ads lean intense: shirtless or stringer, 40–45, flawless muscular condition, hard gym light. 🎲 Surprise me / random: up to 30% of men's slots are HARDCORE (bible 2026-11-04 caps shirtless male talent at 30%) (`core/scripts/pick_styles.py --product <id> --n <N> --audience men|women|both` tags them). Whenever recommending a cast, mood or style for men, recommend hardcore first ("💪 Hardcore shirtless" as a mood). Copy still never ties the body to the product: no before/after, body comparison, body-composition claims or "ripped/shred".

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

Disclaimer: the bible's Wolverine Stack ad disclaimer, verbatim in `product.json` (`bible_sync.py --check` confirms it).

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
  - **product correctness:** the label matches the Wolverine Stack vial render (EVERLIFE / WOLVERINE / BPC-157 + TB-500 / 3MG/3MG/ML / RX ONLY / 5ML); not mirrored (`--mirror-until <cut>`);
    **no syringe, needle, pen, dropper, droplets or injecting in any frame**; no capsules or pills anywhere
  - people: rugged, strong men 25–55 per `mens-direction.md`; no competition posing, no mirror selfies; **no blood, gore or
    animal death**; nobody in a before/after or side-by-side body comparison
  - no garbled text on props, no second phone (`--zoom 1.2`), no clinic/physio settings
  - product name pronounced clearly ("Wolverine Stack"); nothing said that isn't on the bible page
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product wolverine --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** each clip is already in the Prompt & Outcome Log (logged when submitted, `video-prompting.md`); now log the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log (`teamlog.py copy / proof / run`, then `close` ✅ before SESSION.md). Unreachable → the pending file, never block. **Ad Review:** post each finished video as an `entry` with its preview (end card or best frame; no rating; then `teamlog.py posted`), and read the product's flagged losers before writing the next script (`core/ad-review/AD-REVIEW.md` §3–4).

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "wolverine", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["WOLVERINE STACK BY EVERLIFE"], "head_always": true,
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "<✅ bible>"],
 "ingredients_label": "RECOVERY STACK",
 "ingredients": [["TENDONS", "Reinforces Tendons + Ligaments"], ["MOBILITY", "Maintains Mobility"], ["GUT LINING", "Supports Gut Lining Health"]],
 "cta": "<✅ bible CTA in caps>", "vocab": "Wolverine Stack by Everlife."}
```
`"product"` is required. The end card shows the vial alone, centred. Don't type the disclaimer into copy.json. The "ingredients"
rows are ✅ benefit pillars, **never ingredient claims** (ingredients only together, as on the label, in the label line).

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("Wolverine Stack"), merge one-word chunks, re-run. Check 4 frames (hook,
mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch.

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product wolverine` (see `image-batch.md`). `finish_modern.py` refuses this product until its
`product_zones` are calibrated in product.json. Legacy `core/scripts/finish_image.py` layouts work (`standard`,
`checklist`, `article`, `letter`, `split`, `frame`) with `"product"` in copy.json (article kicker defaults to "RECOVERY");
`compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (audience, angle, look), cost, any known issue in plain words.
