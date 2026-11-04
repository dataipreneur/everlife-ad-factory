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
  - **product correctness:** the right FORM; the label matches its render; not mirrored (`--mirror-until <cut>`); sublingual:
    the tablet matches the tablet render exactly and there is exactly one; spray: no tablet anywhere, never sprayed on camera
  - people: real-looking, 30–55, clothed, shoulder-up/waist-up, candid; **no bed or bedroom in any frame**; palette right (women)
  - no needles/syringes/vials, no body shots, no garbled text on props, no second phone (`--zoom 1.2`)
  - product name pronounced clearly ("P-T one-forty-one"); nothing said that isn't on the bible page
  - last spoken line ends before ~12.5 s
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing — premium post-edit (DEFAULT since 2026-11-02; ask the style question first)
After the raw passes §1 QA, ASK the post-edit style question and finish with `premium_finish.py`, exactly as
`core/references/premium-finish.md` says (4 styles: V1 Champagne, V2 Black Label, V3 Subtle, V4 Quiet Luxe; recommended = least
recently used for this product, alternating bold/calm; log the choice). The classic `full_layout.py` route below is used only when
the user asks for it or a job needs one of its extras (review burst, mirror fix, zoom); its copy rules (bible-only lines, verbatim
disclaimer, caption spellings) apply to premium.json too.

## 2b. Classic finishing (full_layout.py, on request only)
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product pt-141 --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** each clip is already in the Prompt & Outcome Log (logged when submitted, `video-prompting.md`); now log the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log (`teamlog.py copy / proof / run`, then `close` ✅ before SESSION.md). Unreachable → the pending file, never block. **Ad Review:** post each finished video as an `entry` with its preview (end card or best frame; no rating), and read the product's flagged losers before writing the next script (`core/ad-review/AD-REVIEW.md` §3–4).

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "pt-141", "form": "spray|sublingual", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["LINE 1", "LINE 2"], "sub": "subline (house only)",
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<bible>", "<bible>", "<bible>"],
 "ingredients_label": "NON-HORMONAL DESIRE SUPPORT",
 "ingredients": [["BRAIN-BASED","Supports central desire pathways"],["ON-DEMAND","Desire support on your schedule"],["NON-HORMONAL","Supports brain-based desire"]],
 "cta": "<bible CTA in caps>", "vocab": "PT-141."}
```
`"product"` and `"form"` are required: the tools take everything product-specific from `product.json` (verbatim disclaimer,
the form's renders, name casing, review highlight) and refuse a job without a product. `"form": "spray"` puts the spray alone,
centred, on the end card (no tablet); `"form": "sublingual"` puts the navy bottle + the tablet. Don't type the disclaimer into
copy.json; if it's there, it must match product.json exactly. The "ingredients" rows are the three-pillar card (PT-141 has one
ingredient, so the rows are approved benefit pillars, not ingredient claims).

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` ("PT-141", "non-hormonal"), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `default` (house navy/gold) · `tiktok` · `editorial`; vary across a batch. Women-only: prefer `tiktok`/`editorial` (check nothing reads orange).

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product pt-141` (see `image-batch.md`). `finish_modern.py` refuses this product until its
`product_zones` (the colours that let it find the product in a photo) are calibrated in product.json for each form. Legacy
`core/scripts/finish_image.py` layouts work (`standard`, `checklist`, `article`, `letter`, `split`, `frame`) with `"product"`
in copy.json (article kicker defaults to "INTIMATE WELLNESS"); `compare` is refused (no approved comparison).

## 4. Report to the user
One block per asset: path, what it is (audience, hook, look), cost, any known issue in plain words.
