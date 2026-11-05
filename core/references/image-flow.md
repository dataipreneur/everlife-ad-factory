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
- **Who's in them?** depends on `product.json` → `"audience"` (Mitansh 2026-11-05):
  - **both** (PT-141, Spark, Restora-Z, NAD+, GLP-1, MOTS-c, Epithalon, BPC-157, Sermorelin, Sermorelin GHK): "Mix of men and women
    (Recommended): about a quarter with a real person, the rest product worlds" / "Men" / "Women" / "Product only".
  - **men** (Titan-Rx, Spartan, Wolverine) or **women** (Lovara, GHK Cream): "Mix (Recommended): about a quarter with a real person,
    the rest product worlds" / "Product only" / "More people". Never ask men or women here: the dealer refuses the other gender.
  The answer becomes `deal_worlds.py --audience <men|women|both>` (omit it for Mix: the product's own audience is the default).
- Product-specific only if `product.json` has more than one **form** (`two-forms`: PT-141, NAD+, GLP-1) or more than one **strength**
  (`two-strengths`: Sermorelin GHK, Sermorelin): **Form** "Pick per ad (Recommended)" / each form · **Strength** "Either (Recommended):
  never mentioned, default bottle" / "500 mcg" / "1000 mcg" ("Double Strength" wording only with the 1000 mcg bottle in frame). The prompt
  attaches that form's / strength's own bottle render.
Never ask for: mood, style, palette, copy density, boldness, hook angle, placement, framework, pain point. The dealer and you
decide those, differently for every slot, and the batch table shows the picks. A designer can still type anything in chat
("all comic", "women only", "use the boarding pass world") and you honour it.

## 2. Deal the worlds (code decides the MIX, you decide the AD)
```
python3 core/scripts/deal_worlds.py --product <id> --n <N> [--audience <men|women|both>] [--prefer <world ids of the chosen direction>]
```
The dealer reads the product's **variations** from `product.json` (`core/references/ENGINE.md`): `hardcore-men` tags up to 30% of men's
slots, `intimacy-tasteful` drops bed / body worlds, `vial-product` leads with material / scene worlds and marks them
`ultra_premium` (write the `core/references/ultra-premium.md` codes into those prompts), `womens-palette` trims the accents.
It hands you N slots, each with a **world** (from `core/references/world-deck/worlds.json`: magazine cover, wanted poster,
boarding pass, claymation, blueprint, fluted glass, neon sign, search bar, hold-out, brutalist type… 130 worlds in 10 families),
a type pairing, an accent, a headline placement, a light, the focal (pill / bottle / person), the proof (trust / count / none),
a persona for person slots, the hardcore tag where the product allows it, and the ratio pair. Guarantees: no world repeats in
the batch or in this product's last 3 batches, max 2 per family, no two slots share a type pairing, accent or placement.
Re-deal (`--seed`) if a world makes no sense for the product; **never swap a slot's world for one already in the batch.**
When the batch is approved: run it again with `--log` so the ledger remembers.

**Team scale (Mitansh 2026-11-05: 6 designers × 70 images a day):** the ledger is per laptop, so before dealing, pull the worlds
the TEAM used for this product in the last 2 days and pass them as `--skip`: finals are named `FINAL_<n>_<world>_<WxH>` and are
posted to Ad Review, so `teamlog.py summary --product <id>` (recent ad titles) → the world ids → `--skip a,b,c`. Also take the
front door's product recommendation (`everlife-ads`: the product with the fewest recent finals) so six people don't all make the
same product on the same day. Variety budget: 132 worlds × 10 type pairings × 18 accents × 6 placements × 7 lights; a product
can run ~16 batches before any world is allowed back, and the deck grows weekly from winners and the reference harvest.

## 3. Write each ad from its slot (this is the creative work)
For every slot, in order:
1. **Open one reference.** First a winner for this product (`references/winners/`), else a batch-2 ad from the same world
   (`_sheets/` + the file named for the world, e.g. `*_boarding*.png`), else the world card alone. Take the IDEA and the
   LAYOUT, never the words, never the theme of another product.
2. **Translate the world to this product.** The card's "translate" line is the hint: a boarding pass for a sleep product flies
   FROM tossing & turning TO deep sleep; for a muscle product FROM sore TO back on the bar; for an intimacy product FROM
   calendars TO moments. Keep it one clear idea a 50+ reader gets in two seconds.
3. **Headline: write it.** The bible's headlines and benefits are your references and inspiration, never a fence (Mitansh
   2026-11-05: "be as bold and creative as you want; that is mandatory for diversity"). Write the line the WORLD would say: a wanted
   poster shouts, a dictionary defines, a memo is terse, a boarding pass prints. **The only fence is the Hard NOs** (section 2 + the product page's Hard NOs): no disease / cure / treat words, no outcome
   promises or guarantees, no body-composition, no pronoun questions, no first person, no competitor names, no "Get Started Now".
   Everything else is yours. Never a line already in the product copy log. **CTA = one of the product's current bible CTAs, exactly**
   (`references/bible.json` → `cta_default`, normally "Save Up to N%"; `python3 core/scripts/product_copy.py <id>` prints them); the gate hook
   refuses any other CTA string, any retired line and any % that is not the product's featured discount (bible pipeline, 2026-11-05).
   **Price CTA = the dealt slot's `cta`, exactly** (bible: the product's "$/day" line on 10% of all ads): the batch table's CTA column marks the
   💲 slots (`deal_worlds.py` → `price_plan.py`); a 💲 slot's CTA line is the price line, every other slot's is the default offer CTA, and the gate
   refuses the price line anywhere else. Never swap them by hand; the share is kept over batches so small batches still average 10%.
4. **Supporting lines:** up to 3 short lines in the same voice, the bible's benefits as the reference for what to say; same fence. Peptide stacks name every peptide.
5. **Type & colour:** the world's own type hint leads; the dealt pairing is the partner face. Accent from the dealt list
   (men's products skip rose / blush; women's and intimacy skip orange / green). Placement and light as dealt. Headline ≥ 9%
   of canvas height per line, every other line ≥ 3.5%, no thin grey text, no shadows or outlines on type.
6. **Prompt** (template §4). Both ratios: write the 9:16 prompt, then the 4:5 prompt (same world, same copy, its own LAYOUT block).
7. **Persona pass** (if the skill has `references/personas.md`): one line of critique per ad, fix, move on.

Show ONE compact table: # · world · focal · proof · headline · lines · persona · ≈2 credits. One AskUserQuestion:
"Generate all N in both sizes (≈2N credits, includes one re-make per ad if needed)" / "Swap some" / "Rewrite headlines". That click approves the batch; Jeremy's compliance sign-off still comes before anything goes live.

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
line; every other line at least 3.5%; strong contrast; no thin grey text; no shadows or outlines on type; max 3 supporting
lines. Texture and depth behind the product, never flat colour; nothing covers the product, the CTA or any text.

TEXT: render ONLY these strings, exactly as written, nothing else (no extra words, no logos, no stars, no badges, no prices,
no website, no disclaimer):
  Headline: "<headline>"   (accent on: "<phrase>")
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"
  CTA (in a button): "<cta_default from references/bible.json, or another of its ctas[]>"
  <world-specific text, e.g. the ticket fields, the dictionary entry, the poll options>

<STRICT LAYOUT block for this ratio, pasted from core/references/prompt-layout-zones.md>

Reference only, never render: everlife slot=<n> ratio=<9:16|4:5> product=<id> job=<the batch folder, e.g. ~/Everlife-Creative/output/PT-141/2026-11-05_batch-1>
```
The last line is the **batch reference**: the gate hook (`core/hooks/batch_hook.py`) refuses any Everlife image prompt without it or
without the STRICT LAYOUT block for that ratio, counts every fired slot × ratio in `<job>/renders.jsonl`, and the Stop hook will not
let the turn end until every slot has BOTH sizes finished (`batch_check.py <job>` shows what is owed). Save the deal first:
`deal_worlds.py … --json > <job>/deal.json`.
Attach: bottle render, tablet render (if any), Trustpilot badge is NOT attached (the finisher adds proof). Never attach a
reference ad: only you look at references.

## 5. Generate, both sizes, no pauses
Fire every 9:16 (`model_playground_generate` GPT Image 2.5 on Creatify, 4 in flight), then every 4:5 straight after.
Download all raws, then `finish_batch.py <raw> <final> --ratio <r> --product <id> --proof <slot proof>` for each; the
finisher refuses a raw whose content runs under the proof row: fix with the free-fix skill (0 cr), else re-roll that size.
Log each generation (`teamlog.py gens --wave`), one record per wave.

## 6. QA by looking, fix inside the budget, then show (the heavy lifting is yours, not the designer's)
Read every final. Text exactly the approved strings and spelled right · label legible · nothing covered · headline + lines
readable at phone size · both sizes present for every ad · the world is recognisable in two seconds · no two ads alike.
- **A failed size gets ONE automatic re-make inside the approved budget** (the approval question says "≈2N credits, includes one
  re-make per ad if needed"): same slot, the fix named in the prompt ("benefit lines at least 36 px tall", "product base at y 760").
  Free fixes first (`free-fix` skill for footer collisions). Still failing → show it honestly with the cost of another try.
- Build one contact sheet with both sizes per ad, **open the output folder on their screen** (`open <folder>`; Windows
  `explorer.exe`), show the sheet, and say in one line what's in it and what's next: "Another 8 (new worlds)" / "Variations of #k" /
  "Re-make #k". Plain words, no file lists, no technical reasons.
- Append headlines to the product copy log, `deal_worlds.py --log`, post finals to Ad Review, `teamlog.py` records.

## 7. What made batch 2 great (keep doing this)
- Every ad lives in a **different universe**: paper, screens, materials, places, people, type. Not a different palette on the same layout.
- The **product name is big and the world carries the emotion**; benefits are short, in the world's own voice.
- Humour is welcome (a grumpy clock, a sheet ghost, a clay blob with coffee) as long as nobody is mocked and no claim is implied.
- Real rooms, real light, real textures. The surreal ones are photoreal (a moon hammock you could touch).
- Fonts and placements change every single ad. Two ads in a row with the same type is a fail.

## 8. Bare minimums: the run contract (every image batch, in this order; `skill_lint.py` fails if this section loses a step)
Mitansh 2026-11-05: "make sure we have the bare minimums: 4:5 AND 9:16 in one batch, post-editing by Claude, the logging workflow."
These are the steps the old per-skill files carried; they live here once now. Code enforces what it can; the lint checks the text.

| # | Step | Command / check | Enforced by |
|---|---|---|---|
| 1 | Preflight | `bash <skill>/core/scripts/preflight.sh` (connections, tools, bible version check) | script |
| 2 | Read the product | `references/product-brief.md` (hard stops, variations, the bible facts block) · `references/product-bible.md` (generated from the bible) · `references/lessons.md` · `references/winners/`; exact copy strings: `python3 core/scripts/product_copy.py <id>` (reads `references/bible.json`) | you |
| 3 | Lean team reads | Copy Ledger + Ad Review flags saved to files (`ArtifactData` `out_dir` = `<job>/_team/ledger`, `<job>/_team/review`), then only the digest: `teamlog.py summary <job>/_team/ledger <job>/_team/review --product <id>` (used headlines, team styles/worlds → `--skip`, reviewer flags → explicit checks for this batch). Page unreachable → say so, carry on | TEAM-LOGS §2.2, AD-REVIEW §3 |
| 4 | Deal | `deal_worlds.py --product <id> --n N --audience A [--prefer …] [--skip …] --json > <job>/deal.json` (the MANIFEST: N slots × 2 ratios owed); proof per slot follows `finish_batch.py --proof-plan N` (42/28/30); CTA per slot: the price line on ~10% of ads (`price_plan.py`, kept in `~/Everlife-Creative/price-ledger.jsonl`; `--log` records the batch) | code |
| 5 | Write | every ad: 9:16 prompt AND 4:5 prompt, each with its STRICT LAYOUT block (`prompt-layout-zones.md`), copy inside the Hard NOs; `prompts.md` | you + lint on the prompt (zones present) |
| 6 | Approve | one AskUserQuestion with the cost: "Generate all N in both sizes (≈2N credits, includes one re-make per ad if needed)" | gate: never spend without it |
| 7 | Generate | all 9:16 raws, then all 4:5 raws (GPT Image 2.5 on Creatify, 4 in flight); never crop / pad / mirror one size into the other. Every prompt ends with the batch reference line; the gate hook refuses it otherwise and counts what was fired | **code: `batch_hook.py gate` + `fired`** |
| 8 | Log generations | `teamlog.py gens <job> --wave W.json` per wave (exact prompt, model, cost, slot) | TEAM-LOGS §2 |
| 9 | Finish | `finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <r> --product <id> --proof <slot proof>` for EVERY raw of EVERY ad, both sizes: logo at the top, proof row inside the safe area (ends ≤ y 1385; on a collision the finisher drops it by the minimum needed, up to 20% of the height, approved 2026-11-05), verbatim disclaimer + AI disclosure from `product.json`; refuses a raw that runs under the footer → `free-fix` (0 cr) → else one re-make | code (`safezones.py`, `standard_footer.py`) |
| 10 | QA | Read every final (text exact, legible, nothing covered, world recognisable, both sizes present); `teamlog.py qa <job> <doc_id…> --pass/--fail`; one automatic re-make per failed size inside the budget | you + TEAM-LOGS |
| 11 | Both-sizes + proof audit | `batch_check.py <job>` must print ✅ (every slot finished in 9:16 AND 4:5; the Stop hook blocks the turn otherwise) and `finish_batch.py --proof-check <batch folder>` must pass (≈42/28/30 per ratio) before the sheet is shown | **code: `batch_hook.py stop`, `batch_check.py`, `--proof-check`** |
| 12 | Show | one contact sheet with both sizes per ad; open the output folder; plain words | you |
| 13 | After the batch | `teamlog.py copy` per ad · `teamlog.py proof` per creative · `teamlog.py run` · **`teamlog.py close <job>` must print ✅ closed** · `teamlog.py sent <job> --all` (or `--queued`) · post every final to Ad Review (`entry` + preview; `teamlog.py posted <job> <ad_id…>`) · append headlines to `~/Everlife-Creative/<id>-copy-log.md` · `deal_worlds.py --product <id> --n N --log` | TEAM-LOGS §2, AD-REVIEW §4, Stop hook |
| 14 | Hand-off | `~/Everlife-Creative/output/<Product>/<date>_SESSION.md`: one row per asset (path, world, headline, lines, CTA, proof, cost, issues, any Hard-NO doubt for Jeremy). Drafts only; delivery (Drive, Master Library, Asana) only after approval | you |
| 15 | **Next-batch questionnaire** (compulsory) | after the sheet is shown: ONE AskUserQuestion for the SAME product, first question headed `Next batch` (§9) → `<job>/next_asked.json` | **code: `batch_hook.py stop` blocks the turn until it is asked; `batch_check.py` shows it** |

The Stop hook (`core/hooks/teamlog_hook.py`, installed by `install.sh`) sends Claude back once when a job holds unsent records or
unposted finals. If `~/.claude/settings.json` has no hooks, run `install.sh` (or `update.sh`) on that machine: preflight warns.

## 9. The next-batch questionnaire (compulsory, enforced by code)
Mitansh 2026-11-05: "Compulsory requestionnaire after 1 batch of images is done! For that same product! Shouldn't be a memory or
something, do by code." Once every slot of a batch is finished in both sizes (`batch_check.py` ✅), the Stop hook
(`core/hooks/batch_hook.py`) will not let the turn end until this question has been asked; asking it writes
`<job>/next_asked.json` (questions + answers). It runs whatever happened in the batch (good, re-rolled, free-fixed), right after
the contact sheet is shown. A batch the user stopped on purpose is released with `batch_check.py <job> --release "<their words>"`.

One AskUserQuestion, the SAME product, every first option ✨ Recommended:
1. **header `Next batch`** (exactly; the hook matches it), "Next batch of <Product> images?": "Another 8, new worlds (Recommended)" /
   "Another 4" / "Variations of one ad" / "Done for now".
2. **Direction:** "🎲 Surprise me (Recommended)" + three NEW pitches from `world-deck/INSPIRATIONS.md` (never the last batch's three;
   fold in what the user said about the batch, e.g. "more comic").
3. **Who's in them?** as in §1.
4. **Form / Strength**, only if the product has them (§1).
"Done for now" is a valid answer: the file is still written and the session can end. Any other answer starts §2 for the same product
with the last batch's worlds skipped; the spend gate still holds (nothing is generated before the batch table is approved).

