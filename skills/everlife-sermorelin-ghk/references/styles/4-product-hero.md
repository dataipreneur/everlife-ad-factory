# Category 4 — Product as Hero

Library folders: Product Highlight · Pill-Product Focused · Minimalist · Product-as-Hero · Polaroid · Billboard (boards 1, 3, 4, 5).
Why it works: this style fills the 50% pill-focused share of the bible's focal-point mix (2026-11-03; it replaced "the pill/tablet is the hero"); real renders make fidelity easy.

**Statics:** GPT Image 2.5 via Creatify with bottle + tablet + type specimen attached (~1 cr). **Video:** Seedance 2.0 or Boreal-style for a single locked shot. Tablet prompt line, always: "use the attached tablet reference exactly; do not invent, alter, or substitute a different pill."

---

## 4A — Premium still life
- **Men:** the tablet large in the foreground on warm stone or a chalked barbell collar, bottle behind, sun-lit, texture and depth. **Women:** the tablet on blush linen or travertine with soft morning light.
- **Video:** slow push-in, the tablet settling in slow motion, light sweeping across.
- **Finishing:** `finish_batch.py` (F2 / F12).

## 4B — Tablet in hand
- **Looks like:** an extreme close-up of a 45+ hand (real skin) holding ONE tablet up to warm window light; a gym or kitchen softly out of focus.
- **Guardrails:** exactly one tablet; no swallowing several.

## 4C — Minimal bold
- **Looks like:** dark textured background, single key light on the tablet + bottle, one short headline (≤ 4 words, e.g. reference *Lean. Powerful. Unstoppable.*), a 3-benefit strip.

## 4D — Ad in a frame
- **Looks like:** a hand holding a phone or polaroid showing the ad, a gym-locker poster, a billboard at dawn. Generate the scene with a blank frame; finishing places the ad in it (`finish_image.py --layout frame`).
- **Guardrails:** no fake handles, like counts or brand names.

## 4E — Morning routine ASMR
- **Looks like:** top-down counter at sunrise: gym bag zip, water glass, the tablet placed under the tongue (sublingual), keys, out the door.
- **Guardrails:** plain props with no text; exactly ONE tablet; say "easy sublingual delivery" only.
- **Finishing:** `editorial`.
