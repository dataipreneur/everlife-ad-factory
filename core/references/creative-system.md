# Creative system (shared by every Everlife product skill) — adopted 2026-10-29

> **⛔ PROMPT LAYOUT ZONES = `core/references/prompt-layout-zones.md` (Mitansh, 2026-11-04, HARD, every image prompt, every product; wins over every LAYOUT number in this file):** every 9:16 / 4:5 prompt carries that file's STRICT LAYOUT block (9:16: top 16% empty, all text + product in 16-56%, plain calm surface below, central 67% width; 4:5: top 14% empty, product last and lowest, bottom 33% plain). Never 12% tops or 70-76% widths again.

> **🔁 NEVER STOP AFTER A BATCH (Mitansh, 2026-11-02, every product, images AND video: "As soon as 1st batch is done, start writing prompts for 2nd batch! this is the rule for all products!"):** the moment a batch is finished, shown and rated, start the NEXT batch in the same turn, without asking: same setup (audience, strength/form, ratio, model, boldness, mood) unless the user changed it; new styles/scenes per the variety rules (untried styles first); fix what QA found in the last batch inside the new prompts; show the batch table + Tier B headline options and ask for the approval (cost shown). The spend gate still holds: nothing is generated until the user approves that batch. Videos: the next script is written while the last one renders (SKILL.md step 4).

> **⛔ Proof row ALWAYS inside the Meta safe area (Mitansh, 2026-11-02, HARD, every product, every skill, image AND video):** the Trustpilot / Doctor Prescribed / Ships Free / 100,000+ proof row ends at or above y 1385 on 1080×1920 (`safezones.py`). Never move it lower or outside the safe area by any means (env `EVERLIFE_PROOF_AT`, copy.json `proof_at`, flags, manual edits); the tools refuse. If the product or text collides with the proof row: re-roll the raw (cost approved) or ask the user. Never move the footer. The disclaimer alone may sit at the very bottom.

> **✋ TABLET-IN-HAND CAP (Mitansh, 2026-11-02: "Holding tablets in hand should never be more than 20% of times!"; OVERRIDES "the tablet is HELD", "Slot 1 is always F2 tablet in hand" and every hold line below):** at most 20% of the ads in any batch show a hand holding the tablet (5 ads → max 1; 10 → max 2). Every other ad stages the tablet WITHOUT a hand: on a surface beside the bottle, on a gym bench / plate / chalk tray, macro hero on texture, a big floating product shot, tablet on top of the cap, in the S-plate metaphor. The tablet stays the hero (large, sharp, exact render) and the person, if any, does something else (training, resting, looking at camera). Plan the hold column in the batch table and count it before asking to generate.

> **⛔ NEVER `reposition_916.py`, edge-stretch, blur or padding colour on a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. **If its text or product runs into the footer, ALWAYS fix it in code first (Mitansh, 2026-11-02: "make sure to do it always"):** `$T/venv/bin/python -I $T/mirror_fit_916.py <raw> repo/rN.png --top <content top> --bottom <content bottom>` (0 credits: uniform scale into the band 0.115–0.635, margins filled by mirror-tiling a thin text-free edge strip), then the finisher as above on `repo/rN.png`. LOOK at the result. Re-roll (cost approved) ONLY when a person, text or the product touches a side edge of the raw (the mirror would copy it) or the tool refuses (scale < 0.65). Never ship a smeared edge.

Source: the creative team member's Restora-Z work (audit `my-ad-changes.md`, 2026-10-29) distilled to what holds for ANY form:
a capsule bottle, a tablet, a vial, a spray, a cream. Mitansh: "add these across all skills". Product-specific facts stay in each
skill's `product-bible.md` / `product.json`; the form's hero element is `product.json → hero`.

## 0. MANDATORY in every video, no exceptions (Mitansh, 2026-10-30; bible v3 "[Product] by Everlife" in every intro)
- **The VO says "<Product> by Everlife"** (e.g. "Restora-Z by Everlife…", "BPC-157 by Everlife…", "PT-141 by Everlife…") in the
  first spoken lines (by ~3 s, right after or inside the hook), and the script refers to the product by name, not only "this".
  This overrides any brief that says "never say the product name".
- The same "<PRODUCT> by Everlife" line is on screen in the intro (header/subline from frame 0).
- Write the pronunciation into the prompt: "Restora-Z" = "res-TOR-uh zee" (Creatify TTS: "Restora Zee"); BPC-157 = "B-P-C
  one-fifty-seven"; PT-141 = "P-T one-forty-one". Transcript QA must hear the product name AND "by Everlife"; if either is
  missing or mispronounced, the raw fails (re-roll with cost, never ship).
- Statics are unchanged: no "by Everlife" on images (Priestley, 2026-10-29); the logo carries the brand.

## 1. Variety is structural (the batch table enforces it)
Every slot in a batch differs on ALL of these; "same layout, new background" is not a variation:
- **Structure** (rotate; never two alike in a batch): split · stacked panels · timeline · poster · billboard · calendar page ·
  type-only · **article** (newspaper page, magazine spread, open letter, caption post) · product-hero · comparison of methods.
- **Product angle**: upright · tilted · lying · levitating · cap/top off · overhead · held · low angle. Mix "with the pack" and "hero only".
- **Typeface named in the prompt** for the concept (a real face or a precise description); the type-specimen reference is dropped
  when variety is wanted. Heavy condensed / wide extended / slab / high-contrast serif / rounded / mono / stencil / serif+italic word.
- **Own palette per ad** (name 2–3 colours). Never two ads in one batch in the same colour world; never the same world two batches running.
- **Product-name treatment** rotates: oversized behind the subject · overlapped by the hero · vertical · stacked · masthead · small and quiet.
- **Headline placement** rotates: top-left · centred · split either side of the product · bottom-third above the footer.
- **Focal point** (bible Standards 03, 2026-11-03; replaces "the pill is the hero, not the bottle"): **40% pill-focused** (pill in the foreground, sharp, the primary focal point) · **30% bottle-focused** (premium product photography of the bottle) · **30% person-focused** (a person is the primary focal point: lifestyle, emotion, relatability). Plan it in the batch table's **Focal** column before writing prompts (batch of 4 = 2 pill / 1 bottle / 1 person; 8 = 3 / 3 / 2; odd counts round the pill share up). A person may appear in a pill- or bottle-focused ad (the hardcore-men share counts men in any slot; Justin OK 2026-11-03); "person-focused" means the person is the main subject. Products without a pill (vials, the GHK pump): **75% product-focused · 25% person-focused** (Justin, 2026-11-03: "For non pill products the vial should be 75%"). Every ad: product and benefit identifiable in under 2 s, product in focus. **Videos follow the same split as statics** (Justin, 2026-11-03: "Videos and statics should really be the same in the sense of how we’re presenting products"): plan each video's Focal by its main product shot.
Article formats get at least ONE slot in every batch of 5 (they performed on Restora-Z and are product-agnostic).

## 2. The model draws the scene; real brand assets are laid deterministically afterwards
Never trust the model with a logo, a label, a rating badge, a disclaimer or a product render:
- **Logo:** prompt "NO logo or wordmark anywhere" (or, for mastheads/comics, "an EMPTY white box top-right of the masthead"), then
  `finish_batch.py` lays the real mark: default 311 px; large = `--logo-w 40%` (top-centre) or `--logo-w 36% --logo-pos right|left`
  (small variants 30% / 28%); ink switches to dark when the top band is brighter than `LOGO_T` (135). Masthead box → `logo_in_box.py`.
- **Label / render:** garbled or wrong-strength label → `reposition_916.py --composite <render> x0 y0 x1 y1` (pastes the real
  transparent render over the generated product; matched perfectly on BPC-157 batch 1). Never pay for an AI label fix.
- **Proof + disclaimer:** always the approved footer art, verbatim text from `product.json`; never typed into the prompt. On 9:16 the
  proof row sits in the safe area (ends y 1385), ~32% bigger than the 2026-10-28 size and ~1000 px wide (it crosses the Reels side
  bands by ~116 px: Mitansh 2026-10-29 "it's alright"), and the disclaimer sits at the very bottom of the frame. All of this is the
  shared finisher's default (EVERLIFE_PROOF_SCALE 1.3225, EVERLIFE_PROOF_W 1000, EVERLIFE_DISC_AT bottom): no per-skill setup.
- **One footer size everywhere (Justin 2026-11-02):** the trust row is 990 px wide and the disclaimer is 18 px Inter Medium,
  exactly 2 lines, on every creative, image or video ending (`core/tools/standard_footer.py`; every finisher uses it).
- **Proof split (Mitansh 2026-11-02, from bible Standards 02 · 06; graphics looked cluttered):** **30%** of creatives carry NO proof
  element; **70%** carry ONE footer proof: of those, **60%** the trust row (Trustpilot / Doctor Prescribed / Ships Free) and **40%** the
  approved Trustpilot 4.9 Excellent badge + "Over 100,000 happy customers" (Mitansh: "over 100k customers should at least have the
  trustpilot logo besides it"). Overall ~42% trust / ~28% count / ~30% none (`standard_footer.SHARE`). Images: run
  `finish_batch.py --proof-plan N` for an N-ad batch (it opens on the trust row), put its answer in the batch table's **Proof**
  column, and pass it on every finish: `--proof trust` / `--proof count` / `--proof none`. An ad's 4:5 and 9:16 use the same value.
  Videos too (Priestley 2026-11-02): `core/scripts/proof_next.py --product <id> --log <tag>` → copy.json `"proof"`; the footer
  carries the one proof (or none) through the end card, which has no count line of its own. Logo and verbatim disclaimer stay on every creative.
- **Enforced, no exceptions (Mitansh 2026-11-02: "have this enforced everywhere… without any conflicts!"):** the split holds per batch
  AND per ratio. (1) Plan it before writing prompts (`--proof-plan N`, Proof column). (2) Every slot planned trust/count gets a clean
  shelf in its LAYOUT block: 9:16 product, CTA, sticker and faces end above y 1150 of 1920 (raw 2048: y 1225), with plain scene under
  it; 4:5 / 1:1 bottom 18% calm. (3) Finish with the planned value; if the row would cover the product, CTA, a sticker or a face, do
  NOT switch to none: re-roll that raw (cost shown) or ask. (4) `finish_batch.py --proof-check <batch folder>` must print ✅ before the
  batch is shown (it reads `proof_log.jsonl`, written by every finish). Videos: `proof_next.py` per video, never overridden to none.

## 2b. Both sizes at once (Mitansh, 2026-11-04, every product, every image batch)
"You did this crazy fast… always do such thing, both sizes simultaneously." Every image ad = a fresh 9:16 render AND a fresh 4:5
render in the same run (proven on PT-141 "We're Sorry" and GLP-1 batch 1, 2026-11-04).
1. Write BOTH prompts per ad before the first submit. Each carries its own STRICT LAYOUT block from
   `core/references/prompt-layout-zones.md` (9:16 zones; 4:5 element order, product last and lowest).
2. Submit every 9:16 raw, then every 4:5 raw straight after (Creatify queues past 4 in flight; never stop to finish or QA between).
3. Only then download all raws, finish both ratios with the SAME planned proof per ad, QA both, and show one sheet with both sizes.
4. Separate work folders (`916/`, `45/`) or `adN_916` / `adN_45` names; finals carry `_1080x1920` / `_1080x1350`.
5. Never crop, pad, stretch or paste one size into the other (`compose916.py` is for re-making an approved old ad only).
6. Quote 2 credits per ad (GPT Image 2.5). A size that fails QA is fixed alone (Free Fix, 0 cr; or a re-roll of that size only).
Both sizes are drafts: the approval gate (gates §7) still governs delivery, and Jeremy signs off before anything goes live.

## 3. The hero is deliberate and sized
The form's hero (`product.json → hero.element`: the capsule, the tablet, the vial, the spray) fills **≥ 35% of the canvas width**,
is never abstracted (no glass orbs, icons or silhouettes), and its label follows the curved surface in perspective. Random, tiny or
duplicated heroes fail QA. Multiples (floating pills, stacked vials) need MANY elements at different depths, not three; the hero
and every label stay sharp (bible 2026-11-02: "the product is always in focus, in every static and video asset"), only background
repeats may soften.
`hero.never` lists what must never appear with it (e.g. syringes for a vial).

## 4. Required strings are prompt strings with a post-check
CTA (bible list), headline, every benefit line and any offer go in the prompt's TEXT block as exact strings, and QA reads every
result for each string (the model still drops a CTA ~1 in 10). A missing or altered string = fail → one free local fix or one re-roll.

## 5. The footer must not degrade what sits above it
- **No proof row → no shadow band (Mitansh, 2026-11-02, every product, image + video: "Why do you have this shadow??"):** the
  finishers only paint the footer scrim/gradient when there IS a proof row (or disclaimer block) to read. `--proof none` /
  copy.json `"proof": "none"` leaves the art untouched except the small fade behind the bottom disclaimer. QA every no-proof
  final for a dark band across ~y 1230–1545; if one shows up, the installed toolkit is stale: `bash core/scripts/preflight.sh --install`.
- Run `unfade_cta.py raw final out --ratio …` when a CTA or line sits just above the footer (the transparent footer's fade washes it out).
- A native 9:16 raw is finished AS IS: `finish_batch.py --fit trusted --shift 0` (logo, proof row in the safe area, disclaimer at the
  bottom). NO repositioning, padding, blur or auto-shift (Mitansh 2026-10-29: "0 blurring, the raw ones look better"). If the raw
  collides with the logo or the proof row, re-roll with a stronger LAYOUT line or accept it. Never a paid reposition edit either.

## 6. 9:16 is built from the approved 4:5, never re-prompted
`compose916.py approved_4x5.png plate_9x16.png out.png` places the approved ad as an exact **740×925 panel at (170,150)**, feathered
32 px, on a text-free 9:16 background plate generated FROM that ad (1 credit; state the horizon height so it lines up), then
`finish_batch.py --ratio 9:16 --fit trusted` lays the logo and the safe-area footer. 5/5 worked where native 9:16 re-makes failed 5/5.

## 7. Feedback becomes rules the same day
**Team logs (every batch, 2026-11-03):** before writing copy read the Copy Ledger (no repeated lines, the team's recent styles and
proof split); log every generation to the Prompt & Outcome Log; after the batch log copy, styles, proofs and the run's spend.
Never blocks a batch. How: `core/team-logs/TEAM-LOGS.md`. Learning report only when someone asks.
Team feedback → `references/lessons.md` with the fail count → applied in the next batch → helper promoted into `core/tools/`.
Nothing lives only in an output folder.

## What stays product-specific (do NOT generalise)
Ingredient panels with real tablet colours (combo supplements only), the Ambien pill, palettes tied to a category, "glow" words,
men's/women's direction, claims. Those live in each skill's bible.

## Prompt checklist (paste into every batch table review)
structure ≠ any other slot · article slot present · product angle ≠ others · typeface named · palette named · name treatment ·
headline placement · hero ≥ 35% width, real, label wraps · CTA string in TEXT · "NO logo" or "empty box" · forbidden elements named

## No haze behind the footer (Mitansh 2026-11-04, every product, image AND video)
The creative director flagged "the blurry area behind the Trustpilot footer" all day. Every finisher now lays the proof row and the
disclaimer straight on the art, with NO scrim, gradient band or panel fade behind them (`finish_batch.py`, `finish_modern.py` feed
footer, `core/scripts/finish_image.py`, `full_layout.py`, `premium_finish.py`). The text colour follows what is behind it
(`standard_footer.tone_of` / `video_tone`: mean luminance above 118 → dark text and the dark-text trust row
`assets/proof_row_clear_dark.png`, badge art untouched; below → cream text). So prompts must keep the footer band CALM (plain
continuing background, no product, no busy texture); if the product or CTA reaches the footer, drop the footer or re-roll, never add
a haze. `EVERLIFE_SCRIM=1` brings the old haze back for one run (only if Mitansh asks); `EVERLIFE_FOOTER_TONE=dark|light` forces a tone.
