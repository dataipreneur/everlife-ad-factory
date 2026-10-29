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

## First Sermorelin GHK batch (2026-10-28, men, 5 statics, 7 credits incl. 2 re-rolls)
- **Hyphens can render as "="** ("3=in=1", "Youthful=Looking"). Fix that worked: in TEXT add "every hyphen is a normal short
  hyphen '-', never an equals sign" + a spelling check line for each hyphenated string. Add it up front next time.
- **Product too low again** (the Restora trap): an identity-post photo put the bottle and tablet in the footer zone. Fix that
  worked: give an explicit band, "the product group between 40% and 72% of the canvas height". Use it whenever a person is in shot.
- **Type specimen is Restora's** ("Sleep deeper, wake clear", purple accent). Saying "ONLY a lettering style guide; ignore its
  words, its purple colour and its layout" kept every ad clean. A Sermorelin-specific specimen would be safer (to do).
- Tablet piles render a slightly deeper green than the reference; single tablets stay true. Acceptable; mention in QA.
- What worked first time: real 500 bottle label (incl. "500 MCG"), the green "S" tablet, exact Tier A strings, clothed
  mature talent, text-only 3-in-1 tiles (no made-up ingredient pills), "Save up to 47%" badge.

## Video discipline (creative lead, 2026-10-27; from the Restora-Z lessons, applies to every product)
- A video costs 45–75 Higgsfield credits (= 45–75 Creatify images). Review the script AND the full prompt line by line, then
  review again, before offering "Approve & generate". Never send a first draft to the video model.
- Realistic people talking/acting → Marketing Studio UGC (75 cr / 15 s, 720p). Seedance humans were rejected; Seedance only for
  comedic, stylised or animated ideas.
- Prove the angle with a 1-credit static before spending on a video of it.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.

## Creative lead, 2026-10-28: logo at the top, and stop repeating the same type
- **The Everlife logo sits at the TOP of every static**, never in the footer. `finish_batch.py` now lays it in the top
  safe band and nudges the image down if the generation left no headroom; the prompt asks for a calm top 12% (10% feed).
- **Fonts and colours must change from ad to ad.** The batch kept coming back as the same serif with the same purple
  accent on white: "they don't need to be always the same". Use `image-batch.md` §2b: a different pairing and a
  different accent for every ad, the type specimen only when the house look is asked for.
- **Footer inside the Meta safe area, never at the bottom (Mitansh, 2026-10-29).** A live Reels screenshot
  (`core/references/safe-zones/reels_placement_2026-10-29.jpg`) showed our bottom-anchored proof footer under the
  "Learn more" button and caption. The toolkit is back in safe mode: the 9:16 footer ends at y 1385, so the raw keeps
  everything in its top ~52% (LAYOUT block) and `finish_batch.py` refuses when content runs under the footer. Old raws
  composed to the bottom need one reposition edit; an automatic scale-down-and-extend was tried and rejected.
