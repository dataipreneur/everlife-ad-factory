# Category 1 — Real People Talking

> **💪 HARDCORE MEN = `core/references/hardcore-men.md` (Jeremy via Mitansh, 2026-11-02; OVERRIDES every "fully clothed / no bare torso / never shirtless / no flexing / not a bodybuilder / natural build" line and every winner's "Don't copy: shirtless" note in this skill):** men's ads lean intense: shirtless or stringer, 40–45, flawless muscular condition, hard gym light. 🎲 Surprise me / random: up to 30% of men's slots are HARDCORE (bible 2026-11-04 caps shirtless male talent at 30%) (`core/scripts/pick_styles.py --product <id> --n <N> --audience men|women|both` tags them). Whenever recommending a cast, mood or style for men, recommend hardcore first ("💪 Hardcore shirtless" as a mood). Copy still never ties the body to the product: no before/after, body comparison, body-composition claims or "ripped/shred".

Library folders: UGC · Talking Head Avatar · AI Avatar · Conversational · Podcast · Voice Over (boards 1, 2, 4, 6).
Why it works: the highest trust for a 35–65 buyer; a real face naming the goal out loud.

**Engine: Marketing Studio UGC** (`--mode ugc --product_ids @<skill>/assets/product_ids.json --duration 15 --resolution 720p --aspect_ratio 9:16 --generate-audio true`), 75 credits. Never Seedance or still-image lip-sync for these.

Universal prompt lines: "ultra-realistic creator UGC, real handheld phone shake, real skin texture, real room audio, no beauty filter; the filming phone is NEVER visible; exactly ONE tablet; no vial or second container; label readable and never mirrored; clothed unless HARDCORE (then shirtless per hardcore-men.md) (men: the CAST line in `video-prompting.md`); nobody says 'I' or 'my'; keep the bottom 25% free of faces." The product-name line goes over the hands-only shot and is re-voiced in the actor's cloned voice (`finishing.md` §1b).

---

## 1A — Creator to camera
- **Looks like:** one person (men 45–65 in a garage gym or truck after training; women 40–65 in a sunlit kitchen) talking to their phone, bottle by the cheek.
- **Beats:** 0–2 a pattern-interrupt action (sets down a heavy kettlebell mid-sentence) → 2–6 the goal as a pronoun-free question ("Energy fading by mid-afternoon?") → 6–10 bottle up + ONE mechanism line ("Sermorelin supports the body's own growth hormone production") → 10–12 the tablet to the lens.
- **Finishing:** `tiktok`. **Guardrails:** describe the product, never their results.

## 1B — Training partner POV
- **Looks like:** a training partner films him/her between sets, teasing; the person holds up their OWN bottle from the gym bag.
- **Guardrails:** Rx never shared; the off-camera voice never testifies ("he's jacked now" ✗).
- **Finishing:** `tiktok` or `editorial`.

## 1C — Friends chatting
- **Looks like:** two friends 50+ on a trail or a café terrace after a walk; A asks what's on the counter these days; B describes the product: "Doctor prescribed. Easy sublingual delivery. Supports natural growth hormone activity."
- **Finishing:** `house`.

## 1D — Podcast set
- **Looks like:** two hosts at a warm podcast desk, the bottle and tablet on the desk.
- **Beats:** the host's hot take ("Nobody talks about growth hormone after 40") → mechanism line → one ✅ benefit → product on desk.
- **Finishing:** `editorial`. **Guardrails:** no "studies show" for the product.

## 1E — Voice-over lifestyle
- **Looks like:** a calm narrator over 3–4 candid shots of one person's morning (training, work, family), benefit chips added in finishing.
- **Finishing:** `house` or `editorial`.
