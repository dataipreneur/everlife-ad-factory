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
    matches its render; not mirrored (`--mirror-until <cut>`); exactly one tablet; **no injection vial** (the past ads
    always paired the bottle with one: models will add it back)
  - people: real-looking, the cast age (men 42–50 hardcore fitness-model build; HARDCORE slots shirtless 40–45 per hardcore-men.md); no bedroom;
    the tablet held (fingers or palm) beside the bottle, not covering the label
  - no needles/syringes/vials, no gym-mirror body shots, no garbled text on props, no second phone (`--zoom 1.2`)
  - "growth hormone" said in full; never "GH"; product name pronounced clearly; no "GHK" anywhere
  - speech starts in the first second; last spoken line ends by ~10.5 s (end card 11–15 s)
- Fails finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 1a. Header + logo on screen the whole time (every Sermorelin video)
Team feedback 2026-10-29 ("needs to be on the screen from the start… this applies to every product"): in copy.json set
`"head": ["SERMORELIN BY EVERLIFE"]` and `"head_always": true` (otherwise the finisher hides the logo + header whenever a
face passes under it). The prompt's HEADROOM line keeps faces below the top 25%; check it in QA.
**9:16 footer (automatic from product.json, same as Sermorelin GHK):** the Trustpilot / Doctor Prescribed / Ships Free
row ends at y 1385 inside the Reels safe area; the verbatim disclaimer sits alone at the very bottom, full width, on 2
lines (`"disclaimer_at": "bottom"`); the tiktok end card shifts down to clear the bigger logo (`"end_card_safe_shift"`).
`keep_case` keeps "Sermorelin by Everlife" with a lowercase "by" in the header.

## 1b. Product-line voice (REQUIRED for every video, before finishing)
**No on-camera speaker (Seedance/Boreal, "no dialogue"):** voice the approved script with Creatify `composer_voice_line`
(Fabian `9nZr75s2rhJ2gFpei7j3`, ~0.1 cr), Whisper-check it, mux it (command in `lessons.md`), starting at ~0.3 s.

**On-camera actor (Marketing Studio):** the product-name line is re-voiced in the actor's cloned voice. Cost ≈ 0.9
Higgsfield credits (3 takes at 0.3); ask before spending, show the cost. Work in `<job>/revoice/`.
`FF=$($T/venv/bin/python -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")`
1. **Transcribe with word times and find the cuts:**
   `$T/venv/bin/python -I -c "from faster_whisper import WhisperModel as W; m=W('medium',compute_type='int8'); [print(' '.join(f'{w.word}@{w.start:.2f}' for w in s.words)) for s in m.transcribe('<job>/out/raw.mp4',language='en',word_timestamps=True)[0]]"`
   `$FF -i <job>/out/raw.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -o "pts_time:[0-9.]*"`
   Note where each line falls, the hands-only shot's start/end, when speech ends, any mispronounced word.
2. **Voice reference:** 2.5–4 s of the actor's own clean speech (no drug names), mono 24 kHz:
   `$FF -ss <a> -to <b> -i raw.mp4 -vn -ac 1 -ar 24000 voice_ref.wav` (join two clips with `concat` if needed).
3. **Three takes** of the product line, different spellings ("Sermorelin", "Sir-mor-ELL-in", "Ser-mo-REL-in"):
   `higgsfield generate create seed_audio --prompt "<line>" --audio voice_ref.wav --wait --json > takeN.json`
   The result is the URL containing `/hf_` (the first URL in the JSON is your uploaded reference).
4. **Pick** the take both Whisper `small` and `medium` hear closest; it must fit inside the hands shot (trim leading
   silence with `atrim`, speed up to ×1.15 with `atempo` if needed). If none is clean, LISTEN and ask the user.
5. **Build the cut:** keep the hands shot; place the take inside it; **mute the original audio there (volume=0, never a
   duck: at 5% it is heard as a second voice)**; drop any mispronounced on-camera line (trim + `concat`); then hold the
   last frame so the end card gets ≥ 4 s: `-vf tpad=stop_mode=clone:stop_duration=<s> -af apad=pad_dur=<s>` as its own
   pass (inside a trim chain it can silently fail; check the video length after).
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
**Proof split, videos too (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of videos carry NO proof; 70% carry ONE footer proof: the trust row (60% of those) or the Trustpilot 4.9 badge + "Over 100,000 happy customers" (40%); the end card has no count line of its own. Before finishing run `python -I core/scripts/proof_next.py --product sermorelin --log <tag>` and put its answer in copy.json as `"proof": "trust"`, `"count"` or `"none"` (animated stills: `animate_still.py --proof …`).

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** each clip is already in the Prompt & Outcome Log (logged when submitted, `video-prompting.md`); now log the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log (`teamlog.py copy / proof / run`, then `close` ✅ before SESSION.md). Unreachable → the pending file, never block.

Write `<job>/copy.json` fresh each time (all copy from the bible, new against the copy log):
```json
{"product": "sermorelin", "style": "default|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["SERMORELIN BY EVERLIFE"], "head_always": true, "sub": "subline (house only)",
 "end_head": ["END LINE 1", "END LINE 2"], "benefits": ["<✅ bible>", "<✅ bible>", "<✅ bible>"],
 "cta": "<bible CTA in caps>", "vocab": "Sermorelin."}
```
`"product"` is required: the tools take everything product-specific from `product.json` in this skill (verbatim
disclaimer, renders, name casing, review highlight and reviews file) and refuse a job without it. **Never** `"product":
"sermorelin-ghk"` for this skill: that prints the other product's renders. Don't type the disclaimer into copy.json; if
it's there, it must match product.json exactly. The default bottle is 1000 mcg; 500 mcg jobs set
`"bottle": "sermorelin500_bottle.png"` (in assets/ since 2026-10-29).

Single-ingredient product, but the `tiktok` and `editorial` end cards **require** `ingredients_label` + `ingredients`
(`core/tools/styles.py`; `house` doesn't). Fill them with the three ✅ benefits, never a made-up ingredient claim:
```json
 "ingredients_label": "DOCTOR-PRESCRIBED SERMORELIN",
 "ingredients": [["ENERGY","Supports Energy + Stamina"],["STRENGTH","Supports Strength + Vitality"],
                 ["GROWTH HORMONE","Supports Natural Growth Hormone Activity"]]
```
**`tiktok` look:** the third row collides at that length ("Growth Hormone" runs into its claim; seen in the 2026-10-28
smoke test), so use `["DELIVERY","Easy sublingual delivery"]` as the third row and carry growth hormone in the VO or
the header. Its CTA button fits ≈ 20 characters: "EXPLORE SERMORELIN", "GET STARTED NOW", "BUILD YOUR PLAN" fit;
"SUPPORT NATURAL GROWTH HORMONE" overflows (use it in `house`/`editorial` only, and check the frame). Check the end card renders without "3-in-1" wording and nothing overlaps.
The round tablet is drawn at `pill_end_scale` (product.json, 0.62) of the default end-card pill size so it doesn't cover
the label line or dwarf the bottle.

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 11 [--mirror-until <s>] [--zoom 1.2]`
(end card 11–15 s so it stays up 4 s for 50+ readers; if speech runs past 10.5 s, hold the last frame, §1b step 5)

Then fix whisper's spellings in `<job>/layers_full/<Tag>_caps.json` (Sermorelin, growth hormone, sublingual), merge
one-word chunks, restore "?", re-run. Check 4 frames (hook, mid, product, end card), copy to `<job>/FINAL_<Tag>_15s_9x16.mp4`, `open` it.

**Review burst:** gated (no screened reviews yet, see `reviews.md`).

Looks: `house` · `tiktok` · `editorial`; vary across a batch. **In copy.json the house look is `"style": "default"`**
(`"house"` crashes `styles.make`; found in the 2026-10-29 test). Run finishing with this skill's toolkit until the
`pill_end_scale` change is installed: `EVERLIFE_TOOLS=<repo>/core/tools EVERLIFE_SKILLS_DIR=<repo>/skills` and `cd` into
`<repo>/core/tools` (don't run preflight `--install` from a branch: it overwrites the shared toolkit other sessions use). Women: prefer `tiktok`/`editorial` (the `house` navy/gold
is fine too; bible v3 sets no colour limit for Sermorelin).

## 3. Image finishing
Batch Mode: `finish_batch.py --product sermorelin` (see `image-batch.md`). `finish_modern.py` refuses this product until
its `product_zones` (the colours that let it find the bottle and tablet in a photo; orange label + orange tablet, so
both zones will sit in the same hue band) are calibrated in product.json. Legacy `core/scripts/finish_image.py` layouts
work (`standard`, `checklist`, `article`, `letter`, `split`, `frame`) with `"product"` in copy.json (article kicker
defaults to "STRENGTH · LONGEVITY"); `compare` is refused (no approved comparison for this product).

## 4. Report to the user
One block per asset: path, what it is (audience, hook, look), cost, any known issue in plain words.
