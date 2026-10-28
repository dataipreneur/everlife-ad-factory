# Changelog

Originals of every edited file are kept in `_originals/<date>/` (same relative path).

## 2026-10-28 — Creative lead: Everlife logo at the TOP of statics; vary type and colour per ad (branch `logo-top-type-variety`)
Two rules from Mitansh after the first Sermorelin GHK batch, applied to every product skill:
- `core/tools/finish_batch.py`: the logo moved out of the footer to the top safe band (9:16 y=150, feed y=60/56; 200 px wide,
  ink on light scenes, cream on dark, soft top fade). If the generation left too little headroom above its first text/edge
  the image is nudged down (max 140 px; the calm bottom under the footer absorbs it); `--shift auto|<px>`. The footer keeps
  the proof art row + verbatim disclaimer. Regression vs main: only the 3 `batch.png` fixtures differ (expected); smoke 12/12.
- `skills/*/references/image-batch.md`: new §2b "Type & colour: be different every time" (a menu of 8 headline pairings and
  accent colours, product palettes still win; never two alike in a batch; placement and light vary too). The prompt's
  TYPOGRAPHY block is now per-ad; the type specimen is no longer attached by default (house look only). LAYOUT asks for a
  calm top 12% (9:16) / 10% (feed) for the logo.
- `skills/*/references/lessons.md`: both rules recorded as creative-lead lessons (2026-10-28).
- `skills/everlife-sermorelin-ghk/assets/creatify.json`: the Creatify project created on Mitansh's account for batch 1.
Video looks (`styles.py` house / tiktok / editorial) and `finish_modern.py` already carry the logo at the top; unchanged.

## 2026-10-28 — Mitansh's post-zip Restora changes ported (branch `mitansh-sync`)
Mitansh's Mac (fingerprint `3be3a588e802`) differed from the zip this repo started from (`4d128f8be668`) in five files.
Diffed against the unzipped original (`~/Downloads/everlife-restora-z.zip`, 27 Oct 21:51); everything else was identical.
- `tools/composite.py`, `tools/full_layout.py`: he added an `$EVERLIFE_SKILL` override for the hard-coded
  `~/.claude/skills/everlife-restora-z` path. Already covered here in a product-neutral form: both tools now resolve renders and
  the reviews file through `product.py` (`$EVERLIFE_SKILLS_DIR`), so no code change was needed. `$EVERLIFE_SKILL` is not read.
- `scripts/preflight.sh`: his new step 0 (link the skill into `~/.claude/skills` when preflight runs from a project copy) ported
  product-neutrally into `core/scripts/preflight.sh` (link name = the skill folder's name; never replaces a real folder).
- `references/lessons.md`: new section "Video discipline (creative lead, 2026-10-27)" copied verbatim.
- `assets/product_ids.json`: his Marketing Studio product id (`14cd145c-…`, written by preflight on his Mac 2026-10-28) replaces
  `01898c30-…`. ⚠ This file is machine-written per account; consider ignoring it in git so pulls don't flip it between Macs.
- `README.md` in his skill folder is unchanged from the zip (not ported; the repo README replaced it in the reorganisation).
- `HANDOFF-MITANSH.md` step 1 now accepts `3be3a588e802`.
Before/after check (his installed tools vs this branch): see the pull request for the `compare` / `smoke` output.

## 2026-10-28 — Sermorelin GHK 1000 skill + product-neutral video finishing (branch `sermorelin-ghk-1000`)

New skill `skills/everlife-sermorelin-ghk-1000/` (copied from the Restora-Z structure, all product copy rewritten):
- `references/product-bible.md`: the Sermorelin GHK Men + Women pages copied verbatim from the creative bible (diff-checked),
  plus a separate, labelled compliance pre-screen (❌/⚠ ingredient claims that collide with global Hard NOs, for Jeremy).
- SKILL.md flow adds an audience step (Men / Women) and a hard stop while product renders are missing.
- Renders NOT included: the Drive connector couldn't list the SERMORELIN GHK folder. See `assets/MISSING_RENDERS.md`.
- No reviews on file → review spotlight / review burst gated. No Creatify project yet.
- Style boards 1–6 copied (generic library thumbnails); Restora's sleep-specific boards not copied.

Core changes (Restora-Z behaviour unchanged; every new setting defaults to the old Restora value):
- `core/tools/styles.py`: new `_cased()` restores names listed in copy.json `keep_case` after `.title()`/`.lower()`
  (was a hard-coded Restora-Z replace; "Sermorelin GHK" would have printed as "Sermorelin Ghk").
- `core/tools/review_burst.py`: highlight regex is now `HIGHLIGHT` (default Restora-Z), set from copy.json `highlight`.
- `core/tools/full_layout.py`: `--reviews-json` defaults to copy.json `reviews_json`, then Restora's file; passes `highlight`.
- `core/tools/composite.py`: default renders come from `$EVERLIFE_SKILL_DIR/product.env` (BOTTLE/PILL), else Restora-Z.
- `README.md`: new skill listed; "Known Restora-specific bits" replaced by what's now configurable and what's still Restora-only.

Later the same day:
- Added `assets/sghk1000_bottle_ref.jpg` (user's download, checked against the landing page: label reads SERMORELIN GHK 1000 · 1000 MCG).
  Still missing: the transparent bottle PNG and the tablet render (`assets/MISSING_RENDERS.md`).
- `references/image-batch.md`: bottle label wording added to the prompt notes. `references/product-bible.md`: "1000" question
  updated (1000 mcg is sold on the page; whether copy may say "1000" is still open).
- Added `assets/sghk1000_tablet.png` (from the user's "SERMORELIN GHK TABLET.webp"); accepted by the user on the evidence of the
  live Sermorelin GHK winners. Ed/Ronnel to confirm the 1000 uses the same tablet.

## 2026-10-28 — ⚠ PENDING CREATIVE-LEAD CONFIRMATION: headline rule, Restora-Z + Sermorelin GHK 1000
Changed at Priestley's request; marked "PENDING CREATIVE-LEAD CONFIRMATION" in each file. Originals in `_originals/2026-10-28/`.
- Why: the 2026-10-27 rule ("bible headlines are references, fresh wording is fine") conflicts with the global gate in
  CLAUDE.md (headlines only from the bible/brief; new hooks need explicit approval), which ranks above skills. Restora's batch
  mode also treated the batch click as approval for new headlines, with no Tier B label or Jeremy flag.
- New rule: Tier A (bible wording) by default; Tier B (fresh wording or non-bible winner headlines) max 2 per batch, marked
  PROPOSED, approved line by line, listed for Jeremy; warn when the Tier A pool runs low.
- Files: `skills/everlife-restora-z/SKILL.md` (golden rule 1), `skills/everlife-restora-z/references/image-batch.md` (§0, §2 step 2),
  `skills/everlife-sermorelin-ghk-1000/SKILL.md` (golden rule 1), `skills/everlife-sermorelin-ghk-1000/references/image-batch.md`
  (§0, §2 step 2; also added "Citrulline is not a peptide").
- To close: the creative lead and Jeremy confirm → remove the ⚠ notes; or they reject → restore the originals.

## 2026-10-28 — Product-neutral shared tools (branch `product-config`, from checkpoint 512785f)
Originals in `_originals/2026-10-28/`. Why: every new product meant editing shared tools, with Restora-Z values as
silent fallbacks. Now a product is data only, and the tools refuse rather than guess.
- New `core/tools/product.py`: loads `skills/everlife-<id>/product.json` (lookup dir `$EVERLIFE_SKILLS_DIR`, default
  `~/.claude/skills`). Jobs name their product in copy.json (`"product": "<id>"`); missing product → refused; a copy.json
  disclaimer that differs from product.json → refused.
- New `skills/everlife-restora-z/product.json` and `skills/everlife-sermorelin-ghk-1000/product.json`: disclaimer (verbatim),
  renders, keep_case, review_highlight, reviews, kicker_default, split_titles, notify_app/notify_icon, compare_allowed,
  product_zones (Restora's teal-bottle / blue-capsule colours moved here from code; Sermorelin: not calibrated yet).
- `full_layout.py`: disclaimer, renders, keep_case, reviews file and highlight from product.json (copy.json keys
  reviews_json / highlight / keep_case removed); copies missing renders from the skill's assets.
  Also fixed an existing bug: when the end card shifts down, the stretched filler strip could cut through a long end
  headline and turn into vertical bars (seen with Sermorelin); it now picks the nearest clean strip. Restora unchanged.
- `styles.py`, `review_burst.py`: no Restora defaults (review_burst gains `--highlight` for standalone use).
- `composite.py`: `--product <id>` (or explicit `--bottle`/`--pill`); no default product.
- `finish_modern.py`: product colours + notification app/icon from product.json; refuses products without product_zones.
- `finish_image.py`: disclaimer, article kicker and split titles from product.json; `compare` only if compare_allowed.
- `finish_batch.py`: `--product <id>` supplies the verbatim disclaimer (`--disclaimer` still works, must match).
- `build_layers.py`: docstring marks the standalone run as legacy Restora-only. `preflight.sh`: checks product.json.
- New `core/tests/regression.py` + fixtures (3 Restora raws, resized): `run` / `compare` / `smoke`.
- Skill docs (both): copy.json templates use `"product"`; finish_batch uses `--product`.
- Verified: Restora-Z 124/124 images identical to the checkpoint; vs original main, 1 intended difference (editorial
  headline now prints "Restora-Z" instead of "restora-z", from the earlier casing fix). Smoke 12/12 (Sermorelin renders
  with its own disclaimer, casing and kicker; every guard refuses correctly).
- Rollout: `git pull` → `bash install.sh` (links skills, so the tools can find product.json) → preflight `--install`.
  Older Restora job folders need `"product": "restora-z"` added to copy.json before re-running.
- Noted, not changed: Restora's tiktok end card prints "3-In-1" (old behaviour); adding "3-in-1" to Restora's keep_case
  would fix it but changes Restora output, so it's left for the creative lead to decide.

## 2026-10-28 — Skill renamed: `everlife-sermorelin-ghk-1000` → `everlife-sermorelin-ghk` (both strengths)
At Priestley's request; one skill now covers Sermorelin GHK 500 mcg and 1000 mcg. Pre-rename copy in
`_originals/2026-10-28/skills/everlife-sermorelin-ghk-1000-before-rename/`.
- Folder, product id (`sermorelin-ghk`), product name, output folder (`~/Everlife-Creative/output/Sermorelin-GHK`) and copy
  log (`~/Everlife-Creative/sermorelin-ghk-copy-log.md`) renamed; the local copy log and output folder were empty and were moved.
- Tablet renamed `sghk_tablet.png` (shared by both strengths). 1000 bottle files keep their names.
- product.json: new `strengths` block (500 / 1000 bottle files and label text). SKILL.md: new setup question
  "Strength: Either (Recommended) / 1000 / 500" and an "Audience: Both (5 each)" option; renders gate is per strength.
- 500 bottle renders are NOT added: product images must come from the Drive asset library, not the website image.
  500 ads wait for `sghk500_bottle_ref.jpg` / `sghk500_bottle.png` (see assets/MISSING_RENDERS.md).
- Copy still never states a strength or dose by default (open question for the creative lead; "double strength" needs Jeremy).
- Bible extract re-checked: verbatim section identical. Smoke test 12/12 with the new id. Earlier entries keep the old name.
- Anyone who installed the old skill name: run `bash install.sh` again (it links the new folder; remove the stale
  `~/.claude/skills/everlife-sermorelin-ghk-1000` link if present).

## 2026-10-28 — Sermorelin GHK winner cards
- New `skills/everlife-sermorelin-ghk/references/winners/`: `winners.md` (one card per winner from the Winning Ads page,
  week Oct 9–15: numbers, format, works / don't copy / rebuild-with) + 14 small preview images (≈840 KB).
- 13 of 15 checked by eye (12 statics + VIDEO49 frames and transcript). Not checkable: M1 VIDEO7-1.01 (both Drive links
  dead) and F4 BASE125-00 video (over the Drive connector's 10 MB limit; thumbnail only).
- Skill wired to them: SKILL.md reading table, image-batch.md step 2 (winner first, generic refs second), video-prompting.md.

## 2026-10-28 — Handoff instructions for Mitansh
- New `HANDOFF-MITANSH.md`: written for Mitansh's Claude Code. Version check (tool fingerprint `4d128f8be668` = the
  tested baseline), backups, clone + `product-config`, the before/after check on his Mac before installing, install,
  a real-job Restora check, rollback, day-to-day, and starting the Sermorelin GHK skill (what's ready / what's not).
- Step 4 was run here exactly as written: `identical: 123 different: 1` (the intended casing fix), smoke 12/12.
- README points existing zip users to it.

## 2026-10-28 — Handoff: step 1b for Mitansh's newer version
Mitansh's tool fingerprint is `3be3a588e802`, not the tested `4d128f8be668`, and matches no package on Priestley's Mac: he
kept working after the 17:49 zip. HANDOFF-MITANSH.md gains step 1b: don't merge or install; on a `mitansh-sync` branch,
diff his installed skill against `restora-known-good`, port his changes into the new layout (product values into
product.json, not tool code), prove with the before/after check using HIS tools as the baseline, then open a pull
request into `product-config` for Priestley to review.

## 2026-10-28 — After merging #2: preflight old-copy warning, product_ids.json out of git, handoff paths
- `core/scripts/preflight.sh` (step 0 from #2): an old, unlinked copy in `~/.claude/skills/<skill>` is now a ❌ with the fix
  (`install.sh`), instead of a ✅ "already present" while Claude keeps using the old copy. Tested on Priestley's Mac (old copy
  present → ❌, nothing moved).
- `skills/*/assets/product_ids.json` removed from git and ignored: preflight writes it per account/Mac. Existing local copies
  stay; after a pull it may disappear and the next preflight recreates it.
- `HANDOFF-MITANSH.md`: repo path note (Mitansh's clone is `~/Desktop/everlife-ad-factory`); step 5 says where he starts.
- Checked on the merged branch: vs `restora-known-good` 123/124 identical, vs Mitansh's tools (3be3a588e802) 123/124
  identical (the one intended "Restora-Z" casing change in both), smoke 12/12.

## 2026-10-28 — Sermorelin GHK: 500 bottle renders added; 500 is the default bottle (branch `sermorelin-first-batch`)
- Added `assets/sghk500_bottle.png` (transparent, 864×1891, from "SERMORELINGHK NOBG 2.webp") and `assets/sghk500_bottle_ref.jpg`
  (500 on white, 584×1280). Labels checked: SERMORELIN GHK · 30 TABLETS · 500 MCG, same render as the site.
- product.json `renders.bottle` and product.env `BOTTLE`/`RENDERS` now default to the 500 bottle (the only transparent bottle
  on file; also the site's default strength). 1000 jobs set `"bottle"` per strength; 1000 videos still need `sghk1000_bottle.png`.
- Registered "Sermorelin GHK" in Higgsfield Marketing Studio (Everlife workspace) with the 500 bottle + tablet:
  product id a5b49393-165a-4230-8082-aaae6ba20ed3 (stored locally in product_ids.json, not in git). Preflight 10/10.
- The "1000 on white" JPG received at 16:26 is the same picture as the existing 1000 reference; not added.

## 2026-10-28 — Offer: the creative bible wins over landing pages
Priestley's decision: ads use only the bible's offer ("Save up to 47%"). Corrected the same day: the men's page shows 52%
for the GHK tablets (and "Get 47% Off Now!" on its button); 59% is the plain Sermorelin injection sold on the same page;
the women's page shows 47% for the tablets.
Recorded in the Sermorelin GHK bible page's facts section (not the verbatim extract), with the two current landing-page links
(men m-fb-v9, women f-fb-v10) for the session sheet.

## 2026-10-28 — Reference priority rule (Sermorelin GHK only)
- New `core/references/REFERENCE-PRIORITY.md`: pick reference ads in this order: 1 our winners → 2 Meta Ad Library →
  3 Pinterest (`static-refs`: 50 board-1 pins, 20 board-2 pins, 20 DOC). References set idea and layout only; words come from
  the bible; the generator never sees references; record the level and file used per ad.
- New `core/references/meta-refs/SOURCES.md` (empty log + how to add Meta Ad Library references).
- Wired into Sermorelin GHK only (`SKILL.md` reading table, `image-batch.md` step 2). **Restora-Z unchanged** at Priestley's
  request: its owner decides whether to adopt the rule.

## 2026-10-28 — Sermorelin GHK Pinterest references (priority 3)
- New `skills/everlife-sermorelin-ghk/references/pinterest/` (19 images, 1.5 MB, `SOURCES.md`): screened 661 pins from four
  Pinterest idea pages (supplement advertising, supplement creative ads, us-vs-them ad examples, male ad); kept supplement /
  wellness / skincare ads for the ad types our winners don't cover: Us vs Them, phone UI, question, reasons why, sticky note,
  visual metaphor, features, brand mood, and a new 13_EXTRA_Identity_Age (men 50+ / active seniors). Dropped a GLP-1 fat-loss
  ad and an art poster with a violent line. Each row: what to take (layout) and what not to copy.
- Sermorelin GHK checks its own Pinterest folder before the shared sleep-heavy `static-refs`. Restora-Z unchanged.

## 2026-10-28 — Merged main (#3 logo-top + type variety) into sermorelin-first-batch; Creatify note per person
- Brought #3 (Mitansh: logo at the top of statics, varied type/colour) into this branch. Both sides kept in the Sermorelin GHK
  `image-batch.md` and `lessons.md` (his §2b + logo band; our reference order, Pinterest folder, strength label wording).
- `skills/everlife-sermorelin-ghk/assets/creatify.json` is no longer in git (a Creatify project belongs to one account: Mitansh
  and Priestley each made one today). Each Mac keeps its own; new `creatify.example.json` explains how to create one.
  SKILL.md setup row updated. Restora's creatify.json untouched.
- Checks after the merge: vs new main 124/124 identical, smoke 12/12, both preflights 10/10, Restora 0 lines changed.
  Today's 5 Sermorelin ads re-finished with the new finish_batch (logo top, shifts 38–53 px): all clean
  (`~/Everlife-Creative/output/Sermorelin-GHK/2026-10-28_batch-1/refinish-logo-top/`).
