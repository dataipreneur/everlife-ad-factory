# Category 2 — Authority & Proof

Library folders: Clinical-Research · Trustpilot Reviews · Open Letter · Article · Advertorial (boards 1, 2, 4, 6).
Why it works: pharmacy and clinician framing is a deliberate trust cue for 45+; desire support is a category where trust matters more than hype.

## 2A — Clinician moment
- **Looks like:** a calm clinician 40–60 in a bright consult room, shoulder-up, the product on the desk. Explains ONE mechanism line (the bible's "Supports Desire + Physical Response", with the combo named together; never one ingredient's action) and "Doctor prescribed, shipped free from the pharmacy".
- **Guardrails:** an AI clinician → the verbatim disclaimer covers it (AI depiction); no "clinically proven", no "treatment for low libido".
- **Finishing:** `editorial` (video) or `finish_image.py --layout letter/article` (static).

## 2B — Review spotlight — ❌ GATED
- Needs screened, verbatim Spark Trustpilot reviews in `reviews.json` (none on file). Never invent, paraphrase or borrow another product's review.

## 2C — Open letter
- **Looks like:** "Dear Everlife community," letter card beside the product; every sentence assembled from bible lines; signed "The Everlife team" (no fake names).
- Static: `finish_image.py --layout letter`.

## 2D — Article
- **Looks like:** an editorial page, kicker "INTIMATE WELLNESS", Tier A headline ("Spontaneity, Back On"), a candid daytime photo of a woman or man 30–65 (shoulder-up), product and proof. No fake byline, no fake site menu.
- Static: `finish_image.py --layout article`.

## 2E — Mechanism map
- **Looks like:** a clean diagram of the three approved pillars (brain-based · non-hormonal · on-demand), product hero.
- **Guardrails:** no receptor names, no "melanocortin", no claims beyond the page.
