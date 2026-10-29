# Lessons already paid for (read every session)

No BPC-157 ads have been made with this skill yet (2026-10-29). These lessons come from Restora-Z, Sermorelin GHK and PT-141 and
from the creative team's written feedback. Add BPC-157 lessons at the bottom.

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
- **Headers split unnaturally:** product name on ONE line, never hyphen-broken ("BPC-157" stays whole).
- **Logo at the TOP**, 311 px wide, laid by the finisher; never ask the image model for a logo.
- **Safe zones on 9:16:** compose for them; the finishers refuse violations. Footer ends at y 1385 (2026-10-29).
- **Video:** benefit frames ≥ 2.5 s; fades over hard cuts; end card needs air; talent well-rested and real; write the pronunciation
  ("B-P-C one-fifty-seven"); preview the still before the video.

Generation traps:
- Selfie / front-camera prompts **mirror the label** → `--mirror-until`.
- Marketing Studio may render a **second phone** → "the filming phone is never visible"; fix with `--zoom 1.2`.
- Props with labels come out **garbled** → plain, unbranded props.
- GPT Image 2.5 on Creatify places the product 8–15% LOWER than asked → ask for the lowest element at 40%; one cheap reposition edit if needed.
- Cropping 4:5 to 9:16 puts the footer on the product → generate 9:16 natively.
- Model voices mangle product names → write the pronunciation; keep spoken product names ≤ 2.
- Whisper misspells product names → hand-fix captions ("BPC-157").
- Long scripts run under the end card → ≤ 35 spoken words, finishing by ~12 s.

BPC-157-specific risks to watch (expected, not yet seen):
- **Any "peptide vial" prompt invites a syringe, needle, pen or droplets.** Every prompt says "the vial is a still object; no syringe,
  needle, pen, dropper, droplets or injecting anywhere" and QA checks every frame. One syringe = reject, no exceptions (global Hard NO).
- **"Recovery" copy drifts to cure talk** ("heals", "repairs", "reduces inflammation", "pain"): the docx's section 6 is full of it and is
  BLOCKED. Only the seven quick-hit "Supports…" lines.
- **Men must look HARDCORE (Mitansh, 2026-10-29: "extremely masculine, gym, barbells, bodybuilders with tattoos")**: the Sermorelin
  "not bodybuilders" rule does not apply here. Use `mens-direction.md`; the only body rules left are no before/after, no body comparison,
  no body-composition words in copy.
- **Only ONE product image exists (the vial)**: the capsule form is out of scope; the model must never invent capsules or pills.
- **The vial is 3 mg/mL · 5 mL (confirmed 2026-10-29)**; the docx offer line's 2.5 mg/mL · 6 mL is stale. Copy never states either.
- **Women's "glow" hooks** read as skin claims → mood only; prefer the Pilates/strength lines.
- **No live product page yet** (404 on 2026-10-29): renders verified against the asset library only; re-check when the H2 page ships.

Compliance traps:
- Disclaimer = the PT-141 wording, confirmed by Mitansh for BPC-157 (2026-10-29); Jeremy still signs off.
- Reference ads in the library use $ prices, "Breaking", first person, old proof numbers, needles. Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- "GHK-Cu" never appears in BPC-157 creative (Hard NO carried in the docx); the Wolverine/Spartan stacks are separate products.

## BPC-157 batch 1 (2026-10-29, Nano Banana Pro, Men)
- **Paid reposition edits are dead.** Nano Banana Pro ignored "scale down and move up" on 5/5 edits (7.5 credits), removed only the
  logo/bucket, and once swapped the real vial for a white generic one. Fix = `reposition_916.py` (0 credits) + finisher.
- **Show the raws before ANY fix spend.** Mitansh: "No! First show them to me!", then "I can't waste this much time": contact sheet,
  his call, then fix. "One automatic re-roll" never means an automatic spend. And keep it FAST: one question round, defaults, go.
- **Local render composite beats an AI label fix:** `--composite bpc157_vial.png x0 y0 x1 y1` over the generated vial matched perfectly.
- Models draw their own EVERLIFE wordmark despite "no logos": crop it locally, never pay to remove it.
- The blurred-plate lower half from `reposition_916.py` is the default 9:16 look now (approved on batch 1).

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.

## Mitansh, 2026-10-29: vial images must look very premium
- Every vial-hero image or video borrows its staging from `vial-refs/` (large, tilted, label to camera, real material, hard
  directional light, monochrome harmony with the slate label, lots of air). Never a syringe, never a grid of vials, never flat colour.
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
