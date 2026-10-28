# Handoff: updating Mitansh's Mac to the new ad factory (Restora-Z + Sermorelin GHK)

**For:** Claude Code on Mitansh's Mac. Mitansh: open Claude Code in any folder and say
*"Follow HANDOFF-MITANSH.md from github.com/dataipreneur/everlife-ad-factory, branch product-config"*
(or paste this file). Written 2026-10-28 by Priestley's Claude session.

## What changed and why (read first, 1 minute)
Mitansh's Restora-Z package (`everlife-restora-z.zip`, 27 Oct, 17:49) is now a git repo with:
- **One shared toolkit** (`core/`) + **one folder per product** (`skills/everlife-restora-z/`, `skills/everlife-sermorelin-ghk/`), installed by `install.sh` as links.
- **Product-neutral tools:** everything product-specific (verbatim disclaimer, renders, name casing, review highlight, the colours `finish_modern` uses to find the bottle) moved from tool code into `skills/<product>/product.json`.
- **Every job's `copy.json` now needs `"product": "restora-z"`** (or `"sermorelin-ghk"`). Without it the tools stop with a clear error instead of guessing. The disclaimer now comes from product.json (don't type it; if it's typed it must match exactly).
- `finish_batch.py --product restora-z` replaces `--disclaimer "<text>"` (the old form still works).
- **Headline rule (pending the creative lead's confirmation, marked in the files):** Tier A (bible wording) by default; Tier B (fresh wording) max 2 per batch, approved line by line, flagged for Jeremy.
- A new **Sermorelin GHK** skill (500 + 1000 mcg).
- **Restora-Z output is unchanged:** a before/after check rendered 124 Restora images with Mitansh's original tools and the new ones, and they were identical except one intended fix (the editorial headline now prints "Restora-Z", not "restora-z").
- Full detail: `CHANGELOG.md`. Rollback point: git tag `restora-known-good` (= the original package, reorganised).

## Rules for this session (Claude)
- Do the steps **in order**. After each step, tell Mitansh the result in one line.
- **STOP and ask Mitansh** whenever a step says STOP, a check fails, or anything would overwrite or delete his files.
- **Back up before replacing anything** (steps 2–3). Never delete; move to a backup folder.
- **No paid generation** in this handoff (no Higgsfield / Creatify credits). Everything here is free.
- Don't change the bible, disclaimers or claims. Compliance questions go to Jeremy.

---

## Step 1 — Is this Mac on the version we tested against? (read-only)
```bash
ls -la ~/.claude/skills/ | grep -i everlife
cd ~/.claude/skills/everlife-restora-z 2>/dev/null && cat tools/*.py scripts/*.py | shasum | cut -c1-12
```
- If it prints **`3be3a588e802`** (Mitansh's Mac, 2026-10-28; his post-zip changes are ported in this branch) or
  **`4d128f8be668`** (the original zip): same tools as the tested baseline. Continue.
- If it prints something else: his version is **newer** than the one
  this branch was built from. **Do NOT merge the pull request or run `install.sh`** (that would replace his newer tools
  with older ones). Do **step 1b** instead, then come back to step 2.

## Step 1b — Bring Mitansh's newer Restora work into the branch (only if step 1 didn't match)
Goal: the repo gets his improvements, in the new layout, and the before/after check proves his output is unchanged.
1. Backup first (step 2 below), then get the repo (step 3 below) and make a working branch:
   `cd ~/everlife-ad-factory && git checkout product-config && git checkout -b mitansh-sync`
2. See what he changed since the version this branch started from (the tag `restora-known-good`). Old → new layout:
   `tools/` → `core/tools/` · `scripts/` → `core/scripts/` · `references/global-rules.md` → `core/references/global-rules.md` ·
   `references/static-refs/` → `core/references/static-refs/` · everything else → `skills/everlife-restora-z/`.
   ```bash
   M=~/.claude/skills/everlife-restora-z; K=$(mktemp -d); git archive restora-known-good | tar -x -C "$K"
   diff -rq "$M/tools" "$K/core/tools"; diff -rq "$M/scripts" "$K/core/scripts"
   diff -rq "$M/references" "$K/skills/everlife-restora-z/references"; diff -q "$M/SKILL.md" "$K/skills/everlife-restora-z/SKILL.md"
   diff -rq "$M/assets" "$K/skills/everlife-restora-z/assets"
   ```
   Show Mitansh the list and a one-line summary per changed file. Ignore pure path differences (`scripts/…` vs `core/scripts/…`).
3. Port each change onto `mitansh-sync` (`git diff restora-known-good -- <file>` shows what this branch changed in the same file):
   - **Tool code** → `core/tools/` / `core/scripts/`. Keep this branch's rule: **no product names or product values in
     tool code.** Anything Restora-specific he added (text, colours, file names, the disclaimer) goes into
     `skills/everlife-restora-z/product.json` and is read through `product.py`, like the existing settings.
   - **Instructions, lessons, prompts, styles, bible, reviews, assets** → `skills/everlife-restora-z/…`. Keep this branch's
     additions: `"product": "restora-z"` in copy.json templates, `--product` for `finish_batch.py`, and the headline-tier
     note marked PENDING CREATIVE-LEAD CONFIRMATION (if his version changed headline rules, keep both and flag it to Priestley).
   - New files of his: same mapping. Don't delete anything of his; if unsure, ask Mitansh.
4. Prove it: render with **his** installed tools as the baseline and with the branch, and compare.
   ```bash
   cd ~/everlife-ad-factory; PY=~/Everlife-Creative/tools/venv/bin/python; T=$(mktemp -d); mkdir -p "$T/core"
   cp -R ~/.claude/skills/everlife-restora-z/tools "$T/core/tools"; cp -R ~/.claude/skills/everlife-restora-z/scripts "$T/core/scripts"
   $PY -I core/tests/regression.py run "$T/core" "$T/before"
   $PY -I core/tests/regression.py run core "$T/after"
   $PY -I core/tests/regression.py compare "$T/before" "$T/after"
   $PY -I core/tests/regression.py smoke core "$T/smoke"
   ```
   Expected: only `video_editorial/layers_full/top.png` differs (the intended "Restora-Z" casing fix), unless one of his own
   changes intentionally alters that output (say which). Smoke `12/12`. Anything else → fix the port, re-run. If his tools
   fail the `run` itself (missing assets etc.), tell Priestley.
5. Update the fingerprint line in step 1 of this file to his version's value, add a CHANGELOG entry ("Mitansh's
   post-zip Restora changes ported"), commit, `git push -u origin mitansh-sync`, and open a pull request **into
   `product-config`** for Priestley to review: `gh pr create --base product-config --head mitansh-sync` (or on github.com).
6. Stop here. After Priestley merges that, PR #1 (`product-config` → `main`) contains both people's work; then do steps
   5–8 below on this Mac (step 4 is already done).

Also check (read-only) and report: does `~/.claude/CLAUDE.md` contain "EverlifeMD Creative Gates"? Does
`~/.claude/everlife/creative-bible.md` exist? Both came with the original package and the skills rely on them. If either is
missing, **STOP** and ask Mitansh (don't create or edit `~/.claude/CLAUDE.md` yourself).

## Step 2 — Back up the working setup (nothing is deleted)
```bash
B=~/Everlife-Creative/backup-before-repo-$(date +%Y%m%d-%H%M)
mkdir -p "$B"
cp -R ~/.claude/skills/everlife-restora-z "$B/skill-everlife-restora-z"
cp -R ~/Everlife-Creative/tools "$B/tools"            # preflight --install will overwrite this folder later
ls "$B"
```
Tell Mitansh the backup path. (Copy logs and `output/` are never touched by this update.)

## Step 3 — Get the repo (doesn't change his install yet)
**Paths:** the commands below use `~/everlife-ad-factory`. If the repo already lives somewhere else (Mitansh: `~/Desktop/everlife-ad-factory`), use that path everywhere instead, including step 7 and the rollback.
```bash
cd ~ && git clone https://github.com/dataipreneur/everlife-ad-factory.git   # needs access to the repo
cd ~/everlife-ad-factory && git fetch --all --tags
git checkout product-config      # until the pull request is merged; afterwards use: git checkout main && git pull
git log --oneline -5 && git tag
```
If the clone fails (no access): **STOP**, Mitansh asks Priestley for access to `dataipreneur/everlife-ad-factory`.
The tag list must include `restora-known-good`.

## Step 4 — Before/after check on THIS Mac (still nothing installed; ~2 min, free)
It renders Restora jobs with the original tools (`restora-known-good`) and with the new ones, using the existing
toolkit venv, and compares them pixel by pixel.
```bash
cd ~/everlife-ad-factory
PY=~/Everlife-Creative/tools/venv/bin/python
TMP=$(mktemp -d)
git archive restora-known-good core | tar -x -C "$TMP"
$PY -I core/tests/regression.py run "$TMP/core" "$TMP/before"
$PY -I core/tests/regression.py run core "$TMP/after"
$PY -I core/tests/regression.py compare "$TMP/before" "$TMP/after"
$PY -I core/tests/regression.py smoke core "$TMP/smoke"
```
**Expected:** `compare` prints exactly one difference, `video_editorial/layers_full/top.png` (the intended "Restora-Z"
casing fix; open both PNGs and confirm the only change is "restora-z" → "Restora-Z"), then `identical: 123 different: 1`.
`smoke` prints `12/12 passed`. Lines with `rc=2` during `run` are normal (the image finisher refusing layouts that would
touch the product on those test images); they must be the same in both runs.
**Anything else → STOP** and send Priestley the full output.

## Step 5 — Install
(Mitansh, 2026-10-28: steps 1–4 and 1b are done; PR #2 and PR #1 are merged. Start here: `cd ~/Desktop/everlife-ad-factory && git checkout main && git pull`, then the commands below.)
```bash
cd ~/everlife-ad-factory
bash install.sh                 # links both skills into ~/.claude/skills; moves the old Restora copy to ~/.claude/skills-backup/
bash ~/.claude/skills/everlife-restora-z/core/scripts/preflight.sh --install     # installs the new toolkit
bash ~/.claude/skills/everlife-sermorelin-ghk/core/scripts/preflight.sh
```
Order matters: `install.sh` first (the new tools find products through the linked skills).
**Expected:** Restora preflight all ✅ (incl. "product.json valid (product id: restora-z …)"). Sermorelin preflight: two
known ❌ only, "Sermorelin GHK not registered in Marketing Studio" and "Missing render sghk1000_bottle.png" (the
transparent 1000 bottle hasn't been supplied yet). Anything else → STOP.

## Step 6 — Real Restora check on one of Mitansh's own finished jobs (free)
Pick a recent static job in `~/Everlife-Creative/output/Restora-Z/` that has a `FINAL_*.png`, `copy.json` and `out/raw.png`.
Work on a **copy** of it, never the original:
```bash
J=~/Everlife-Creative/output/Restora-Z/<job>      # Mitansh picks
C=$(mktemp -d)/check && cp -R "$J" "$C"
python3 - "$C/copy.json" <<'EOF'
import json, sys; p = sys.argv[1]; d = json.load(open(p)); d["product"] = "restora-z"; json.dump(d, open(p, "w"), indent=1)
EOF
```
Re-run the same finisher and template the job used (see its `out/finish*.log` or the session sheet), e.g.
`~/Everlife-Creative/tools/venv/bin/python -I ~/Everlife-Creative/tools/finish_modern.py "$C/out/raw.png" "$C/copy.json" "$C/recheck.png" --ratio 4:5 --template hero`,
then open the new file next to the job's FINAL and confirm they match. If the job was a video: same idea with
`full_layout.py` on the job copy (it reuses the job's edited captions). Differences → STOP.

**If anything goes wrong after step 5 (rollback):**
```bash
B=<the backup folder from step 2, e.g. ~/Everlife-Creative/backup-before-repo-20261029-1015>
rm ~/.claude/skills/everlife-restora-z ~/.claude/skills/everlife-sermorelin-ghk     # these are links only
cp -R "$B/skill-everlife-restora-z" ~/.claude/skills/everlife-restora-z
rm -rf ~/Everlife-Creative/tools && cp -R "$B/tools" ~/Everlife-Creative/tools
```
(Ask Mitansh before running it.) That restores exactly the setup from step 2.

## Step 7 — Day to day from now on
- Restora: `/everlife-restora-z` as before. New copy.json files carry `"product": "restora-z"` (the skill's instructions
  already say so). **Old job folders** need that one line added before re-running.
- Updates: `cd ~/everlife-ad-factory && git pull && bash install.sh`, then preflight `--install` if `core/tools/` changed.
- Changing a shared tool: branch → run step 4's check → pull request. Product details: edit that product's `product.json`.

## Step 8 — Start the Sermorelin GHK skill
Say `/everlife-sermorelin-ghk` (or "make Sermorelin GHK ads"). It asks: **Audience** (Men / Women / Both) ·
**Strength** (Either, recommended / 1000 / 500) · **Images or video**.

What works today and what doesn't:
| Ready | Not yet |
|---|---|
| Image batches for **1000** or **"either"** (strength never mentioned): bottle reference + tablet on file | **500 ads**: the 500 bottle renders must come from the Drive asset library (`sghk500_bottle_ref.jpg` / `sghk500_bottle.png`); never the website image |
| Bible page + compliance pre-screen, headline tiers, 15 winner cards (`references/winners/`) | **Videos**: need the transparent 1000 bottle (`sghk1000_bottle.png`) for end cards and Marketing Studio |
| Free dry run: the full flow up to the batch table, no credits | `finish_modern.py` for Sermorelin (refused until its product colours are calibrated; Batch Mode uses `finish_batch.py`) |

First image run on this Mac: `assets/creatify.json` has no Sermorelin project yet; the skill creates one in Mitansh's
Creatify account (uploads the bottle reference, the tablet and the type specimen) and saves it there. Every generation
still needs Mitansh's explicit approval with the credit cost shown.

Open items (don't block a dry run): the creative lead confirms the headline tiers and whether copy may say
"500"/"1000"; Jeremy rules on the ingredient-claim pre-screen and "double strength"; Ed/Ronnel confirm the tablet for
1000 mcg and supply the transparent 1000 bottle and the 500 renders. Details: `assets/MISSING_RENDERS.md`,
`references/product-bible.md` (top), `CHANGELOG.md`.
