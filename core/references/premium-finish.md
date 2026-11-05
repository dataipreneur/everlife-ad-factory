# Premium post-edit: the 4 styles + the style question (every video, every product; Mitansh 2026-11-02)

The default video finish is `core/tools/premium_finish.py` (installed at `$T/premium_finish.py`). The old sticker-box look
(`full_layout.py`, black/teal header boxes, coloured caption stickers, flat white end card) was rejected ("worse / bad
post editing… I want this type of text to be a new normal"). Use `full_layout.py` only when the user asks for the classic look
or needs one of its extras (review burst, `--mirror-until`, `--zoom`): or apply those to the raw first, then run premium.

Visual reference: `core/references/premium-styles.jpg` (the same footage in all 4 styles: hook / mid / end card). Read it and show it
when the user wants to see the styles.

| Style key | Name | Feel | Type | Accent (men / women) | End card |
|---|---|---|---|---|---|
| `champagne` | V1 Champagne | bold, luxurious | Avenir Next Heavy, tracked caps | champagne gold / rose gold | navy wash over the blurred video, cream CTA pill |
| `blacklabel` | V2 Black Label | bold, hard-hitting | Helvetica Neue Condensed Black caps; last caption word in the accent | bottle-label red / deep rose | near-black, square bullets, solid accent CTA |
| `subtle` | V3 Subtle | calm, cool, editorial | Futura Medium, left-aligned, one-line name | ice blue / blush | bright frosted panel, navy type, outline CTA |
| `quietluxe` | V4 Quiet Luxe | calm, warm, refined | Helvetica Neue Light, tracked caps, centred | warm sand (both) | smoked glass, sand dots, sand outline CTA |
"Not everyone needs to be this big and bold every time" (Mitansh): keep the calm styles in the rotation.

## The question (ASK it every video: after the raw passed QA, right before finishing)
One AskUserQuestion, header "Post-edit", question "Which post-edit style for <video name>?", 4 options in this order, the
✨ recommended one FIRST with "(Recommended)" in its label:
- "V1 Champagne": "Bold + luxurious: big tracked Avenir, champagne gold, navy end card, cream CTA"
- "V2 Black Label": "Bold + hard-hitting: condensed caps, bottle-red accent, black end card, red CTA"
- "V3 Subtle": "Calm + editorial: light Futura, left-aligned, ice blue, bright frosted end card"
- "V4 Quiet Luxe": "Calm + refined: light spaced caps, warm sand, smoked-glass end card"
(Women: say rose gold / deep rose / blush instead of champagne / red / ice blue.) Put a short ASCII mock in each option's
`preview` if useful. The user may type "all" (render all 4 and show a comparison sheet) or "classic" (full_layout.py).
**Recommendation rule:** the style least recently used for this product (column "finish" in the product's copy log), alternating
bold ↔ calm between consecutive videos; two videos in one session never share a style unless the user picks it.
Log the chosen style in the copy log row and in SESSION.md ("finish: <key>").

## Run it
1. Write `<job>/premium.json` (copy only from the bible/brief; NEVER a disclaimer: the tool takes the product's verbatim one from
   product.json):
```json
{"product": "<id>", "audience": "men|women", "end": 11.0,
 "head": "SERMORELIN GHK", "sub": "DOUBLE STRENGTH",
 "end_label": "SERMORELIN GHK  ·  DOUBLE STRENGTH", "end_head": "Power Your Prime", "end_sub": "3-in-1 Sermorelin GHK",
 "benefits": ["Supports Natural Growth Hormone Production", "Promotes Lean Muscle + Performance", "Supports Workout Pumps + Endurance"],
 "cta": "EXPLORE SERMORELIN GHK", "bottle": "sghk1000_bottle.png"}
```
   Optional: `"pill"` (`""` = no pill, e.g. a spray form), `"audio"` (job-relative file, e.g. a re-voiced mix), `"head_display"`
   (V3's sentence-case name). `head` = the product name (on screen from frame 0, every product); `sub` = an optional short line
   (e.g. Double Strength on SGHK 1000, ⚠ pending Jeremy). Keep benefits ≤ 3 and short; CTA = a bible CTA.
2. Captions: `cd $T && venv/bin/python -I premium_finish.py <job> <raw.mp4> --style <key> --caps-auto` writes sentence captions
   into premium.json and stops. **Hand-fix every product name** (whisper writes "Sermirellan", "Restore Z"…), drop anything after `end`.
3. Render: `venv/bin/python -I premium_finish.py <job> <raw.mp4> --style <key> --out <job>/FINAL_<Tag>_<key>_15s_9x16.mp4`
4. QA (free): frames at 0.5 / mid-caption / end card + `safezones.overlay` view. Check: captions don't sit on the product label
   (if they do, shorten the caption or shift its start/end around the product moment), sub-labels readable on bright footage,
   end card complete, logo + proof + disclaimer present. Open the file for the user.

## Safe zones (enforced: the tool refuses to export; never override)
Text, logo and CTA stay in x 156–924 × y 144–1385, out of the Reels profile notch (x 156–375 × y 1216–1385); captions and the end
card end above y ≈ 1206. Proof row = the approved footer art, full width (allowed). Disclaimer: product.json `disclaimer_at:
"bottom"` → alone at the very bottom (Sermorelin, Sermorelin GHK, PT-141); otherwise in the footer under the proof row, ending
by y 1385 (Restora-Z, BPC-157). On a refusal: shorten the copy (head/benefits/CTA) and run again.

## Product notes
Every product uses the same 4 styles; renders come from product.json (`renders_for`, `strengths`, `forms`) or `bottle`/`pill` in
premium.json. Women's creative uses the women's accents automatically (no orange/green; pinks/tans/rose). Intimate products
(PT-141, Spark, Lovara): calm styles (V3/V4) are the safer recommendation. AI Avatar Video: run premium on the composited raw; the
captions sit at y ≈ 1150–1200, clear of the presenter face band (y 700–880).
Fonts are macOS system fonts (Avenir Next, Helvetica Neue, Futura): no install needed on a Mac.
