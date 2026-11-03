# QA + finishing (zero manual editing)

Tools: `T=${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}`; ffmpeg = `$T/venv/lib/python3.9/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1` (preflight prints the exact path as `FF=`).

## 0. Safe zones (Standards 03): applies to EVERY 9:16 image and video
Meta's UI covers: Stories top 144 px + centre-bottom 664×248 reply bar; Reels left/right 156 px, bottom 535 px, lower-left 219×169 profile. The logo, headline, offer, CTA, captions, proof and disclaimer live only inside **x 156–924, y 144–1385, minus 156–375 × 1216–1385** (`tools/safezones.py`). `full_layout.py` and `finish_modern.py` lay everything out inside it and **refuse to export** on a violation (exit code 3 for video, 2 for statics). QA view: `python -c "import safezones,PIL.Image as I; safezones.overlay(I.open('frame.png')).save('qa.png')"` shades the unsafe zones in red. Look at it for every 9:16 asset. Feed (4:5, 1:1): 60 px margin.

## 1. QA the raw output (always, before the user sees it)
- Download the result URL into `<job>/out/raw.mp4` (or `raw.png`).
- **Contact sheet:** `$FF -v error -y -i raw.mp4 -vf "fps=2,scale=180:-1,tile=10x3" -frames:v 1 sheet.jpg`, then Read it.
- **Cuts:** `$FF -i raw.mp4 -vf scdet=threshold=12 -f null - 2>&1 | grep -oE 'scd.time: [0-9.]+'`
- **Transcript:** faster-whisper from `$T/venv` (word-level). Compare it with the approved script.
- Pass/fail checklist (tell the user every fail, honestly):
  - feels *filmed*: real motion, performance, room audio (UGC); not a talking photo
  - same person throughout; real-looking skin and hands
  - bottle label readable and **not mirrored** (selfie shots mirror it → fix with `--mirror-until <cut>`)
  - exactly one capsule; no garbled text on props, doormats, mugs, boxes or books
  - no second phone in the frame (fix: `--zoom 1.2`)
  - lines said as written; "Restora-Z" and drug names pronounced clearly
  - the last spoken line ends before ~12.5 s (or accept that it plays under the end card)
- Fails that finishing can't fix → offer a re-roll with its cost (max 2 per concept).

## 2. Video finishing — premium post-edit (DEFAULT since 2026-11-02; ask the style question first)
After the raw passes §1 QA, ASK the post-edit style question and finish with `premium_finish.py`, exactly as
`core/references/premium-finish.md` says (4 styles: V1 Champagne, V2 Black Label, V3 Subtle, V4 Quiet Luxe; recommended = least
recently used for this product, alternating bold/calm; log the choice). The classic `full_layout.py` route below is used only when
the user asks for it or a job needs one of its extras (review burst, mirror fix, zoom); its copy rules (bible-only lines, verbatim
disclaimer, caption spellings) apply to premium.json too.

## 2b. Classic finishing (full_layout.py, on request only)
Write `<job>/copy.json` (all copy from the bible, all new against the copy log):
```json
{"product": "restora-z", "style": "house|tiktok|editorial", "kicker": "optional label for editorial",
 "head": ["LINE 1", "LINE 2"], "sub": "subline (house style only)",
 "end_head": ["END LINE 1", "END LINE 2"],
 "ingredients_label": "3-IN-1 SLEEP FORMULA",
 "ingredients": [["TRAZODONE","<bible claim>"],["HYDROXYZINE","<bible claim>"],["DOXEPIN","<bible claim>"]],
 "cta": "<bible CTA in caps>", "vocab": "Restora-Z."}
```
`"product"` is required (since 2026-10-28): the verbatim disclaimer, the renders, name casing, the review highlight and
the reviews file all come from this skill's `product.json`, and the tools refuse a job without it. Don't type the
disclaimer; if it's in copy.json it must match product.json exactly. Older job folders need `"product": "restora-z"` added
before re-running. Keep `vocab` to "Restora-Z." only (longer vocab makes whisper drop those caption lines).

Run: `cd $T && venv/bin/python -I full_layout.py <job> <job>/out/raw.mp4 <Tag> --end 12.8 [--mirror-until <s>] [--zoom 1.2]`

Then open `<job>/layers_full/<Tag>_caps.json` and fix whisper's spellings (Trazodone, Hydroxyzine, Doxepin, Restora-Z, "Three a.m."), merge one-word chunks, restore "?" on questions, and drop a caption that is cut off at the end card. Re-run the same command (it reuses the edited captions). Check 4 frames (hook, mid, product, end card), then copy the result to `<job>/FINAL_<Tag>_15s_9x16.mp4` and `open` it.

**Review burst (the team's favourite):** add `--reviews R1,R3,R4,R2 --reviews-at <s>` to drop a ~2.4 s insert where verbatim Trustpilot review cards slam in one after another (the first zoomed in with "Restora-Z" highlighted), stacking into a collage; the proof bar stays on top and the audio keeps playing. IDs come from `references/reviews.json` (✅ screened reviews only). Best placed on a proof beat (e.g. while the line "Doctor prescribed…" plays), 1–2 s before the end card. List the review ids, dates and source in SESSION.md for Jeremy.

Looks: `house` (gold condensed headline on a navy fade, white caption pills, navy end card), `tiktok` (white sticker headline, word-by-word yellow highlight, cream end card), `editorial` (serif italic headline + kicker, lowercase serif subtitles on a soft band, dark end card with ingredient columns). Vary the look across a batch.

## 3. Image finishing
9:16 statics: the proof footer ends at y 1385 (bottom of the Reels safe area; see image-batch.md "Footer position"), never at the bottom of the frame.
 (default: `finish_modern.py`; see image-prompting.md)

**Finish statics like a designer, by hand. The script is a starting point, not the judge.** After every render, open it at full size and check:
1. **Nothing touches the product.** Type, chips and cards keep ≥ 30px clear of the bottle, cap and capsule. The script auto-detects the product (teal label/bottle, blue capsule) and refuses to place over it: exit code 2 or a "falling back" note means it couldn't fit. Don't ship that blindly: shorten or resize the headline (`m_size`), switch template, or regenerate the image with more empty space.
2. **Hierarchy:** headline first, product second, proof last. The headline is never timid: if it looks lost in empty space, raise `m_size` (e.g. 104–118 for a 2-line, left-aligned strip headline).
3. **Legibility 50+:** chip and card text ≥ 25px, the proof line ≥ 24px, nothing clipped at the edges.
4. **Balance:** cards and chips sit in the calm area (beside, never on, the subject); faces are never covered.
5. Then copy it to `FINAL_…png`. If any check fails, fix and re-render before showing the user. Never describe an overlap as "fine".

Use `finish_modern.py --template hero|strip|notify|toggle|chips` for every static unless the format needs a legacy layout below.

Legacy layouts:
`$T/venv/bin/python -I <skill>/core/scripts/finish_image.py <raw.png> <job>/copy.json <out.png> --ratio 4:5 --layout <standard|checklist|compare|quote|article|letter|split|frame>`
copy.json needs `"product": "restora-z"` (same for `finish_modern.py`). Every layout adds the logo, the transparent Trustpilot / Doctor Prescribed / Ships Free row and the verbatim disclaimer (from product.json); the layout adds the middle (cards, ❌✅ list, Restora-vs-Ambien table with both pills, review card, article panel, letter, pain→benefit split, or the ad placed inside a frame). The copy.json keys for each layout are listed at the top of `finish_image.py`. Make 1:1 and 9:16 versions from the same raw image only after the 4:5 master is approved (`--ratio`). Check the result, then save `<job>/FINAL_<Tag>_<ratio>.png` and `open` it.

**Team logs, videos too (`core/team-logs/TEAM-LOGS.md`):** log each generated clip to the Prompt & Outcome Log, the video's copy and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log. Unreachable → the pending file, never block.

## 4. Report to the user
One block per asset: the file path, what it is (hook, look), the cost, and any known issue in plain words.
