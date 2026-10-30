# Changelog

Originals of every edited file are kept in `_originals/<date>/` (same relative path).

## 2026-10-30 — Wolverine Stack: PROVISIONAL swap + headlines + offer, gate lifted (branch `wolverine-skill`)
Logged before editing. Bible-updates hand-off §6; Priestley approved all three. PROVISIONAL — Jeremy to confirm.
- `references/product-bible.md`: pre-screen now uses the Spartan page's benefit lines (the 2-peptide ones); "Two Peptides. One
  Recovery Stack." moved here; provisional headlines "Two Peptides. One Mission." and "Bounce Back Stronger"; "Recover Like Wolverine"
  ❌ until Jeremy (Marvel). Offer "Save up to 39%" PROVISIONAL: landing page only, an approved exception to "offers never from landing
  pages"; must be added to the bible.
- `SKILL.md`, `image-batch.md` (F6 offer framework back), `video-prompting.md`: ⛔ gate → ⚠ PROVISIONAL note; ingredients named together
  as on the label; the KPV inflammation line moves to Spartan. `product.json`: `_blocked` → `_provisional`.
Originals in `_originals/2026-10-30/stack-provisional/wolverine/`.

## 2026-10-30 — Wolverine Stack: labels confirmed, waiting for the bible fix (branch `wolverine-skill`)
Same as the Spartan Stack: the vial labels are correct (Wolverine = BPC-157 + TB-500), the bible's stack pages are swapped.
Priestley: wait for the bible fix. Block wording updated in SKILL.md, image-batch.md, video-prompting.md, product.json, RENDERS.md
and product-bible.md.

## 2026-10-30 — Wolverine Stack: borrowed winners (branch `wolverine-skill`)
Logged before editing. Same as the Spartan Stack: Emily's "use GHK and Sermorelin visuals, rugged manly men", approved by Priestley.
New `references/winners/winners.md` (5 statics + 2 videos from the Sermorelin / GHK men's winners, linked, with take / swap / never
copy), referenced from SKILL.md and image-batch.md.

## 2026-10-30 — Wolverine Stack skill setup (branch `wolverine-skill`, from `main` 4ee62c6)
Logged before editing. New product skill `skills/everlife-wolverine/` (recovery stack, vial, active men 25–55), scaffolded with the
new-product builder from the `everlife-bpc-157` template and adapted with the same script as the Spartan Stack. Bible checked first:
no changes; Wolverine disclaimer ✅. Vial render from Priestley's download (`asset-library/VIALS/WOLVERINE/WOLVERINE VIAL.jpg`).
**⛔ Generation blocked:** the vial label (BPC-157 + TB-500, two peptides) contradicts the bible page (BPC-157/KPV/TB500,
"3-peptide"); Spartan is the mirror image. Also PENDING: all 4 headlines (⏳; "Recover Like Wolverine" ⚠ Marvel IP + implied
healing), offer ([PLACEHOLDER]). Includes the `bible_sync --check` "bible_section" commit cherry-picked from `spartan-skill`.
Setup only: no credits, no push, no PR until every skill is tested.
- Adapted like Spartan (originals in `_originals/2026-10-30/skills/everlife-wolverine/`), plus: "inflammation" stays banned except the
  bible's exact "Supports Healthy Inflammatory Balance"; product.json `bible_section` set.
- `core/tests/regression.py`: 4 Wolverine checks (static disclaimer, wrong disclaimer refused, end cards default + tiktok, looked at
  both; the black vial is low-contrast on the dark default card, watch it). Smoke 22/22. `bible_sync --check`: Wolverine ✅.

## 2026-10-30 — Creative bible: the live artifact is the source; repo copy synced from it (branch bible-live-sync)
Logged before editing. The bible now lives as a shared claude.ai artifact (visible to the whole Everlife org):
https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG (replaces the Claude Design project, which closes 14 Dec 2026).
Priestley: reference it from the repo so Mitansh and every teammate's Claude use the same bible.
- `core/scripts/bible_sync.py`: converts the artifact's HTML (as saved by Claude's Artifact read) into
  `core/claude/creative-bible.md` (one `##` section per product, badges kept: Weak / Pending approval / Hard NO conflict /
  Approved by JL) and reports what changed per section; `--check` verifies every product skill's disclaimer against it.
- `core/claude/creative-bible.md`: replaced by the sync of the live artifact (version 1793291361-2416, read 30 Oct 2026).
  Real changes vs the 29 Oct PDF import: new global "08 · Women's color & typography" (pinks, tans, neutrals, warm tones
  + more white and teal, white for advertorials, preferences not limits); Lovara direction gains the same colour line;
  "Approved by JL" on TB-500, Tesamorelin/Ipamorelin, GHK-Cu/Epithalon; a "Landing page & email disclaimer" block.
  Products unchanged otherwise (Spark, Lovara, MOTS-c, Spartan, Wolverine identical).
- `core/claude/everlife-team.md` + `README.md`: where the live bible is and the "check the bible for updates" steps.
- Not changed here (flagged): the gates file's women's palette line now conflicts with the bible's new global section.
Originals in `_originals/2026-10-30/bible-live-sync/`.

## 2026-10-29 — Day-1 onboarding for non-technical teammates (branch onboarding-day-one)
Logged before editing. Priestley: help a non-technical person start using the repo and the skills as smoothly as possible.
- `ONBOARDING.md`: rewritten as a Day-1 guide for a brand-new person (before you start: GitHub invite, Claude Code,
  Apple developer tools; one pasted setup prompt that signs in to GitHub, downloads the repo and installs everything;
  logins; first test batch; a "what to type" cheat sheet; who to ask). The version-2 upgrade guide it replaces is kept
  in `_originals/2026-10-29/onboarding-day-one/`.
- `core/claude/everlife-gates.md`: the EverlifeMD creative gates (copied verbatim from Priestley's ~/.claude/CLAUDE.md)
  and `core/claude/creative-bible.md` (the bible v3 import from ~/.claude/everlife/), so every teammate works under the
  same rules. **Jeremy to confirm before merge** (the gates are the compliance checklist).
- `install.sh`: also adds the gates to the user's ~/.claude/CLAUDE.md as one managed import block (skipped when the
  gates are already there; an existing CLAUDE.md is backed up, never replaced), links the bible to
  ~/.claude/everlife/creative-bible.md when the user has none, and adds a short list of read-only commands to Claude
  Code's allow list (never anything that spends credits).
- `core/scripts/update.sh`: "update my ad tools" in one step (pull main, re-link skills, re-install the toolkit, check).
- `README.md`: setup section points to ONBOARDING.md and update.sh.
Originals in `_originals/2026-10-29/onboarding-day-one/`.
- Follow-up (logged before editing): ONBOARDING.md also connects the **Creatify general server** (`claude mcp add
  --transport http --scope user creatify https://api.creatify.ai/mcp`, sign-in via `/mcp`), which the image setup needs
  for the Nano Banana models (the Ad Agent plugin only runs GPT Image 2.5). Same Everlife Creatify account and credits.
- Follow-up (logged before editing): Mitansh aligned `core/claude/everlife-gates.md` with his tested local rules (no
  Asana-brief stop; product.json disclaimer when the bible has none; known gaps). Priestley: follow Mitansh on those, but
  **keep our women's palette rule** (bible v3: "no oranges or greens" applies only to GHK-Cu Cream and Glow Stack; other
  women's creative has no palette limit; Justin's Sermorelin GHK direction allows teal/white). Mitansh has not tested
  women's ads. Restored that one line.
- Follow-up (logged before editing): Priestley reverted that: the women's palette line follows Mitansh's version
  ("Women's creative (incl. GHK cream): pinks, tans, beige — no oranges or greens."). Note: the Sermorelin GHK skill's
  women's colour rules (Justin, teal/white) are looser than this gate; the gate wins.
- Follow-up (logged before editing): Priestley: the women's palette applies to Sermorelin too. Both Sermorelin skills
  (GHK + plain) now use pinks, tans, beige (cream / warm white as neutral backgrounds); no oranges or greens, teal
  included; the real product keeps its colours (green-teal GHK tablet, plain Sermorelin's orange label). Replaces
  Justin's 29 Oct direction (white + teal, "no colour banned", explore slots, >=1 teal ad): tell Justin.
  Files: GHK SKILL.md, image-batch.md §2b + template, lessons.md, product-bible.md note; plain Sermorelin SKILL.md,
  image-batch.md §2b + checklist + template, video-prompting.md, product-bible.md. Originals in
  `_originals/2026-10-29/sermorelin-womens-palette/`.
- Follow-up (logged before editing): **reverted** the entry above (commit 382c1be). It came from a misread question
  ("did Justin's GHK suggestion apply to plain Sermorelin too?"), not a request. Both Sermorelin skills are back to
  Justin's women's colour direction; the gates keep Mitansh's palette line. Open: which rule wins for Sermorelin
  women's ads (ask Justin).
- Follow-up (logged before editing): Priestley: keep Justin's women's colour direction for **Sermorelin and Sermorelin
  GHK**. The gates' palette line keeps Mitansh's wording for every other product and gains that exception (pinks,
  tans, neutrals, warm tones preferred; white and teal welcome, white for advertorials; preferences, not limits).
- Follow-up (logged before editing): **zip distribution** (Priestley: the team may get a zipped folder instead of GitHub).
  New `ONBOARDING-ZIP.md` (no GitHub account: unzip to ~/everlife-ad-factory, one pasted setup prompt, updates = a new
  zip); `core/scripts/make_zip.sh` builds the zip from a git commit (`git archive`: no .git, no _originals, symlinks
  kept; tested with Finder/ditto and unzip); `update.sh` works without git (zip installs: skips the pull, re-installs
  and checks); `install.sh` re-creates a skill's `core` link if an unzip tool flattened it. README points to both.
  Originals in `_originals/2026-10-29/onboarding-zip/`.
- Follow-up (logged before editing): **Windows support via WSL** (Priestley: "don't limit to Mac"). The tools run
  unchanged inside WSL (Ubuntu): bash, symlinks, Python venv, the bundled ffmpeg. The one blocker was Apple system
  fonts (Avenir Next, Helvetica Neue, Baskerville, Arial Unicode): `core/tools/build_layers.py` `font()` now falls
  back to the bundled open fonts when an Apple font file is missing (sans → Inter, Baskerville → Fraunces, weight
  matched by name). **Mac output unchanged** (regression identical); Windows videos use Inter/Fraunces, so they look
  slightly different (Mitansh to review). Both onboarding guides gain a Windows section (install WSL + Ubuntu, Claude
  Code inside Ubuntu, unzip/clone into the Linux home, open outputs with explorer.exe). Originals in
  `_originals/2026-10-29/windows-wsl/`.
- Follow-up (logged before editing): both guides made exact enough for Claude Code to follow from the start:
  the official Claude Code install (`curl -fsSL https://claude.ai/install.sh | bash`, Mac/Linux/WSL, from
  code.claude.com/docs/en/setup; paid Claude plan required) replaces "ask Mitansh"; the GitHub CLI step is an exact
  command (latest release for macOS/Linux and the chip, into ~/.local/bin; tested on Apple silicon, Linux URL checked);
  the `/mcp` names match what Claude Code shows (`plugin:creatify-ad-agent:creatify-ad-agent`, `creatify`); and a
  "read the guide and set me up" shortcut once the folder is on the computer.

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
- `references/winners/`: ⭐ all-time section from the Meta exports the user downloaded ("All-Time Top Ads by Account",
  monthly "Top Ads by CPA" Jan–Jul 2025): Sermorelin target $400 / max $500; top sellers 273393-3.01 (454 sales),
  281319-1.01 (332), 273400-2.04 (women, 137 at $248). Proven mechanic = one tablet held to the lens (~1,500 sales):
  now batch slot 1 and marked ⭐ in style 4B. Video winners listed by ID; their files aren't on this Mac.
- Reference priority (1 winners → 2 Meta → 3 Pinterest) wired into plain Sermorelin like Sermorelin GHK:
  `core/references/REFERENCE-PRIORITY.md` and `core/references/meta-refs/SOURCES.md` copied **byte-identical** from branch
  `sermorelin-first-batch` (so the merge is clean). ⚠ After both branches merge, update its line "Wired into: Sermorelin
  GHK only" to include plain Sermorelin (not edited here, to avoid a conflict).
- `references/pinterest/`: the same 19 screened pins as Sermorelin GHK, re-checked for plain Sermorelin, with a new
  header (best fits, green/orange backgrounds banned for women, wording traps). SKILL.md + image-batch §2 follow the order.
- Pinterest, Restora method: Restora-Z's set (Mitansh's package; board links never recorded) is ~70 pins of **same-category**
  modern DTC ads (sleep brands) + 20 DOC examples, sorted into 12 ad types; the GHK set was generic idea-page searches.
  A helper agent searched ~65 Pinterest Ideas pages (~735 pins) for men's health / healthy aging / longevity / women 40+
  wellness ads; Claude looked at all 66 shortlisted and kept 58 (`references/pinterest/<type>/cat_*.jpg`, 7 MB) with a
  table (layout to take, what not to copy, source page). Dropped 8 (same-person before/after, abs shot, intimate, lips
  macro, sauna towel, stroke ad, duplicate). Still thin: sticky notes, men 50+ training, "new and improved" side-by-sides.

## 2026-10-29 — First real test of the plain Sermorelin skill (branch `sermorelin`)
Approved by Priestley: 1 Seedance video (480p, 45 Higgsfield cr) + 5 Creatify statics (6 cr incl. one re-roll).
Output + hand-off sheet: `~/Everlife-Creative/output/Sermorelin/2026-10-29_SESSION.md`. Finishing ran on this branch's toolkit.
- Video: generated, QA'd, finished end to end (FINAL_SERM01, draft). Product correct (round "S" tablet, label, no vial).
  **Defect: the voice says "Sermoral"**; VO ran to 14.8 s. **Fixed the same day:** re-voiced with a Creatify TTS line
  (voice Fabian, 0.1 cr), verified by Whisper, ends at 11.0 s; re-finished as `FINAL_SERM01_15s_9x16.mp4`.
- Statics: 4 finished (FINAL_1–4), product exact in all; #5 flagged, not shipped (bottle label text garbled twice).
- Creatify project created (`assets/creatify.json`). Skill fixes from the test: `"style": "default"` is the house look
  (docs said `house`, which crashes); lessons (voice, word budget ≤ 22, small-label garbling, bottle above the footer);
  image prompt LAYOUT now sizes/places the bottle; finishing notes how to run the branch toolkit without `--install`.

## 2026-10-29 — Plain Sermorelin aligned with bible v3 + the GHK hand-off (branch `sermorelin`)
Sources: bible v3 (`~/.claude/everlife/creative-bible.md`, imported 2026-10-29, pages 4 + 7–10) and
`~/Downloads/Sermorelin-handoff-2026-10-29.md` (from the GHK session, PR #4). Skill files only (`skills/everlife-sermorelin/`);
originals in `_originals/2026-10-29/skills/everlife-sermorelin/`. No GHK claims, headlines or casting quotes copied.
- `product-bible.md`: verbatim section re-copied from v3. New: men's talent line ("rugged, strong and unmistakably
  masculine…"), "Supports Sleep Quality + Recovery" (both), "2x-Strength Growth Hormone Support" (men),
  "Supports Toned Strength After 35" (women). Pre-screen: sleep/recovery ✅, 2x-Strength ✅ with care (1000 mcg only),
  Toned Strength ⚠ Jeremy. Women's "no orange/green" limit removed (v3 keeps it only for GHK-Cu Cream and Glow Stack).
- Images: winners lead (≥ 3 of every 5 slots); tablet held (thumb + index "pull" or open palm, beside the bottle);
  per-ad font + colour menu, no elegant/italic serif or script on men's headlines; Justin's women's colour direction
  (preferred incl. white + teal, advertorials on white, ≥ 1 teal ad, ≤ 1 pink-led, ≤ 2 of 5 explore); "SERMORELIN by
  Everlife" on every ad; product ends above 72%, text above 76%, calm top 14% / bottom 22%.
- Video: 15 s, end card 11–15 s, speech ≤ 20 words from the first second, finished by ~10.5 s; hook by 2.5 s;
  "Sermorelin by Everlife" in the first line and header (`"head": ["SERMORELIN BY EVERLIFE"]`, `"head_always": true`);
  men cast 42–50 "fit silver fox", hardcore fitness-model build, fully clothed (replaces "natural build, not a
  bodybuilder"; ⚠ the global CLAUDE.md still says "not bodybuilders"); cloned-voice product line for on-camera actors
  (Marketing Studio), Creatify TTS stays for no-dialogue Seedance cuts.
- Also brought in line: `SKILL.md`, `finishing.md` (§1a header, §1b voice, `--end 11`), `lessons.md` (GHK's 29 Oct
  lessons), `styles/1-real-people.md`, `4-product-hero.md`, `6-lifestyle-identity.md` (casting, colours).
- Needs PR #4 merged into `main` (then `main` into this branch) for `head_always`, the bible-v3 logo size and the 2-line
  disclaimer; until then this branch's finishers ignore `head_always` and keep the old logo/disclaimer.

## 2026-10-29 — `main` (with PR #4) merged into `sermorelin`
PR #4 merged into `main` (ec0f334, Priestley's go-ahead), then `main` into this branch. Our versions backed up in
`_originals/2026-10-29/` (`core/tools/styles.py`, `core/references/REFERENCE-PRIORITY.md`, `CHANGELOG.md`). Conflicts:
- `core/tools/styles.py`: kept both: our `pill_scale` (round tablet smaller on the end card) and main's cap that keeps a
  tall tablet off the label line.
- `core/references/REFERENCE-PRIORITY.md`: main's version (adds "winners lead the batch"), plus plain Sermorelin in
  "Wired into" and its 58 same-category Pinterest ads.
- `CHANGELOG.md`: every entry from both sides kept.
Now live here: `head_always`, bible-v3 logo size (31% / 40%), 2-line disclaimer, logo at the top of statics.

## 2026-10-29 — Plain Sermorelin 500 mcg bottle added (branch `sermorelin`)
`assets/sermorelin500_bottle.png` (user download "SERMORELIN 500 MCG BOTTLE .png", looked at and pixel-diffed against
the 1000 render: same jar and label, only the strength line and a re-set name band differ) + `sermorelin500_bottle_ref.jpg`
(flattened on white). `product.json` already pointed at these names. `MISSING_RENDERS.md` (original backed up) and
`image-batch.md` updated. The downloaded tablet is identical to the one on file.

## 2026-10-29 — Plain Sermorelin: second video winner card (branch `sermorelin`)
Priestley shared the "Sermorelin M" / "Sermorelin F" Drive folders (Emily's): the same folders as the 2026-10-28 zips;
the Drive connector can't list them. Re-checking the men's zip found winner 274068Video-2.01 (18 sales, $364) under
another filename: looked at, carded as MV2 in `winners/winners.md` (original backed up) with `MV2_274068Video.jpg`.
Then the men's zip's Base56 / Base57 videos (Aug 2026), which the all-time export lists as winners (Base56-05 13 sales):
watched + transcribed, carded as MV3 (Base56, 28 s framed monster battle) and MV4 (Base57, 11 s viking split frame) with
`MV3_BASE56.jpg` / `MV4_BASE57.jpg`. The "Sermorelin F" zip has no videos.

## 2026-10-29 — Plain Sermorelin: 9:16 static layout for the Reels-safe footer (branch `sermorelin`)
Ahead of Mitansh's PR #5 (open): `image-batch.md` (original from earlier today in `_originals/2026-10-29/`) now has a
separate 9:16 LAYOUT (content in the top half, lowest element asked at 40%, bottom 55% calm) and a note pointing at the
shared safe-zone rule as the source of truth, with the 1-credit reposition fix. Skill file only; the finisher change
arrives with PR #5. Not pushed (Priestley: no push for now).

## 2026-10-29 — Plain Sermorelin images: no "by Everlife" (branch `sermorelin`)
Priestley, after the second test: images never say "by Everlife"; the name reads "SERMORELIN" only (the finisher's
Everlife logo carries the brand). This overrides bible v3's "[Product] by Everlife in every intro" for statics only;
videos keep it in the header and first spoken line. Changed: `SKILL.md`, `image-batch.md` (template Name line + QA),
`product-bible.md` (Intro fact). Originals of today's versions in `_originals/2026-10-29b/`.
Then (Priestley: "why is it the same guy in every picture?", "women have no product name?"): `image-batch.md` now
requires a different person per ad (own CAST per ad: age, ethnicity, hair, beard, wardrobe) and QA rejects look-alikes;
QA also requires "SERMORELIN" as one of the two biggest texts. Originals in `_originals/2026-10-29c/`.

## 2026-10-29 — `main` (with PR #5, PT-141 + Reels-safe footer) merged into `sermorelin`
PR #5 merged into `main` by the other session (24045d7); then `main` into this branch (local, not pushed). Our versions
backed up in `_originals/2026-10-29c/`. Conflicts: `core/tools/full_layout.py` + `styles.py` (×2): kept main's "no
tablet → bottle alone, centred" branch (PT-141 spray) with our `pill_scale` inside it; `CHANGELOG.md`: both sides kept.

## 2026-10-29 — Plain Sermorelin video composition for the Reels-safe footer (branch `sermorelin`)
`video-prompting.md` (original in `_originals/2026-10-29c/`): key action now 8–55% of the frame height, bottom 45%
background only (was 8–63%). Since PR #5 the 9:16 video footer + captions sit at ~55–72%; the re-finished test video
had the bottle label under the footer. Only this skill (Priestley: "just update our Sermorelin skill for now"); the
GHK, PT-141 and Restora video prompts still say 8–63%. Known, not fixed here: the 9:16 video disclaimer wraps to 3
lines in safe mode (shared `full_layout.py`).
Then: the regenerated video's man came out as a Sylvester Stallone look-alike (rejected, not finished). Casting in
`video-prompting.md` + `image-batch.md` now always names a specific look and adds "ordinary, non-famous face; must not
resemble any celebrity"; `lessons.md` adds that and the upload-ID workaround for repeated "no response received".
## 2026-10-29 — `main` (with PR #7, GHK bottom disclaimer) merged into `sermorelin`; plain Sermorelin opts in
PR #7 merged by the other session (20:41); then `main` into this branch (local, not pushed). Ours backed up in
`_originals/2026-10-29d/`. Conflicts: `styles.py` (kept main's end-card shift `dy`/`pw` with our `pill_scale` on `pw`),
`full_layout.py` (both setting lines kept), `CHANGELOG.md` (both sides kept).
Plain Sermorelin now matches Sermorelin GHK (Priestley: "disclaimer should be two lines at the bottom"):
- `product.json`: `"disclaimer_at": "bottom"`, `"end_card_safe_shift": true`, `keep_case` + "Sermorelin by Everlife".
- `video-prompting.md`: action 8–58%, full-bleed scene (GHK's numbers). `image-batch.md`: 9:16 LAYOUT = GHK's (text in
  the central column, pictures full-bleed down to 56%) + the bottom-disclaimer note. `finishing.md`: stale PR #4 note
  replaced by the 9:16 footer description.
## 2026-10-29 — Animated still (BPC-157): approved static + 8 s Seedance motion
New Question A option in `skills/everlife-bpc-157` (`references/animated-still.md`): the batch RAW goes to Seedance image-to-video
(8 s, 9:16; Unlimited mode in Chrome for 0 credits, else CLI ≈ 36–56 cr), then the new shared `core/tools/animate_still.py` lays the
logo + proof footer on every frame (`finish_batch.finish()` is now a reusable function; CLI unchanged). Reference V43 (Sculptra video
pin) added to `vial-refs/`. Tested on a synthetic 3 s clip; smoke 12/12.

## 2026-10-29 — Batch default 4 (Mitansh): Creatify runs 4 image tasks per project at once, so a batch of 4 finishes in one wave;
the size question is now 4 / 8 / 12 in every skill and the onboarding guide.

## 2026-10-29 — Image model choice per batch (Mitansh: "Claude asks which image generation model to use for this batch of 5")
All images stay on Creatify. The Ad Agent connector only runs GPT Image 2.5 (tested: a request for another model still renders on
gpt-image-2.5-sunburst), so Nano Banana runs through Creatify's general MCP server (`claude mcp add --transport http --scope user
creatify https://api.creatify.ai/mcp`, sign in with `/mcp`): its Model Playground tools (`model_playground_list_models /
get_model_schema / generate / get`) take any Creatify image model and bill the same workspace credits. Reference renders are uploaded
once with `upload_file` and their cdn_url kept in each skill's `assets/creatify.json`. `core/tools/creatify_gen.py` (REST + API key in
`~/Everlife-Creative/creatify.env`) stays as a fallback. Every skill's image setup round now asks
"Image model" with three options (Mitansh: GPT Image 2.5 via the connector, Nano Banana 2.1, Nano Banana Pro); rules in `core/references/image-models.md`; preflight reports whether the key file exists.
Prices from Creatify's model docs are in `image-models.md` (e.g. Nano Banana 2.1 = 1.0 credit at 1K, Seedream 5 Pro / Flux 2 Pro = 0.5,
GPT Image 2.5 = 1.0 at quality high); the API spends Creatify API-plan credits, a separate pool from the workspace credits the
connector uses. Untested against the live API until an API key is on this machine.

## 2026-10-29 — BPC-157 skill (recovery peptide, Rx vial), built from the BPC-157 creative messaging docx
`skills/everlife-bpc-157/`: SKILL.md modelled on the Restora-Z question flow (Question A, then one round: audience Men/Women/Both ·
form vial/capsule/either · angle mix/bottleneck/comeback/inside-out · boldness; images add mood/density/people/how many), product.json
vial-only (Mitansh: the vial render is the only product image; label 3 mg/mL · 5 mL confirmed, the docx offer's 2.5 mg/mL · 6 mL is
stale; the capsule form is out of scope), bible extract with a compliance
pre-screen (the docx's section 6 "approved benefits" is blocked as direct claims; the glow/skin hooks ⚠; one pronoun question ❌; three
"Image – Pending approval" headlines ⏳), image-batch with the vial/capsule prompt template and a no-needle rule in every block,
video-prompting, finishing, reference guide, personas (Lifter Marcus / Pilates Dana), lessons, 6 style files, and `mens-direction.md`
(Mitansh: men's ads extremely masculine: hardcore gym, barbells, bodybuilders, tattoos; the Sermorelin "not bodybuilders" rule is
product-specific and does not apply; references = team style boards Fighter UFC / Hero Fitness Guy / Retro, Sermorelin male winners M2/M3/M8).
- Disclaimer: not in the docx or the bible; Mitansh confirmed the PT-141 wording for BPC-157 (Jeremy to sign off). While it was
  missing, `core/tools/product.py` gained a guard that refuses to load any product with an empty disclaimer (kept: compliance gate
  for every product). Smoke 12/12.
- `core/scripts/preflight.sh`: a product with no pill render (PILL="") passes the render check and gets a bottle-only Marketing Studio
  create command.
- Open: Jeremy's sign-off on the disclaimer wording; Marketing Studio registration on the first session; live product page 404 on 2026-10-29 (renders verified against the asset library only).

## 2026-10-29 — tiktok end-card safe-area shift becomes a product opt-in (Restora-Z stays as on main)
Logged before editing. Pre-merge regression (main vs this branch) showed Restora-Z's tiktok end card changed (5 layers):
our safe-area fix (card 44 px lower, tablet 250 px) applied to every product. Priestley: keep Restora unchanged.
- `core/tools/styles.py`: the shift applies only when the product opts in (`C["_end_safe_shift"]`); otherwise main's
  layout (no shift, 300 px tablet).
- `core/tools/full_layout.py`: passes product.json `"end_card_safe_shift"` to the style.
- `skills/everlife-sermorelin-ghk/product.json`: `"end_card_safe_shift": true`.
Mitansh can roll it out to every product later (flip the default in styles.py). Originals in `_originals/2026-10-29/end-card-opt-in/`.

## 2026-10-29 — Sermorelin GHK lesson: never place the product name "beside" a prop
Logged before editing. Batch-9 ad 5: "SERMORELIN GHK" asked "beside the bottle on the right" landed on the coffee mug and
read as a mug print. `references/image-batch.md` §2c + `lessons.md`: name placements are fixed text positions (top, under
the headline, lower-third band, split panel), never "beside" an object; props stay plain.

## 2026-10-29 — Sermorelin GHK: per-batch variety plan (scene, light, composition, name placement), men + women
Logged before editing. Batch 9 (men) came out as five near-identical dark-gym ads ("is it always using the same theme?").
Root causes: the variety rules covered font, accent, ad type, headline and hold but not scene / light / composition;
winners-first carried the winners' dark-gym mood along with their layout; the men's "hardcore training" direction (meant for
casting) was applied to every scene; the 9:16 safe-zone layout + "name big" + "tablet held" settled into one composition;
all prompts written from one template in one pass. Approved by Priestley for men and women.
- `skills/everlife-sermorelin-ghk/references/image-batch.md`: new §2c "Variety plan" (scene, light, composition, name
  placement rotations; distinct per ad; men max 2 gym scenes; at least 2 of 5 bright; winners give layout only; the men's
  direction is casting, not scenery); the approval table gains scene · light · composition columns; the men's scene line
  in the template no longer fixes a dark palette; contact-sheet check after generation.
- `references/lessons.md`: the root cause.
Originals in `_originals/2026-10-29/variety-plan/`.

## 2026-10-29 — Sermorelin GHK 9:16: 2-line bottom disclaimer; pictures use more of the frame (team feedback)
Logged before editing. Feedback on the latest image with the bottom disclaimer: "always keep that disclaimer to 2 lines
total (not 3)" and "use as much of the artboard as possible around the safe zones".
- `core/tools/finish_batch.py` + `full_layout.py` (only with the product's `"disclaimer_at": "bottom"`): the bottom
  disclaimer fits 2 lines across the full width (≈19 px for the Sermorelin GHK text; never below the 13 px minimum).
- `skills/everlife-sermorelin-ghk/references/image-batch.md` 9:16 LAYOUT: only TEXT (logo band, headline, lines, badges)
  is held to the safe column; pictures (product, hands, people, background) run full-bleed and down to ~64% of the height
  (just above the Trustpilot row at y ≈1280); ask for the lowest element at ~56% because the model lands it lower.
- `references/video-prompting.md` block 7: faces / product / hands between 8% and 58% (captions now sit just above the
  Trustpilot row), full-bleed scene.
Originals in `_originals/2026-10-29/disc2-fullbleed/`.

## 2026-10-29 — Sermorelin GHK setup question: women's colour note brought in line with Justin's direction
Logged before editing. SKILL.md step 1 still said "Women → pinks, tans, beige; never orange or green" (pre-Justin). Now
points to image-batch.md §2b (preferred pinks/tans/neutrals/warm/white/teal, no colour banned) and adds the men's casting.

## 2026-10-29 — Sermorelin GHK 9:16: disclaimer alone at the very bottom (product opt-in; Restora / PT-141 unchanged)
Logged before editing. Team feedback relayed by Priestley: "Disclaimer should always be nested at very bottom" — only the
disclaimer; the Trustpilot / Doctor Prescribed / Ships Free row stays in the Meta safe area (Mitansh's footer). Scoped to
Sermorelin GHK until Mitansh updates the shared core ("for now keep it to us").
- `skills/everlife-sermorelin-ghk/product.json`: `"disclaimer_at": "bottom"`.
- `core/tools/finish_batch.py` (9:16): when the product sets it, the proof row ends at y 1385 as before and the verbatim
  disclaimer is drawn alone, full width (W−80), ending 40 px above the frame bottom, on a soft band.
- `core/tools/full_layout.py` (9:16 video): same split; captions sit above the proof row. The bottom disclaimer is an
  intentional exception to the safe-area check (it sits in Reels' bottom 535 px, so Reels' caption/CTA can partly cover
  it; Stories shows it below the reply bar) — flagged for Jeremy.
Products without the key render exactly as before. Also `styles.py`: with the `head_always` product line, a two-line tiktok end
headline moves the bottle 18 px lower so its cap clears the text; `full_layout.py` keeps captions above the Reels profile
corner when the disclaimer is at the bottom. Originals in `_originals/2026-10-29/disclaimer-bottom/`.

## 2026-10-29 — Merged main after PR #5 (Mitansh's pt-141-skill) into `sermorelin-first-batch`: Mitansh's version kept
Merged origin/main (24045d7, PR #5) into this branch. Shared tools taken from main exactly (`finish_batch.py`,
`safezones.py` identical to main); our additive features re-applied on top of his code: `full_layout.py` per-job
`"proof_at"` override; `styles.py` TikTok end card safe-area fit (+44 px, 250 px tablet, on top of his tall-pill guard) and
the `head_always` product line on the end card. Sermorelin GHK guides: Mitansh's text kept; our final-test lessons restored.
Check: vs new main only the 5 tiktok end-card layers differ (expected); smoke 12/12; preflights Sermorelin GHK 10/10,
Restora 10/10, PT-141 9/10 (not registered in Marketing Studio). Test render of Boxing v2 OK.
Incident: running preflight from a temporary PR #5 checkout re-linked `~/.claude/skills/everlife-{sermorelin-ghk,restora-z,
pt-141}` to that checkout (then deleted); re-linked to this repo. Lesson: never run `preflight.sh` from a temporary
worktree (its step 0 re-links the installed skill).

## 2026-10-29 — "Sermorelin GHK by Everlife" on the end card too, with a lowercase "by" (branch `sermorelin-first-batch`)
Logged before editing. Priestley: the product line should show the whole time (end card included) and read "by", not "By".
- `skills/everlife-sermorelin-ghk/product.json` `keep_case`: adds "Sermorelin GHK by Everlife" (first), so the title-cased
  header keeps a lowercase "by".
- `core/tools/styles.py` TikTok end card: when a job sets `"head_always"`, the header line is drawn under the logo on the
  end card too and the card moves down 44 px more (only jobs with `head_always`; other output unchanged).
Originals in `_originals/2026-10-29/brandline/`.

## 2026-10-29 — Sermorelin GHK lessons: re-check captions after every re-cut; no dead air (branch `sermorelin-first-batch`)
Logged before editing. Morning v2 showed "CERMERELLIN": re-running `full_layout.py` on a re-cut clip re-transcribed and
overwrote the hand-fixed captions. Boxing v2 "stopped": ~2 s with no speech and a still shot before the end card.
- `skills/everlife-sermorelin-ghk/references/lessons.md`: rewrite `<Tag>_caps.json` after every re-cut and check the
  printed caption list before sharing; cut on action right after the last line; no silent gap > 0.5 s mid-line (trim
  pauses inside cloned takes); put room tone under a held/silent end card.

## 2026-10-29 — tiktok end card fits the 9:16 safe-area layout (shared tool; tell Mitansh)
Logged before editing. With the safe-area footer (Mitansh's default) the end card is no longer shifted down, so its
headline touched the bigger logo and the 300 px tablet overlapped the "Sermorelin + GHK + Citrulline" label (seen in the
Boxing v2 / Morning v2 drafts). Approved by Priestley.
- `core/tools/styles.py` TikTok end card: in safe mode the whole card moves down 44 px and the tablet render is 250 px
  (bottom mode unchanged: 0 / 300). CTA still ends well above the proof block.
Expected regression differences: tiktok end-card layers only. Originals in `_originals/2026-10-29/endcard-safe/`.

## 2026-10-29 — Merged Mitansh's PR #5 (`pt-141-skill`) into `sermorelin-first-batch`: Mitansh's changes kept
Priestley: "keep Mitansh changes all". Merged origin/main (PR #4) and origin/pt-141-skill; every overlap resolved to
Mitansh's version: 9:16 footer in the Meta safe area by default for all products (ends at y 1385, may cross the Reels
profile notch), his disclaimer wrapping, logo ≈1.55× (LOGO_W 311 / video 435), the raw-content refusal (`--fit force`).
Dropped from our side: `finish_batch.py --proof-at safe` and the sample-matched footer (uncommitted, saved as a patch in the
session scratchpad), the 2-line/3-line disclaimer fitting, the bible-v3 31%/40% logo sizes, the +28 px header and +30 px
end-card nudges. Kept (no overlap, off unless a job asks): `"head_always"` and per-job `"proof_at"` in `full_layout.py`;
`"end_rows": "benefits"` in `styles.py`; the hidden-pixel preflight warning. Sermorelin GHK skill text aligned (no
`--proof-at`; 9:16 raws keep content in the top ~52%). Regression vs Mitansh's branch: 121/121 identical; smoke 12/12.
Note: CLAUDE.md-level rule "follow the bible" for the Reels notch was superseded by this choice.

## 2026-10-29 — Sermorelin GHK: 9:16 statics test (safe zone) and the workflow that passed (branch `sermorelin-first-batch`)
Logged before editing. Test (1 men + 1 women, 9:16, `--proof-at safe`): first takes failed (the model put the product
low, the footer covered the tablet / label; men's pills ran into the side zones). Priestley chose "native 9:16 + fix
edits". What passed: one reposition edit per image (top 15% empty, all text 15% in from the sides, product ends above
52%, below 55% calm) and, if the finisher's logo nudge pushes the product into the footer, `--shift <px>` (60 worked).
- `skills/everlife-sermorelin-ghk/references/image-batch.md` (9:16 note) + `lessons.md`: that workflow.
Cost of the test: 4 Creatify credits.

## 2026-10-29 — Static finisher: stronger backing behind the 9:16 safe-zone footer (branch `sermorelin-first-batch`)
Logged before editing. Priestley: "the footer should be clearly visible". In `--proof-at safe` the band behind the
Trustpilot row + disclaimer is now ~88% opaque (was ~73%); `scrim()` gains an `opacity` argument (default unchanged, so
the bottom footer and Restora output are identical). No cropping: the image stays full-frame.

## 2026-10-29 — Static finisher: safe-zone footer for 9:16 image ads (opt-in) (branch `sermorelin-first-batch`)
Logged before editing. Priestley: safe zones "should" apply to images too. 9:16 statics put the Trustpilot row and the
disclaimer at the very bottom (Reels bottom 535 px; proof row partly in the Stories reply box). 4:5 / 1:1 feed ads have no
Meta overlay and are unchanged.
- `core/tools/finish_batch.py`: new `--proof-at safe` (9:16 only): the proof row + disclaimer sit inside the safe column
  (x 156–924), ending above y 1206 (Reels notch), disclaimer up to 3 lines (~17 px) like the videos; a soft band behind it.
  Default stays `bottom` (Restora unaffected).
- `skills/everlife-sermorelin-ghk/references/image-batch.md` + `finishing.md`: Sermorelin GHK 9:16 statics finish with
  `--proof-at safe`; the 9:16 prompt keeps the product and text in the top ~55% (8–55%).
Originals in `_originals/2026-10-29/static-safe/`.

## 2026-10-29 — Sermorelin GHK: compose videos for the safe-zone footer (branch `sermorelin-first-batch`)
Logged before editing. Re-finishing today's four videos with `"proof_at": "safe"` put the captions, Trustpilot row and
disclaimer across the product shots (tablet and "SERMORELIN GHK" label covered in Gym, Pilates, Boxing): those videos
were composed for the bottom footer. The four finals were restored to the bottom footer (safe versions kept as
`out/SAFE_MODE_*.mp4`). For new videos:
- `skills/everlife-sermorelin-ghk/references/video-prompting.md` prompt block 7: faces, bottle, tablet, hands and key
  action between 8% and 50% of the frame height (the safe-mode captions + footer sit at ~52–63%); the bottom 50% is calm
  background (table, floor, torso out of focus).

## 2026-10-29 — Sermorelin GHK videos: safe-zone footer + product-line opener (branch `sermorelin-first-batch`)
Logged before editing. Priestley, after the Stories safe-zone template ("Safe Zone - Story.jpg") showed our captions in
the reply-bar box and the proof/disclaimer in the Reels bottom 535 px (bible v3 "Safe zones": keep them out):
- `core/tools/full_layout.py`: copy.json `"proof_at": "safe"` puts captions, proof row and disclaimer inside the safe area
  for that video (per job; default stays "bottom", Restora unaffected). In safe mode the disclaimer may use 3 lines
  (~17 px, readable for 50+) instead of 2, because the safe column is only 768 px wide: **exception to bible v3's "two
  lines maximum" for 9:16, flag for Justin.**
- `core/tools/styles.py` + `full_layout.py`: in safe mode the end-card headline starts below the bigger v3 logo (it
  collided with it).
- Emily's feedback ("too long where he is holding the tablet… nothing is happening"; "start off saying Sermorelin GHK
  supports…"): `skills/everlife-sermorelin-ghk/references/video-prompting.md` + `finishing.md`: product name spoken within
  the first 2.5 s in every Sermorelin GHK video; hands-only shots 2 s max and always moving; default opener = a short
  moving product shot with "Sermorelin GHK by Everlife supports…" (other openers allowed if the name lands by 2.5 s);
  copy.json sets `"proof_at": "safe"`.
Originals in `_originals/2026-10-29/safe-mode-opener/`.

## 2026-10-29 — Sermorelin GHK statics: product name without "by Everlife" (branch `sermorelin-first-batch`)
Logged before editing. Priestley: "for Image Ads we don't need 'by Everlife' along with 'Sermorelin GHK'". Statics show
"SERMORELIN GHK" big (the Everlife logo already sits at the top); videos keep "Sermorelin GHK by Everlife" in the header
and the spoken intro (bible v3 "[Product] by Everlife" in intros, scripts and voiceovers).
- `skills/everlife-sermorelin-ghk/references/image-batch.md`: template Name line and QA; `SKILL.md` product truths;
  `references/lessons.md` note.
Originals in `_originals/2026-10-29/statics-name/`.

## 2026-10-29 — 9:16 proof footer back inside the Meta safe area (Mitansh, after a live Reels screenshot)
The bottom-anchored footer (2026-10-27) sat under Meta's "Learn more" button and caption in a real Reels placement
(`core/references/safe-zones/reels_placement_2026-10-29.jpg`; numbers confirmed against the team's Safe zones page).
- `core/tools/safezones.py`: `EVERLIFE_PROOF_AT` defaults to `safe` again (footer ends at y 1385, the bottom of the Reels safe area; the footer may cross the profile notch, Mitansh 2026-10-29); `bottom` kept behind the env var for old jobs. `full_layout.py` / `finish_modern.py` / `styles.py` follow it.
- `core/tools/finish_batch.py`: 9:16 footer ends at y 1385 inside the 768 px safe column (disclaimer wraps to 4 lines), scrim fades
  in above and out below it; refuses (exit 2) when the raw's content runs under the footer (edge-density `content_bottom`);
  safe-zone check on footer + logo; `--fit force` for QA previews. Feed ratios unchanged. A `--fit auto` inset was tried and dropped.
- Prompts: 9:16 LAYOUT block in all three `image-batch.md` (everything in the top 52%, bottom 48% calm), "Footer position" note with
  the one-edit fix for old raws; lessons + finishing.md updated. Smoke 12/12.
- Existing 9:16 finals (PT-141 batches 1–3, Restora batch-2/3 + cosmic-20, Sermorelin batch-1) were composed to the bottom and need
  the reposition edit before re-finishing (credits → user OK).

## 2026-10-28 — Everlife logo bigger at the top (Mitansh: +35%, then +15% more ≈ 1.55×), all products
Shared tools, so every product skill picks it up (`skills/*/core` → `core/`): `finish_batch.py` LOGO_W 200→311; `full_layout.py`
280→435 / 260→404 (LOGO_H strip SY0+70→SY0+80 to clear the taller mark); `build_layers.py` 300→466; `styles.py` 230→358, 240→373,
210→327; `finish_modern.py` 190→296; `core/scripts/finish_image.py` 240→373. Logo asset is 1684×242, so heights grow 29→45 px (batch) and 40→63 px (video).
Originals in `_originals/2026-10-28/logo-135/`. PT-141 batch 2 re-finished with the new size.

## 2026-10-28 — PT-141 skill (branch `pt-141-skill`, local only, not pushed)
New skill `skills/everlife-pt-141/` built with Mitansh: two forms (nasal spray + sublingual tablet, both in scope), audience Men /
Women / Both, the agreed angle ("everyone else sells the ability; PT-141 sells the wanting"; unplanned nights; your body changed).
- `product.json` adds `"forms"` (per-form bottle/pill renders + label wording); copy.json names the form (`"form": "spray|sublingual"`).
- Shared tools: `product.renders_for()`; the pill render is now optional (`full_layout.py`, `build_layers.py`, `styles.py` centre the
  bottle alone when a form has no tablet); `composite.py --form`. Regression vs `logo-top-type-variety`: identical 124 / different 0;
  smoke 12/12. PT-141 end cards rendered for both forms (no credits).
- References: bible page (verbatim + pre-screen + the agreed angle), image-batch (F13 "Portrait + line", form-aware prompt template),
  video-prompting (shoulder-up, no beds), 6 style files, lessons (incl. the creative team's Restora feedback), research brief for the
  Pinterest reference library, 9 team references picked from Emily's PT-141 Drive folder (`references/team-refs/`), winners placeholder.
- Docs fix: the video look key is `default` (house), not `house` (Sermorelin finishing.md corrected too).
- Open: Marketing Studio registration for PT-141 (preflight prints the command); Jeremy on the three "Pending approval" headlines and
  "Gentle on the Vascular System"; a larger transparent tablet render; PT-141 performance data for winner cards; screened reviews.

## 2026-10-29 — Sermorelin GHK: approved headlines and CTAs may be reused (pool exhausted) (branch `sermorelin-first-batch`)
Logged before editing. Every usable bible headline (women) and nearly all (men), plus all 5 bible CTAs, are already in the
copy log. Priestley approved reuse: bible headlines / CTAs may come back, least-recently-used first; never twice in one
batch; never the same headline with the same layout (framework) it had before. Variety comes from layout, casting, colour.
- `skills/everlife-sermorelin-ghk/SKILL.md` golden rule 6 and `references/image-batch.md` §0 updated.
Originals in `_originals/2026-10-29/copy-reuse/`.

## 2026-10-29 — Video header + logo stay on screen the whole time (opt-in; Sermorelin GHK on) (branch `sermorelin-first-batch`)
Logged before editing. Feedback on the men's "Gym" video, relayed by Priestley for men and women: "I would keep
['Sermorelin GHK by Everlife'] up at the top with the logo the whole time." The finisher hid the whole top band (logo +
header) whenever a face moved under it.
- `core/tools/full_layout.py`: new copy.json key `"head_always": true` skips the face check, so the top band (logo + header)
  stays on from 0 s to the end card. Default unchanged (Restora-Z output is not affected).
- `skills/everlife-sermorelin-ghk/references/finishing.md` + `video-prompting.md`: every Sermorelin GHK video sets
  `"head": ["SERMORELIN GHK BY EVERLIFE"]` and `"head_always": true`; prompts keep faces below the top 25% so the header
  never covers a face.
Originals in `_originals/2026-10-29/head-always/`.

## 2026-10-29 — Sermorelin GHK: Justin's women's colour & typography direction (branch `sermorelin-first-batch`)
Logged before editing. Justin (owns Sermorelin GHK marketing), relayed by Priestley: pinks, tans, neutrals and warm tones
"still strongly encouraged"; "incorporate more white and teal", "particularly white backgrounds for advertorial-style
ads"; "preferred options, not strict limitations"; keep exploring current colour and typography trends.
- `skills/everlife-sermorelin-ghk/references/image-batch.md` (§2b, template, QA): no colour banned for women; preferred
  colours (pinks, tans, neutrals, warm tones, white, teal) lead most ads; up to 2 of every 5 women's ads explore new colour
  and type trends; article/advertorial ads on a white background; at least one teal-led or teal-accent ad per women's
  batch; keep teal soft/pale next to the bottle's deep red label; still at most one pink-led ad, no two ads with the same
  lead colour, varied fonts.
- `references/lessons.md`: direction recorded.
Originals in `_originals/2026-10-29/justin-colours/`.

## 2026-10-29 — Shared finishing tools: bible v3 logo size + 2-line disclaimer (branch `sermorelin-first-batch`)
Logged before editing. Bible v3 "Creative direction guidelines" (§03 logo sizing, §04 disclaimers). Approved by Priestley
after before/after images (statics MA/WB/ME, video Track); **this changes Restora-Z's output too** (bigger logo, 2-line
disclaimer); tell Mitansh. Restora's skill files are untouched.
- `core/tools/finish_batch.py`: logo width 31% (4:5, 1:1) / 40% (9:16) of the canvas (was a fixed 200 px ≈ 18%); disclaimer
  auto-fits to at most 2 lines (font 21 px down to the 13 px minimum, line width W-56).
- `core/tools/full_layout.py`, `core/tools/styles.py`: video logo 432 px (40% of 1080) in all looks (was 210–280); the
  opening header moves down 28 px to clear the taller logo; the disclaimer auto-fits to at most 2 lines (min 13 px).
- `skills/everlife-sermorelin-ghk/references/image-batch.md`: the prompt's calm top band 11% → 14% for the bigger logo.
- Installed toolkit (`~/Everlife-Creative/tools`) synced. Regression: expected differences in every finished picture
  (logo/disclaimer); smoke test must pass.
Originals in `_originals/2026-10-29/v3-logo-disclaimer/`.

## 2026-10-29 — Align with bible v3: women's palette, skill bible header, global rules file (branch `sermorelin-first-batch`)
Logged before editing. Approved by Priestley:
- `skills/everlife-sermorelin-ghk/references/image-batch.md`: v3 dropped "Women's creative: pinks, tans and beige. No
  oranges or greens." from the general standards (kept only on GHK-Cu Cream and Glow Stack) → no palette limit for
  Sermorelin GHK women; keep rotating the lead colour (at most one pink-led ad per batch).
- `skills/everlife-sermorelin-ghk/references/product-bible.md`: header marks the copy as checked against v3 (29 Oct; the
  Sermorelin GHK pages are identical); women's palette line in "Product facts" updated.
- `~/.claude/CLAUDE.md` (Priestley's global rules, outside the repo; backup in `~/.claude/everlife/_originals/2026-10-29/`):
  women's palette line → only GHK-Cu Cream / Glow Stack; known gaps: NAD+ page no longer missing; the "Parts B/C have no
  disclaimer" lines → v3 has disclaimers on most pages, "Disclaimer pending" on 11 (stop and flag those).
Pending: logo 40%/31% + 2-line disclaimer in the shared finisher (before/after to be shown first).

## 2026-10-29 — Sermorelin GHK: the cloned-voice product line is a planned step in every video (branch `sermorelin-first-batch`)
Logged before editing. Priestley: write it into the skill so anyone making a video follows the same path (no credits to
write; ~0.9 Higgsfield credits per video to run). Every Marketing Studio take today mispronounced the drug names and put
lines where it liked; re-generating (75 cr) doesn't fix that reliably.
- `skills/everlife-sermorelin-ghk/references/video-prompting.md`: script rule: on camera only easy words (hook, "Doctor
  prescribed…"); the product-name line is written for the hands-only shot and always voiced afterwards in the actor's
  cloned voice; hard words ("sublingual", "Citrulline") on screen, not spoken.
- `references/finishing.md`: new required §1b "Video check + product-line voice": transcribe + find cuts, clone the voice,
  3 takes, pick, place inside the hands shot with the original MUTED, cut any mispronounced on-camera line, hold the last
  frame for a 4 s end card, re-caption, re-check; exact commands included.
Originals in `_originals/2026-10-29/voice-step/`.

## 2026-10-29 — Sermorelin GHK: team feedback on the men's video + bible v3 creative direction (branch `sermorelin-first-batch`)
Logged before editing. Team chat after the "Track" video (Emily, Sarah, Jeremy, Justin), approved by Priestley for the
Sermorelin GHK skill ONLY (Restora, plain Sermorelin and the shared toolkit unchanged):
- **Men only (casting):** 40s–50s "fit silver fox", hardcore fitness-model build (visibly muscular, lean, athletic;
  tattoos optional), a serious gym-goer (bible v3: "rugged, strong and unmistakably masculine — a serious gym-goer with a
  hardcore training feel"); Jeremy: "too old, not ripped enough… hardcore fitness model 40's to 50s". Priestley: fully
  clothed in a fitted training tee or long sleeve; no bare torso, no flexing or body-focus poses.
- **Men + women:** "SERMORELIN GHK" on screen from the first frame (Emily: "applies to every product"); speech starts in the
  first second and the hook lands within 2.5 s (Emily "start talking way sooner", Jeremy's one-pager, bible v3);
  "Sermorelin GHK by Everlife" in every intro: copy, scripts, voiceovers (bible v3); the tablet is held: thumb + index
  "pull" or resting in an open palm, sharp in the foreground (bible v3).
- Files: `SKILL.md` (product truths), `references/video-prompting.md` (timing, casting, header), `references/image-batch.md`
  (name line, held tablet, men's casting), `references/finishing.md` (QA + copy.json header), `references/lessons.md`.
- Safe zones (Justin): already enforced by the finishers with the bible's numbers; no change.
Originals in `_originals/2026-10-29/team-feedback/`.

## 2026-10-29 — Local creative bible re-imported from the master (v3, 48 pages) (outside the repo)
Logged before editing. Priestley exported the master ("Creative Messaging.pdf", Claude Design project 8cc4e3fe…, file
"Creative Messaging Reference.dc.html") and approved update 1 only: replace `~/.claude/everlife/creative-bible.md`
(27 Oct import of Parts A/B/C) with the full v3 text. Old copy backed up to `~/.claude/everlife/_originals/2026-10-29/`.
What v3 changes (reviewed with Priestley; NOT yet applied to any skill or tool):
- Creative standards: "Women's creative: pinks, tans and beige. No oranges or greens." removed (palette now only on
  GHK-Cu Cream and Glow Stack pages).
- New "Creative direction guidelines" page: tablets held (thumb + index "pull" or open palm); "[Product] by Everlife" in
  every intro; video hook within 2.5 s; logo 40% width (9:16) / 31% (4:5), 3.5% height; disclaimer at the bottom, 2 lines
  max, 13 px min; mobile text minimum blank ("confirm w/ Justin"); 50% trust-focused / 50% minimalist trust callouts
  (conflicts with the global "every ad carries visible social proof").
- New "Safe zones" page (matches the toolkit). Sermorelin GHK: Justin's update now in the master; new men's direction
  "Talent: rugged, strong and unmistakably masculine — a serious gym-goer with a hardcore training feel."
- New product pages (Wolverine, Klow, GHK-Cu/Epithalon, Glow Stack, NAD+); plain Sermorelin adds "Double Strength
  Sermorelin" lines; Restora-Z page changed (Restora skill untouched; for Mitansh).
Skill and toolkit updates (items 2–4) were offered and not approved yet.

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
