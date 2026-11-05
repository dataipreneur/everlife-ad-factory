# Category 2 — Authority & Proof

Library folders: Clinical-Research · Trustpilot Reviews · Open Letter · Article · Advertorial (boards 1, 2, 4, 6).
Why it works: pharmacy and clinician framing is a deliberate trust cue for 45+; men's performance is a category full of gas-station hype, so calm proof stands out.

## 2A — Clinician moment
- **Looks like:** a calm clinician 40–60 in a bright consult room, shoulder-up, the product on the desk. Explains the bible's plain line ("Promotes Circulation + Firmness", the formula named together; never one ingredient's action) and "Doctor prescribed, shipped free from the pharmacy".
- **Guardrails:** an AI clinician → the verbatim disclaimer covers it (AI depiction); no "clinically proven", no "treatment", no "ED".
- **Finishing:** `editorial` (video) or `finish_image.py --layout letter/article` (static).

## 2B — Review spotlight — ❌ GATED
- Needs screened, verbatim Titan-Rx Trustpilot reviews in `reviews.json` (none on file). Never invent, paraphrase or borrow another product's review.

## 2C — Open letter
- **Looks like:** "Dear Everlife community," letter card beside the product; every sentence assembled from bible lines; signed "The Everlife team" (no fake names).
- Static: `finish_image.py --layout letter`.

## 2D — Article
- **Looks like:** an editorial page, kicker "MEN'S PERFORMANCE", bible reference headlines ("When It’s Go Time, Be Ready"), a candid photo of a rugged man 40–65 (shoulder-up, clothed) or the product, plus proof. No fake byline, no fake site menu.
- Static: `finish_image.py --layout article`.

## 2E — Formula map
- **Looks like:** a clean diagram: "3-in-1 Performance Formula" with the three ingredients named together in one line, and three ✅ benefit pillars (daily · circulation · readiness) that are NOT tied to individual ingredients; capsule hero.
- **Guardrails:** no arrows from one ingredient to one benefit (ingredient claims are ⚠/❌ today); no anatomy; no claims beyond the page.
