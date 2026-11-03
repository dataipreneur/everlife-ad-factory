# 7 · ⚔️ Animated Warriors (video, Wolverine Stack)

> Mitansh, 2026-11-03: "This was an absolute banger video!" Rated 5, hook-ledger `winner`. Built from the team's Sermorelin GHK
> Base116 ad (3D ingredient figures smash through a wall of problem words, then work inside "body worlds").
> First ad: V3 "Breakthrough", `~/Everlife-Creative/output/Wolverine-Stack/2026-11-03_remake-base116/`.
> Examples in `animated-warriors/`: `example_start_frame.png`, `example_raw_sheet.jpg` (1 frame/s of the raw),
> `example_final_sheet.jpg` (finished), `example_premium.json` (finishing config).

## What it is
A 15 s, 9:16, **one-shot** (single generation) stylized 3D ad. Two macho vinyl-toy / Pixar-quality action figures in **matte black +
gold** (the vial label's colours) smash through a wall stamped with problem words. Then, in fast cuts, they stand guard beside
the real vial and "do the work" inside glowing body worlds, one per ✅ benefit. An announcer voiceover sells the whole way through,
and the video ends on the vial + CTA.

**Why it works:** the hook is spectacle, the pitch starts at second 2, every beat is a benefit, and it's fun rather than clinical.
There are no humans on screen, so an off-screen announcer is allowed (the on-camera-speech rule covers people only;
Jeremy to confirm for mascots).

## Rules for this style (on top of the skill's rules)
- **The two figures are a team.** They do every job TOGETHER, and neither one ever stands for one ingredient: the bible forbids
  tying a benefit to one ingredient. Don't label them BPC-157 / TB-500.
- No claws, no animal features, no blood, no weapons, nobody hurt (Wolverine Hard NOs). Comedic macho swagger.
- The vial = the real render (`assets/wolverine_bottle.png`) as a reference, a still hero object on a plinth. Never thrown, opened or
  near a needle. No pills or capsules.
- Wall words = the pain point in plain, claim-free words (e.g. "HEAVY DAYS. / HEAVY WEAR. / SLOW BOUNCE-BACK."). Never injury, pain or
  body words. Change the words every ad (copy log).
- Body worlds = one ✅ benefit each: gold cable fibres → "Supports Tendons + Ligaments"; soft pink-peach folds → "Supports Gut Lining
  Health"; a big gold joint hinge → "Supports Mobility" / "Promotes Mobility + Flexibility"; glowing muscle-fibre bundles → "Supports
  Muscle Recovery". Pick 3 per ad and vary the world's look.
- This is the user-approved exception to the Hook Engine's "no surreal 3D" line (§1.7), for this style only.

## Vary every new ad (never a copy of V3)
Change at least 3 of these: the figures' look (helmets, beards, gym gear, fighter wraps; always black + gold) · the hook mechanic
(wall smash → e.g. the duo bursts out of a gym locker, drops through the ceiling on chains, smashes a "problem" barbell plate)
· the wall/problem words · the body worlds and their order · the plinth/setting of the vial hero · the VO lines · the finish style.

## Recipe (Creatify only, 0 Higgsfield; ≈ 35 Creatify credits)
1. **Start still** (≈ 1 cr): `gpt-image-2.5-sunburst/edit` on the Creatify Model Playground, `image_urls` = [vial render CDN URL],
   `image_size` "portrait_16_9", quality "high". Prompt: the exact hook instant (wall exploding, the duo mid-leap toward camera), the
   wall words spelled exactly, both figures described in detail (they define the look for the whole video), "the vial is NOT in this
   frame", composition (words 10–45% height, duo 25–63%, bottom 37% floor only). **Show it to the user.**
2. **Video** (≈ 34 cr for 15 s 720p): `bytedance/seedance-2.5/reference-to-video`, `image_urls` = [start still, vial render],
   duration "15", aspect "9:16", resolution "720p", generate_audio true. Prompt blocks, in order:
   - Format line ("stylized 3D animated ad, premium vinyl-toy / Pixar-quality action figures, fast punchy cuts, saturated, hard light").
   - HOOK 0.0–2.5 s: "The video OPENS EXACTLY on @image1, already mid-explosion…" + the sound at 0.0 s.
   - CAST: only the two figures from @image1, identical in every shot, plus the guards (no claws, blood or weapons).
   - PRODUCT: "@image2 is the Wolverine Stack vial. Reproduce it EXACTLY… still standing object… no syringe, needle, pills".
   - SHOTS with timestamps: 2.5–5 vial hero on a plinth + duo landing · 5–8 world 1 · 8–10.5 world 2 · 10.5–12.5 world 3 ·
     12.5–15 back to the vial hero, slow push-in, label large and readable for the last 2 s.
   - VOICEOVER: "one deep, gravelly, hyped male announcer, off screen, the characters do not speak; say exactly these words
     and nothing else, all speech ends by 14 seconds", the lines in quotes with spelled-out pronunciation ("Wolverine Stack by
     Everlife", "B-P-C one-fifty-seven plus T-B five hundred", "thirty-nine percent"). ~40 words max.
   - AUDIO: the 0.0 s impact + heavy trap-metal war-drum music under the voice + whooshes on cuts.
   - COMPOSITION (central column, 8–63% height, bottom 37% background) + "no new on-screen text except the wall words and the label".
3. **QA** (free): contact sheet at 1 fps, a label crop of the last 2 s, a word-timed transcript. Then **show the raw right away**
   (open it + paste the sheet).
4. **Finish** (0 cr): `premium_finish.py --style champagne` (it suits the black + gold; rotate styles across ads),
   `premium.json` like `animated-warriors/example_premium.json` ("end" ≈ 12.6, hand-written caps, `"proof"` from `proof_next.py`).
   - A long CTA in all caps overflows the pill: write it in sentence case ("Build Your Recovery Protocol").
   - The header covers the wall words: for the first ~2.2 s overlay the graded raw's top 600 px back over the final
     (ffmpeg `overlay … enable='lt(t,2.2)'`), so the name appears at ~2.2 s, right as the VO says it (still inside the gates' 3 s).

## VO pattern (write fresh lines every time; claims only ✅)
Pain (2–4 words, matching the wall) → "Meet Wolverine Stack by Everlife." → "BPC-157 plus TB-500, in one stack." → three
"Supports …" lines matching the worlds → "Doctor prescribed." → "Save up to 39%." → the ✅ CTA.

## Known quirks
- In the final second the label text can swell or float; the end card covers it.
- The last VO word can get clipped or mumbled near 14.5 s: keep the VO ≤ 40 words and end it by 14 s.
- Seedance on Creatify is this style's engine. Mitansh asked for it for this video even though he had turned it down for a realistic
  concept earlier that day, so for realistic videos ask first.
