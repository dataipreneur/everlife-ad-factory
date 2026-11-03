# 🚗 Car Throw Review: a video style for every tablet / capsule product (Mitansh, 2026-11-03)

> Mitansh, 2026-11-03, on the Sermorelin GHK 1000 car review: "This was amazing!!! Save it as a form in video 'Mood'
> questionnaire, Car Throw Review" … "and have it for all the tablets".
> First ad (the reference): `~/Everlife-Creative/output/Sermorelin-GHK/2026-11-03_car-review/FINAL_SGHK1000_CarReview_fastthrow_blacklabel_21s_9x16.mp4`.
> Examples: `skills/everlife-sermorelin-ghk/references/styles/car-throw-review/` (start frame, raw and final sheets, the
> fast-throw strip, the finishing config). SGHK's exact winning script: `skills/everlife-sermorelin-ghk/references/styles/7-car-throw-review.md`.

**Products:** every oral tablet / capsule skill: Sermorelin GHK, Sermorelin, Restora-Z, PT-141 (tablet form only), Spark,
NAD+ (tablet form only), Titan-Rx, Lovara (and any new tablet / capsule product). Not for vials, sprays, creams or injectables.
Every video Style question in those skills offers **"🚗 Car Throw Review"** (always shown, never dropped).

## What it is
A real-looking, everyday person (not a model look) in a parked car, filmed by a phone on the dashboard. A friend outside throws the
SEALED bottle in through the open passenger window, they snatch it, and then give a warm, honest, impressed "here's what's in this"
breakdown to camera, ending on an urgent spoken CTA. It's simple UGC, and it doesn't feel like an ad until the last line.

## The script shape (write fresh words every time; claims only from that product's bible)
1. **0–2 s, the problem as a question**, pronoun-free (e.g. SGHK "Training hard but still feeling flat?"). Never a specific age or
   number; never "Are you…?".
2. **The name:** "<Product> by Everlife." (phonetic spelling inside the spoken quote where the skill has one).
3. **One line of genuine reaction** ("Three ingredients, one tiny tablet. Kind of genius.").
4. **What it does, in plain connected sentences**, each claim on its own approved line or ingredient (respect each product's rules:
   e.g. Spark never ties a benefit to one ingredient; PT-141 / Titan-Rx / Lovara stay tasteful).
5. **How it's taken + trust:** "Doctor prescribed", how it's taken (sublingual / capsule), optionally "why isn't everyone on this yet?".
6. **Urgent CTA, offer first:** the bible offer exactly, with push ("Save up to 47%. Don't sit on this!"); the end-card button = the
   offer CTA. "Get Started Now" is banned (bible sync 2026-11-03); placeholder offer → "Ships Free From Pharmacy". No fake deadline or scarcity.
- **No first person / testimonial** ("I tried", "my results", "should have tried it earlier" are global Hard NOs; reviews stay gated):
  it's a breakdown, not a personal story. He or she speaks every line ON CAMERA (`core/references/on-camera-speech.md`).
- ~40–45 spoken words over **20 s at a relaxed pace** (15 s came out too fast to follow).

## Recipe (Creatify only, 0 Higgsfield; ≈ 47 Creatify)
1. **Start still** (≈ 1 cr, `gpt-image-2.5-sunburst/edit`, refs = the bottle render): dashboard-phone view of the person in the
   driver's seat; the sealed bottle **clearly mid-air near the open passenger window, cap ON**, a friend's blurred arm outside;
   the person's **hands still down**, head turning toward it. (The first attempt showed the catch already happening, and the
   video then opened with the bottle already in hand: the throw was lost.) Face 20–42% of the height, bottom 37% steering wheel.
2. **Video** (`bytedance/seedance-2.5/reference-to-video`, images = [start still, bottle render, tablet/capsule render], duration
   "20", 9:16, 720p, generate_audio true ≈ 45.5 cr). Prompt musts:
   - "OPENS EXACTLY on @image1… the bottle visibly flies across the car and at ~0.9 s they snatch it one-handed".
   - "The bottle stays CLOSED with the cap ON for the entire video; no pills come out of it" (an open bottle showed a pile of
     the render's placeholder pills = fails "exactly one pill on screen").
   - One held tablet/capsule shot only (thumb + index toward the lens), the single loose pill in the video.
   - "RELAXED, NATURAL, UNHURRIED pace with small pauses"; DIALOGUE ON CAMERA, lips in sync, exact lines, ends ~0.7 s before the end.
   - The usual composition and closing guards.
3. **Speed up the throw in post (0 cr, always):** Seedance renders the throw in slow motion. Speed the clip up to the catch
   (~1.4 s) **3×**, the laugh before the first word **3×**. **Never speed up the talking** (Mitansh 2026-11-03: "Dont increase the speed of talking… keep it as it is!"). Mitansh 2026-11-03 wanted the problem told "as soon as the 2nd second starts": the problem question then starts at ~1.0 s and the name by ~2.8 s:
   `[0:v]trim=0:1.4,setpts=(PTS-STARTPTS)/3 … [0:a]atrim=0:1.4,asetpts=PTS-STARTPTS,atempo=2,atempo=1.5 … trim=1.4:<first word>,
   setpts=/3, atempo=2,atempo=1.5 … rest unchanged → concat`. Check the first word's time with word-level whisper first; the problem
   question should then start by ~1.0 s.
4. **Hold the last frame 2.4 s** (`tpad=stop_mode=clone:stop_duration=2.4`, `apad`) so the end card has room after the last word.
5. **Finish:** `premium_finish.py` (Black Label suited it; rotate styles) with **the header for the first ~5.5 s, then logo only**
   (render a full version + a logo-only version and overlay the full one with `fade=out:st=5.5:d=0.3:alpha=1`); captions
   hand-timed from word-level whisper (shifted by the speed-up); `"end"` = last word + 0.1 s; proof from `proof_next.py`.
6. **Team logs:** before writing the script, read this product's Copy Ledger rows (never reuse a logged hook, line or CTA). Log every paid generation (still, clip, music) to the Prompt & Outcome Log **the moment its job is submitted** (inputs, exact prompt, refs, model, credits), then update that record after QA (pass/fail, reasons, re-takes), the final video's spoken lines, captions, CTA and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log. Unreachable → the pending file, never block.
7. **QA:** throw fast and readable, the bottle sealed, exactly one loose pill, the name said and captioned correctly, the label never
   mirrored. Show the raw right away; any paid re-take needs an explicit go (the free fixes above come first).

**Cost seen (SGHK, 2026-11-03):** the winning 20 s take = 1 still + 45.5 Seedance = 46.5 Creatify; post-editing 0.
