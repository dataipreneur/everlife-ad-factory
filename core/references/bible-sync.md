# Keeping every skill on the latest creative bible (the bible pipeline, 2026-11-05)

**Goal:** Justin updates the bible; one phrase later every product skill carries the change, the next batch of ads uses it, and
the next patch to the team contains it. Nothing is copied by hand, so nothing drifts. Mitansh, 2026-11-05: "Even a small update in
the bible about a single product … that product's skill should have that updated and the next batch of ads should have it done.
Very simple. Super robust."

## Where the bible lives, and what is generated from it

```
Justin's live bible (claude.ai page)                 ← the source. Only Justin edits it.
        │  "sync the bible": the Artifact read saves artifact-<id>-<version>.html; bible_pipeline.py sync <html>
        ▼
core/claude/creative-bible.md                        ← the repo copy (bible_sync.py). Version on line 1. Never edited by hand.
        │  core/scripts/bible_model.py parses it (ONE parser, used by everything below)
        ▼
skills/everlife-<p>/references/bible.json            ← GENERATED (build_product_bibles.py): offer, cta_default, ctas, benefits,
                                                       headlines, proof, hard NOs, disclaimer, screening statuses, retired lines
skills/everlife-<p>/references/product-bible.md      ← GENERATED: the same as a page + the verbatim bible section + hand notes
skills/everlife-<p>/references/product-brief.md      ← GENERATED (build_product_briefs.py): brief + the bible facts block
skills/everlife-<p>/product.json "disclaimer"        ← rewritten from the bible when it changes (verbatim rule)
```

Hand files per skill (small; the only things a person edits):

| File | Holds | Edit when |
|---|---|---|
| `product.json` → `bible_sections` | the bible page heading(s) the product is generated from (Men + Women for the Sermorelins) | a product's page is renamed or split |
| `references/bible-screen.json` | `lines`: ❌ / ⚠ overrides with a why (Jeremy / Justin) · `patterns`: product regexes · `retired`: lines that left the bible and stay refused | Jeremy flags or clears a line; a product rule needs a pattern |
| `references/hard-stops.md` | the product's own hard stops (casting, settings, form words). **Never an offer, CTA or price**: lint fails | a product rule changes |
| `references/product-notes.md` | notes, history, the angle | whenever |

Live page: https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG (visible to the Everlife org; the full page is returned only to editors).

## Who does what

| Who | What |
|---|---|
| **Justin** | Edits the live bible. The only person who does. |
| **Every teammate's Claude** | Compares the live version with the repo copy at the start of every product session (read-only; warns, never blocks). |
| **Mitansh (or anyone with git + edit access)** | Says "sync the bible", reads the report, then gives the go to commit / release. |
| **Jeremy** | Reviews the "NEW lines" the report lists, and any disclaimer change. Nothing goes live without his sign-off. |
| **Everyone** | Gets the synced version with the next patch / zip. |

## "Sync the bible", step by step (one command; nothing by hand)

1. Claude reads the live page with the Artifact tool. The tool saves it as `…/tool-results/artifact-<id>-<version>.html`
   (`bible_pipeline.py newest` prints the newest one).
2. On a branch (never `main`): `python3 core/scripts/bible_pipeline.py sync` (it takes the newest saved page, or a path). It:
   - converts the page and **refuses to write on a weak parse** (fewer than 20 product pages, a skill whose section is missing or
     has no disclaimer / CTAs, no discount table, no version);
   - writes `core/claude/creative-bible.md`;
   - regenerates every product skill (`bible.json`, `product-bible.md`, `product-brief.md`, `product.json` disclaimer);
   - runs `skill_lint.py` and the two tests (`core/tests/bible_pipeline_test.py`, `batch_gate_test.py`); any failure stops it;
   - writes the CHANGELOG entry and prints: sections changed → skills, what changed per product (offer, default CTA, CTAs,
     benefits, proof, hard NOs, disclaimer), and the **NEW lines for Jeremy** (usable right away, auto-screened, not yet reviewed).
3. Mitansh reads the report and the diff. Then, on his go: `--commit` (commit on the branch) and `--release` (merge into `main`,
   push, build the team patch from `core/team-logs/team-versions.json`). Without the flags nothing touches git.
4. Jeremy reviews the NEW lines (and any disclaimer change). A line he rejects goes into that skill's `bible-screen.json` as ❌ /
   ⚠ with the why, then `bible_pipeline.py regen` and the next patch carry it.

Already synced (same version) → the command says so and stops. `--force` regenerates anyway (after a code change).

## What enforces it (so it cannot drift)

- **Lint** (`skill_lint.py`, run by the sync and before every patch): every generated file carries the synced bible's version;
  no hand "Bible sync" banner anywhere; `product.json` disclaimer == the bible's; `bible_sections` resolve; `bible-screen.json`
  is valid and names only current lines; `hard-stops.md` has no offer / CTA; no prose file quotes a % that is not the product's
  featured discount or a retired line; the gates' numbers (discount table, proof split, focal mix, logo widths, 24 px, shirtless cap)
  match the bible.
- **The gate hook** (`core/hooks/batch_hook.py`, before every image generation): refuses a prompt whose CTA is not one of the
  product's bible CTAs, any retired line, a "Save Up to N%" that is not the featured discount, a Hard NO in the headline /
  supporting lines, and any prompt from a skill whose `bible.json` is behind the synced bible ("run regen"). 0 credits are spent.
- **Check** (`bible_pipeline.py check`): regenerates into a temp folder and fails if the committed extracts differ (stale files).
- **Idempotent generators**: running them twice changes nothing; they never read their own output except the retired list.

## Products without a skill
The report prints "no skill yet" for bible pages no `product.json` claims (TRT / Enclomiphene, Optima-NAD+, Tesamorelin, TB-500,
LDN, Tesamorelin/Ipamorelin, Klow, GHK-Cu/Epithalon, Glow, and new pages such as "Sermorelin GHK 1000"). Nothing is generated for
them until a skill exists (`everlife-new-product`) or an existing skill adds the page to its `bible_sections`.

## Known limits
- The artifact prints some badges as plain text glued to the line ("…SignalingWeak benefit"); the converter brackets them. Ask
  Justin to fix them at the source when convenient.
- Men + Women pages must agree on CTAs and the disclaimer; the generator stops with the heading names if they diverge.
- The weekly cloud check (Priestley's account) is still planned, not active: the per-session version check covers it for now.
