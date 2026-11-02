---
name: everlife-new-product
description: Builds a new EverlifeMD product ad skill (the next product in the build plan) step by step, bible-first. Picks the product, reads everything it can from the synced creative bible, the local asset library, the reference ads and the Meta winners export, shows ONE summary card, asks only about the gaps (template, form, missing renders, flagged copy errors), then scaffolds the skill on its own branch, adapts it, tests it for free and stops at the two human gates (the first paid test batch, the PR). Use when the user says "build the skill for <product>", "new product skill", "next product", "add Spark / Spartan Stack / Wolverine Stack / MOTS-c", or pastes the plan doc's kickoff prompt. Not for making ads (use the product's own skill).
---

# New product skill builder

You build a new Everlife product skill the way the plan doc's recipe says ("New Product Skills: Build Plan",
https://claude.ai/artifact/8y75Kmn6hUKtSsoTLzxhaf → "How to build one product skill"), with as few questions as possible:
**everything the bible already says is read, never asked.** You drive with `AskUserQuestion`, one round at a time.

Non-negotiable (same as every Everlife session):
1. **The bible wins.** Claims, headlines, CTAs, offers and disclaimers only from the synced bible (`core/claude/creative-bible.md`).
   Pending lines need explicit approval, weak lines are avoided, Hard NO conflicts are never used. Never take claims from a landing page.
2. **No ad disclaimer on file → STOP.** Nothing is built for that product until Jeremy adds one (MOTS-c, Tesamorelin, Klow… today).
   Exception, only when Priestley asks to set it up anyway: `create … --pending-disclaimer` scaffolds it **blocked** (empty
   disclaimer + `_disclaimer_status` in product.json), so every finisher refuses it; add a smoke check that proves the refusal.
3. **Log before editing:** a CHANGELOG entry first, originals backed up to `_originals/<date>/`; one branch per product (`<id>-skill`,
   from the latest `main`); never work on another session's branch.
4. **Never touch `skills/everlife-restora-z/`** unless Priestley asks; never copy it as a template without his OK.
5. **No credits without approval:** show the cost and wait for an explicit OK before any Creatify or Higgsfield generation.
6. **No push or PR** until the tests pass AND a real test batch has been looked at and approved.

Files:

| File | When |
|---|---|
| `scripts/new_product.py` | `list`, `inspect "<Product>"`, `create "<Product>" --template <skill>` (all local, free) |
| `references/human-inputs.md` | what only people can provide, who, and when to ask |
| `references/templates.md` | which existing skill to copy for which kind of product |
| `references/adapt-checklist.md` | every file to adapt after the scaffold, the rules every new product inherits, the tests |

Run the script with the toolkit Python: `PY=~/Everlife-Creative/tools/venv/bin/python`; `$PY -I <skill-dir>/scripts/new_product.py …`.

---

## Step 0 — Sync (no questions)
1. Read the plan doc (Claude Docs connector, `read` the doc, then its tab) for the build order and approvals.
2. Check the bible for updates: read the live bible artifact (https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG) with the Artifact
   tool (`read`; it saves the HTML), then `$PY -I core/scripts/bible_sync.py <saved html>` (changes) and `--check` (disclaimers).
   If the live bible changed, say what changed for the queued products; syncing the repo copy is its own small PR (`--write`).
3. `$PY -I scripts/new_product.py list` → every bible product without a skill, its category, disclaimer status and approved headlines.

## Step 1 — Which product? (one AskUserQuestion)
Options: the next 3 products of the plan's build order that aren't built (first one "(Recommended)"), each with its status in the
description ("disclaimer ✅, 3/10 headlines approved, CTAs pending"). A product with no disclaimer is shown as blocked and not offered.

## Step 2 — The summary card (no questions)
`$PY -I scripts/new_product.py inspect "<Product>"` and show it compactly:
- from the bible: audience, category, creative direction, product Hard NOs, headlines/benefits/CTAs with their status, offer, landing page;
- from disk: renders found (`~/Everlife-Creative/asset-library/`, `~/Downloads`) and the form they imply, reference ads
  (`~/Everlife-Creative/reference-ads/`), winners rows from the Meta all-time export (`~/Downloads/Everlife_All-Time_Top_Ads_by_Account.xlsx`);
- the suggested template (`references/templates.md`) and every flag (another product named in a CTA/headline, placeholders, pending blocks);
- **Gaps (human inputs)**: the short list of things only a person can answer.
LOOK at every render it found (Read the image): the right product, the label, the strength, a clean background. Never infer from a file name.

## Step 3 — Ask only the gaps (one AskUserQuestion, ≤ 4 questions, only those that apply)
- **Template:** "<suggested> (Recommended)" / the next best / "Other". Skip when the card's suggestion is unambiguous and the user said "go".
- **Form / strengths:** only if the card says UNKNOWN or the renders disagree with the bible.
- **Renders:** only if missing: "I'll download them now" (they drop the asset-library folder in Downloads; you unzip it into
  `~/Everlife-Creative/asset-library/` with a UTF-8-safe unzip) / "Build without them (generation stays blocked)".
- **Flagged copy errors / pending blocks:** don't ask the user to decide compliance; list them for Justin/Jeremy and choose the safe
  default (❌ until confirmed). Ask only "Build now and send these to Justin/Jeremy?".
Then confirm in one line what you'll build and start.

## Step 4 — Scaffold (no questions)
1. `git fetch origin && git checkout -b <id>-skill origin/main` (from the repo / your worktree; never another session's branch).
2. CHANGELOG entry first (what, why, template, branch), commit it.
3. `$PY -I scripts/new_product.py create "<Product>" --template <skill> [--form …] [--bottle …] [--pill …]`: copies the template,
   removes its own renders / winners / team refs / reviews, writes product.json (verbatim disclaimer, `disclaimer_at: bottom`) and
   product.env, the bible extract with a draft pre-screen, the renders (cut out from white when needed, + the `_ref.jpg` on white) and
   the copy-log seed, and lists every file still naming the template product.

## Step 5 — Adapt (no questions; `references/adapt-checklist.md`)
Rewrite every listed file for the new product: SKILL.md, product facts + pre-screen, image-batch (bottle wording from the real render,
recipes, colours), video-prompting, finishing (copy.json example), personas, reference guide, lessons, styles ×7. Apply the inherited
rules (§3 of the checklist). Grep until the template product's name only appears where it's deliberate.
**Required:** the image setup offers **"✨ Ultra premium, product only"** once (`core/references/ultra-premium.md`; add the
product's row to its "Per product" table; vial products stage from `vial-refs/`). Checklist §3 and test 5; a skill without it is not done. Same for **"🧑‍💼 AI Avatar Video"** (⛔ ALL-CREATIFY: 0 Higgsfield, Seedance 2.5 presenter on Creatify, see `core/references/ai-avatar-video.md`) in "What are we making?" (`core/references/ai-avatar-video.md`;
checklist §3, test 6).

## Step 6 — Test for free
- `bible_sync.py --check` (the new product's disclaimer must match), the skill's `preflight.sh`, `core/tests/regression.py smoke` before
  and after adding the product's block (static finish + wrong-disclaimer refusal + end-card renders in two looks).
- LOOK at an end-card frame (`frames.py` or ffmpeg): the pill/capsule/vial must not cover the headline; set `pill_end_scale` in
  product.json if it does (0.62 round tablet, 0.36 tall capsule).
- Commit locally. Report: what's built, what's blocked, the human inputs still open (`references/human-inputs.md`).

## Step 7 — The two human gates
1. **First real test:** a 4-image batch with the product's own skill (~4 Creatify credits), approved first with the cost shown. Look at every
   image, fix or redo, log the copy, write the lessons into the new skill.
2. **PR:** only after the tests pass and the batch looks right; Mitansh reviews, Jeremy signs off the bible lines and claims. After merge:
   `git pull` + `bash install.sh` in the main checkout so the skill link points there.
