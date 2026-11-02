# Category 1 — Real People Talking

Library folders: UGC · Talking Head Avatar · AI Avatar · Conversational · Podcast · Voice Over (boards 1, 2, 4, 6).
Why it works: the highest trust for a woman 30–55; a real face naming the product calmly. The talk stays about the product and the
routine, never about her results, her age or her skin's "problems".

**Engine: Marketing Studio UGC** (`--mode ugc --product_ids @<skill>/assets/product_ids.json --duration 15 --resolution 720p --aspect_ratio 9:16 --generate-audio true`), 75 credits; needs GHK-Cu Cream registered (still to do). Never Seedance or still-image lip-sync for these.

Universal prompt lines: "ultra-realistic creator UGC, real handheld phone shake, real skin texture, real room audio, no beauty filter;
the filming phone is NEVER visible; label readable and never mirrored; head-and-shoulders framing; lean and naturally fit, never
muscular; pinks, tans, beige, no orange or green; an ordinary, non-famous face; nobody says 'I' or 'my'; keep the bottom 25% free of
faces." The product-name line goes over a hands-only shot and is re-voiced in the actor's cloned voice (model voices mangle names).

---

## 1A — Creator to camera
- **Looks like:** one woman 35–50 at a sunlit bathroom counter at 7 a.m., talking to her phone propped by the mirror, the bottle beside her.
- **Beats:** 0–2.5 a pattern-interrupt action with the first words (the pump click) → 2.5–5 a ✅ territory line ("Peptide-powered
  skin support.") → 5–8.5 product up (hands-only shot) + ONE ✅ line ("Supports collagen and elastin.") → 8.5–10.5 "Doctor prescribed.
  Ships free from the pharmacy."
- **Finishing:** `tiktok`. **Guardrails:** describe the product and the routine, never her results; no close-up of her skin "before".

## 1B — Friend-to-friend
- **Looks like:** two friends 35–55 after a morning walk or at a café; A asks what the slim gold bottle is; B: "GHK Peptide Cream.
  A daily peptide step. Doctor prescribed."
- **Guardrails:** Rx never shared; the off-camera voice never testifies; no comparing each other's skin.
- **Finishing:** `default` (house look).

## 1C — AI avatar (Jeremy, 30 Oct 2026: ≥ 2 per video batch)
- `core/references/ai-avatar-video.md`: a woman 30–55 presenter, shoulder-up, fresh and natural; B-roll from the real bottle render.
  Same copy rules; needs Marketing Studio registration first.

## 1D — Voice-over lifestyle
- **Looks like:** a calm narrator (TTS) over 3–4 candid morning shots of one woman (tea at the window, the school run, after a
  run in everyday activewear, setting the bottle on the vanity), benefit chips added in finishing.
- **Finishing:** `editorial`.
