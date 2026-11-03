# Lessons already paid for (read every session)

No GHK cream batch has been made yet (skill built 2026-11-02). The general lessons come from Restora-Z, Sermorelin GHK, plain
Sermorelin, PT-141 and Lovara (Oct 2026) and from the creative team's written feedback. Add GHK cream lessons at the bottom.

What the creative lead / team rejected, and why:
- **Reusing lines across ads:** "redundant… do better". Every ad gets its own angle, header, end card and CTA. Use the copy log.
- **Seedance "UGC"** (camera following a person, hands-only ASMR at 480p): "nowhere close to realistic UGC humans". Realistic humans → Marketing Studio UGC.
- **Lip-sync on a still image:** "Bad!" Never for UGC.
- **Split-screen layouts / text boxes over faces:** keep full-frame video and light, box-free overlays.
- **Surreal/cinematic built from scratch:** "quality was trash". Start from real human moments and winners; 720p for hero pieces.
- **Busy direct-response statics** (all-caps condensed, chips everywhere, badge stacks): 4/10. Aim for a modern brand look.
- **Layout variety** (Berna): vary headline placement, product angle and scale per ad, not just the scenery.
- **Fonts and colours repeat** (Berna, Michael): `image-batch.md` §2b, a different pairing and accent per ad.
- **Three benefits mandatory when a benefits section exists** (Berna).
- **Product name split** ("REST / ORA-Z"): the name on ONE line (or "GHK" / "PEPTIDE CREAM" stacked), never hyphen-broken.
- **Logo:** never ask the image model for one; the finisher adds the real logo at the top.
- **Video:** benefit frames ≥ 2.5 s, fades over hard cuts, more air on the end card, talent fresh-looking, a 1-credit preview still
  before any video (Stephen, Michael).

Priestley's image review rules (2026-10-29, all products):
- **Images never say "by Everlife"**; the product name runs big (a small name line reads as "no product name").
- **A different person in every ad** (one pasted casting line gave the same face 5 times): own casting per ad.
- **Ordinary, non-famous face** in every cast line: a generic "silver fox" video cast came back as a Sylvester Stallone look-alike
  (rejected, 67.5 credits) and the next was blocked by Higgsfield's IP check. Cast videos from a picked preview still.

**Mitansh on people statics (PT-141, 2026-10-28):** the GPT Image "smiling person + bottle + three lines + icons" formula was "generic
trash… AI slop… premium means look at Hims / Ro"; product-only versions were "amazing". Start GHK cream statics **product-only** (ONE
sentence-case headline, one tiny line, the bottle as an object on real material with hard light and a real shadow, monochrome
harmony in blush/tan/beige; `core/references/static-refs/13_Premium_DTC/`), and test people in 2–3 shots before a whole batch.

Generation traps:
- Selfie / front-camera prompts **mirror the label** → `--mirror-until`.
- Marketing Studio may render a **second phone** → "the filming phone is never visible"; fix with `--zoom 1.2`.
- Props with labels come out **garbled** → plain, unbranded props.
- Model voices mangle product names → TTS line or cloned-voice line; keep spoken product names ≤ 2.
- Whisper misspells product names → hand-fix captions ("GHK Peptide Cream").
- GPT Image 2.5 places the product LOWER than asked → ask high ("ends above 66%"); 9:16 from the approved 4:5 (`compose916.py`).
- Higgsfield "no response received" on submit = the upload failing → upload first and pass the IDs (not charged when it fails).
- Lovara batch 1: the model can ignore "text above 72%" and finish_batch does NOT refuse that at 4:5 (only 9:16 checks): LOOK at
  every final. Finish with `--shift 0` when the raw already has the top 14% calm.

GHK cream risks to watch (expected, not yet seen):
- **Naming:** the model (and whisper) will reach for "GHK-Cu" or "copper peptide", the words the skincare world uses. Every TEXT
  string, VO and caption says "GHK Peptide Cream" (H2: "GHK-Cu Cream" as the name only); QA greps for "copper" and "-Cu".
- **Invented strength:** the asset library also has 0.5% and 2% bottles; the model may print a percentage on the label. The render
  used has none: reject any label with a number other than 30G.
- **Slim bottle reads small:** a 1:4 pump next to a headline shrinks to a sliver. Stage it upright and tall, or on its side, and
  check the label is legible; the video end card draws it small (look at the frame).
- **Skincare clichés:** before/after faces, split-face, magnifier close-ups of pores or wrinkles, droppers, serum jars, "glass skin"
  gloss. All out (global Hard NOs + product truth).
- **Palette drift:** "warm golden hour" grades turn orange, and spa props bring green leaves and citrus. Say "no orange, no green"
  in every prompt and check every frame.
- **Fitness drift:** "beauty and fitness" can drift to gym bodies. Lean and fit, everyday activewear at most; never muscular or posed.
- **The cream itself:** its colour and texture aren't on file. Keep it off camera until the team confirms what it looks like.

Compliance traps:
- Rx is never shared: only the person's OWN pharmacy delivery.
- Reference ads use $ prices, "Breaking", first person, old proof numbers, "clinically proven", "erase wrinkles". Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- **Disclaimer is PROVISIONAL** (standard ad disclaimer, bible says "Disclaimer pending"): every SESSION.md says "provisional
  disclaimer: Jeremy to confirm". The global AI-disclosure line differs from it: open question for Jeremy.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- 9:16: proof row inside the Reels safe area (ends at y 1385), disclaimer alone at the very bottom (`"disclaimer_at": "bottom"`).
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.

## Shared creative system (2026-10-29)
`core/references/creative-system.md`: structural variety, article slot, product-angle rotation, named typefaces, own palette, hero
large and real, CTA string + QA, real logo/label composited, footer unfade, 9:16 built from the approved 4:5. Read it before every
batch table; tools: `reposition_916.py`, `unfade_cta.py`, `logo_in_box.py`, `compose916.py`.

## GHK cream batches
(none yet: the first 4-image test needs approval, ~4 Creatify credits)
- 2026-11-03: the bible now carries the standard disclaimer for GHK-Cu Cream (same text as product.json): the provisional flag is retired.
