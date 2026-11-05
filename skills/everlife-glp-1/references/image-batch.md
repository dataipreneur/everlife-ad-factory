# GLP-1 IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product glp-1`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to GLP-1.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only ✅ pre-screen lines; ⚠ lines (every weight-loss outcome line) only with the user's explicit OK + flagged for Jeremy.
- **Every ad carries the price line:** "One Price, No Surprise Increases" / "One predictable price" (as a line, a pill or the offer badge).
- **"GLP-1" in headers; "compounded semaglutide" / "compounded tirzepatide" whenever a drug is named.**
- No before/after, body comparison, body areas, scales, tape, waistlines; no melt / burn / shred; no timing promises; no
  guarantees; no disease words. "Supports / helps".
- **No needles, syringes, pens, injecting or "needle-free"** in words or pictures. One vial or both side by side (the winners), a still object.
- No "Are you/Do you…?" questions, no first person, no named competitors or drug brands, no "clinically" for the product.
- Offer: "Up to 59% off" (percent, never $) and/or "One predictable price".
- "GLP-1" big in every ad; never "by Everlife" on images. Proof exact; disclaimer verbatim (the footer handles both).

**Headline tiers:** Tier A = a ✅ bible headline or benefit · ⚠ lines: explicit OK per line · Tier B (max 2): PROPOSED, Jeremy.

## 1. Product facts for the prompt
- **Product:** GLP-1 (`glp-1`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `glp1_semaglutide_vial.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Forms (one per ad; the image question asks which):** **semaglutide** = compounded semaglutide (bottle `glp1_semaglutide_vial.png`); **tirzepatide** = compounded tirzepatide (bottle `glp1_tirzepatide_vial.png`)
- **Hero:** the GLP-1 vial of the ad's form, or both vials side by side (a still object, labels to camera); min width 0.35 of canvas; never: needles, syringes, pens or injecting; scales, tape measures, waistlines, bellies, before/after or any body-composition cue; food 'cheat' imagery; another product's vial.
- **Cast & mood:** active adults 30–65, bright real rooms; no body-composition or targeted fat-loss claims, no before/after.
- **World translation family for the dealer:** `metabolic` (each world card's `translate.metabolic` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/winners/winners.md` | reference level 1: our own winners, open first |
| `references/personas.md` | the critique pass per ad |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |
| `assets/RENDERS.md` | what each render is |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product glp-1 --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/GLP-1/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/glp-1-copy-log.md`;
`deal_worlds.py --product glp-1 --n <N> --log` once approved.
