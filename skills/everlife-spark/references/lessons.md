# Lessons already paid for (read every session)

No Spark ads have been made with this skill yet. The lessons below were carried over from the PT-141 skill (Spark's template):
they come from Restora-Z, Sermorelin GHK and PT-141 (Oct 2026) and from the creative team's written feedback (Stephen, Berna,
Michael, Mitansh). Where they say "PT-141" or "the spray", they describe that product's batches; Spark has one form (sublingual
tablet). Add Spark lessons at the bottom.

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
- **Tablets replaced by orbs/icons; tablet too small; label flat on an angled bottle:** "use the attached tablet exactly", "tablet large and
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
- Two tablets in a palm read as a two-tablet dose → "exactly ONE tablet". Never show the tablet with the nasal spray.
- Model voices mangle product names → write the pronunciation; keep spoken product names ≤ 2.
- Whisper misspells product names → hand-fix captions ("PT-141").
- Long scripts run under the end card → ≤ 35 spoken words, finishing by ~12 s.
- GPT Image 2.5 on Creatify places the product LOWER than asked → one cheap reposition edit on the raw.
- Cropping 4:5 to 9:16 puts the footer on the product → generate 9:16 natively.

PT-141-specific risks to watch (expected, not yet seen):
- Any "intimacy" prompt drifts to **beds, lingerie, bodies, couples in bed** → every prompt names the setting (kitchen, hallway, terrace,
  car, café, bathroom counter) and says "fully clothed, daytime, no bed, no bedroom, shoulder-up".
- "Attractive woman" drifts to glamour/objectifying shots → "candid, laughing or calm, eyes to camera or mid-moment, head and shoulders".
- Image models invent **syringes, vials, pills in hands** for peptide scenes → "no needles, syringes or vials"; the spray is held by the
  bottle, never sprayed on camera; the tablet sits on a surface.
- The label on the sublingual bottle reads "PT 141" (no hyphen) and prints "ON-DEMAND INTIMACY SUPPORT FOR MEN & WOMEN": that text is the
  product's own label, fine in the picture; our copy still never says "intimacy support" as a claim unless it's on the bible page.
- "Desire" copy drifts to outcome promises ("tonight", "guaranteed", "in minutes") → mechanism first, "supports", no timing claims.

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

## Spark (from 2026-10-30)
- Lovara batch-1 (2026-10-30): the 4:5 LAYOUT block worked 3 of 4; one raw put its benefit lines at 83-90%, under the footer, and finish_batch did NOT refuse it (only 9:16 checks). Look at every final.
- Four light-coloured ads in a row read samey (Priestley, 2026-10-30): at least one dark ad per batch; the black + rose-gold bottle suits dark stone and warm brass.
- Never tie a benefit to one ingredient (bible Hard NO): the three ingredients only ever appear together.
- Spark batch 1-2 (2026-10-30, 14 credits): native 9:16 failed 4/4 on safe zones (bottom, side bands, logo); the old finisher passed 3 of them (fix: branch safezone-sides). The 4:5 → compose916 → finish_batch --fit trusted route passed 4/4: make 9:16 that way. At 4:5, 2 of 4 raws put the bottle under the proof row (paid 1-credit fix each): ask for the bottle base at 62% and check every final.
