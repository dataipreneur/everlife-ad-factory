# QA + finishing (zero manual editing)

> **💪 HARDCORE MEN = `core/references/hardcore-men.md` (Jeremy via Mitansh, 2026-11-02; OVERRIDES every "fully clothed / no bare torso / never shirtless / no flexing / not a bodybuilder / natural build" line and every winner's "Don't copy: shirtless" note in this skill):** men's ads lean intense: shirtless or stringer, 40–45, flawless muscular condition, hard gym light. 🎲 Surprise me / random: 40% of men's slots are HARDCORE (`core/scripts/pick_styles.py --product <id> --n <N> --audience men|women|both` tags them). Whenever recommending a cast, mood or style for men, recommend hardcore first ("💪 Hardcore shirtless" as a mood). Copy still never ties the body to the product: no before/after, body comparison, body-composition claims or "ripped/shred".

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg path = preflight's `FF=` line.

## 0. Safe zones (every 9:16 image and video)
Logo, headline, offer, CTA, captions, proof and disclaimer live only inside **x 156–924, y 144–1385, minus the Reels
profile notch 156–375 × 1216–1385** (`tools/safezones.py`). The finishers refuse to export on a violation (exit 3 video,
2 image): never override; fix the layout or re-roll. QA view: `python -c "import safezones,PIL.Image as I; safezones.overlay(I.open('frame.png')).save('qa.png')"`.
Feed (4:5, 1:1): 60 px margin.

## 1. QA the raw output (always, before the user sees it)
- Contact sheet: `$FF -v error -y -i raw.mp4 -vf "fps=2,scale=180:-1,tile=10x3" -frames:v 1 sheet.jpg`, then Read it.
- Cuts: `$FF -i raw.mp4 -vf scdet=threshold=12 -f null - 2>&1 | grep -oE 'scd.time: [0-9.]+'`
- Transcript: faster-whisper from `$T/venv`; compare with the approved script.
- Pass/fail (tell the user every fail):
  - **product correctness:** the tablet matches the tablet render exactly (shape, colour, markings) and the bottle label
    matches its render; not mirrored (`--mirror-until <cut>`); exactly one tablet
  - people: real-looking, the right age (men 40s–50s fitness-model build, fitted top; HARDCORE slots shirtless 40–45 per hardcore-men.md); speech starts in the first second; "SERMORELIN GHK" on screen from frame 1 (copy.json `head`, e.g. `["SERMORELIN GHK BY EVERLIFE"]`); no bedroom (men); palette right (women)
  - no needles/syringes/vials, no gym-mirror body shots, no garbled text on props, no second phone (`--zoom 1.2`)
  - "growth hormone" said in full; product name pronounced clearly
  - last spoken line ends before ~10.5 s (15 s clip); if it runs later, start the end card after the last word or re-roll
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 1a. Header + logo on screen the whole time (every Sermorelin GHK video, men and women)
Feedback 2026-10-29: "keep 'Sermorelin GHK by Everlife' up at the top with the logo the whole time." In copy.json set
`"head": ["SERMORELIN GHK BY EVERLIFE"]` and `"head_always": true` (the captions, Trustpilot row and disclaimer already sit
in Meta's safe area by default for every product, Mitansh 2026-10-29) (otherwise the finisher hides the logo + header whenever a
face passes under it). The prompt's HEADROOM line keeps faces below the top 25%, so the header never sits on a face; check
it in QA.

## 1b. Video check + product-line voice (REQUIRED for every video, before finishing)
Cost ≈ 0.9 Higgsfield credits (3 voice takes at 0.3); ask before spending, show the cost. Work in `<job>/revoice/`.
`FF=$($T/venv/bin/python -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")`
1. **Transcribe with word times and find the cuts:**
   `$T/venv/bin/python -I -c "from faster_whisper import WhisperModel as W; m=W('medium',compute_type='int8'); [print(' '.join(f'{w.word}@{w.start:.2f}' for w in s.words)) for s in m.transcribe('<job>/out/raw.mp4',language='en',word_timestamps=True)[0]]"`
   `$FF -i <job>/out/raw.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -o "pts_time:[0-9.]*"`
   Note: where each line falls, the hands-only shot's start/end, when speech ends, any mispronounced word.
2. **Voice reference:** 2.5–4 s of the actor's own clean speech (no drug names), mono 24 kHz:
   `$FF -ss <a> -to <b> -i raw.mp4 -vn -ac 1 -ar 24000 voice_ref.wav` (join two clips with `concat` if needed).
3. **Three takes** of the product line, different spellings ("Sermorelin", "Sir-mor-ELL-in", "Sermorelin G. H. K."):
   `higgsfield generate create seed_audio --prompt "<line>" --audio voice_ref.wav --wait --json > takeN.json`
   The result is the URL containing `/hf_` (the first URL in the JSON is your uploaded reference).
4. **Pick** the take both whisper `small` and `medium` hear closest; check its length fits inside the hands shot
   (trim leading silence with `atrim`, speed up to ×1.15 with `atempo` if needed). If none is clean, LISTEN and ask the user.
5. **Build the cut:** keep the hands shot; place the take inside it; **mute the original audio there (volume=0, never a
   duck: at 5% it is heard as a second voice)**; drop any on-camera line that was mispronounced (trim + `concat`); then hold
   the last frame so the end card gets ≥ 4 s: `-vf tpad=stop_mode=clone:stop_duration=<s> -af apad=pad_dur=<s>` as its
   own pass (inside a trim chain it can silently fail; check the video length after).
6. **Re-caption** `layers_full/<Tag>_caps.json` to the new timings (correct spellings), run `full_layout.py … --end <after
   the last word>`, then re-transcribe the FINAL once: one voice per line, every name right, nothing under the end card.
7. Record in SESSION.md: which line was re-voiced, the take, the cut times, the cost. Tell the user to LISTEN to the names.

## 2. Video finishing — premium post-edit (DEFAULT since 2026-11-02; ask the style question first)
After the raw passes §1 QA, ASK the post-edit style question and finish with `premium_finish.py`, exactly as
`core/references/premium-finish.md` says (4 styles: V1 Champagne, V2 Black Label, V3 Subtle, V4 Quiet Luxe; recommended = least
recently used for this product, alternating bold/calm; log the choice). The classic `full_layout.py` route below is used only when
the user asks for it or a job needs one of its extras (review burst, mirror fix, zoom); its copy rules (bible-only lines, verbatim
disclaimer, caption spellings) apply to premium.json too.

## 2b. Classic finishing (full_layout.py, on request only)
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product sermorelin-ghk --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "sermorelin-ghk", "style": "default|tiktok|editorial" (house look = "default"; "house" crashes), "kicker": "optional label for editorial",
 "head": ["LINE 1", "LINE 2"], "sub": "subline (house only)",
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<bible>", "<bible>", "<bible>"],
 "ingredients_label": "3-IN-1 PEPTIDE SUPPORT",
 "ingredients": [["SERMORELIN","<✅ Sermorelin claim>"],["GHK","<✅ GHK claim>"],["L-CITRULLINE MALATE","<✅ Citrulline claim>"]],
 "cta": "<bible CTA in caps>", "vocab": "Sermorelin GHK."}
```
`"product"` is required: the tools take everything product-specific from `product.json` in this skill (verbatim
disclaimer, renders, name casing so nothing prints "Ghk", review highlight and reviews file) and refuse a job without it.
Don't type the disclaimer into copy.json; if it's there, it must match product.json exactly. Until the transparent
bottle exists, add `"bottle": "sghk1000_bottle_ref.jpg"` (shows its black background on the end card: preview only).
500 mcg jobs set `"bottle": "sghk500_bottle.png"` (once it's in assets/); the tablet is the same for both strengths.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 11 [--mirror-until <s>] [--zoom 1.2]`

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` (Sermorelin, GHK, growth hormone, Citrulline), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

**`tiktok` end card:** Sermorelin GHK's ingredient names and claims are too long for its name + claim rows (they overlap).
Set `"end_rows": "benefits"` and `"ingredients_label": "SERMORELIN + GHK + CITRULLINE"`: the rows then show the 3 bible
benefits. **Clip shorter than its speech + end card?** Marketing Studio fills the whole clip with speech, so hold the last
frame (`ffmpeg -vf tpad=stop_mode=clone:stop_duration=2.5 -af apad=pad_dur=2.5`) and start the end card after the last word.

Looks: `house` (style "default") · `tiktok` · `editorial`; vary across a batch. **Until the shared end card is fixed, use `tiktok` with `"end_rows": "benefits"`:** the house and editorial end cards cut Sermorelin GHK's ingredient claims off after 2 lines (2026-10-29). Women: prefer `tiktok`/`editorial` (the `house` navy/gold
is fine; check nothing reads orange).

## 3. Image finishing
**Disclaimer at the very bottom (team feedback, 2026-10-29; product setting `"disclaimer_at": "bottom"`):** on 9:16 statics
and videos the Trustpilot / Doctor Prescribed / Ships Free row stays in the Meta safe area (ends at y 1385) and the verbatim
disclaimer sits alone at the bottom of the frame, full width. Automatic for Sermorelin GHK; no flag needed. (Reels' caption
and CTA can partly cover the bottom 535 px; flagged for Jeremy.)
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.

Batch Mode: `finish_batch.py --product sermorelin-ghk` (see `image-batch.md`). `finish_modern.py` refuses this
product until its `product_zones` (the colours that let it find the bottle and tablet in a photo) are calibrated in
product.json. Legacy `core/scripts/finish_image.py` layouts work (`standard`, `checklist`, `article`, `letter`, `split`,
`frame`) with `"product"` in copy.json (article kicker defaults to "STRENGTH · LONGEVITY"); `compare` is refused
(no approved comparison for this product).

## 4. Report to the user
One block per asset: path, what it is (audience, hook, look), cost, any known issue in plain words.
