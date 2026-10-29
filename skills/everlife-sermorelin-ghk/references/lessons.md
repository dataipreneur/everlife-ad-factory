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

## Second Sermorelin GHK batch (2026-10-28, women, 5 statics, 6 credits incl. 1 reposition)
- **Re-install the toolkit after a tool changes in git.** The installed `finish_batch.py` was still the old one and put the
  logo in the footer. After pulling a tool change, run `bash core/scripts/preflight.sh --install` (or copy the file) before
  finishing, and check the finisher's log line says `logo=top@…`.
- **Long ingredient claims run into the footer** ("…glycosaminoglycan production" wrapped to 4 lines). Give the text block an
  explicit end ("all text ends above 76% of the height"), or pick the shorter approved claim for narrow columns. It
  overflowed again in batch 3 even with a band; in a two-column layout prefer "Promotes radiant, firmer, youthful-looking skin".
- **Don't drop the bottle.** This batch went tablet-only to dodge the tan-tablets-in-bottle render; W2–W4 then never said
  what the product was (fails "identifiable in 2 seconds") and didn't look like our winners. Rule now: bottle + tablet in
  every ad until a corrected render is confirmed (image-batch.md step 3).
- Pinterest layouts (level 3) translated well for women: split, cards, staircase, sticky note. Backgrounds still sneak in
  peach skies and plant greens → name them in the "avoid" line.
- "Lean/Leaner" headlines with a person in shot need Jeremy (pre-screen ⚠: never with a body shot).
- With the bottle in shot the model makes the BOTTLE the hero (W4, batch 3). Say "the tablet about twice the size it would
  naturally be, in front of the bottle" and keep the logo band clear of props (a sticky note rose into it).

## First Sermorelin GHK video (2026-10-28, women, UGC 1A, 15 s, 75 credits, failed QA)
- **Check the product images AS HIGGSFIELD SEES THEM.** The tablet PNG hid red/magenta streaks under its transparent
  background; Creatify ignores them, Higgsfield showed a glitchy black tablet. Combined with the bottle render's round tan
  tablets, the video invented a dish of mixed green and round white pills. Fixed: hidden pixels set to white (visible
  pixels unchanged), product re-registered in Marketing Studio (dc55181a…). Preflight now warns on hidden junk.
- **No dishes, piles or open bottles.** One tablet between fingertips in a hands-only close-up; "no other pills anywhere".
- **Marketing Studio stretches dialogue to fill the clip** (~2 words/s, same as winner F4). 32 words ran to 14.5 s and
  left no room for the end card. Budget ≈ 2 words per second of speech time, and say "finish speaking by <t> s".
- **MS starts talking at 0 s** unless told "silent for the first 2 seconds".
- **Watch the winner video itself, not only its card.** F4 cuts between a talking head and separate hands-only product
  close-ups and pins a product bar (logo + name + bottle + tablet) for the whole video.
- Shorter is cheaper: MS UGC 720p costs 40 (8 s) / 50 (10 s) / 60 (12 s) / 75 (15 s). 8 s is a proven length (winner M5).

## Reference priority in practice (2026-10-29)
- **Pick the winners first, then the frameworks.** Batches 2–3 (women) picked a framework per slot and then looked for a
  matching winner, so W1–W4 fell to Pinterest and only W5 built on a winner. Rule now (image-batch.md step 2): at least
  3 of 5 slots start from a winner for the audience; Pinterest fills the rest.

## Video length (2026-10-29)
- **15 s is the standard, as Restora-Z**; the bible sets no length. The end card starts at 11 s (not Restora's 12.8) so it
  stays up 4 s for 50+ readers; speech ≤ 18 words, finished by ~10.5 s. 8 s only for a simple hook + product idea.

## First 15 s men's video "Kettlebell" (2026-10-29, 2 + 75 credits)
- **Preview stills worked:** cast (fit, ~50, clothed) and the single green "S" tablet came out right in the video too.
- **"Finish speaking by 10.5 s" was not obeyed:** 17 words ran 2.6–12.4 s (MS still stretches). Hold the last frame
  (~1.7 s) so the end card keeps 4 s; next time try ≤ 14 words, or accept a ~17 s finished file.
- **Product name likely mispronounced** ("Semrigin GK KH" to two whisper models) even with the pronunciation line. The name
  is said over the hands-only shot, so a re-voiced line could be dropped in there without lip-sync. Listen before review.
- **Tablet in front of the bottle hides the product name** on the label. Ask for "the tablet held to the side of the
  bottle, never covering its label".
- **End card looks:** `"style": "house"` crashes (the house look is `"default"`); the default and editorial end cards cut
  the long ingredient claims off. `tiktok` + `"end_rows": "benefits"` is the only clean one for this product today.
- **Fix a mispronounced line for 0.3 credits** when it falls over a shot without a visible mouth: clone his voice with
  `higgsfield generate create seed_audio --prompt "Sermorelin G. H. K. …" --audio <his own correct lines>.wav --wait --json`
  (the result is the `/hf_…` URL; the first URL in the JSON is your uploaded reference), trim/atempo it to fit inside the
  shot's cut times (`select='gt(scene,0.3)'`), MUTE the original voice there (volume 0, not a duck: at 5% it is still heard as a second voice, Priestley 2026-10-29), splice, re-caption, re-finish.
  "G. H. K." with dots read correctly in 3 of 3 takes. So: say the product name over a hands-only shot by design.

## Batch 4 (2026-10-29, 5 men + 5 women, 9 winners + 1 Pinterest, 17 credits incl. 7 fixes)
- **Winners-first works:** 9 of 10 built on a winner; the strongest-looking ads are the winner rebuilds (M1 from M8, M2 from M3, W1 from F2).
- **The product still lands low.** "Between 45% and 78%" → 6 reposition edits in 7. "Ends above 72%, bottom 22% calm"
  → clean first time (W3, W5). Template updated (image-batch.md §3). Text blocks with 3 ingredient rows also run low (W1).
- **Tablet size drifts small when a person shares the frame** (W4: 11% of the width). Say "at least 17% of the width" there.
- **Justin's new lines render well:** "Supports Natural Growth Hormone Production", "Supports Workout Pumps + Endurance",
  "Supports Exercise Recovery", "Supports Firmer, Glowing Skin From Within".
- **Women's Tier A headlines are nearly used up**: left unused: "Your GLP-1 Complement for Lean Muscle + Glow",
  "GLP-1 Complement: Lean. Strong. Radiant.", "The GLP-1 Complement for Muscle, Skin + Hair" (hair ⚠). Ask Justin for more.

## Review feedback on batch 4 (2026-10-29)
- **Women: "Pink is great for most women, but everything pink like that looks the same."** 4 of 5 women's ads were
  pink-led. The bible allows pinks, tans AND beige; rotate the lead colour, at most one pink-led ad per batch (image-batch.md §2b).
- **Men: the font on M3 ("The Edge You've Been Missing", elegant serif with a gold italic) was called "not right".** The
  bible has no font rule; the serif came from the creative lead's "vary fonts" rule. The bible lines that point the way:
  "Product names run big" (M3 showed the name only on the label) and "Reference top-performing, lowest-CPA creative"
  (every men's winner uses heavy condensed caps). Reviewer follow-up: "men shouldn't use that font IMO" → rule now: no elegant / italic serif or brush headlines on
  men's ads (image-batch.md §2b).

## Batch-5 videos "Track" (men) + "Pilates" (women), 2026-10-29 (227 Higgsfield incl. one failed take)
- **Marketing Studio ignores "say line 1 over the hands-only shot"**: both takes put every line on the face, and both said
  "Sermorelin" wrong ("Surmergene", "Surmeasine", "Cermalacup"). Plan the edit instead: let the hands shot run silent or
  with a throwaway line, re-voice the product line in the cloned voice over it, and cut the on-camera product line out.
- **Any window shows the outside.** Pilates take 1 had an orange wall and green trees through the window (women's palette
  fail, not fixable in edit). For women's interiors say "interior wall only, the window NOT in frame, no outdoor view, no plants".
- **"Sublingual" is mispronounced too** ("sub-single", "subliberal"). Keep it on screen, not spoken, or over a hands shot.
- The Seed Audio clone fixes names in 1 of 3 takes reliably; spelling "Sir-mor-ELL-in" or plain "Sermorelin" worked best.

## Team feedback on the men's "Track" video (2026-10-29: Emily, Sarah, Jeremy, Justin)
- "He needs to start talking way sooner": no silent openings; speech in the first second, hook within 2.5 s.
- "Sermorelin GHK needs to be on the screen from the start… this applies to every product": the header is the product name.
- "Too old… not ripped enough… hardcore fitness model 40's to 50s, tats or no tats" / "a fit silver fox… men look at him and
  want to look like this dude": casting changed (video-prompting.md CAST). Kept fully clothed (Priestley).
- Bible v3 adds "[Product] by Everlife" in every intro and a held tablet (thumb + index or open palm).
- Safe zones: already enforced by the finishers (same numbers as the bible's safe-zone page).

## Justin's women's colour direction (2026-10-29)
- Pinks, tans, neutrals, warm tones still preferred (they performed); add **white** (especially advertorials) and **teal**.
  Preferences, not limits: keep exploring trends (up to 2 of 5 ads). Rules in image-batch.md §2b.
- Statics: product name only ("SERMORELIN GHK"), no "by Everlife" (Priestley, 2026-10-29). Videos keep "by Everlife".

## 9:16 statics with the safe-zone footer (test, 2026-10-29)
- The model ignores "keep the product in the top 55%": first takes had the tablet/label under the footer and full-width
  pills in Meta's side zones. One reposition edit per image fixed both; the finisher's automatic logo nudge (up to 140 px)
  can push the product back down: re-finish with `--shift 60`. The footer reads clearly on the stronger band.
