# Lessons already paid for (read every session)

Lovara batches 1 and 2 were made on 2026-10-30 (their lessons are at the bottom). The general lessons come from Restora-Z, Sermorelin GHK, plain Sermorelin and PT-141
(Oct 2026) and from the creative team's written feedback. Add Lovara lessons at the bottom.

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
- **Product name split** ("REST / ORA-Z"): the name on ONE line, never hyphen-broken.
- **Logo:** never ask the image model for one; the finisher adds the real logo at the top.
- **Video:** benefit frames ≥ 2.5 s, fades over hard cuts, more air on the end card, talent fresh-looking, a 1-credit preview still
  before any video (Stephen, Michael).

Priestley's image review rules (2026-10-29, all products):
- **Images never say "by Everlife"**; the product name runs big (a small name line reads as "no product name").
- **A different person in every ad** (one pasted casting line gave the same face 5 times): own casting per ad.
- **Ordinary, non-famous face** in every cast line: a generic "silver fox" video cast came back as a Sylvester Stallone look-alike
  (rejected, 67.5 credits) and the next was blocked by Higgsfield's IP check. Cast videos from a picked preview still.

**Mitansh on PT-141 people statics (2026-10-28, intimate wellness, same register as Lovara):** the GPT Image "smiling person + bottle +
three lines + icons" formula was "generic trash… AI slop… premium means look at Hims / Ro"; product-only versions were "amazing".
Start Lovara statics **product-only** (ONE sentence-case headline, one tiny line, the product as an object on real material with hard light
and a real shadow, monochrome harmony; `core/references/static-refs/13_Premium_DTC/`), and test people in 2–3 shots before a whole batch.

Generation traps:
- Selfie / front-camera prompts **mirror the label** → `--mirror-until`.
- Marketing Studio may render a **second phone** → "the filming phone is never visible"; fix with `--zoom 1.2`.
- Props with labels come out **garbled** → plain, unbranded props.
- Two capsules in a palm read as a two-capsule dose → "exactly ONE capsule".
- **The capsule comes out ~half the size asked** → ask for more, and fix with a 1-credit "make the capsule twice as large" edit.
- Model voices mangle product names → TTS line or cloned-voice line; keep spoken product names ≤ 2.
- Whisper misspells product names → hand-fix captions ("Lovara").
- GPT Image 2.5 places the product LOWER than asked → ask high ("ends above 66%"); 9:16 from the approved 4:5 (`compose916.py`).
- Higgsfield "no response received" on submit = the upload failing → upload first and pass the IDs (not charged when it fails).

Lovara-specific risks to watch (expected, not yet seen):
- Any "intimacy" prompt drifts to **beds, lingerie, bodies, couples, lips** → every prompt names a daytime, non-bedroom setting and says
  "fully clothed, daytime, no bed, no bedroom, shoulder-up".
- "Women's desire" copy drifts to explicit or outcome wording ("crave", "ignited", "hits deeper") → ✅ "Supports…" lines; ⚠ only with OK.
- The **ingredient list is under review** (Justin): men's performance ingredients on a women's product. Keep claims product-level until it's
  confirmed; ingredient claims only on their own ingredient.
- "Support Your Spark" CTA names another product → ❌ until Justin confirms.
- The PMG samples ("Horny in 30 min", lips, bedroom) are the opposite of the brief: never copy their words, timing or scenes.

Compliance traps:
- Rx is never shared: only the person's OWN pharmacy delivery.
- Reference ads use $ prices, "Breaking", first person, old proof numbers, "ED", "Viagra". Never copy those.
- Build every copy.json fresh (retired lines sneak back via reused files).
- Disclaimer stays the bible's verbatim text. The global AI-disclosure line differs from it: open question for Jeremy.

## Footer + legibility
- Proof is ALWAYS the approved footer art (`tools/assets/footer/`), never typed stars, never generated.
- 9:16: proof row inside the Reels safe area (ends at y 1385), disclaimer alone at the very bottom (`"disclaimer_at": "bottom"`).
- Type minimums: 24 px (disclaimer), 36 px (subline), 72 px (headline), cards 32+.

## Shared creative system (2026-10-29)
`core/references/creative-system.md`: structural variety, article slot, product-angle rotation, named typefaces, own palette, hero ≥ 35%
and real, CTA string + QA, real logo/label composited, footer unfade, 9:16 built from the approved 4:5. Read it before every batch table;
tools: `reposition_916.py`, `unfade_cta.py`, `logo_in_box.py`, `compose916.py`.

## Batch-1 test (2026-10-30, 4:5, 5 Creatify credits)
- The capsule reference came through exactly on all 4 (rose-gold, printed LOVARA); bottle label correct. Prompt template works as is.
- The model can ignore "text above 72%": L4 put its benefit lines at 83-90%, under the footer. finish_batch does NOT refuse that at 4:5 (only 9:16 checks), so LOOK at every final; fix = a 1-credit edit moving the lines under the headline.
- Hands holding the capsule push the product low; ask for the product to end above 66% and check the footer fade does not swallow the capsule.

## Winners (2026-10-30, Emily)
- The all-time top statics (INT24 120 sales, INT4 112, INT13 95) have no files yet; the files on hand (360555, Base161, Videos 32/26/18) show the format: huge LOVARA + "3-in-1 Female Sexual Wellness Blend" + "From Distant to Deeply Connected", three icon callouts, blush light; videos = a fixed info frame over golden-hour lifestyle footage. Most break today's rules (lingerie, bed, per-ingredient claims, old proof numbers): format only.
- Batch 2 (2026-10-30, from the winners): all 4 passed after one fix (W3 product under the footer). Finish with --shift 0 when the raw already has the top 14% calm; the auto logo shift pushed CTAs into the footer in 3 of 4 products today. unfade_cta.py rescues a CTA just above the footer.
