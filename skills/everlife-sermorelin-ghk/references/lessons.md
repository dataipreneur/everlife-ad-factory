# Lessons already paid for (read every session)

No Sermorelin GHK ads have been made with this skill yet. These lessons come from the Restora-Z skill (2026-10-27) and
apply to every product. Add Sermorelin-specific lessons at the bottom as they happen.

What the creative lead rejected, and why:
- **Reusing lines across ads:** "redundant… do better". Every ad gets its own angle, header, end card and CTA. Use the copy log.
- **Seedance "UGC"** (camera following a person, hands-only ASMR at 480p): "nowhere close to realistic UGC humans". Realistic humans → Marketing Studio UGC.
- **Lip-sync on a still image** (talking photo + TTS): "Bad!" Never for UGC.
- **Split-screen layouts / text boxes over faces:** keep full-frame video and light, box-free overlays; proof at the bottom on a transparent background.
- **A weak storyline after a strong hook:** the hook has to pay off in a human story.
- **Surreal/cinematic built from scratch** (the "Come Back Down" 3D ad): "quality was trash". Start from the Drive ★ Winners and real human moments; keep people close and expressive; 720p for hero pieces.
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

Sermorelin-specific risks to watch (expected, not yet seen):
- "Fit man at the gym" prompts drift to shirtless, bodybuilder or mirror-selfie bodies → state "fully clothed, natural build, not a bodybuilder, no mirrors".
- Any "toned" visual can turn into a body before/after → never show two states of one body.
- Image models like to add syringes or vials to "peptide" scenes → put "no needles, syringes or vials" in every prompt.
- Women's palettes drift into peach/orange or plant greens → name the palette and the two banned colours.

Compliance traps:
- Rx is never shared: only the person's OWN pharmacy delivery.
- Reference ads in the library use $ prices, "Breaking", first person, old proof numbers (4.8 / 50,000 / 70,000), "Dad bod", "new 40". Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- Disclaimer stays the bible's verbatim text. The global AI-disclosure line differs from it: open question for Jeremy.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.
