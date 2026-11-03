# ⛔ HARD RULE: the human on screen does the talking (Mitansh, 2026-11-03)

> Mitansh, 2026-11-03: "In all the videos, whichever requires a human! The voice / speech should be coming from the human, not
> as a background voiceover! The human should be speaking it!"

Applies to **every Everlife video in every product skill** (all `everlife-*` skills, incl. new ones built by `everlife-new-product`).
It **overrides** every older line that says "off-screen narrator", "voiceover", "VO over B-roll", "he never speaks / mouth stays
closed", "say the product line over the hands-only shot so it can be re-voiced", or "the voice is an off-screen narrator".

## The rule
1. **If a person is in the video, the person speaks the lines**, on camera, lips moving in sync, to camera or to someone in frame.
   No disembodied narrator, no background voiceover over a person, no "he never speaks".
2. The speaker is the **main on-screen human** (the hero, the presenter, the creator). Two people in frame → one of them speaks,
   or they talk to each other. Pronoun rules still apply (no "I / me / my", no "Are you…?").
3. **Cutaways are fine as J-cuts / L-cuts:** the same person keeps talking in their own voice while the picture cuts briefly to
   the product or a detail (≤ 2 s, like real UGC). The voice is still theirs, and the next shot returns to their face.
4. **No-human videos are the only exception:** objects-only product heroes, animated stills, motion graphics, sci-fi product
   dives with no person in frame may use a voiceover. If a person appears at any point, rule 1 applies.

## How to write it into the prompt (every route)
- Dialogue block header: `DIALOGUE (spoken ON CAMERA by <the man/woman>, lips in sync, looking into the lens; say exactly these
  lines and nothing else; all dialogue ends by <t> s)`. Never "off-screen", "narrator" or "voiceover".
- Cast line: replace "he never speaks; his mouth stays closed" with "he speaks every line himself, to camera, natural lip sync".
- Shots: every spoken line has his face (mouth visible) on screen for at least most of the line; plan product shots as short
  cutaways UNDER his continuing voice, or have him hold the product in frame WHILE he talks (best: both in one shot).
- Route choice: realistic talking human → Marketing Studio UGC or Seedance 2.5 image-to-video with a start frame of him facing
  camera (both lip-sync natively). Wan / other models only after a test shows real lip sync.
- AI Avatar Video route already complies (the presenter speaks).

## Pronunciation (the old re-voice trick no longer works on a visible mouth)
- Write hard names phonetically INSIDE the spoken quote ("Sermorellin G. H. K. by Ever-life") and add the skill's pronunciation block.
- Keep hard names ≤ 2 per video; say the product name once in the intro (still required by ~3 s).
- QA unprimed. If the name is wrong: (a) if that line falls on a cutaway (J-cut, no visible mouth), the 0.3-credit clone re-voice
  still works there; (b) otherwise offer a re-take (cost shown) — never paste a narrator over his face.

## QA (every raw with a person)
- Every spoken line comes from a visible mouth (or a ≤ 2 s cutaway inside his own line). A voice with no on-screen speaker = FAIL.
- Lip sync looks natural; no second voice; no mouth moving while silent.
