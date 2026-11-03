# QA + finishing (zero manual editing)

> **💪 HARDCORE MEN = `core/references/hardcore-men.md` (Jeremy via Mitansh, 2026-11-02; OVERRIDES every "fully clothed / no bare torso / never shirtless / no flexing / not a bodybuilder / natural build" line and every winner's "Don't copy: shirtless" note in this skill):** men's ads lean intense: shirtless or stringer, 40–45, flawless muscular condition, hard gym light. 🎲 Surprise me / random: 40% of men's slots are HARDCORE (`core/scripts/pick_styles.py --product <id> --n <N> --audience men|women|both` tags them). Whenever recommending a cast, mood or style for men, recommend hardcore first ("💪 Hardcore shirtless" as a mood). Copy still never ties the body to the product: no before/after, body comparison, body-composition claims or "ripped/shred".

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

Disclaimer: the PT-141 wording, confirmed by Mitansh for BPC-157 (2026-10-29), stored verbatim in `product.json`; every SESSION.md
flags it for Jeremy's sign-off.

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
  - **product correctness:** the label matches the vial render (BPC-157 · 3MG/ML · RX ONLY · 5ML); not mirrored (`--mirror-until <cut>`);
    **no syringe, needle, pen, dropper, droplets or injecting in any frame**; no capsules or pills anywhere
  - people: MEN hardcore per `mens-direction.md` (bodybuilders, tattoos, chalk, hard light; shirtless or stringer fine), no
    competition posing, no mirror selfies; WOMEN strong and soft, clothed, 30–55; nobody in a before/after or side-by-side body
    comparison; women's palette right
  - no garbled text on props, no second phone (`--zoom 1.2`), no clinic/physio settings
  - product name pronounced clearly ("B-P-C one-fifty-seven"); nothing said that isn't on the bible page
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing — premium post-edit (DEFAULT since 2026-11-02; ask the style question first)
After the raw passes §1 QA, ASK the post-edit style question and finish with `premium_finish.py`, exactly as
`core/references/premium-finish.md` says (4 styles: V1 Champagne, V2 Black Label, V3 Subtle, V4 Quiet Luxe; recommended = least
recently used for this product, alternating bold/calm; log the choice). The classic `full_layout.py` route below is used only when
the user asks for it or a job needs one of its extras (review burst, mirror fix, zoom); its copy rules (bible-only lines, verbatim
disclaimer, caption spellings) apply to premium.json too.

## 2b. Classic finishing (full_layout.py, on request only)
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product bpc-157 --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "bpc-157", "form": "vial", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["LINE 1", "LINE 2"], "sub": "subline (house only)",
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["Supports Joints + Tendons", "Supports Faster Recovery", "Supports Gut Lining Health"],
 "ingredients_label": "RECOVERY SUPPORT",
 "ingredients": [["JOINTS + TENDONS","Supports connective tissue repair"],["MOBILITY","Supports mobility + flexibility"],["GUT LINING","Supports gut lining health"]],
 "cta": "<bible CTA in caps>", "vocab": "BPC-157."}
```
`"product"` and `"form": "vial"` are required. The end card shows the vial alone, centred. Don't type the disclaimer into copy.json. The "ingredients" rows are the three-pillar
card: BPC-157 is one compound, so the rows are quick-hit benefit pillars, never ingredient claims.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("BPC-157"), merge one-word chunks, re-run. Check 4 frames (hook,
mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch. Women-only: prefer `tiktok`/`editorial`
(check nothing reads orange or green).

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product bpc-157` (see `image-batch.md`). `finish_modern.py` refuses this product until its
`product_zones` are calibrated in product.json. Legacy `core/scripts/finish_image.py` layouts work (`standard`,
`checklist`, `article`, `letter`, `split`, `frame`) with `"product"` in copy.json (article kicker defaults to "RECOVERY");
`compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (audience, angle, look), cost, any known issue in plain words.
