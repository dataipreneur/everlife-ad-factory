# Epithalon IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product epithalon`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Epithalon.

## 0. Copy rules (product-specific; kept from the original skill)
**✅ Disclaimer now in the bible (sync 1793728650-5a0d, 2026-11-03):** the bible's Epithalon page carries the standard ad disclaimer, word for word the text already in product.json (`bible_sync.py --check` ✅). The old "provisional disclaimer: Jeremy to confirm" flag is retired; Jeremy's usual sign-off before anything goes live still applies.

**Hard stops:**
- Claims: only the ✅ lines of the pre-screen (`product-bible.md`); ⏳ headlines H3/H4 and ⚠ "Supports DNA + Cellular Health" only
  with the user's explicit OK per line + flagged for Jeremy; H1/H2 not without Jeremy; ❌ never (both sleep benefits, the offer).
- Epithalon is LONGEVITY support: healthy aging, oxidative stress defense. **No sleep or overnight words or images** (product Hard
  NO: no beds, night, waking up, alarm clocks). **Healthy aging, never reversal:** no "anti-aging", "reverse", "younger", "turn back
  the clock"; no before/after, no younger-vs-older comparison, no mirrors. No body-composition claims, no disease words. "Supports",
  never "repairs / reverses / builds". No timing promises, no guarantees.
- **No needles, syringes, pens, injecting or "needle-free"** in words or pictures. The vial is a still object.
- One product image: the Rx vial. Never a strength, dose, mL or count in copy.
- People: adults 40–65, men and women, in calm, sun-lit daytime moments; never a physique shot (`direction.md`).
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically" for the product.
- **Offer: none.** The bible's offer is [PLACEHOLDER]: no %, no $, no offer slot (F6 skipped) until Justin fills it.
- "Epithalon" big in every ad (the bible's spelling; the vial label's "EPITALON" is never edited); never "by Everlife" on images. Proof exact; disclaimer verbatim (the footer handles both).

**Headline tiers:** Tier A = a ✅ benefit line, verbatim (no headline is approved yet) · ⏳ H3 "Support Healthy Aging at the Cellular Level" / H4 "Longevity Support, Made Simple" and ⚠ B3: explicit OK per line, Jeremy · Tier B (max 2): PROPOSED, Jeremy. **Two ✅ benefits only:** a three-row layout uses "Doctor Prescribed" (sourced trust signal) as the third row, or B3 with an OK.

## 1. Product facts for the prompt
- **Product:** Epithalon (`epithalon`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `epithalon_bottle.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the Epithalon vial (a still object, label to camera); min width 0.35 of canvas; never: needles, syringes, pens or injecting (and the words 'needle-free'); capsules, tablets or pills; beds, bedrooms, pillows, night or overnight scenes, waking up, alarm clocks, moons or any sleep cue (DSIP's territory, product Hard NO); before/after, younger-vs-older-self or any body or age comparison; age-reversal or 'turn back the clock' imagery; DNA-helix or lab-result graphics presented as a medical result; scales, tape measures or any body-composition cue; another product's vial (incl. the GHK-Cu/Epithalon stack).
- **Cast & mood:** active adults 30–65, bright real rooms; no body-composition or targeted fat-loss claims, no before/after.
- **World translation family for the dealer:** `metabolic` (each world card's `translate.metabolic` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/personas.md` | the critique pass per ad |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |
| `assets/RENDERS.md` | what each render is |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product epithalon --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Epithalon/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/epithalon-copy-log.md`;
`deal_worlds.py --product epithalon --n <N> --log` once approved.
