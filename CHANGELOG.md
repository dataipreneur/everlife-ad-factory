# Changelog

Originals of every edited file are kept in `_originals/<date>/` (same relative path).

## 2026-10-28 — Plain Sermorelin skill (branch `sermorelin`, from `main`)
New skill `skills/everlife-sermorelin/` for **plain Sermorelin** (a separate product from Sermorelin GHK: own bible pages,
tablet, bottle, offer "Save up to 65%", landing page). Built per README "Adding a product skill", same flow as the
Sermorelin GHK skill. Data only: no `core/` changes.
- `references/product-bible.md`: bible Part A "Sermorelin — Men / Women" + "more claims" copied verbatim (diff-checked
  against `~/.claude/everlife/creative-bible.md` lines 88–211), plus a labelled compliance pre-screen for Jeremy:
  ❌ "From Dad Bod to Man Bod", "Targets Visceral Fat", every injections line; ⚠ "Get Toned and Lean", "Lean Muscle
  Definition", "Metabolism + Body Tone", "60/50 Is the New 40/30", "The Power of Growth Hormone in a Tablet",
  "Save 70% compared to HGH", "$95/month", "…With Your TRT". Leaves a small clean pool (3 men's / 4 women's headlines,
  3 benefits).
- Sublingual tablet only (the bible also lists injections; creative never shows or mentions them).
- `product.json` / `product.env`: id `sermorelin`, verbatim disclaimer, renders `sermorelin_bottle.png` /
  `sermorelin_tablet.png` (**not added**: see `assets/MISSING_RENDERS.md`; past ads show two different orange tablets, so
  which one is current must be confirmed).
- `assets/type_specimen.png`: new, drawn with the repo fonts from approved lines (the GHK skill's specimen is Restora's
  sleep one).
- `references/winners/winners.md`: no CPA-ranked winners yet; notes from ~300 past plain-Sermorelin ads (user's Drive
  downloads "Sermorelin M/F") on layouts worth keeping and a long don't-copy list.
- Video `tiktok`/`editorial` end cards need an `ingredients` list (`core/tools/styles.py`): `finishing.md` fills it with
  the three ✅ benefits instead of changing core.

Later the same day:
- `references/winners/`: CPA-ranked winners from the Winning Ads Reference page ("Sermorelin — Male", Oct 9–15; "Sermorelin
  — Female", Oct 2–8, stale), matched by code to the "Sermorelin M/F" Drive downloads, looked at, and written up as cards
  with small previews (M2 INT91, M3 ID323819 3.01 + 1.01, M4 VIDEO82B contact sheet + transcript, M5 BASE130-01, F1
  ID273400-3.04). M1 VIDEO83B isn't in the downloads. Every winner breaks a current rule; cards say what to rebuild.
- Findings applied: two strengths (1000 mcg "double strength", 500 mcg; catalog on that page), so renders are now
  `sermorelin1000_bottle(_ref)` / `sermorelin500_bottle(_ref)` + `product.json` "strengths"; the round "S" tablet is in
  every current men's winner (still to confirm); SKILL step 1 asks strength; batch/video guides start from the winners.
- `skills/everlife-sermorelin-ghk/SKILL.md` (original in `_originals/2026-10-28/`): description no longer claims
  "let's make Sermorelin ads"; it asks which product and points plain Sermorelin to `everlife-sermorelin`.

Renders + tests (same day, evening):
- Added `sermorelin_tablet.png` (round orange "S", small: ~250 px tablet) and `sermorelin1000_bottle.png` (+ a
  white-flattened `_ref.jpg`) from the user's asset-library downloads; bottle checked against the live page (same jar and
  label as the site's 500 mcg bottle). Injection images downloaded alongside were not added (no needles in creative).
- `core/tools/full_layout.py`, `core/tools/styles.py` (originals in `_originals/2026-10-28/core/tools/`): new optional
  product.json `pill_end_scale` (default 1) scales the end-card pill. Round tablets drawn at the capsule size covered the
  label line and dwarfed the bottle. Plain Sermorelin sets 0.62; Restora-Z and Sermorelin GHK don't set it.
- `core/tests/regression.py` (original in `_originals/2026-10-28/core/tests/`): smoke now also renders plain Sermorelin
  (3 video looks, finish_batch, disclaimer guard, composite). tiktok uses a shorter third row (the long growth-hormone
  row collided; a 30-character CTA overflows its button) — written into the skill's `finishing.md`.
- Before/after (`main` core vs this branch): identical 124, different 0. Smoke: 18/18 passed. Preflight: 9/10 (Marketing
  Studio registration pending). Not yet done: a real generated video.

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
