# Lessons already paid for (read every session)

> **Wolverine Stack (adapted 2026-10-30 from BPC-157):** audience is active men 25–55 only (ignore any women's notes), cast 25–55 (not only bodybuilders), fighting imagery fine without blood or gore, no animal death; "Wolverine Stack" is the brand name in every asset. Where this file says BPC-157 it describes the template product's history, not Wolverine Stack facts.


No Wolverine Stack ads have been made yet. The lessons below come from BPC-157 (2026-10-29). The general ones come from Restora-Z, Sermorelin GHK and PT-141 and
from the creative team's written feedback. Add Wolverine Stack lessons at the bottom.

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
  are a different ask (the Sermorelin male winners M2/M5 were exactly that and performed). Still: show ONE test shot first.

Creative team feedback (2026-10-28), fixed by default here:
- **Layout variety:** vary headline placement, product angle and scale per ad, not just the scenery.
- **Fonts and colours repeat:** `image-batch.md` §2b, a different pairing and accent per ad.
- **Three benefits when a benefits section exists** (never two).
- **Headers split unnaturally:** product name on ONE line, never hyphen-broken ("Wolverine Stack" on one line; "BPC-157" and "TB-500" stay whole).
- **Logo at the TOP**, 311 px wide, laid by the finisher; never ask the image model for a logo.
- **Safe zones on 9:16:** compose for them; the finishers refuse violations. Footer ends at y 1385 (2026-10-29).
- **Video:** benefit frames ≥ 2.5 s; fades over hard cuts; end card needs air; talent well-rested and real; write the pronunciation
  ("Wolverine Stack"; ingredients, if spoken: "B-P-C one-fifty-seven", "T-B five hundred"); preview the still before the video.

Generation traps:
- Selfie / front-camera prompts **mirror the label** → `--mirror-until`.
- Marketing Studio may render a **second phone** → "the filming phone is never visible"; fix with `--zoom 1.2`.
- Props with labels come out **garbled** → plain, unbranded props.
- GPT Image 2.5 on Creatify places the product 8–15% LOWER than asked → ask for the lowest element at 40%; one cheap reposition edit if needed.
- Cropping 4:5 to 9:16 puts the footer on the product → generate 9:16 natively.
- Model voices mangle product names → write the pronunciation; keep spoken product names ≤ 2.
- Whisper misspells product names → hand-fix captions ("Wolverine Stack", "BPC-157", "TB-500").
- Long scripts run under the end card → ≤ 35 spoken words, finishing by ~12 s.

Wolverine Stack risks to watch (carried from BPC-157, an ingredient and the template; facts re-checked 2026-11-02):
- **Any "peptide vial" prompt invites a syringe, needle, pen or droplets.** Every prompt says "the vial is a still object; no syringe,
  needle, pen, dropper, droplets or injecting anywhere" and QA checks every frame. One syringe = reject, no exceptions (global Hard NO).
- **"Recovery" copy drifts to cure talk** ("heals", "repairs", "reduces inflammation", "pain"): only the lines in `product-bible.md`
  (✅ benefits; ⏳ / ⚠ headlines with an OK, flagged for Jeremy). there is no ✅ repair line ("Supports Tissue Repair" is ⚠ Jeremy;
  the page says "No direct claims"). "Supports Healthy Inflammatory Balance" is held (KPV's benefit; asked Justin).
- **Men must look HARDCORE (Mitansh, 2026-10-29: "extremely masculine, gym, barbells, bodybuilders with tattoos")**: the Sermorelin
  "not bodybuilders" rule does not apply here. Use `mens-direction.md`; the only body rules left are no before/after, no body comparison,
  no body-composition words in copy.
- **Only ONE product image exists (the vial)**: the model must never invent capsules or pills.
- **The vial label reads BPC-157 + TB-500 · 3MG/3MG/ML · 5ML** (asset library `VIALS/WOLVERINE/`, confirmed 2026-10-30): a squat
  vial, matte black label with gold type, grey cap. Copy never states a strength or volume.
- **Offer "Save up to 39%" is PROVISIONAL** (landing page only; Jeremy to confirm): exact string, never a $ price.
- **Men 25–55 only** (bible): ignore any women's notes carried from the template.
- **No landing page on file** (bible: [PLACEHOLDER]): renders verified against the asset library only; re-check when the page ships.

Compliance traps:
- Disclaimer = the Wolverine Stack ad disclaimer from the bible, verbatim in product.json; Jeremy still signs off.
- Reference ads in the library use $ prices, "Breaking", first person, old proof numbers, needles. Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- "GHK-Cu" never appears in any creative (global Hard NO). The Spartan Stack, and BPC-157 or TB-500 alone, are separate products:
  never their claims or vials.

## BPC-157 batch 1 (2026-10-29, Nano Banana Pro, Men; the closest product: these lessons apply to the Wolverine Stack)
- **Paid reposition edits are dead.** Nano Banana Pro ignored "scale down and move up" on 5/5 edits (7.5 credits), removed only the
  logo/bucket, and once swapped the real vial for a white generic one. Fix = `reposition_916.py` (0 credits) + finisher.
- **Show the raws before ANY fix spend.** Mitansh: "No! First show them to me!", then "I can't waste this much time": contact sheet,
  his call, then fix. "One automatic re-roll" never means an automatic spend. And keep it FAST: one question round, defaults, go.
- **Local render composite beats an AI label fix:** `--composite bpc157_vial.png x0 y0 x1 y1` over the generated vial matched perfectly (Wolverine: `wolverine_bottle.png`).
- Models draw their own EVERLIFE wordmark despite "no logos": crop it locally, never pay to remove it.
- SUPERSEDED the same day: the blurred-plate lower half is no longer the 9:16 look; Mitansh's "0 blurring" rule (image-batch.md) = edge fill.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.

## Mitansh, 2026-10-29: vial images must look very premium
- Every vial-hero image or video borrows its staging from `vial-refs/` (large, tilted, label to camera, real material, hard
  directional light, monochrome harmony with the matte-black and gold label, lots of air). Never a syringe, never a grid of vials, never flat colour.
  One test shot before a batch.

## Shared creative system (2026-10-29)
The creative team member's Restora-Z improvements were distilled into `core/references/creative-system.md` (product-agnostic:
structural variety, article slot, product-angle rotation, named typefaces, own palette, hero ≥35% and real, CTA string + QA, real
logo/label composited, footer unfade, 9:16 built from the approved 4:5). Read it before every batch table; tools: `reposition_916.py`,
`unfade_cta.py`, `logo_in_box.py`, `compose916.py`, `finish_batch.py --logo-w 40%`. Nothing lives only in an output folder.

## BPC-157 batch 5 (2026-10-29, GPT Image 2.5, Men, product only) — Mitansh: "Amazing!"
- The recipe that pleased: Problem → solution angle, product-only hardcore scenes from the scene bank (loaded bar + plain shaker,
  boxing apron, 5 a.m. kitchen article page, tailgate gym bag), ONE headline + ONE quick-hit line, a different structure and
  typeface per slot (stencil split / slab stacked question / editorial-serif article / wide-extended billboard). 4/4 strings exact,
  4/4 labels clean, 0 syringes. Two setup rounds, one table, generate.
- GPT Image 2.5 overshoots most on "scene fills the frame" structures (article page caption at 70%, overhead vial at 75%);
  reposition_916.py --fill reflect fixed both at 0 credits and Mitansh approved the result. Split and stacked layouts landed as-is.
- A plain, unlabelled prop (grey shaker) as "the old way" renders clean; keep props unbranded.

## Wolverine Stack (from 2026-10-30)
- Resolved 2026-11-02: Justin un-swapped the bible's Spartan / Wolverine pages; the vial labels were right all along.
- Test 1 (2026-10-30, 4 ads, shared lines only): 2 of 4 had the CTA under or at the footer at 4:5; the finisher does not catch it at 4:5: look at every final.
- Lovara batch-1 (2026-10-30): at 4:5 `finish_batch.py` does not refuse text under the footer: look at every final.


## Mitansh, 2026-11-02: smeared edges (PT-141 batch 11)
- `reposition_916.py` shrank 4 raws and edge-stretched the margins: visible streaks on the sides and bottom. "why the hell are these things blurry on the edges! Who told you to do that!" → never reposition/shrink/stretch/blur; finish as-is with `--shift 0`; a colliding raw is re-rolled.

## Wolverine V1 (2026-11-02): avatar presenter via Seedance on Creatify
- Mitansh: "I dont want to burn higgsfield credits, make videos through seedance on creatify". Route that worked: presenter still (GPT Image 2.5, green) → `bytedance/seedance-2.5/image-to-video` on the Creatify Model Playground (10 s 480p, generate_audio, exact quoted lines + pronunciation) = 10.25 Creatify, 0 Higgsfield; every word exact, locked shot, tiny mic kept.
- Boreal end-frame vial sat behind the presenter's head → `avatar_video.py bgvideo --dx 230` cleared it (0 cr).
- premium_finish quietluxe title-cased the sub ("Bpc-157 / Tb-500"); fixed in core/tools (labels with digits keep their case).
- caps-auto dropped the opening line: always hand-check captions against the transcript.
- Mitansh: "the only problem… it doesnt have very strong manly background music!" → every men's video gets a heavy track: `composer_generate_music` (0.8 Creatify, Lyria 3 Pro, ~11 s, hit at 0.0 s = the hook's real sound), ducked under the VO with ffmpeg sidechaincompress. First pick trap-metal (A), then the user asked for a new sound and chose D: hip-hop / hard-rock walk-out (90 BPM boom-bap, palm-muted power chords, stomp-claps, big final chord). Offer 2 contrasting takes each round.
