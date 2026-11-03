# Lessons already paid for (read every session)

> **Epithalon (adapted 2026-11-02 from MOTS-c, itself from BPC-157):** adults 40–65, men and women; calm, sun-lit healthy aging, never age reversal; no sleep or overnight words or images (product Hard NO); the vial is a still object. If any MOTS-c, BPC-157, endurance or gym wording remains, it describes the template product, not Epithalon: `direction.md` and `product-bible.md` win.


The general lessons below come from Restora-Z, Sermorelin GHK, PT-141 and BPC-157 (the template this skill was copied from) and
from the creative team's written feedback; MOTS-c (the template) added its vial lessons. Add Epithalon lessons in the Epithalon section at the bottom.

What the creative lead rejected, and why:
- **Reusing lines across ads:** "redundant… do better". Every ad gets its own angle, header, end card and CTA. Use the copy log.
- **Seedance "UGC"** (camera following a person, hands-only ASMR at 480p): "nowhere close to realistic UGC humans". Realistic humans → Marketing Studio UGC.
- **Lip-sync on a still image:** "Bad!" Never for UGC.
- **Split-screen layouts / text boxes over faces:** keep full-frame video and light, box-free overlays; proof inside the safe area on a transparent background.
- **Busy direct-response statics** (chips everywhere, badge stacks): 4/10. Aim for a modern brand look.
- **"Generic AI slop" (PT-141 batch 1):** premium means Hims / Ro. `core/references/static-refs/13_Premium_DTC/README.md` codes: ONE
  sentence-case headline, one tiny line, product as an object on real material with hard light, monochrome harmony. Show 2–3 test
  shots in a new direction before a batch; never five of the same recipe.
- **People rendered by GPT Image were "trash"** for PT-141 (twice): those were candid, smiling faces. Hardcore gym bodies in hard light
  are a different ask (the Sermorelin male winners M2/M5 were exactly that; never for Epithalon, see direction.md). Still: show ONE test shot first.

Creative team feedback (2026-10-28), fixed by default here:
- **Layout variety:** vary headline placement, product angle and scale per ad, not just the scenery.
- **Fonts and colours repeat:** `image-batch.md` §2b, a different pairing and accent per ad.
- **Three benefits when a benefits section exists** (never two).
- **Headers split unnaturally:** product name on ONE line, never hyphen-broken ("Epithalon" stays whole).
- **Logo at the TOP**, 311 px wide, laid by the finisher; never ask the image model for a logo.
- **Safe zones on 9:16:** compose for them; the finishers refuse violations. Footer ends at y 1385 (2026-10-29).
- **Video:** benefit frames ≥ 2.5 s; fades over hard cuts; end card needs air; talent well-rested and real; write the pronunciation
  ("Epithalon" = "eh-PITH-uh-lon", to confirm with Justin); preview the still before the video.

Generation traps:
- Selfie / front-camera prompts **mirror the label** → `--mirror-until`.
- Marketing Studio may render a **second phone** → "the filming phone is never visible"; fix with `--zoom 1.2`.
- Props with labels come out **garbled** → plain, unbranded props.
- GPT Image 2.5 on Creatify places the product 8–15% LOWER than asked → ask for the lowest element at 40%; one cheap reposition edit if needed.
- Cropping 4:5 to 9:16 puts the footer on the product → generate 9:16 natively.
- Model voices mangle product names → write the pronunciation; keep spoken product names ≤ 2.
- Whisper misspells product names → hand-fix captions ("Epithalon"; it writes "Epitalon" / "Epithelon").
- Long scripts run under the end card → ≤ 35 spoken words, finishing by ~12 s.

Epithalon-specific risks to watch (written 2026-11-02; MOTS-c's vial lessons kept where they apply):
- **The bible page contradicts itself on sleep.** "Supports Restorative Sleep", "Supports Healthy Sleep-Wake Cycles" and the
  "sleep quality" audience line sit on a page whose Hard NO is "No sleep or overnight claims" (DSIP's territory). The Hard NO wins:
  all ❌, and no sleep imagery either (beds, pillows, night, waking up, alarm clocks, yawns). Open question for Justin.
- **Spelling: "Epithalon" (bible, all copy) vs "EPITALON" (the vial label).** Never edit, redraw or "correct" the label; QA that the
  generated label still reads EPITALON; `keep_case` holds both. Open question for Justin.
- **Aging copy drifts to reversal** ("anti-aging", "younger", "turn back the clock", "reverse") and to medical DNA/telomere claims:
  only the ✅ lines; "Supports DNA + Cellular Health" is ⚠ (OK + Jeremy). No before/after, younger-vs-older or mirror images.
- **Only two ✅ benefits and no approved headline:** the name + one ✅ line carries most ads; the third row of a benefits layout is
  "Doctor Prescribed" unless B3 is OK'd. No offer ([PLACEHOLDER]).
- **Any "peptide vial" prompt invites a syringe, needle, pen or droplets** (MOTS-c lesson): every prompt says "the vial is a still
  object; no syringe, needle, pen, dropper, droplets or injecting anywhere" and QA checks every frame. One syringe = reject.
- **Only ONE product image exists (the vial)**, from a 592×1280 screenshot: the model must never invent capsules or pills; a larger
  render is on the wish list (`assets/RENDERS.md`). Copy never states a strength or volume.
- **The GHK-Cu/Epithalon stack is another product:** never its lines, never "GHK-Cu" in creative.

Compliance traps:
- Disclaimer = the standard ad disclaimer, PROVISIONAL (2026-11-02, same text as MOTS-c); Jeremy to confirm.
- Reference ads in the library use $ prices, "Breaking", first person, old proof numbers, needles. Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- "GHK-Cu" never appears in any creative (global Hard NO); MOTS-c, NAD+, GLP-1, DSIP, the stacks and the GHK-Cu/Epithalon stack are separate products: never their claims or vials.

## Tool lessons from BPC-157 batch 1 (2026-10-29, Nano Banana Pro; still valid for Epithalon)
- **Paid reposition edits are dead.** Nano Banana Pro ignored "scale down and move up" on 5/5 edits (7.5 credits), removed only the
  logo/bucket, and once swapped the real vial for a white generic one. Fix = `reposition_916.py` (0 credits) + finisher.
- **Show the raws before ANY fix spend.** Mitansh: "No! First show them to me!", then "I can't waste this much time": contact sheet,
  his call, then fix. "One automatic re-roll" never means an automatic spend. And keep it FAST: one question round, defaults, go.
- **Local render composite beats an AI label fix:** `--composite bpc157_vial.png x0 y0 x1 y1` over the generated vial matched perfectly (Epithalon: `epithalon_bottle.png`).
- Models draw their own EVERLIFE wordmark despite "no logos": crop it locally, never pay to remove it.
- SUPERSEDED the same day: the blurred-plate lower half is no longer the 9:16 look; Mitansh's "0 blurring" rule (image-batch.md) = edge fill.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.

## Mitansh, 2026-10-29: vial images must look very premium
- Every vial-hero image or video borrows its staging from `vial-refs/` (large, tilted, label to camera, real material, hard
  directional light, monochrome harmony with the vial's teal label, lots of air). Never a syringe, never a grid of vials, never flat colour.
  One test shot before a batch.

## Shared creative system (2026-10-29)
The creative team member's Restora-Z improvements were distilled into `core/references/creative-system.md` (product-agnostic:
structural variety, article slot, product-angle rotation, named typefaces, own palette, hero ≥35% and real, CTA string + QA, real
logo/label composited, footer unfade, 9:16 built from the approved 4:5). Read it before every batch table; tools: `reposition_916.py`,
`unfade_cta.py`, `logo_in_box.py`, `compose916.py`, `finish_batch.py --logo-w 40%`. Nothing lives only in an output folder.

## Lessons from BPC-157 batch 5 (2026-10-29, GPT Image 2.5, Men, product only) — Mitansh: "Amazing!" (layout and tool lessons
apply; the hardcore-gym scenes do NOT: Epithalon scenes come from direction.md)
- The recipe that pleased: Problem → solution angle, product-only hardcore scenes from the scene bank (loaded bar + plain shaker,
  boxing apron, 5 a.m. kitchen article page, tailgate gym bag), ONE headline + ONE quick-hit line, a different structure and
  typeface per slot (stencil split / slab stacked question / editorial-serif article / wide-extended billboard). 4/4 strings exact,
  4/4 labels clean, 0 syringes. Two setup rounds, one table, generate.
- GPT Image 2.5 overshoots most on "scene fills the frame" structures (article page caption at 70%, overhead vial at 75%);
  reposition_916.py --fill reflect fixed both at 0 credits and Mitansh approved the result. Split and stacked layouts landed as-is.
- A plain, unlabelled prop (grey shaker) as "the old way" renders clean; keep props unbranded.

## Inherited from MOTS-c test-1 (2026-10-30; tool/layout lessons, valid for any vial product)
- **Test-1 (2026-10-30, GPT Image 2.5, 4 ads, 4:5 + native 9:16), 12 credits:** 4/4 strings exact, 4/4 labels clean, 0 needles.
  - 4:5: 3/4 raws put the CTA in the bottom 18% even when told not to: the finisher fades it under the footer and does NOT
    refuse at 4:5. Look at every final; a 1-credit "more room: top 11% and bottom 20% empty" edit worked 2/2.
  - 9:16: asked for the lowest element at 58%, got 72–80% (4/4). Ask for 52% and a compact layout (rows beside the vial).
    Article-style text ran into the Reels side bands: say "central 70% of the width" and check with the safezone-sides finisher.
  - Free local fixes: shrink + edge fill only on plain backgrounds (paper, pale stone); it streaks glow and photo scenes.
    A small shift (≤ 120 px) clears the logo or a side band. `unfade_cta.py` restores a CTA the footer gradient fades.

## Epithalon (from 2026-11-02)
- Built 2026-11-02 from everlife-mots-c (vial). No ads, winners or reference ads yet: update this line after the first batch.
- Disclaimer pending in the bible: product.json carries the PROVISIONAL standard text; Jeremy to confirm.
- Open for Justin: the sleep contradiction (Hard NO wins), the spelling (Epithalon vs the label's EPITALON), the offer and landing
  page ([PLACEHOLDER]), the four ⏳ headlines, the VO pronunciation.
- 2026-11-03: the bible now carries the standard disclaimer for this product (same text as product.json): the provisional flag is retired.
