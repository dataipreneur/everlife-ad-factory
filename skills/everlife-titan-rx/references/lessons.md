# Lessons already paid for (read every session)

No Titan-Rx ads have been made yet (skill built 2026-11-02 from the Spark skill). The general lessons were carried over from
Spark / PT-141: they come from Restora-Z, Sermorelin GHK, PT-141, Spark and Lovara (Oct 2026) and from the creative team's written
feedback (Stephen, Berna, Michael, Mitansh). Where they say "PT-141", "Spark", "the spray" or "the tablet", they describe those
products' batches; Titan-Rx has one form (an oral capsule, once daily). Add Titan-Rx lessons at the bottom.

What the creative lead rejected, and why:
- **Reusing lines across ads:** "redundant… do better". Every ad gets its own angle, header, end card and CTA. Use the copy log.
- **Seedance "UGC"** (camera following a person, hands-only ASMR at 480p): "nowhere close to realistic UGC humans". Realistic humans → Marketing Studio UGC.
- **Lip-sync on a still image:** "Bad!" Never for UGC.
- **Split-screen layouts / text boxes over faces:** keep full-frame video and light, box-free overlays; proof at the bottom on a transparent background.
- **A weak storyline after a strong hook:** the hook has to pay off in a human story.
- **Surreal/cinematic built from scratch:** "quality was trash". Start from real human moments and winners; keep people close and expressive; 720p for hero pieces.
- **Busy direct-response statics** (all-caps condensed, chips everywhere, badge stacks): 4/10. Aim for a modern brand look.

Creative team feedback on the Restora-Z factory (2026-10-28) — fix these by default here:
- **Layout variety:** "the structural composition remained essentially locked in place" (Berna). Vary headline placement, product angle and
  scale per ad, not just the scenery. Product angles: ask for a different angle/tilt per ad; never the identical pose five times.
- **Fonts and colours repeat** (Berna, Michael: "more header styles"): `image-batch.md` §2b, a different pairing and accent per ad.
- **Three benefits mandatory when a benefits section exists** (Berna: "only 2 points instead of the mandatory 3").
- **Headers split unnaturally** ("REST / ORA-Z"): ask for the product name on ONE line, never hyphen-broken.
- **Logo:** at the TOP, 311 px wide (`finish_batch.py`; was 200, then +35% and +15% more per Mitansh 2026-10-28; all finishers scaled the same); never ask the image model for a logo ("small everlife logos" came out wrong).
- **Pills replaced by orbs/icons; pill too small; label flat on an angled bottle:** "use the attached capsule reference exactly", "capsule large and
  close", "label follows the bottle's perspective".
- **Safe zones on 9:16** (Stephen, Berna): compose for them; the finishers refuse violations. 9:16 headers must be bigger than 4:5 (Michael).
- **People in statics:** Michael: product-only works for Restora, but PT-141's category convention is a tasteful woman → use people in ~half
  the batch (shoulder-up, clothed, candid, 30–55, no beds).
- **Video:** transitions too fast and benefits fade too early (Stephen) → hold benefit frames ≥ 2.5 s; prefer fades over hard cuts (Michael);
  end card too cramped (Michael) → more air; talent "fresher looking" (Michael) → 30–55 for PT-141, well-rested, real; pronunciation of
  drug names → write the pronunciation ("P-T one-forty-one"); preview the still before the video (Stephen) → always show a 1-credit
  static of the character/scene first.

Generation traps:
- Selfie / front-camera prompts **mirror the label** → `--mirror-until`.
- Marketing Studio may render a **second phone** → "the filming phone is never visible"; fix with `--zoom 1.2`.
- Props with labels come out **garbled** → plain, unbranded props.
- Two pills in a palm read as a two-pill dose → "exactly ONE capsule".
- Model voices mangle product names → write the pronunciation; keep spoken product names ≤ 2.
- Whisper misspells product names → hand-fix captions ("PT-141").
- Long scripts run under the end card → ≤ 35 spoken words, finishing by ~12 s.
- GPT Image 2.5 on Creatify places the product LOWER than asked → one cheap reposition edit on the raw.
- Cropping 4:5 to 9:16 puts the footer on the product → generate 9:16 natively.

Titan-Rx-specific risks to watch (expected, not yet seen):
- **"Rugged gym-goer" drifts to bodybuilders, bare torsos and flexing** → every prompt: "clothed (training tee / hoodie / flannel),
  shoulder-up or waist-up, fit and strong but not a bodybuilder, not posing, no bare torso"; 40–65, grey, real hands.
- **"Men's performance" drifts to supplement-bro hype**: flames, lightning, rockets, "MAX", red-and-black gas-station looks → the
  bottle's own matte black + chrome reads premium; one red accent (the chevron) at most; no fire, no explosions.
- **Any "intimacy" prompt drifts to beds, couples in bed, lingerie** → name the setting (gym, garage, workshop, kitchen, terrace)
  and say "fully clothed, no bed, no bedroom, shoulder-up". The partner lines ("Be Ready When She Is Ready") pull hardest.
- **The chrome capsule reflects the scene** (warm light turns it gold, dark scenes turn it black) → QA it still reads silver/chrome
  with the TITAN-RX print legible; one capsule, never a handful; never two capsules read as a dose.
- **The label's own text** ("3-IN-1 INTIMACY SUPPORT FOR MEN", "TADALAFIL + VARDENAFIL + L-ARGININE", "30 CAPSULES") is fine in the
  picture; our copy never types "intimacy support", a count or an ingredient claim unless the pre-screen says ✅.
- **"Once-daily" drifts to timing copy** ("ready in 30 minutes", "all day", "tonight") → only the bible line "Once-Daily, No Timing
  Required"; never a number of hours or minutes. Tadalafil's "all-day readiness" is ⚠ Jeremy.
- **Offer creep**: reference pins and old Everlife ads carry "% off" and prices → no offer until "Save up to 49%" is verified.
- **Spelling**: the bible writes Titan-rx / Titan-Rx / Titan-RX / TitanRx / Titan Rx → creative uses "Titan-Rx" / "TITAN-RX"
  (Justin to confirm); never hyphen-broken across two lines.

Compliance traps:
- Rx is never shared: only the person's OWN pharmacy delivery.
- Reference ads in the library use $ prices, "Breaking", first person, old proof numbers, "ED", "Viagra". Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- Disclaimer stays the bible's verbatim text. The global AI-disclosure line differs from it: open question for Jeremy.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.

## Creative lead, 2026-10-28: logo at the top, and stop repeating the same type
- **The Everlife logo sits at the TOP of every static**, never in the footer (`finish_batch.py` does it; the prompt keeps a calm top 12%).
- **Fonts and colours must change from ad to ad.** `image-batch.md` §2b: a different pairing and accent for every ad.

## Skeptical Dave (target-buyer critique of the first PT-141 video, 2026-10-28)
- Two forms in one ad confused him in 2 seconds → **one form per ad**.
- "Desire support" three times in five seconds read as robot copy dodging the rules → one claim per beat, no synonym stacking.
- "Brain-based" and "Non-hormonal" meant nothing without a plain line → pair every claim word with the bible's plain sentence.
- A cartoon selling a prescription felt fake → real render, real pharmacy proof, price as "Save up to 23%".
- "On your timing" was vague → show the unplanned moment; never a number of minutes.
- Full personas and the 5-point rubric: `personas.md`. Run it on every concept before the approval question.

## Mitansh, 2026-10-28, after PT-141 image batch 1 (all five rejected)
- "Generic trash… AI slop… premium means look at Hims / Ro." The person ads were "pathetic". Causes: the §3 prompt template asks for the DTC-stock formula (smiling person + bottle + three supporting lines + icons + "marble ledge"). Fix: for PT-141 statics use `core/references/static-refs/13_Premium_DTC/README.md` codes: ONE sentence-case headline, one tiny line, product shot as an object on real material with hard light and a real shadow, monochrome harmony, people candid and off-camera. No bullets, no icons, no tiles.
- Show 2–3 test shots in a new direction before a batch; never five of the same recipe.
- **People in statics, round 2 (same day):** the Hims-style candid-off-camera versions (batch 2 D + E, GPT Image 2.5) were still "trash" for Mitansh. Product-only A/B/C were "amazing". Until fixed, PT-141 statics ship **product-only**. Proposed (not yet approved, no credits spent): shoot people with Higgsfield Soul 2.0 (~1 credit, 9:16, style "Neutral pastel film" / "Muted cool film" / "Warm contrast film"), cast against type (receding hairline, glasses, grey, freckles, no makeup, real clothes, mid-action in a real room), then build the panel ad in code (photo + flat panel + headline in our fonts + the real spray render + finish_batch) so GPT Image never renders a face.
- **Footer inside the Meta safe area, never at the bottom (Mitansh, 2026-10-29).** A live Reels screenshot
  (`core/references/safe-zones/reels_placement_2026-10-29.jpg`) showed our bottom-anchored proof footer under the
  "Learn more" button and caption. The toolkit is back in safe mode: the 9:16 footer ends at y 1385, so the raw keeps
  everything in its top ~52% (LAYOUT block) and `finish_batch.py` refuses when content runs under the footer. Old raws
  composed to the bottom need one reposition edit; an automatic scale-down-and-extend was tried and rejected.

## Shared creative system (2026-10-29)
The creative team member's Restora-Z improvements were distilled into `core/references/creative-system.md` (product-agnostic:
structural variety, article slot, product-angle rotation, named typefaces, own palette, hero ≥35% and real, CTA string + QA, real
logo/label composited, footer unfade, 9:16 built from the approved 4:5). Read it before every batch table; tools: `reposition_916.py`,
`unfade_cta.py`, `logo_in_box.py`, `compose916.py`, `finish_batch.py --logo-w 40%`. Nothing lives only in an output folder.

## Carried from Spark / Lovara (2026-10-30), still true for Titan-Rx
- Lovara batch-1: the 4:5 LAYOUT block worked 3 of 4; one raw put its benefit lines at 83-90%, under the footer, and finish_batch did
  NOT refuse it (only 9:16 checks). Look at every final.
- Four ads of the same tone in a row read samey (Priestley, 2026-10-30): Titan-Rx defaults dark (the bottle's matte black + chrome),
  so put at least one warm/light ad in every batch of 4.
- Spark batch 1-2: native 9:16 failed 4/4 on safe zones; the 4:5 → compose916 → finish_batch --fit trusted route passed 4/4: make
  9:16 that way. At 4:5, 2 of 4 raws put the bottle under the proof row (paid 1-credit fix each): ask for the bottle base at 62%.
- Spark test batch: the pill was smaller than the bottle in 4/4 → ask for the capsule "at least 25% of the canvas width and larger
  than the bottle"; fix with a 1-credit "twice as large" edit.

## Titan-Rx (from 2026-11-02)
- Skill built; no batches yet. First test: 4 images (~4 Creatify credits), approved with the cost shown.
- End card (smoke test, 2026-11-02): the capsule is wide and horizontal, so Lovara's 0.36 (tall capsule) made it tiny; at 1.0 it
  touched the bottle's label in `default`. `pill_end_scale` = 0.85: capsule about as wide as the bottle, headline and label clear in
  `default` and `tiktok`. `tiktok` title-cases headlines: "It's" / "She'll" are in `keep_case` so they don't become "It'S".
