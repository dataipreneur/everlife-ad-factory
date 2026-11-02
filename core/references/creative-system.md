# Creative system (shared by every Everlife product skill) — adopted 2026-10-29

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
- **Proof split (bible 2026-11-02, Standards 02 · 06; graphics looked cluttered):** trust callouts (the Trustpilot / Doctor
  Prescribed / Ships Free row) go on ~60% of graphics, "Over 100,000 happy customers" on ~40%. Each image ad gets exactly ONE of
  the two, so none is left without proof. Images: run `finish_batch.py --proof-plan N` for an N-ad batch, put its answer in the batch
  table's **Proof** column, and pass it on every finish: `--proof trust` (the row) or `--proof count` (the customer-count line in
  the row's place). An ad's 4:5 and 9:16 use the same value. Videos too (Priestley 2026-11-02): `core/scripts/proof_next.py
  --product <id> --log <tag>` → copy.json `"proof"`; the footer carries the one proof through the end card, which has no count
  line of its own. Logo and verbatim disclaimer stay on every creative.

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
- Run `unfade_cta.py raw final out --ratio …` when a CTA or line sits just above the footer (the transparent footer's fade washes it out).
- A native 9:16 raw is finished AS IS: `finish_batch.py --fit trusted --shift 0` (logo, proof row in the safe area, disclaimer at the
  bottom). NO repositioning, padding, blur or auto-shift (Mitansh 2026-10-29: "0 blurring, the raw ones look better"). If the raw
  collides with the logo or the proof row, re-roll with a stronger LAYOUT line or accept it. Never a paid reposition edit either.

## 6. 9:16 is built from the approved 4:5, never re-prompted
`compose916.py approved_4x5.png plate_9x16.png out.png` places the approved ad as an exact **740×925 panel at (170,150)**, feathered
32 px, on a text-free 9:16 background plate generated FROM that ad (1 credit; state the horizon height so it lines up), then
`finish_batch.py --ratio 9:16 --fit trusted` lays the logo and the safe-area footer. 5/5 worked where native 9:16 re-makes failed 5/5.

## 7. Feedback becomes rules the same day
Team feedback → `references/lessons.md` with the fail count → applied in the next batch → helper promoted into `core/tools/`.
Nothing lives only in an output folder.

## What stays product-specific (do NOT generalise)
Ingredient panels with real tablet colours (combo supplements only), the Ambien pill, palettes tied to a category, "glow" words,
men's/women's direction, claims. Those live in each skill's bible.

## Prompt checklist (paste into every batch table review)
structure ≠ any other slot · article slot present · product angle ≠ others · typeface named · palette named · name treatment ·
headline placement · hero ≥ 35% width, real, label wraps · CTA string in TEXT · "NO logo" or "empty box" · forbidden elements named
