# 🧑‍💼 AI Avatar Video (every product skill, from 2026-10-30)

> **⛔ ALL-CREATIFY RULE (Mitansh, 2026-11-02, every skill, every avatar video): "AI Avatar videos always go to Creatify for
> everything!!! No Higgsfield needed at all!"** Presenter still, presenter video, background, music: ALL on Creatify. **0 Higgsfield
> credits, never `higgsfield …`, no Marketing Studio product registration needed.** This wins over every older line below or in a
> skill that mentions Higgsfield / Marketing Studio / 52.5 / 35 credits for this format. Proven: Wolverine
> `output/Wolverine-Stack/2026-11-02_two-peptides-one-mission` (10 s: 17.45 Creatify, 0 Higgsfield).

A talking presenter holding a TINY wireless mic (see MIC below) stays in the lower-left of the frame as an anchor, while full-bleed B-roll behind
them changes every 1–2.5 s as a literal metaphor for each line. The house overlays sit on top. The format comes from Spark Base14
(`~/Everlife-Creative/output/Restora-Z/2026-10-30_nightshift-presenter/source/reference_spark_base14.mp4`). Mitansh, 2026-10-30:
"the hook was awesome"; this became an option in every skill. Proven jobs: `Restora-Z/2026-10-30_3am-meeting` and
`Restora-Z/2026-10-30_sheep-quit`.

## ⚡ DEFAULT ROUTE (2026-11-02): Creatify Seedance human + Creatify Boreal-H3 animated background + Creatify music
"Boreal h3 1088p should be making a 10-12 second video, of the graphics animation we want… then higgs would add that human
model on top… cheaper from creatify to make animations for it in the background. Which should involve crazy stuff + our
product images." This REPLACES the still push-in B-roll (Step 3.2) and wins over anything below that says otherwise:
1. **Human (Creatify Model Playground, Seedance 2.5 image-to-video):** a super-realistic presenter on green speaking the script (Step 4; tiny mic).
2. **Background (Creatify Boreal-H3, 1088P):** ONE 10–12 s animated clip (or two 5–6 s clips) of bold, wild graphics animation:
   sci-fi / molecular / energy / product-in-motion, built WITH the real product renders. `composer_generate_clip`
   `mode: "r2v"` with `images: [bottle render, tablet render]` (≤ 9 refs), `resolution: "1088P"`, `aspect_ratio: "9:16"`,
   `duration: 10–12`. Cost ≈ **1.5 Creatify per 5 s** (12 s ≈ 3.6). Objects only, no people. Prompt the motion as a
   timeline that follows the script beats ("0–3 s: … ; 3–6 s: …"), keep the key action in the upper-centre/right with the
   lower-left 45% darker (the presenter goes there), exactly one tablet when a loose tablet appears, label never mirrored or
   altered, no text/numbers/logos except the real label. 768P (≈ ⅓ the price) only for a cheap test.
3. QA the clip (contact sheet: product exact? label legible? junk text? one tablet?) BEFORE the Seedance presenter (the biggest Creatify spend).
4. `$AV bgvideo <job> gen/bg1.mp4 [gen/bg2.mp4]` → `broll_track.mp4` (scaled/cropped to 1080×1920, last frame held to the
   presenter's length so it runs under the end card), then Step 5 (key, composite, full_layout) as usual.
**Cost (all Creatify, 0 Higgsfield):** presenter still ~1 · background ~3 (10 s) / ~3.6 (12 s) · Seedance presenter ~1.03 per second (10 s = 10.25, 15 s ≈ 15.4) · music 0.8 per take (men: 2 takes) → **10 s ≈ 16–18, 15 s ≈ 21–23 Creatify.**
5. **Music (Creatify `composer_generate_music`, Lyria 3 Pro, 0.8 each):** heavy track with a hit at 0.0 s (it is the hook's real sound), ducked under the VO with ffmpeg `sidechaincompress`; check the VO with an unprimed transcript. Men: strong, manly (picked 11-02: hip-hop / hard-rock walk-out; trap-metal also liked). Offer 2 contrasting takes.
No comedic metaphor hook for Sermorelin GHK (and avoid by default: Mitansh, 2026-10-30).

Never 720p and never Seedance B-roll for this format (the 146-credit plan the user rejected: "too too expensive"). Seedance is only for the presenter, at 480p.

The product skill's own rules win on any conflict (casting, colours, banned settings, claims). Global gates and
`creative-system.md` §0 always apply: the VO says **"<Product> by Everlife"** by about 3 s.

## Tools
`T=~/Everlife-Creative/tools`, `PY=$T/venv/bin/python`, `AV="$PY $T/avatar_video.py"` (source: `core/tools/avatar_video.py`).
Images come from the Creatify connector (`composer_edit_image`, GPT Image 2.5, 1 credit each) in the skill's project
(`assets/creatify.json`), with at most 4 in flight. Download with `curl` from `footage_urls`.

## Step 1 · One setup question (AskUserQuestion, a ✨ Recommended option first in every question)
- **Presenter:** "✨ New presenter for this product (Recommended)" / "Reuse <last presenter still>" / "Two presenters (2 ads)". Casting
  follows the skill (age 45+ by default, warm, casual-premium clothes, holding a TINY wireless mic (MIC below); never a doctor and
  never a white coat; Sermorelin men = fit silver fox, fully clothed; PT-141 = shoulder-up). No green or teal clothing (keying).
- **Length:** "15 s (Recommended): ≈ 22 Creatify, 0 Higgsfield" / "10 s: ≈ 17 Creatify, 0 Higgsfield".
- **Angle / hook:** "✨ Auto (Recommended)" + 2 approved pain points or benefits. Run the Hook Engine "Pick the opening hook" step.

## Step 2 · Script (one per ad; approve with the cost in the option)
- About 35 words for 15 s (the presenter finishes by ~13 s), 25–28 words for 10 s. Each line gets ONE B-roll metaphor.
- A comedic metaphor hook that runs through the whole ad as a throughline (winners: "Your brain just booked a meeting. For
  3 a.m." / "Counting sheep? Bad news. The sheep quit."). The hook pays off in the product beat. No benefit lists after a strong hook.
- **"<Product> by Everlife" spoken by about 3 s** and the product named (not just "this"), with the pronunciation written in the prompt.
- Claims come only from the bible (quick-hit benefits); new wording is Tier B and gets flagged for Jeremy. No I/me/my, no "Are you…?".
- The table shown to the user has Time · Spoken line · B-roll. Then: claims → bible source, Tier B lines, cost. **"Approve & generate (≈N cr)"**.

## Step 3 · Stills (Creatify, ~1 cr each)
1. **Presenter still** `gen/p01_presenter_green.png` (9:16): waist-up, centred, head at ~12–35% of the height, tiny wireless mic (MIC below) at
   the chin, on a "perfectly flat, evenly lit, uniform chroma-key green backdrop (no texture, shadows, gradient or spill)". Attach
   the bottle only as "a COLOUR reference only; do NOT show any product".
2. **B-roll stills** (7–8): photoreal and cinematic, never cartoonish. Each one in the prompt: "key subject in the upper-centre/right
   between 12–20% and 55–65% of the height; the lower-left 45% dark and out of focus (the presenter goes there); the bottom 30%
   calm; no text, numbers, logos". Product shots attach the real renders with the skill's exact PRODUCT line (exactly one
   pill/tablet/capsule, label never mirrored). Analog clocks with NO numerals. Before/after pairs: make the second one as an edit of
   the first ("Keep EVERYTHING identical… change only X") so the crossfade lines up.
3. Contact sheet (`$AV sheet`) → QA every still (product, label, faces, no text) before spending on the presenter.

## Step 4 · Presenter video (Creatify Seedance 2.5, the approved cost; NEVER Higgsfield)
`model_playground_generate(model_name="bytedance/seedance-2.5/image-to-video", input_params={"image_url": <the presenter
still's Creatify cdn url from footage_urls>, "duration": "10"|"15", "resolution": "480p", "generate_audio": true, "prompt": …})`.
The result card self-updates: do NOT loop `model_playground_get`; wait with a background `sleep 240`, then check once and curl
`outputs[0].url` → `out/presenter_raw.mp4`. The prompt: "One continuous locked-off shot; the camera never moves, no zoom, no cuts.
The same <man|woman> from the start image… stands waist-up in the centre against the same perfectly flat chroma-key green backdrop
for the whole video… holds the same tiny furry wireless mic… No props, no product, no text." + "He/She starts speaking at the
very first frame… says exactly these words and nothing else, in English: "<script>"" + the phonetic pronunciation + a performance
note per line + "finishes speaking by about <8.5 | 13> seconds, then holds a relaxed, confident look" + "Audio: only the voice, no
music, no sound effects. Nobody says I or my. No white coat." 480p is fine because the presenter only fills a corner.
(Wolverine 2026-11-02: every word exact, locked shot, mic kept, 10.25 Creatify.)

While it renders: write `plan.json`, build the B-roll (`$AV broll <job> plan.json`) and the free animatic
(`$AV animatic <job> gen/p01_presenter_green.png`). For a new format or cast, show the animatic before step 4.

**Team logs (every video made with this recipe, `core/team-logs/TEAM-LOGS.md`):** before writing the script, read this product's Copy Ledger rows (never reuse a logged hook, line or CTA). Log every paid generation (still, clip, music) to the Prompt & Outcome Log (inputs, exact prompt, refs, model, credits, QA result), the final video's spoken lines, captions, CTA and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log. Unreachable → the pending file, never block.

## Step 5 · Assemble (0 cr)
1. Download `result_url` → `out/presenter_raw.mp4`. Transcribe with word timestamps (faster-whisper in `$T/venv`). QA: same
   person, every line said as written, **product name + "by Everlife" heard**, ends by ~13.5 s.
2. Retime `plan.json` to the real word times (each cut on the line it illustrates; the last shot runs under the end card) → `$AV broll`.
3. If a product shot sits under the presenter, the headline or the captions → `$AV shift <in> <out> --scale 0.84 --dx … --dy …`
   (feathered, 0 cr). Never a paid reposition.
4. `$AV key <job> --width 500` (default fade 0.90 1.0: the presenter is SOLID, never see-through; Mitansh 2026-10-30) (a man in a wider shot: `--width 600 --fade 0.42 0.68`).
   `$AV composite <job> --x -50 --y 620` (man: `--x -60 --y 590`). These numbers keep the face at y ≈ 700–880: above the caption
   / proof band and clear of the Reels profile notch. The body fades into the background from the chest down, so the proof and
   disclaimer sit on dark.
5. `copy.json` (fresh, from the bible; `"product"` and the `benefits` list are required; omit `style`; `sub` carries "<PRODUCT> by
   Everlife" or "<PRODUCT> · …" so the name shows from frame 0). Run
   `cd $T && $PY -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end <time of the CTA line>`.
6. Captions: write `phrases.json` (clean phrases, drug names spelled right) → `$AV caps <job> <Tag> phrases.json` → re-run
   full_layout. **full_layout regenerates the captions whenever raw.mp4 changes: re-run `caps` after every recomposite.**
7. QA frames (hook, every shot, end card): nothing on faces, nothing touching the product, proof readable, safe zone. Hook Engine
   §7 QA. Save `FINAL_<Tag>_15s_9x16.mp4`, `open` it, and log it (copy log, hook ledger, SESSION.md).

## Known traps (paid for on 2026-10-30)
- ffmpeg `chromakey` made cream and teal clothes see-through → use `avatar_video.py key` (green-dominance matte).
- A still with no `-loop` gives a 1-frame overlay (the animatic tool handles it).
- The first placement put full_layout's captions and proof across the presenter's face → keep the face y ≈ 700–880 (step 5.4).
- The header covered the bottle cap when the product shot sat high → `shift` it down (`--dy 330`).
- The default 10 s / 12 s version felt short ("why not 15 seconds!?") → 15 s is the default.

## Mitansh, 2026-10-30 (every product): MIC + B-ROLL rules
- **MIC:** never a big handheld/interview mic ("They are holding a very big mic! No NO"). The presenter holds a TINY wireless
  creator mic like the DJI Mic Mini: a small matte-black square transmitter (about the size of a thumb tip) with a fluffy black
  furry windscreen on top, unbranded, no logo, held between thumb and fingers just below the chin. Write that into the presenter
  still prompt AND the presenter video prompt ("the same tiny furry wireless mic… never a large handheld microphone").
- **B-ROLL: objects only.** "The background shouldn't have other stuff like humans etc, only objects and stuff." No people,
  faces, bodies or second actors in B-roll stills: products, equipment, anatomy/molecule visuals, environments. The presenter
  is the only human in the ad. (Product skills that require a hand holding the tablet: ask the user, see the skill's notes.)
- **Product-name pronunciation (2026-10-30):** put the PHONETIC name inside the spoken quote, add the skill's pronunciation block
  (Sermorelin GHK: `skills/everlife-sermorelin-ghk/references/pronunciation.md`), say the name once, QA with an UNPRIMED
  transcript, and fix a miss with the 0.3-credit Seed Audio re-voice of that one line (recipe in that file).
