# Changelog

Originals of every edited file are kept in `_originals/<date>/` (same relative path).

## 2026-10-29 — Sermorelin GHK lesson: mute (don't duck) the original voice under a re-voiced line (branch `sermorelin-first-batch`)
Logged before editing. Priestley heard "two voices" in the Pilates video: the original (mispronounced) line was only
turned down to 5% under the cloned-voice line. Fixed in Pilates and Kettlebell v2 (volume 0 for that window).
- `skills/everlife-sermorelin-ghk/references/lessons.md`: the re-voice lesson now says mute, plus the batch-5 video lessons
  (Marketing Studio ignores "say this over the hands shot"; re-cut instead; Pilates take 1 failed on orange/green outside).
Originals in `_originals/2026-10-29/revoice-mute/`.

## 2026-10-29 — Sermorelin GHK: no elegant / italic serif headlines on men's ads (branch `sermorelin-first-batch`)
Logged before editing. Reviewer on batch 4 M3 ("The Edge You've Been Missing": elegant high-contrast serif with a gold
italic word): "men shouldn't use that font IMO". The bible has no font rule; this is review feedback relayed by Priestley.
- `skills/everlife-sermorelin-ghk/references/image-batch.md` §2b: a men's rule under the font menu: no elegant
  high-contrast serif, no serif-with-italic-word, no brush/handwritten accent for men's headlines; men pick from heavy
  condensed grotesque (the winners' look), wide extended sans, slab serif, or bold sans; product name big in type.
- `references/lessons.md`: the open question replaced by this decision.
Originals in `_originals/2026-10-29/men-font/`.

## 2026-10-29 — Sermorelin GHK: women's colours opened up within the bible (branch `sermorelin-first-batch`)
Logged before editing. Reviewer feedback on batch 4: "Pink is great for most women, but everything pink like that looks
the same." Priestley: "open up colors". The bible says "Women's creative: pinks, tans and beige. No oranges or greens."
(Creative & page standards); it never says pink must lead, and batch 4 made pink the main colour in 4 of 5 ads.
- `skills/everlife-sermorelin-ghk/references/image-batch.md` §2b, §3 template, QA: women's lead colour rotates through
  tan, camel, sand, beige, cream, taupe, mocha, burgundy, rose, blush; **at most one pink-led ad per batch**; no two
  women's ads share a lead colour; pink can be an accent anywhere. Still no orange, no green (bible).
- `references/lessons.md`: feedback recorded.
Men's font: no change (the bible has no font rule; noted in lessons for the creative lead).
Originals in `_originals/2026-10-29/women-colours/`.

## 2026-10-29 — Sermorelin GHK: image prompts aim the product higher (lesson from batch 4) (branch `sermorelin-first-batch`)
Logged before editing. Batch 4 (10 statics): 6 of the 7 prompts with "bottom 18% calm / product between 45% and 78%"
came back with the product or text under the footer (6 reposition edits); the 3 prompts with "bottom 22% calm / product
ends above 70–72%" came back clear first time.
- `skills/everlife-sermorelin-ghk/references/image-batch.md` §3 template: bottom band 18% → 22%, top band 10% → 11%, and
  an explicit "the whole product ends above 72% / all text above 76%" line.
- `references/lessons.md`: batch-4 lessons.
Originals in `_originals/2026-10-29/batch4-layout/`.

## 2026-10-29 — Sermorelin GHK: Justin's approved Creative Messaging Reference added to the skill's bible (branch `sermorelin-first-batch`)
Logged BEFORE the edit (Priestley: "Make sure you log this change before making any"). Source: `Sermorelin-GHK-Creative-Messaging-Reference.docx`
(Downloads, 2026-10-29), approved per Priestley; Justin Junior owns marketing for this product. Copy of the doc + the old
`product-bible.md` in `_originals/2026-10-29/justin-messaging-doc/`.
Planned change, `skills/everlife-sermorelin-ghk/references/product-bible.md` only:
- New top section "APPROVED UPDATE (Justin, 2026-10-29)", verbatim from the doc; it wins over the older bible copy where they differ.
- New usable lines: quick-hits "Supports Natural Growth Hormone Production" (both), "Supports Workout Pumps + Endurance",
  "Supports Exercise Recovery" (men), "One Daily Tablet for Muscle, Skin + Hair", "Supports Firmer, Glowing Skin From Within"
  (women); Sermorelin "Supports natural growth hormone production"; GHK "…youthful-looking skin and fuller hair".
- Removed by the doc: Sermorelin "A growth hormone–releasing hormone analog", "A safer long-term alternative to synthetic HGH";
  GHK "Reduces inflammation, oxidative stress, and signs of aging" (Justin: high risk).
- Justin's Hard NOs added: "No direct claims"; say "exercise recovery", never "muscle recovery".
- Pre-screen: the two high-risk lines become ❌ per Justin, plus "muscle recovery" and direct claims; the other lines that
  collide with GLOBAL Hard NOs keep their status (❌ fat loss, DNA repair; ⚠ wound healing/hair regrowth, accelerate,
  "lean, defined physique"); women's hair claims stay ⚠ (open question for Justin/Jeremy).
- The global creative bible (`~/.claude/everlife/creative-bible.md`) is NOT changed: it needs re-importing from its source
  when the bible owner adds Justin's lines.

## 2026-10-29 — Sermorelin GHK: lessons from the first 15 s men's video (branch `sermorelin-first-batch`)
- `skills/everlife-sermorelin-ghk/references/finishing.md`: the house look's style key is "default" ("house" crashes);
  use `tiktok` + `end_rows: benefits` until the shared end card stops cutting long ingredient claims.
- `references/lessons.md`: "Kettlebell" lessons (speech ran to 12.4 s, mispronounced name, tablet hid the label) and the
  0.3-credit re-voice fix (cloned voice over the hands-only shot).
Originals in `_originals/2026-10-29/kettlebell/`.

## 2026-10-29 — Sermorelin GHK: video timing follows Restora-Z's 15 s, with a 4 s end card (branch `sermorelin-first-batch`)
The bible sets no video length; Restora-Z uses 15 s for every video. Priestley: "lets work according to it".
- `skills/everlife-sermorelin-ghk/references/video-prompting.md`: 15 s standard with its sources; beats 0–2 hook (product or
  benefit clear by 2 s), 2–5, 5–8.5 reveal, 8.5–11 proof, 11–15 end card (Restora's is 12.8–15; ours keeps the 4 s minimum
  from the Restora feedback); speech ≤ 18 words, done by ~10.5 s; 8 s kept as the cheap option for simple ideas.
- `finishing.md`: `--end 11`, QA "last spoken line before ~10.5 s". `styles/1-real-people.md`, `styles/6-lifestyle-identity.md`,
  `styles/3-cinematic-big-idea.md`: beats and narration end moved to match. `lessons.md`: lesson added.
Restora-Z unchanged. Originals in `_originals/2026-10-29/video-timing/`.

## 2026-10-29 — Sermorelin GHK: winners lead every image batch (branch `sermorelin-first-batch`)
Priestley: "priority is winners". The women's batches built only 1 of 5 ads on a winner because the batch step picked a
framework first and then looked for a matching winner.
- `skills/everlife-sermorelin-ghk/references/image-batch.md` step 2: pick winners first; at least 3 of every 5 slots start
  from a winner for that audience (per audience for "Both"); remaining slots may use Meta / Pinterest. The approval table
  gains a source column and a count line ("3 winners · 2 Pinterest").
- `core/references/REFERENCE-PRIORITY.md`: the same rule, noted as Sermorelin GHK's (Restora-Z unchanged).
- `skills/everlife-sermorelin-ghk/references/lessons.md`: lesson added.
Originals in `_originals/2026-10-29/winners-first/`.

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

## 2026-10-28 — Sermorelin GHK: 1000 bottle cut-out (stand-in)
- `skills/everlife-sermorelin-ghk/assets/sghk1000_bottle.png`: transparent 1000 bottle made locally from the user's "1000 on white"
  JPG (white removed from the outer edge only; label untouched; 1 px edge trim to remove a JPEG fringe). Checked on dark, grey
  and light backgrounds. Marked as a stand-in in MISSING_RENDERS.md until the official NOBG file arrives. 1000 videos unblocked.

## 2026-10-28 — Sermorelin GHK lessons: video discipline
Copied Mitansh's "Video discipline" lessons (creative lead, 2026-10-27) into the Sermorelin GHK `lessons.md`: review script and
prompt twice before approval; Marketing Studio for real people; prove the angle with a 1-credit static first. Restora unchanged.

## 2026-10-28 — Sermorelin GHK women's test batch (batch 2) lessons
Added the batch-2 lessons to the Sermorelin GHK `lessons.md` (re-install the toolkit after tool changes; keep long claims out
of the footer; tablet-only default; palette drift; lean headlines with a person → Jeremy). Restora unchanged.

## 2026-10-28 — Sermorelin GHK: bottle in every image ad
Priestley: include the bottle until the corrected render is confirmed. `image-batch.md` step 3 (always attach bottle + tablet;
never drop the bottle to dodge the tan-tablet render), QA line (bottle in shot, name legible), template wording; the batch-2
lesson corrected. Originals in `_originals/2026-10-28/bottle-rule/`. Restora unchanged.

## 2026-10-28 — Sermorelin GHK: clean tablet render, preflight hidden-pixel warning, video lessons
- `sghk_tablet.png`: transparent pixels' hidden RGB set to white (visible pixels verified identical). The hidden red/magenta
  streaks showed in Higgsfield and caused wrong pills in the first video. Original in `_originals/2026-10-28/tablet-clean/`.
- Marketing Studio: new "Sermorelin GHK" product dc55181a… with the clean tablet (old a5b49393… left in place; preflight picks the newest).
- `core/scripts/preflight.sh` (shared): warns when a product PNG hides coloured/dark pixels under transparency. Warning only;
  pass counts unchanged. It now warns on Restora's `rz_bottle.png` (46%): Restora files NOT changed; for Mitansh to decide.
- Sermorelin GHK `lessons.md`: first video lessons.
- `core/tools/styles.py` (shared, tiktok end card): a tall pill render is lifted so it can't cover the label; new opt-in
  `"end_rows": "benefits"` shows the benefits instead of ingredient name + claim rows. Regression: 124/124 identical
  (Restora unchanged). Sermorelin GHK `finishing.md` notes it, plus the hold-last-frame trick for short clips.

## 2026-10-28 — Sermorelin GHK: Restora team feedback applied (skill only)
From the "Claude Ad Factory (Restora-Z) Feedback" doc (Stephen, Berna, Michael), Sermorelin GHK skill only:
SKILL.md step 2b preview stills before video credits; video-prompting.md timing (≈2 words/s, end card ≥ 4 s, ≤ 3 shots
per 8 s, each ≥ 2 s), pronunciation (≤ 2 hard names per line, listen to every take), casting (fresh, well-rested, 48–55);
image-batch.md per-ad product arrangement, no shared framework/accent in a batch, tablet ≥ 15% width and never orbs/icons,
label follows the bottle's perspective, no split "Sermorelin"/"GHK", exactly 3 benefits, no model-drawn logos.
Shared-toolkit items (fades, end-card spacing/variety, 9:16 header size, ghost voice-over) not touched. Restora unchanged.
Originals in `_originals/2026-10-28/restora-feedback/`.

## 2026-10-28 — Sermorelin GHK: themed Pinterest references
Replaced the generic "supplement" Pinterest set with a themed one (like Restora's sleep refs): 25 new picks (795 pins
screened, men 45+ vitality/strength/testosterone/longevity, women 40+ collagen/glow/strength, tablet-led heroes) + 7
on-theme pins kept from the first set; 12 off-theme removed. SOURCES.md rewritten (take / don't copy / sources / gaps).
SKILL.md and REFERENCE-PRIORITY.md counts updated. Old set in `_originals/2026-10-28/pinterest-old/`. Restora unchanged.
