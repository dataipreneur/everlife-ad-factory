# Animated still: an approved static + 8 s of motion (Epithalon; recipe from BPC-157 via MOTS-c, Mitansh 2026-10-29)

> **Team logs, as you go (`core/team-logs/TEAM-LOGS.md` §2.3):** each paid animation job (Seedance image-to-video or any other) gets its `gen` record in the Prompt & Outcome Log the moment it is submitted (inputs, exact prompt, refs, model, credits), updated after QA; a 0-credit `animate_code.py` render is logged too (model "animate_code", credits 0). Copy, proof and spend after finishing (`finishing.md`). Unreachable → the pending file, never block.

The fourth thing the skill makes. Reference: `vial-refs/pins/V43.mp4` (Sculptra, 14 s): a premium vial on a deep single-colour
field, the camera creeping in, headline words drifting around the vial, nothing else moving. Ours is simpler and shorter: the
approved static, 8 seconds, one slow move, the brand layers crisp on top.

## Flow
1. **Start from an approved static** (creative review said yes). Take its RAW (`<batch>/gen/<n>.png`, the GPT/Nano Banana output
   before finishing: it carries the headline and product, not the logo or footer). Never animate the finished PNG: the footer and
   logo would warp; `animate_still.py` lays them on every frame afterwards.
2. **Write the motion prompt** (one line each; this is the whole prompt):
   ```
   Animate this exact image for 8 seconds. Vertical 9:16. The camera pushes in very slowly (about 5%) toward the vial. The vial,
   the label and every word of text stay perfectly still, sharp and unchanged. Only the environment moves: <one of: a slow sweep of
   late-morning sun across the linen · steam rising from a tea cup · leaf shadows moving on the wall · a garden's dappled light
   shifting · the plaster wall's light cooling as a cloud passes>. No new objects, no hands, no syringe, no needle, no droplets, no text changes (the label stays EPITALON),
   no captions, no logo. Natural, premium, calm. No audio.
   ```
   Pick a different environment move per ad in a batch. Never "the vial opens / fills / is drawn from"; never night light, moonlight or a dimming room (no sleep cues).
3. **Generate** (Seedance, image-to-video, 8 s, 9:16, 720p, audio off). Two routes, same prompt:
   - **Unlimited mode in Chrome, 0 credits** (the standing memory: ask the A/B question first; in the web UI set Duration to 8, not 15,
     and use the raw as the single reference image). Preferred.
   - **CLI, costs credits** (quote first): Seedance 2.5 `higgsfield generate create seedance_2_5 --mode omni_reference --start-image
     <raw.png> --prompt "$(cat prompt.txt)" --duration 8 --aspect_ratio 9:16 --resolution 720p --generate-audio false --wait --json`
     ≈ 56 credits; Seedance 2.0 (`seedance_2_0 --start-image … --mode std`) ≈ 36. Always `higgsfield generate cost …` first.
   Download `result_url` to `<job>/out/raw.mp4`.
4. **Finish:** `$T/venv/bin/python -I $T/animate_still.py <job>/out/raw.mp4 <job>/FINAL_<n>_anim8s_9x16.mp4 --product epithalon`
   (logo at the top + proof footer at y 1179–1385 on every frame, same safe-area rules and refusal as the static).
5. **QA** (contact sheet `fps=2,tile=8x2` + the first/last frame at full size): the label is unchanged letter by letter; the headline
   did not warp or drift; the vial did not deform, open or gain a syringe; the move is slow and smooth; nothing new entered the
   frame. One re-roll max; a still that keeps warping stays a static.
6. Save `FINAL_<n>_anim8s_9x16.mp4` beside the static, log it in SESSION.md with the source static's code and the model used.

## Why 8 s and why Seedance
Meta treats a short loop like a static with motion: the first second must already read (the static does), and 8 s is long enough
for one push-in and short enough to loop. Seedance's image-to-video keeps a supplied first frame; H3 via the Ad Agent is the fallback
(`composer_generate_clip(mode="i2v", image=<raw>, duration=8)`) when Seedance is unavailable.

## Code route (2026-10-29, Mitansh): 0 credits, no AI
`$T/venv/bin/python -I $T/animate_code.py <raw.png> <job>/out/raw.mp4 --tone warm|cool --text-region y0,y1 [--clock X,Y,R --clock-color R,G,B] [--twinkle y0,y1,x0,x1] [--anchor top]`
then `animate_still.py` as above. Effects: push-in, light sweep, headline glint, ticking clock, speck twinkle; the vial and text are never warped. Epithalon: no clock effect (it reads as "turn back the clock" next to aging copy).
Use `--anchor top` when the headline sits close under the logo. Recipe per ad in `output/BPC-157/2026-10-29_anim-premium/recipe.md`. Ask Mitansh before adding any new "stupid thing" (his words) to the effect list.
