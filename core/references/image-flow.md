# Everlife IMAGE flow (shared, every product) — the Restora-Z 2nd-batch recipe, made repeatable

This is the golden flow from the Restora-Z batches of 2026-10-27/29 (235 ads, the team's diversity bar; local copy:
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/`, contact sheets in `_sheets/`). It is product-neutral.
Each product skill adds only its facts (`product.json`, `references/product-bible.md`, its `image-batch.md` §0 copy rules).

**Rules are not in this file on purpose.** Claims, Hard NOs, safe zones, proof split, layout zones, disclaimer, logo and
both-sizes live in the gates (`~/.claude/CLAUDE.md`), `core/references/global-rules.md`, `prompt-layout-zones.md` and the
code (`finish_batch.py`, `safezones.py`, `standard_footer.py`). They apply whether or not anyone re-reads them. This file is
about making the ads GOOD.

## Bare minimums (never negotiable, Mitansh 2026-11-05)
1. Every ad is generated in **9:16 AND 4:5 in the same run**, each a fresh render (never crop / pad / mirror one into the other).
2. **Finishing is done by Claude, in code** (`finish_batch.py`: logo, proof row per the plan, verbatim disclaimer), then QA by looking.
3. Claims only from the product bible; the STRICT LAYOUT block from `prompt-layout-zones.md` in every prompt.

## 1. One question, then go
One `AskUserQuestion` with up to 4 questions, every first option ✨ Recommended, so one Enter per question gives a great batch:
- **How many?** "8 (Recommended)" / "4" / "12".
- **Direction** (Mitansh 2026-11-05: "Surprise me first, but give super cool inspirations"): "🎲 Surprise me (Recommended): a different
  world every ad" first, then **three directions you pitch for this product and this batch** from
  `core/references/world-deck/INSPIRATIONS.md` (mutate the seeds, never the same three twice in a row, invent one when you can).
  Label `<Name> · <3–4 worlds>`; description = the idea in one sentence + the twist + "≈2 cr/ad, both sizes". A chosen direction
  becomes `deal_worlds.py --prefer <its world ids>`; the other slots stay random, so the batch is still a mix.
- **Who's in them?** "Mix (Recommended): about a quarter with a real person, the rest product worlds" / "Product only" / "More people".
- Product-specific only if `product.json` has more than one form (`two-forms` variation): **Form** "Pick per ad (Recommended)" / each form.
Never ask for: mood, style, palette, copy density, boldness, hook angle, placement, framework, pain point. The dealer and you
decide those, differently for every slot, and the batch table shows the picks. A designer can still type anything in chat
("all comic", "women only", "use the boarding pass world") and you honour it.

## 2. Deal the worlds (code decides the MIX, you decide the AD)
```
python3 core/scripts/deal_worlds.py --product <id> --n <N> --audience <men|women|both> [--prefer <world ids of the chosen direction>]
```
The dealer reads the product's **variations** from `product.json` (`core/references/ENGINE.md`): `hardcore-men` tags 40% of men's
slots, `intimacy-tasteful` drops bed / body worlds, `vial-product` leads with material / scene worlds and marks them
`ultra_premium` (write the `core/references/ultra-premium.md` codes into those prompts), `womens-palette` trims the accents.
It hands you N slots, each with a **world** (from `core/references/world-deck/worlds.json`: magazine cover, wanted poster,
boarding pass, claymation, blueprint, fluted glass, neon sign, search bar, hold-out, brutalist type… 130 worlds in 10 families),
a type pairing, an accent, a headline placement, a light, the focal (pill / bottle / person), the proof (trust / count / none),
a persona for person slots, the hardcore tag where the product allows it, and the ratio pair. Guarantees: no world repeats in
the batch or in this product's last 3 batches, max 2 per family, no two slots share a type pairing, accent or placement.
Re-deal (`--seed`) if a world makes no sense for the product; **never swap a slot's world for one already in the batch.**
When the batch is approved: run it again with `--log` so the ledger remembers.

## 3. Write each ad from its slot (this is the creative work)
For every slot, in order:
1. **Open one reference.** First a winner for this product (`references/winners/`), else a batch-2 ad from the same world
   (`_sheets/` + the file named for the world, e.g. `*_boarding*.png`), else the world card alone. Take the IDEA and the
   LAYOUT, never the words, never the theme of another product.
2. **Translate the world to this product.** The card's "translate" line is the hint: a boarding pass for a sleep product flies
   FROM tossing & turning TO deep sleep; for a muscle product FROM sore TO back on the bar; for an intimacy product FROM
   calendars TO moments. Keep it one clear idea a 50+ reader gets in two seconds.
3. **Headline:** Tier A from the bible by default (verbatim or lightly trimmed), bent to the world's voice (a wanted poster
   shouts, a dictionary defines, a memo is terse). Tier B (fresh wording) only if the batch is marked Balanced/Bold, max 2,
   marked PROPOSED. Never a line already in the product copy log. Never "Get Started Now". Lead CTAs with the offer.
4. **Supporting lines:** up to 3 approved claims, exact. Peptide stacks name every peptide.
5. **Type & colour:** the world's own type hint leads; the dealt pairing is the partner face. Accent from the dealt list
   (men's products skip rose / blush; women's and intimacy skip orange / green). Placement and light as dealt. Headline ≥ 9%
   of canvas height per line, every other line ≥ 3.5%, no thin grey text, no shadows or outlines on type.
6. **Prompt** (template §4). Both ratios: write the 9:16 prompt, then the 4:5 prompt (same world, same copy, its own LAYOUT block).
7. **Persona pass** (if the skill has `references/personas.md`): one line of critique per ad, fix, move on.

Show ONE compact table: # · world · focal · proof · headline (tier) · lines · persona · ≈2 credits. One AskUserQuestion:
"Generate all N in both sizes (≈2N credits)" / "Swap some" / "Rewrite headlines". That click approves the batch and its Tier A
lines; each Tier B line needs its own explicit OK first.

## 4. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "<Product>" by Everlife, <one-line product truth from product.json>.
WORLD: <world name>: <the card's look, translated to this product in one or two sentences>. The whole ad lives inside this
world: its surfaces, its props, its light (<dealt light>). One clear idea.

PRODUCT: image 1 is the real <bottle/vial/spray>, image 2 the real <tablet/capsule> (if the product has one). Use them
exactly: same shape, colours and label, label facing camera, sharp, never mirrored, never redesigned, never covered.
<focal line: "The tablet is the primary focal point, foreground, sharp" | "The bottle is the hero, 30–45% of canvas height" |
"A real person is the focal point: <persona>, candid, <clothing/framing rule from the skill>; the product in focus beside them">.

TYPOGRAPHY & COLOUR: headline in <world type hint; else dealt pairing[0]>, with ONE phrase picked out in <accent>; supporting
text in <pairing[1]>. Headline placement: <dealt placement>. For readers aged 50+: headline at least 9% of canvas height per
line; every other line at least 3.5%; strong contrast; no thin grey text; max 3 supporting lines.

TEXT: render ONLY these strings, exactly as written, nothing else (no extra words, no logos, no stars, no badges, no prices,
no website, no disclaimer):
  Headline: "<headline>"   (accent on: "<phrase>")
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"
  CTA: "<offer CTA from the bible>"
  <world-specific text, e.g. the ticket fields, the dictionary entry, the poll options>

<STRICT LAYOUT block for this ratio, pasted from core/references/prompt-layout-zones.md>
```
Attach: bottle render, tablet render (if any), Trustpilot badge is NOT attached (the finisher adds proof). Never attach a
reference ad: only you look at references.

## 5. Generate, both sizes, no pauses
Fire every 9:16 (`model_playground_generate` GPT Image 2.5 on Creatify, 4 in flight), then every 4:5 straight after.
Download all raws, then `finish_batch.py <raw> <final> --ratio <r> --product <id> --proof <slot proof>` for each; the
finisher refuses a raw whose content runs under the proof row: fix with the free-fix skill (0 cr), else re-roll that size.
Log each generation (`teamlog.py gens --wave`), one record per wave.

## 6. QA by looking, then show
Read every final. Text exactly the approved strings and spelled right · label legible · nothing covered · headline + lines
readable at phone size · both sizes present for every ad · the world is recognisable in two seconds · no two ads alike.
Build one contact sheet with both sizes per ad and show it. Offer: "Another 8 (new worlds)" / "Variations of #k" /
"Re-roll #k". Append headlines to the product copy log, `deal_worlds.py --log`, post finals to Ad Review.

## 7. What made batch 2 great (keep doing this)
- Every ad lives in a **different universe**: paper, screens, materials, places, people, type. Not a different palette on the same layout.
- The **product name is big and the world carries the emotion**; benefits are short, in the world's own voice.
- Humour is welcome (a grumpy clock, a sheet ghost, a clay blob with coffee) as long as nobody is mocked and no claim is implied.
- Real rooms, real light, real textures. The surreal ones are photoreal (a moon hammock you could touch).
- Fonts and placements change every single ad. Two ads in a row with the same type is a fail.
