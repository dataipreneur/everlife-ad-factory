# Lessons already paid for (read every session)

No plain Sermorelin ads have been made with this skill yet. These lessons come from the Restora-Z skill (2026-10-27) and
the Sermorelin GHK skill, and apply to every product. Add Sermorelin-specific lessons at the bottom as they happen.

What the creative lead rejected, and why:
- **Reusing lines across ads:** "redundant… do better". Every ad gets its own angle, header, end card and CTA. Use the copy log.
- **Seedance "UGC"** (camera following a person, hands-only ASMR at 480p): "nowhere close to realistic UGC humans". Realistic humans → Marketing Studio UGC.
- **Lip-sync on a still image** (talking photo + TTS): "Bad!" Never for UGC.
- **Split-screen layouts / text boxes over faces:** keep full-frame video and light, box-free overlays; proof at the bottom on a transparent background.
- **A weak storyline after a strong hook:** the hook has to pay off in a human story.
- **Surreal/cinematic built from scratch** (the "Come Back Down" 3D ad): "quality was trash". Start from real human moments; keep people close and expressive; 720p for hero pieces.
- **Busy direct-response statics** (all-caps condensed, chips everywhere, badge stacks): 4/10. Aim for a modern brand look.

Generation traps:
- Selfie / front-camera prompts **mirror the label** → `--mirror-until`.
- Marketing Studio may render a **second phone** → "the filming phone is never visible"; fix with `--zoom 1.2`.
- Props with labels (mugs, books, gym equipment branding) come out **garbled** → ask for plain, unbranded props.
- Two pills tipped into a palm read as a two-pill dose → "exactly ONE tablet".
- Model voices mangle drug names → write the pronunciation; keep spoken product names ≤ 2.
- Whisper misspells product names → always hand-fix captions.
- Long scripts run under the end card → ≤ 35 spoken words, finishing by ~12 s.
- GPT Image 2.5 on Creatify places the product LOWER than asked → one cheap reposition edit on the raw.
- Cropping 4:5 to 9:16 puts the footer on the product → generate 9:16 natively.

Seen in the first test (2026-10-29: 1 Seedance video + 5 Creatify statics, `~/Everlife-Creative/output/Sermorelin/2026-10-29_SESSION.md`):
- **Seedance's voice says "Sermoral"** (drops "-lin") and slurs "sublingual", even with "ser-mo-REL-in" in the prompt.
  Check with Whisper `small` + an `initial_prompt`; plan the VO as a separate TTS line (Creatify `composer_voice_line`,
  ~0.1 cr, or Higgsfield audio) muxed over the clip, or ask Seedance for no dialogue at all.
  **Proven fix (same day):** Creatify voice "Fabian — American English" (`9nZr75s2rhJ2gFpei7j3`, calm narration) said
  "Sermorelin" and "sublingual" correctly from plain text, 25 words in 11 s. Mux with a fixed length:
  `ffmpeg -i raw.mp4 -i vo.wav -map 0:v -map 1:a -c:v copy -af "apad=whole_dur=<clip s>" -c:a aac -t <clip s> raw_vo.mp4`
  (plain `apad` + `-shortest` never ends). Next time ask Seedance for **"no dialogue, ambient sound only"** so the foley
  survives under the TTS line.
- **25 spoken words ran to 14.8 s** at a calm pace: budget ≤ 22 words for this voice, or the last line plays over the end card.
- **GPT Image garbles the bottle's small label text** ("30 SUBLINGUAS", missing "TABS") when the bottle is small or low
  in frame; a re-roll edit didn't fix it. 4 of 5 were clean when the bottle was medium/large. Fix: ask for a large bottle,
  or composite the real render (`composite.py --product sermorelin`) instead of re-rolling.
- **Bottles land low** and their base sits behind the transparent footer row (17% of height): ask for the bottle's base
  at ≤ 78% of the canvas height.
- What worked: the round "S" tablet came out exactly right in all 6 images and the video; tablet-in-hand framing (men and
  women) looks like the winners; women's pink/beige palettes held with the orange product.

Sermorelin-specific risks to watch (expected, not yet seen):
- **The injection vial comes back.** Almost every past plain-Sermorelin ad shows the bottle next to an orange-capped vial;
  models trained on similar ads will add one → "no vial, no second container" in every prompt, check every frame.
- **Mixed up with Sermorelin GHK.** Same family name, different product: never attach a GHK render, never write GHK copy,
  check Marketing Studio picked "Sermorelin", not "Sermorelin GHK".
- **Two tablet shapes in past ads** (round "S" vs oblong "SERMORELIN"): only the confirmed render; QA the shape.
- "Fit man at the gym" prompts drift to shirtless, bodybuilder or mirror-selfie bodies → "fully clothed, natural build, not a bodybuilder, no mirrors".
- Any "toned/lean" visual can turn into a body before/after → never show two states of one body.
- Women's scenes pick up the product's orange → name the palette and the two banned colours for the scene.

Compliance traps:
- Rx is never shared: only the person's OWN pharmacy delivery.
- Past plain-Sermorelin ads use "$95", "Breaking News", "Same man, double strength" body splits, "From Flab to Fab",
  "Get Ripped", "Fat burning", "Skip the needles", "Injections or sublingual tablets", "Over 750,000 tablets sold",
  "Featured in NIH / Mayo Clinic" logos, "Sermorelin GH Peptide", a bylined fake article. Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- Disclaimer stays the bible's verbatim text. The global AI-disclosure line differs from it: open question for Jeremy.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.
