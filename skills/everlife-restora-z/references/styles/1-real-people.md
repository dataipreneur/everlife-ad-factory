# Category 1 — Real People Talking

Library folders: UGC · Talking Head Avatar · AI Avatar · Conversational · Podcast · Voice Over (boards 1, 2, 4, 6).
What the library shows: a creator or presenter framed chest-up talking straight to camera, a product held near the face, bold caption bars; two friends on a hike or beach chatting; a podcast desk with a mic; voice-over over lifestyle B-roll with stacked benefit chips.
Why it works for Restora-Z: the highest trust for the 45–65 audience; a real face saying the pain point out loud.

**Engine for every sub-style here: Marketing Studio UGC** (`marketing_studio_video --mode ugc --product_ids @<skill>/assets/product_ids.json --duration 15 --resolution 720p --aspect_ratio 9:16 --generate-audio true`), 75 credits, ~7–10 min. Never Seedance or Creatify lip-sync for these. For a static version, use GPT Image 2.5 with the same cast (a candid phone photo).

Universal prompt lines (always include): "ultra-realistic creator UGC, real handheld phone shake, real skin texture, real room audio, no studio polish, no beauty filter; the filming phone itself is NEVER visible; exactly ONE capsule; label readable and never mirrored; nobody says 'I' or 'my'; say 'Restora-Z' as 'res-TOR-uh zee'; keep the bottom 25% free of faces."

---

## 1A — Creator to camera
- **Looks like:** one person 45–65 (car, kitchen, bedroom edge, porch) talking to their phone, holding the bottle by their cheek, with genuine expressions.
- **Best angles:** morning grogginess · "drained even after a full night" · 3 a.m. wake-ups.
- **Beats (15s):** 0–2 a pattern-interrupt line or action (flashlight-under-chin whisper, a dramatic yawn mid-sentence, holding up a coffee cup like a trophy) → 2–6 the pain point in their words (pronoun-free question) → 6–10 the bottle up, ONE claim → 10–12 one capsule to the lens / a small smile.
- **Script budget:** ≤ 30 words, ≤ 1 drug name spoken.
- **Finishing:** `tiktok` look (white sticker headline, word-highlight captions).
- **Guardrails:** no "I tried / my sleep"; describe the product, not results; no bedroom intimacy.
- **Starter concept:** "Car-park confession": a woman, 55, in a parked car at 7 a.m., sunglasses on her head: "Exhausted, even after a full night in bed? Restora-Z is formulated differently… designed to help you sleep soundly and wake up with a clear head." Header: *Wake Up Energized Without Grogginess*.

## 1B — Partner / family POV
- **Looks like:** someone else holds the phone (a spouse or adult kid), catching the person in a candid moment, then a short story beat. Proven: "Who is this man?"
- **Best angles:** clear mornings · the household noticing the change (no results claims; show behaviour only).
- **Beats:** 0–2 a sneaky filming hook + an off-camera whisper → 2–6 the candid reaction (laugh, eye-roll) → 6–11 the product moment (a pharmacy delivery for THEM, or they hold their own bottle) → 11–12 a toast or smile to camera.
- **Finishing:** `tiktok` or `editorial`.
- **Guardrails:** **Rx is never shared**: the person receives THEIR OWN pharmacy package. The off-camera voice must not testify ("he sleeps great now" ✗).
- **Starter concept:** "Wildlife documentary": the wife films in a hushed nature-doc voice, "A rare sighting… the morning person in his natural habitat." He turns, laughs, holds up his bottle: "Doctor prescribed. Shipped free from the pharmacy."

## 1C — Friends chatting (conversational)
- **Looks like (library: Conversational):** two friends walking a trail, on a beach or at a café, one sharing with the other, shot like a candid vlog. Captions show the dialogue.
- **Best angles:** racing mind · "can't switch off".
- **Beats:** 0–2 friend A: "Okay, why do you look so… awake?" → 2–8 friend B answers with the pain point, then the product (bottle out of a tote bag) → 8–12 A takes a photo of the label ("send me that").
- **Finishing:** `house` look.
- **Guardrails:** nobody offers or shares pills; no first-person results ("it fixed my sleep" ✗). B describes the product, not her outcome: "Doctor prescribed, ships free from the pharmacy."
- **Starter concept:** "Sunrise walk": two women, 52 and 58, on a dawn trail; A notices B's energy; B: "Three prescription ingredients. One capsule. Ships free from the pharmacy."

## 1D — Podcast set
- **Looks like (library: Podcast):** a woman or two hosts at a warm podcast desk with Shure-style mics, the product on the desk, lower-third style captions. (Also works as the 3D capsule-characters podcast → see 3C.)
- **Best angles:** the ingredient story ("three established ingredients…"; use fresh wording from the bible each time) · mechanism.
- **Beats:** 0–2 the host leans into the mic with a hot take ("Nobody talks about the 3 a.m. wake-up") → 2–10 the co-host lists ONE ingredient + its own claim, the host the next → 10–12 product on desk, a nod.
- **Finishing:** `editorial` look.
- **Guardrails:** each ingredient claim stays on its own ingredient; no "studies show" for the product.
- **Starter concept:** "Hot take": "Hot take: counting sheep was never the plan." Co-host: "Doxepin reduces early awakenings. Trazodone aids in falling asleep." Header: *3-in-1 Formula: Trazodone + Hydroxyzine + Doxepin*.

## 1E — Voice-over lifestyle
- **Looks like (library: Voice Over):** no lip-sync; a warm narrator over 3–4 candid lifestyle shots of one person (a night struggle → a calm routine → an easy morning), with benefit chips on screen.
- **Engine note:** Marketing Studio (still realistic humans) with "a calm off-screen narrator says…" (no on-camera speech).
- **Beats:** 0–2 a striking image of the pain point (staring at the ceiling, lit by the phone) → 2–10 the routine + product → 10–12 morning.
- **Finishing:** `house` or `editorial`.
- **Starter concept:** "Ceiling count": a narrator over a man, 60, staring at the ceiling: "Restless tossing and turning? There's a 3-in-1 for that."

## Static versions (any 1x sub-style)
GPT Image 2.5 candid phone photo of the same cast holding the bottle (label readable), with top and bottom kept clear → `finish_image.py --layout standard` (or `quote` if there's a real review to feature).
