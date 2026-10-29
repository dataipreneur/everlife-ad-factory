# Handoff: reviewing and rolling out PR #5 (PT-141 skill + safe-area footer)

**For:** the engineer reviewing https://github.com/dataipreneur/everlife-ad-factory/pull/5 for Mitansh.
Written 2026-10-29 from Mitansh's Claude Code session. You can also hand this file to Claude Code
("Follow HANDOFF-ENGINEER.md from the pt-141-skill branch") and let it run the checks for you.

## 1. What the PR is (2 minutes)
Branch `pt-141-skill` → `main`, three commits on top of `cce781d` (Merge #1):

| Commit | What |
|---|---|
| `5569c65` | Everlife logo moves to the TOP of statics (311 px); type and colour vary per ad (`image-batch.md` §2b in every skill). |
| `f528509` | New **PT-141** skill; premium reference set; **9:16 proof footer moved into the Reels safe area** (the big functional change). |
| `b84c0c3` | `ONBOARDING.md`: paste-into-Claude instructions for the non-technical creative team (use AFTER merge). |

70 files, +1556/−111. Only 16 of them are code under `core/` (+274/−84). Everything else is the PT-141 skill (data,
references, renders) and docs.

**Why the footer moved:** a live Reels screenshot (`core/references/safe-zones/reels_placement_2026-10-29.jpg`) showed the
bottom-anchored footer sitting under Meta's "Learn more" button and caption. The reference ad's trust band sits at ~63–72%
of the frame. Ours now ends at y 1385 on 1080×1920 (the bottom of the Reels safe area per the team's Safe zones page).

## 2. Review order (what actually matters)
1. `core/tools/safezones.py`: `EVERLIFE_PROOF_AT` defaults to `safe` again; `FOOTER_BOTTOM = SAFE[3]` (1385) in safe mode;
   `violations()` lets labels starting with `proof`/`disclaimer`/`footer` cross the lower-left profile notch (creative lead's
   call, 2026-10-29). `full_layout.py`, `finish_modern.py`, `styles.py` read these constants, so video end cards and the
   legacy static finishers move with it.
2. `core/tools/finish_batch.py` (the statics finisher used by every image batch):
   - 9:16 footer at y ~1180–1385 inside the 768 px safe column (disclaimer wraps to 4 lines); scrim fades in above and out below.
   - `content_top()` / `content_bottom()`: edge-density detectors on a 270 px copy (threshold 22, 2% of a row).
   - `--shift auto` now goes both ways: down for logo headroom (max 140) or UP when content runs under the footer (max 320),
     limited by the headroom under the logo band. Still too low → exit 2 with a message. `--fit force` = QA preview only.
   - Safe-zone check on the footer column and the logo before export.
   - Feed ratios (4:5, 1:1) are unchanged: footer over the calm bottom ~18%, as before.
3. `core/tools/product.py` (+14): small additions for the PT-141 `forms` field.
4. `skills/*/references/image-batch.md`: the 9:16 LAYOUT prompt block keeps everything in the top ~52%; a "Footer position"
   note; the lesson that GPT Image lands the product 8–15% lower than asked (ask for 40% to get ~50%).
5. `skills/everlife-pt-141/`: data + references. Check `product.json` (disclaimer must be the bible's, verbatim) and that no
   file in `references/` invents a claim (headlines/benefits all cite the bible page). Compliance itself is Jeremy's, not yours.

## 3. Test it (free, ~10 minutes, no credits)
```
git fetch && git checkout pt-141-skill
bash install.sh                                                   # links the 3 skills into ~/.claude/skills
bash ~/.claude/skills/everlife-pt-141/core/scripts/preflight.sh --install   # toolkit → ~/Everlife-Creative/tools (venv)
T=~/Everlife-Creative/tools/venv/bin/python
$T -I core/tests/regression.py smoke core /tmp/smoke              # expect 12/12
rm -rf /tmp/main && mkdir -p /tmp/main && git archive main core | tar -x -C /tmp/main
$T -I core/tests/regression.py run /tmp/main/core /tmp/before
$T -I core/tests/regression.py run core /tmp/after
$T -I core/tests/regression.py compare /tmp/before /tmp/after
```
**Expected compare result:** 4:5 and 1:1 statics identical except the logo (bigger, at the top); every 9:16 output differs
(footer moved up, logo bigger). Video end cards differ in the footer position too. Anything else that differs is a bug: tell Mitansh.

See the footer on a real raw:
```
$T -I core/tools/finish_batch.py core/tests/fixtures/restora-z/raw_yarn.png /tmp/yarn_916.png --ratio 9:16 --product restora-z
$T -c "import sys; sys.path.insert(0,'core/tools'); import safezones, PIL.Image as I; safezones.overlay(I.open('/tmp/yarn_916.png')).save('/tmp/yarn_qa.png')"
open /tmp/yarn_qa.png      # red = Meta UI zones; the footer must sit above the bottom red band
```
(That fixture was composed for the old layout, so it may exit 2 with "content runs to y …": that is the new guard working.
Add `--fit force` to see the footer anyway.)

## 4. Merge the creative's own tweaks (arrives as `my-ad-changes.md`)
One creative ran v1 and changed things by hand (e.g. a bigger logo). Mitansh sends you their `my-ad-changes.md`, a table
of file · change · old → new · why · date. For each row:
- Already covered by this branch? (Logo: `LOGO_W = 311` in `finish_batch.py`, plus matching sizes in `full_layout.py`,
  `build_layers.py`, `styles.py`, `finish_modern.py`, `finish_image.py`; see CHANGELOG 2026-10-28.) Then skip it.
- A prompt/reference wording change? Apply it to the same file on this branch, keep bible wording verbatim.
- A number in `core/tools/*.py`? Apply, then re-run `smoke` + `compare` (section 3) and note the expected diff.
- A new or replaced asset? Copy it in only if it came from the Drive asset library and matches the website.
Commit on `pt-141-skill` with the creative's name in the message, push, and the PR updates.

## 5. Roll out
1. Merge PR #5 into `main` (squash or merge, your call; keep the three commit messages somewhere, they are the changelog).
2. Tell the creative team to run `ONBOARDING.md` (it is in the repo root; in step 2 of that guide they should use `main` once
   merged, the guide says so). Their old skills are moved to `~/.claude/skills-backup/` by `install.sh`, never deleted.
3. Anyone on the old zip package: `HANDOFF-MITANSH.md` still applies for the first migration.

## 6. Rollback / escape hatches
- Old footer position without any code change: `export EVERLIFE_PROOF_AT=bottom` before running a finisher.
- Revert the footer only: revert `f528509`'s changes to `core/tools/safezones.py` + `finish_batch.py` (the skill is independent of them).
- Full rollback: `git revert` the three commits, or point people at tag `restora-known-good`.

## 7. Not in this PR, on purpose
- No Drive uploads, no Asana, no Master Creative Library rows: delivery happens after creative review + Jeremy's sign-off.
- PT-141 Tier A headline pool is spent (every unflagged bible headline used once); next batch needs Tier B approval or new headlines from Jeremy.
- People in PT-141 statics are parked (product-only until the Soul 2.0 approach is tried).
- Known gaps still open: AI-disclosure wording mismatch (global vs product disclaimer); no disclaimers for Part B/C products.
- Old 9:16 finals (before 2026-10-29) in people's output folders keep the bottom footer; nothing re-renders them automatically.
