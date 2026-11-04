# Lessons already paid for (read every session)

> **💪 HARDCORE MEN = `core/references/hardcore-men.md` (Jeremy via Mitansh, 2026-11-02; OVERRIDES every "fully clothed / no bare torso / never shirtless / no flexing / not a bodybuilder / natural build" line and every winner's "Don't copy: shirtless" note in this skill):** men's ads lean intense: shirtless or stringer, 40–45, flawless muscular condition, hard gym light. 🎲 Surprise me / random: 40% of men's slots are HARDCORE (`core/scripts/pick_styles.py --product <id> --n <N> --audience men|women|both` tags them). Whenever recommending a cast, mood or style for men, recommend hardcore first ("💪 Hardcore shirtless" as a mood). Copy still never ties the body to the product: no before/after, body comparison, body-composition claims or "ripped/shred".

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
- **25 spoken words ran to 14.8 s** at a calm pace: budget ≤ 20 words (end card now starts at 11 s), or the last line plays over the end card.
- **GPT Image garbles the bottle's small label text** ("30 SUBLINGUAS", missing "TABS") when the bottle is small or low
  in frame; a re-roll edit didn't fix it. 4 of 5 were clean when the bottle was medium/large. Fix: ask for a large bottle,
  or composite the real render (`composite.py --product sermorelin`) instead of re-rolling.
- **Bottles land low** and their base sits behind the transparent footer row (17% of height): ask for the bottle's base
  at ≤ 78% of the canvas height.
- What worked: the round "S" tablet came out exactly right in all 6 images and the video; tablet-in-hand framing (men and
  women) looks like the winners; women's pink/beige palettes held with the orange product.

Second test, same day (10 statics 4:5 + one 720p Seedance video, after the v3/hand-off update; SESSION.md "Second test"):
- **The tablet comes out ~half the size asked** (asked 15–18% of the width, got 6–9%) in most ads, worst when a
  person or a big headline shares the frame. A 1-credit edit of the raw ("keep everything identical, make the tablet
  about TWICE as large, matching image 2") fixed it cleanly 4 times; text-size fixes work the same way.
- **"Ends above 66%"** put most products higher than yesterday, but bottles still land low; the finisher's top-logo
  shift pushes them further down. The label band stayed readable above the footer in all 10.
- **Creatify's voice check can fail on the name's first letter** ("Cermorelin"): not charged; retry with a new seed
  and a comma after the name ("Sermorelin, by Everlife.") passed. Whisper with an `initial_prompt` invents words in
  silent clips: check raw audio with `vad_filter=True` and no prompt.
- **Higgsfield can return "no response received"** on submit: check `higgsfield account transactions` before
  retrying (it wasn't charged). When it repeats, the image UPLOAD is failing (a `cost` check without `--image` works):
  pass the upload IDs of an earlier job instead of the file paths (`--image <uuid>`; IDs are in that job's
  `out/job.json` under `params.medias[].data.id`, in the order they were passed). That worked first time.
- **Video model drew a celebrity look-alike** (Stallone) from a generic "silver fox" cast: name a specific look and add
  "ordinary, non-famous face; must not resemble any celebrity" (video-prompting CAST). Rejected, not shipped.
- The `tiktok` look title-cases the header ("Sermorelin By Everlife"); bible wording is lowercase "by".
- What worked: the tablet-pull opening and the silver-fox casting came out right first time; per-ad fonts/colours
  gave 10 visibly different ads; women's teal/pink/cream/white/tan leads held.

Learned on Sermorelin GHK the same day (hand-off 2026-10-29; same models, same team, so they apply here):
- **Team review of a men's video** (Emily, Sarah, Jeremy, Justin): "start talking way sooner" (speech in the first
  second, hook by 2.5 s); the product name on screen from the start, with the logo, "this applies to every product";
  talent "too old… not ripped enough" → 42–50 "fit silver fox", hardcore fitness-model build, kept fully clothed.
- **Men's fonts:** an elegant serif with a gold italic word was "not right… men shouldn't use that font": men's headlines
  use heavy condensed / wide bold / slab / chunky sans (every men's winner uses heavy condensed caps).
- **Winners first:** picking frameworks first left most slots on Pinterest; picking ≥ 3 of 5 winners first gave the
  strongest ads.
- **Marketing Studio ignores "say this line over the hands-only shot"** and mispronounced "Sermorelin" in every take
  ("Surmergene", "Surmeasine"); "sublingual" too ("sub-single", "subliberal"). Plan the cloned-voice edit (finishing §1b).
- **Video models age actors** (asked 48–55, looked 58–60): cast a few years younger and add "fresh, well-rested look".
- **Any window shows the outdoors** (orange walls, trees): "the window NOT in frame, no outdoor view, no plants" when the
  scene's colours matter.
- **A tablet held in front of the bottle hides the product name**: "held beside the bottle, never covering its label".
- **The product lands low in GPT Image 2.5:** "ends above 72%, bottom 22% calm" came out right first time; "between 45%
  and 78%" needed 6 reposition edits in 7.
- **Women's batches all in pink look the same**: rotate the lead colour, at most one pink-led ad (image-batch §2b).

Sermorelin-specific risks to watch (expected, not yet seen):
- **The injection vial comes back.** Almost every past plain-Sermorelin ad shows the bottle next to an orange-capped vial;
  models trained on similar ads will add one → "no vial, no second container" in every prompt, check every frame.
- **Mixed up with Sermorelin GHK.** Same family name, different product: never attach a GHK render, never write GHK copy,
  check Marketing Studio picked "Sermorelin", not "Sermorelin GHK".
- **Two tablet shapes in past ads** (round "S" vs oblong "SERMORELIN"): only the confirmed render; QA the shape.
- "Hardcore fitness-model" casting drifts to shirtless, flexing or mirror-selfie bodies → "fully clothed in a fitted
  training tee, no bare torso, no flexing poses, no mirrors" for NON-hardcore slots only (HARDCORE slots: 💪 hardcore-men.md).
- Any "toned/lean" visual can turn into a body before/after → never show two states of one body.

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


## Mitansh, 2026-11-02: smeared edges (PT-141 batch 11)
- `reposition_916.py` shrank 4 raws and edge-stretched the margins: visible streaks on the sides and bottom. "why the hell are these things blurry on the edges! Who told you to do that!" → never reposition/shrink/stretch/blur; finish as-is with `--shift 0`; a colliding raw is re-rolled.

## Mitansh, 2026-11-02: one-shot 9:16 (hardcore batch)
- Raws with headlines from ~8% and bottles to ~75% can't be finished without mirror-fit, and mirror-fit smears ("trash … one shot them"). The STRICT layout block fixed 3 of 5 in one shot: top 16% "completely EMPTY, near-black, out-of-focus"; text 17–40%; product/tablet/hand 30–50% ("bottle base at 50% height"); below 55% only dark scene. Still failed when a 5-line text stack (strike-through + headline + name + 2 lines) or a 3-line headline was asked: give those a 20% empty top and product ending at 45%.
- Never send a mirror-fitted final; finish raws as-is and drop or re-roll what the finisher refuses. Also check the logo doesn't touch the headline even when the finisher passes.
- Same day, after the 3 finals: "They are holding a tablet in hand! This is soo soo redundant!" → tablet-in-hand max 20% of a batch (banner at the top of image-batch.md); the rest stage the tablet without a hand.
- Same day, round 3: the bottles landed ~65–70% and covered the safe-area proof row; Claude moved the proof to the bottom with `EVERLIFE_PROOF_AT=bottom`. Mitansh: "No NO NO! Why did it override the Meta Safezone instructions!" → NEVER change the footer placement (env or flags) to dodge a collision. The proof row stays in the safe area (ends y 1385); a product under it = re-roll with the bottle base asked at 45%.

## Mitansh, 2026-11-02: 4:5 hardcore batch (restart, Restora-style: one reference ad opened per slot)
- "TOP 14% calm" was ignored in 4 of 5 raws: headlines started at 4–8%, and the finisher's logo landed on or touching them (#3 logo on "SERMORELIN"). Fix that worked as a prompt rule: "TOP 18% COMPLETELY EMPTY … FIRST line of text starts at 19% or lower; head below 20%" (now in the §3 template).
- A headline placed at the bottom-left (copying M2's lower stack) ran under the 4:5 footer: on 4:5 every text line ends above 72%; move M2's stacked headline up under the name.
- Small two-line benefit rows rendered "Actıvity" with a broken i: ask for rows on ONE line, ≥ 4% height, and spell the risky word out letter by letter.
- QA failures are re-rolled by Claude without asking (see the banner in image-batch.md).
- (2026-11-03) No more rating: post every finished ad to Ad Review (`core/ad-review/AD-REVIEW.md` §4); reviewers flag losers.
