# Category 2 — Authority & Proof

Library folders: Clinical-Research · Trustpilot Reviews · Open Letter · Article · Advertorial · Cause & Effect (boards 1, 2, 4, 6).
What the library shows: a white-coat doctor beside a tired patient (in an office or hospital bed) with the product in front; a capsule held in fingers with a review card floating; an "Everlife Community" letter on a dark or photo background; article / social-post framing ("When your brain decides it's time to remember everything at 2 AM", a Restora example); a problem column → benefit column infographic.
Why it works for Restora-Z: it's a prescription product, so authority cues (doctor, pharmacy, ratings) lower the risk for a 45–65 buyer.

**Text-heavy → statics first.** All words come from finishing layouts (`finish_image.py --layout …`), never from the image model. Video versions use Marketing Studio (real doctor-type presenter) or Seedance (scene) + `full_layout.py`.

---

## 2A — Doctor moment
- **Looks like (Clinical-Research):** a warm clinician (45–60, white coat, stethoscope) in a bright consult room listening to a tired patient (50s); the product large in the foreground.
- **Image recipe:** GPT Image 2.5: "candid photo, a friendly female physician in her 50s in a sunlit consult room, listening to a tired man in his late 50s; the Restora-Z bottle (attached reference) large and sharp on the desk in the foreground with one capsule; top 22% and bottom 25% soft and clear."
- **Video recipe:** Marketing Studio UGC, the clinician talking to camera: "Waking at three every night? Ask about a 3-in-1 prescription." (no diagnosis, no "I prescribe").
- **Finishing:** `standard` layout; header from the bible (e.g. *Fall Asleep Fast, Stay Asleep*), 3 ingredient claims, CTA *Get Started Now*.
- **Guardrails:** AI disclosure is already in the verbatim disclaimer ("not actual … medical providers"); the doctor never names a disease or promises results; no "clinically proven Restora-Z".
- **Starter concept:** "The 3 a.m. question": the doctor across the desk from a tired patient; headline *3-in-1 Sleep Support. No Narcotics.* (Any Ambien headline is gated: see 5A.)

## 2B — Review spotlight (Trustpilot)
- **Looks like (Trustpilot Reviews):** a calm bedroom or capsule-in-fingers image with a review card (stars + quote + first name) floating, "Trustpilot rated 4.9 Excellent" bar.
- **HARD RULE:** review text must be a **real, verbatim Trustpilot review**: pick from `references/reviews.md` (✅ list; screened 2026-10-27) or one the team pastes. Never write, paraphrase or invent a review; excerpts only by cutting whole sentences with "…". Never pair a reviewer's name with an AI-generated face: use product, hands, or faceless scenes.
- **Image recipe:** NO identifiable face. A sunlit nightstand with the bottle and one capsule, rumpled linen, a coffee mug; or the capsule held in fingers against a soft morning window (library example). The middle band is kept calm for the card.
- **Video version:** any Category 1 or 3 video + the **review burst** insert (`full_layout.py --reviews R1,R3,R4,R2 --reviews-at <s>`). This is the team's favourite proof moment.
- **Finishing (static):** `--layout quote` with `quote`, `quote_name` in copy.json (stars are drawn by the layout; the rating line is always "Trustpilot rated 4.9 Excellent").
- **Guardrails:** the quote can't contain disease claims or first-person results that break the bible (if the real review says "cured my insomnia" → not usable).

## 2C — Open letter
- **Looks like (Open Letter):** "Dear Everlife Community," then a short letter in a serif on parchment or dark gold, signed "The Everlife Team", a Trustpilot badge on top.
- **Copy:** 4–6 short lines **assembled only from bible lines** (positioning sentence, pain points, cleared Ambien-free alternates, proof). No first-person results; "we" = the company is fine ("We built Restora-Z for…" uses the positioning line).
- **Finishing:** `--layout letter` with `letter` (list of lines), `signoff`. Background: GPT Image 2.5 soft texture or a calm night window (no text).
- **Starter concept:** "Dear 3 a.m. club": opens "Dear Everlife Community," with the lines: pain points "Restless tossing and turning", "Frequent nighttime wake-ups" → positioning → "Doctor prescribed. Ships free from the pharmacy."

## 2D — Article / social post
- **Looks like (Article, Advertorial, Polaroid):** an editorial article frame (kicker, serif headline, a photo, a byline line) or an Instagram-post frame held in a hand. The library's Restora example: "When your brain decides it's time to remember everything at 2 AM 😩".
- **Allowed:** article style. **Banned:** "BREAKING", "Breaking News", fake publisher logos, fake dates or authors.
- **Finishing:** `--layout article` with `kicker` (e.g. "SLEEP · WELLNESS"), `head`, `dek` (one bible line). Photo: GPT Image 2.5 (the 2 a.m. phone glow in bed, a partner asleep, the bottle on the nightstand).
- **Starter concept:** kicker "SLEEP NOTES", headline "Mind Won't Shut Off at 2 A.M.?" (pronoun-free), dek "Hydroxyzine reduces anxiety before sleep. Trazodone aids in falling asleep. Doxepin reduces early awakenings."

## 2E — Problem → benefit map (Cause & Effect)
- **Looks like:** left column of pain icons ("Restless tossing and turning", "Frequent nighttime wake-ups", "Drained, even after sleep") → right column of benefits with the product.
- **Copy:** pain points ONLY from the bible's "Approved pain points"; benefits ONLY from the quick-hit benefits / more approved benefits.
- **Finishing:** `--layout split` (left = pain points, right = benefits) over a calm image.
- **Guardrails:** no disease words ("insomnia" appears as an approved pain point, "Chronic insomnia", but never pair it with "cure / treat / solves").
