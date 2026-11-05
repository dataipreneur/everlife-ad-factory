# Changelog

Originals of every edited file are kept in `_originals/<date>/` (same relative path).

## 2026-11-05 — Bible sync to 1793890033-215f (branch `bible-sync-215f`; originals in `_originals/2026-11-05/bible-sync-215f/`)
Priestley: "There is a bible sync that we need to incorporate in the patch." Justin moved the live bible from …ced5 to …215f. Small sync (4 changes); Restora-Z untouched; all 15 product disclaimers still match.
- **Discount rule reversed (Standards 02):** every ad features the product's HIGHEST discount, whichever variant is pictured: PT-141 59%, Sermorelin 65%, NAD+ 62%, GLP-1 83% (a PT-141 nasal-spray ad still says 59%). Replaces the 2026-11-04 per-variant rule in the gates, global rules, and the PT-141 / Sermorelin / GLP-1 skills (offer lines, CTA question, image-batch rows, video prompts). The bible dropped the CTAs "Save Up to 23%" (PT-141) and "Save Up to 59%" (Sermorelin), which settles the Sermorelin 59-vs-65 question: 65%.
- **GLP-1 vials (new):** show both vials by default; one vial only if it is tirzepatide; never semaglutide alone. The skill's form question no longer offers "Compounded semaglutide" alone.
- **Every ad has a CTA** (new global line, Standards 03).
- **Titan-Rx:** headlines/benefits must make the category clear in under two seconds (daily sexual-performance support for men). ⚠ The bible's wording says "ED support": copy must not say "ED" or any disease word until Jeremy approves.
- Banners "Bible sync 1793890033-215f" added to the pt-141, sermorelin, glp-1, nad and titan-rx product-bible pages (above the ced5 banner, which they supersede on discounts).

## 2026-11-05 — Quick patches for zip installs (branch `patch-updates`)
Priestley: Justin wants bible changes to reach the team fast; teammates have no GitHub, so every change waits for a zip.
- `core/scripts/make_patch.py <from> [to]`: packs only the files that changed between the version the team has and the new one
  (SHA-256 per file; refuses symlinks and files over 5 MB). `core/scripts/apply_patch.py <zip>`: zip installs only; checks the
  VERSION matches, every checksum, no path escapes, no hand-edited files; backs up replaced files to `_originals/`; atomic; `--dry-run`, `--force`.
- Phrases in `core/claude/everlife-team.md`: "Apply the patch" (teammates) and "Build a patch" (whoever has git). ONBOARDING-ZIP.md: "A quick patch".
- Tested (`core/tests/patch_test.py`, 13 checks, on real history): patched copy identical to a fresh install of the new version; PR #52's whole
  bible sync = 656 KB (vs 112 MB zip); e79c3f5 → 2800e8d = 88 KB; refusals: wrong version, hand-edited file, damaged patch, path traversal, git copy; re-apply is a no-op.
- Teammates need one full zip that already contains these scripts before patches work for them.

## 2026-11-05 — "Build the team zip" phrase (branch `team-zip-phrase`)
Priestley: "add the build the team zip phrase" (a teammate with git pulls main and builds the zip for the others).
- `core/claude/everlife-team.md`: saying "build the team zip" makes Claude check the repo is clean on `main`, pull, run
  `core/scripts/make_zip.sh main ~/Desktop`, and verify the zip's `VERSION` sha and that it contains `core/team-logs/PAUSED`. Git copies only.

## 2026-11-04 — Team-log hooks-installed check (branch `teamlog-session-check`)
Priestley: "run the installer and add the check" (after asking how automatic the team logging really is).
- `core/hooks/teamlog_hook.py`: new `start` mode (SessionStart) warns when the capture or Stop hook is missing or points at a missing script. Never blocks.
- `install.sh`: also installs the SessionStart hook (same merge, backup and idempotent logic).
- `core/scripts/preflight.sh`: new check 6b2, fails with the fix when the team-log hooks are not installed (covers machines that never ran the installer).
- **Pause switch** (Priestley: "build the pause switch"): `core/team-logs/PAUSED` exists = hooks silent, preflight says PAUSED, `everlife-team.md` tells Claude to skip every team-log step. Delete the file to resume. TEAM-LOGS §8. Shipped ON for the 2026-11-05 zip rollout.
- `core/team-logs/TEAM-LOGS.md` §7 updated. Tested: simulated settings (none / only Stop / missing script) give the right warnings; the real settings are silent; `bash -n preflight.sh` passes.

## 2026-11-04 — Bible sync to 1793832093-ced5 (branch `bible-sync-ced5`; originals in `_originals/2026-11-04/bible-sync-ced5/`)
Priestley: "Check for bible updates please" → "I think we can sync now". Justin moved the live bible three times in an hour
(…a565, …8765, …ced5); this syncs straight to …ced5 (from …6285). Restora-Z's files are NOT touched (needs the owner's OK).
- **Proof split 42 / 28 / 30** (trust row / Trustpilot bar + "Over 100,000" / none): the bible now states the split Mitansh applied on 2026-11-02 (was 60/40).
- **Focal mix 40 / 30 / 30** (pill / bottle / person; was 50/25/25): gates, global rules, creative-system and every skill's text (batch of 8 = 3/3/2). The 75/25 rule for products without a pill stays until Justin says otherwise.
- **Shirtless talent capped at 30%** for Sermorelin, Sermorelin GHK, TRT, BPC-157, TB-500, Spartan, Wolverine; never on Lovara, PT-141, Spark, Titan-Rx. The hardcore share was 40%: `hardcore-men.json` share 0.3 and `pick_styles.py` now rounds DOWN (5 ads → 1, 10 → 3), docs and 63 skill banners say "up to 30%".
- **AI disclosure:** the bible removed the global "ADVERTISEMENT: AI-generated depiction…" line: "each ad uses the disclaimer from that product's page". Our footers already do; the open question is closed.
- **Logo** 4:5 width 31% → 29% (9:16 stays 40%); **minimum on-screen text 24 px**; new **Product accuracy & realistic scale** standard; the price rule is "lowest price or price per day on 10% of ALL ads".
- **New Hard NOs:** never the phrase "body composition" (rewrite: "supports lean muscle"); no "fat" or "skinny" claims anywhere; benefits only from the Quick-hit list word for word; "Dr. Prescribed" is never a benefit. `teamlog.py` refuses "body composition" and "fat"/"skinny" (2 smoke checks).
- **New section 09, discount accuracy:** the featured product + form's own maximum, always "Save Up to X%": PT-141 nasal 23% / sublingual 59%, Sermorelin sublingual 65% / injection 59%, NAD+ 62% / 62% (sublingual was 56%), GLP-1 semaglutide 83% / tirzepatide 70% (was 59%). PT-141, GLP-1 and NAD+ skills updated.
- **CTA changes:** "Start / Build / Find Your Plan" etc. removed from Epithalon, GLP-1, Lovara, NAD+, Spark, Titan-Rx, Sermorelin GHK; PT-141 CTA "Save Up to 59%"; Sermorelin gets "Save Up to 59%" (⚠ the injection maximum: tablet ads keep 65%); GHK cream CTA "GHK Peptide Cream for $1.50/day".
- **Sermorelin GHK:** the ingredient claim lost "and fat loss" ("Promotes lean muscle growth"); "visceral fat" left the benefit scope. Tesamorelin pages (no skill) lost visceral fat / "Body composition".
- **Open for Justin / Priestley** (also in the gates' known gaps): non-pill 75/25 vs the new 40/30/30; what "benefits only from the Quick-hit list" means for per-ingredient claims; the Sermorelin "Save Up to 59%" CTA vs its 65% tablet maximum; gate §7 (master before other sizes) vs both-sizes in #50/#51; the 9:16 logo (finisher default 29% vs 40%).

## 2026-11-04 — Lean team logging + send/post check (branch `teamlog-fixes`, originals in `_originals/2026-11-04/lean-logging/`)
Priestley: "I want to be wary of token usage bcoz of this logging system" → "Yes" to the lean version with a posting check. The
same day's audit found ~150 generations logged locally but never sent and ~250 finished ads not on Ad Review.
- **Lean reads:** pre-batch rows (Copy Ledger, Ad Review flags) are saved to files with `ArtifactData` `out_dir` and read through
  `teamlog.py summary` (used headlines / hooks / CTAs, the team's recent styles with the `--skip` list, the proof split vs 42/28/30,
  reviewer flags with reasons and recipes). TEAM-LOGS §2.2, AD-REVIEW §3.
- **Grouped logging:** `teamlog.py gens --wave W.json` (a wave in one call), `qa` with several doc ids, `proof` with repeated
  `--ad-id`/`--proof` pairs; `pending` lists what is unsent per page so each page gets one batch. **Light mode:** `teamlog.py light`
  logs a maintenance job (resizes, CTA swaps, text fixes) once with its file list (run `--format maintenance`).
- **Quieter output:** one line per record; page URLs come from `pending`.
- **Send tracking:** `teamlog.py sent` / `posted` (`.sent.json`, `.posted.json` in `<job>/teamlog/`; a record changed after sending
  counts as unsent again; `--queued` for the pending file). `close` lists what is still to send or post. The **Stop hook** now also
  sends Claude back once when a session's job folders hold unsent records or finished ads of a closed run not posted to Ad Review.
- **Checker:** run_id format enforced (`B3` refused); "Save N% Off" without "Up to" refused; any % / $ line on Titan-Rx flagged
  (offer [VERIFY CURRENT], $/day held); single-shot composer tools (`composer_edit_image`, voice lines, music) no longer ask for a
  `tool_prompt`.
- Skill lines updated in 14 product skills (image-batch, video-prompting, animated-still, finishing). **Restora-Z not edited**
  (needs Priestley's OK); it follows TEAM-LOGS / AD-REVIEW, which now describe the lean steps.
- **Pre-screen false positive fixed (found by the first real both-sizes run, Sermorelin GHK):** `screen()` read every cell of a ❌ row as
  a banned line, so a row whose "why" cell quoted the approved replacement (`use "Supports natural growth hormone production"`) made the
  bible's own top quick-hit read "❌ pre-screen" and blocked `copy` / `close`. It now reads only the first (line) cell; the real ❌ lines
  (Visceral-Fat, "safer alternative to synthetic HGH", Recover Like Wolverine, Support Lean Body Goals, …) still refuse.
- Smoke: 67/67 (three new checks: the offer wording, the summary digest, the quick-hit false positive).

## 2026-11-04 — teamlog.py: start time automatic, every record names its page (branch `teamlog-fixes`)
First live runs (BERNS, Edge) showed start times typed after the end and 30 proof records sent to the Activity log. Priestley:
"Fix first 2".
- `teamlog.py run`: `started_at` = the run's first logged generation (no `--started` to type); the checker refuses a run that starts
  after it ends.
- Every record prints "send to: <page> (<url>)"; `close` lists the records per page; TEAM-LOGS §2 says which type goes where.
- Data fixed the same day: Edge's 30 proof records moved from the Activity log to the Copy Ledger (marked `moved_from`); 8 run start
  times set to their first logged generation (`started_at_source` note).

## 2026-11-03 — Ad Review replaces the Winners Board: flag the losers, the data picks the winners (branch `ad-review`)
Team decision relayed by Priestley: no ratings; "we need to be able to basically flag and report losers but not winners. winners will
be identified by the data"; all generated content recorded; reviewers Justin / Sarah / the lead / Jeremy; flags "ingest[ed] back
into the system". Priestley: "try this".
- New `core/ad-review/AD-REVIEW.md` + page `core/ad-review/review-page.html` (same address as the board): every finished ad with its
  preview; reviewers (owner-managed list) flag losers with fixed reasons + a note; a compliance flag bans anything close. Old
  ratings archived, never read.
- 14 skills: the paused board steps become "read the flags first" (never repeat a flagged recipe, fix the top reasons, 3+ same
  reason → a PR) and "post every finished ad" (no rating); finishing.md posts finished videos. Restora-Z included (Priestley: "merge #48 and include Restora-Z").
- TEAM-LOGS points at Ad Review (`ad_id` joins flags to the logs); `WINNERS-BOARD.md` marked archived.

## 2026-11-03 — Bible sync to 1793746711-6285: $/day CTAs, Sermorelin $95/month, advertorial bylines (branch `bible-sync-6285`)
Justin's update: a "<product> for $N/day" CTA on most products; Sermorelin "Starting at $95/month" on 10% of creatives; article ads
bylined "Brian L." (men) / "Erika S." (women). Priestley: "yes sync it". Originals: `_originals/2026-11-03/bible-sync-6285/`.
- Repo bible written; verbatim sections re-copied (10 swapped whole; PT-141, Restora-Z, Sermorelin, Sermorelin GHK patched; BPC-157's
  verbatim is the docx). A "Price CTA" note in each skill: an approved alternative, the offer stays the default, the only $ amount
  allowed. Sermorelin plans the $95/month CTA on 1 in 10. Titan-Rx's $/day held (offer [VERIFY CURRENT]); Spark's needs an OK (list
  pending); GHK cream uses "GHK Peptide Cream" on Meta/Google/TikTok; Spartan has none.
- Gates + global rules: price CTAs; bylines added but ⚠ Jeremy before use (named author on an AI-made advertorial).

## 2026-11-03 — Team logs: automatic capture hooks (branch `teamlog-hooks`)
Priestley: "Are you sure claude will log every time into those artifacts?" → "yes build it, push and merge".
- New `core/hooks/teamlog_hook.py`: `capture` (PostToolUse) writes every paid Creatify / Higgsfield generation call with its exact
  input to `~/Everlife-Creative/teamlog-auto.jsonl`; `stop` (Stop) sends Claude back once when the session's paid calls outnumber
  the `teamlog.py gen` records, then lets it finish with a warning.
- `teamlog.py gen` also appends to `~/Everlife-Creative/teamlog-index.jsonl` (what the Stop hook compares against).
- `install.sh` merges both hooks into `~/.claude/settings.json` (backup first; other hooks kept; re-run replaces only ours).
- Tested: 7 simulated calls (3 paid captured, 4 ignored), stop blocks then releases, other sessions untouched, install twice on a
  fake home with an existing hook (kept, no duplicates). TEAM-LOGS §7.

## 2026-11-03 — Bible sync to 1793743706-38c1: peptide stacks list every peptide (branch `bible-sync-38c1`)
Justin's update: every ad for a peptide stack shows each peptide (Spartan BPC-157 / TB-500 / KPV, Wolverine BPC-157 / TB-500, Klow
BPC-157 / GHK-Cu / KPV / TB-500, Glow [PLACEHOLDER]); Spartan and Klow pages: name + peptide list on every design. Priestley: "yes sync it,
push and merge". Originals: `_originals/2026-11-03/bible-sync-38c1/`.
- Repo bible written; Spartan's verbatim section re-copied; global rules + gates carry the stack rule; Klow "GHK-Cu" vs the GHK Hard NO
  and Glow's placeholder added to the gates' known gaps (Justin).
- Spartan + Wolverine: a 💊 PEPTIDE LIST banner in SKILL.md (statics on the design in 4:5 and 9:16; videos at least on the end card;
  missing list fails QA); Spartan image-batch now requires "BPC-157 / TB-500 / KPV" (Wolverine already had its list).

## 2026-11-03 — Team-log pages: warning reasons shown in the row (branch `teamlogs-flags-visible`)
Priestley on the Copy Ledger: "why check shows warning for few. i dont see any" → the reasons were only in a hover tooltip.
"yes fix it, push and merge". Originals: `_originals/2026-11-03/teamlogs-flags-visible/`.
- All three pages: the Check cell lists each reason under the ⚠ count (no hover needed); "backfilled" is a grey label, not a
  warning, so ⚠ only marks something to fix.

## 2026-11-03 — Prompt log: headline / hook on every generation (branch `teamlogs-headline`)
Priestley: "why is headline missing for few in prompt & outcome log?" → all 20 backfilled rows had an empty `copy`, and
`teamlog.py gen` wrote it empty too. "yes fix it, push and merge". Originals: `_originals/2026-11-03/teamlogs-headline/`.
- `teamlog.py gen --headline / --hook / --cta`; `teamlog.py copy` fills any blank headline / hook / CTA on that ad's takes
  (prints which gen records to re-send); the checker warns on a take with neither.
- Prompt log: column "Headline / hook" (videos show the opening spoken line), "missing" flag, and a data-quality line.

## 2026-11-03 — 🏆 Video winners reference set (every video skill)
Mitansh: "These videos should be refered! BY all video making skills man! Whatever videos I made today all were amazing!"
- New `core/references/video-winners.md` + 8 frame sheets in `core/references/video-winners/` (Wolverine Animated Warriors + Run-Through; SGHK Car Throw Review, Comic Gauge, Comic Heist, AI Avatar Edge Reloaded, Three Orbs; Restora-Z Car Throw Review): format, why it works, recipe, cost, and the shared rules all eight follow.
- 🏆 banner in all 16 `skills/*/SKILL.md`; `video-team-rules.md` §5 points to it.
- Review (Priestley: "bring in the new PR"): a "Known flaws" list (W3/W4 "Get started now", W3 open bottle with a tablet pile,
  W4 testimonial-style line, W5/W6 no captions) and captions + stack peptide list added to the shared rules; merged with main
  (both banners kept in Spartan / Wolverine).

## 2026-11-03 — Team logs: data quality built in (branch `teamlogs-quality`)
Priestley asked to fix the logging system after Mitansh's first (backfilled) records showed summaries instead of prompts, empty
refs, date-only times, re-take counts that didn't match, a banned CTA labelled "bible ✅", a missing CTA line and caption-free
videos ("Lets do it"). Also: "If the user reprompts or modifies the prompt, are those details captured?" Originals:
`_originals/2026-11-03/teamlogs-quality/`.
- New `core/scripts/teamlog.py` (no network): `gen` saves the exact prompt to `<job>/prompts/` and writes the record; `qa`;
  `note` (the operator's feedback on a take); `copy` builds the copy record from copy.json / premium.json / phrases.json and labels
  every line from the global Hard NOs + the product pre-screen (refuses a banned line); `proof`; `run` (made / finished / rerolled /
  spent from the gens; `--captions yes|no`); `check`; `close` (✅ before SESSION.md). Re-takes: `--retake-of` + `--ask`;
  `--edited-by-user` for a prompt the operator rewrote.
- Schema: run.captions; gen.prompt_file, ISO times, retake_of, prompt_by, feedback; ref type `own_ad`; copy kind `caption`, `media`;
  source labels set by the script. TEAM-LOGS §2, §3, new §6.
- Pages: a Data-quality filter and a ⚠ Check column on all three; the Prompt log gets a "Needs attention" tile and shows feedback,
  re-take links and data gaps per generation; the Copy Ledger flags banned lines and shows the proof split against 42/28/30; the
  Activity log shows Captions yes/no (and drops the paused board column).
- Every skill's logging lines (image-batch, finishing, video-prompting, animated-still) and the three video recipes now say to use
  the script and to close before SESSION.md. Smoke: two new teamlog checks.
- **What the tool actually ran** (Priestley: "What a tool does to prompt after receiving it? We cant capture it?" → "yes add it"): `teamlog.py tool <job> <doc_id> --file F --source <call>` saves a tool's expanded prompt / script / concepts as `tool_prompt` next to ours (`prompts/NN_…_tool.txt`); the check and the Prompt log flag Marketing Studio / Ads Studio / composer takes without it. Read calls listed in TEAM-LOGS §6; untested until the first real job per route.

## 2026-11-03 — Team logs reach every video route and Restora-Z (branch `logs-video-routes`)
Priestley asked "are you sure our new logs work?"; a check found no real run logged yet, Restora-Z without log lines and four
self-contained video recipes that never mention the logs. Priestley: "do a first please" (incl. Restora-Z).
Originals: `_originals/2026-11-03/logs-video-routes/`.
- One "Team logs" step in `ai-avatar-video.md` (before Assemble), `car-throw-review.md` (step 6, before QA) and
  `seedance-on-creatify.md`: read the Copy Ledger before the script; log every paid still/clip/music, the final copy and proof,
  and the run's spend. The Hook Engine (Mitansh's) is covered through these routes and each skill's finishing step; not edited.
- Restora-Z: the same two lines the other 14 skills got (`image-batch.md` before §1b, `finishing.md` before §4).
- Verified the same day: all three pages accept a Contributor-level write (self-test rows written and deleted).
- `TEAM-LOGS.md` §2 step 4 no longer says "the Winners Board as today" (paused).
- **Videos log as they go** (Priestley: "yes add it", after Mitansh's unfinished video left nothing in the logs): every skill's `video-prompting.md` and the three recipes write each still/clip/music `gen` record the moment the job is submitted, then update it after QA; `finishing.md` adds only copy, proof and spend; TEAM-LOGS §2.3 says so.
- Coverage check (Priestley: "I hope all products are covered and also both images/videos have it"): all 15 product skills carry the line in `image-batch.md`, `finishing.md` and `video-prompting.md`; added to the 7 `animated-still.md` files (BPC-157, Epithalon, GLP-1, MOTS-c, NAD+, Spartan, Wolverine) and to the new-product checklist.

## 2026-11-03 — Gates: AI avatar model routing (branch `gates-avatar-routing`)
Logged before editing. The gates sent "talking head" to Boreal-style; Mitansh's all-Creatify avatar rule (2026-11-02) routes the
presenter to Creatify Seedance + Boreal-H3 background, 0 Higgsfield. One line added under Model routing in `everlife-gates.md`
(and Priestley's personal CLAUDE.md). Originals: `_originals/2026-11-03/gates-avatar-routing/`.

## 2026-11-03 — 📋 Team video rules (HARD, every skill, every teammate)
Mitansh: "this should be across all skills, not just my local system!"
- New `core/references/video-team-rules.md`: scripts as a clear mini-story (no cryptic fragments, problem in the first 1–2 s, no specific ages, urgent CTA with the approved offer only); scripts shown as chat text with no popup in the same turn; no paid re-take without an explicit "go" (free fix first, never speed up talking); men's music trap-metal / walk-out, never taiko; winners to reuse (Animated Warriors, Car Throw Review); Sermorelin GHK cast = lean, jacked grey-haired fitness model 45–50, not bulky.
- Banner in all 16 `skills/*/SKILL.md`; gates §5 line; `hardcore-men.md` SGHK exception; SGHK SKILL.md men's-talent line rewritten.
- PR #38 review (Priestley, 2026-11-03): "no specific ages" scoped to video scripts and captions; bible-approved image headlines with an age stay usable. Mitansh kept Car Throw Review for Restora-Z and Spark, the review format and the gates wording (flags 1, 2, 7 overridden); Priestley approved the Restora-Z banners.

## 2026-11-03 — 🚗 Car Throw Review video style for every tablet / capsule product
Mitansh on the SGHK 1000 car review: "This was amazing!!! Save it as a form in video 'Mood' questionnaire, Car Throw Review" + "have it for all the tablets".
- New `core/references/car-throw-review.md` (script shape, Creatify Seedance 2.5 recipe, free 3× throw speed-up, end-card hold, header 0–5.5 s then logo, QA).
- Banner in the 8 tablet/capsule skills (Sermorelin GHK, Sermorelin, Restora-Z, PT-141, Spark, NAD+, Titan-Rx, Lovara): every video Style/Mood question always offers "🚗 Car Throw Review".
- Sermorelin GHK: `styles/7-car-throw-review.md` (the winning script) + examples in `styles/car-throw-review/`, INDEX row, video Style question updated.

## 2026-11-03 — Seedance = Creatify; Higgsfield = Marketing Studio only (HARD, every product video)
Mitansh: "All Seedance videos goes to Creatify, remove higgs! Higgs would only go for marketing studio!"
- New `core/references/seedance-on-creatify.md`: the rule, the proven Creatify Model Playground recipe (upload → GPT Image 2.5 start still → `bytedance/seedance-2.5/reference-to-video` 15 s 720p = 34.25 Creatify), costs, animated stills via `seedance-2.5/image-to-video`.
- 🎬 banner added to all 16 `skills/*/SKILL.md` (overrides every Higgsfield Seedance command and Unlimited-mode line); `core/claude/everlife-gates.md` §6 + Spend gate and `core/hook-engine/HOOK-ENGINE.md` §6 Route B updated.
- Wolverine Stack: `animated-still.md`, `video-prompting.md`, `styles/INDEX.md`, `styles/3-cinematic-big-idea.md` rewritten to the Creatify route; new style ⚔️ Animated Warriors (`styles/7-animated-warriors.md`, the V3 "Breakthrough" winner).
- Other skills still contain old Higgsfield Seedance lines underneath; the banner overrides them (clean-up per skill when next touched).

## 2026-11-03 — Humans speak on camera (HARD, every product video)
Mitansh: "In all the videos, whichever requires a human! The voice / speech should be coming from the human, not as a background voiceover!"
- New `core/references/on-camera-speech.md`: any person in a video speaks every line on camera, lip-synced; J-cut product cutaways inside the speaker's line are fine; voiceover only in no-person videos; pronunciation fix = re-voice on a cutaway or re-take.
- Banner added to all 16 `skills/*/SKILL.md`; `core/claude/everlife-gates.md` §5 and `core/hook-engine/HOOK-ENGINE.md` §1 (rule 0) and §6 Route B updated.

## 2026-11-03 — Winners Board locked for reading too (branch `board-lock-read`)
Priestley: "yes lock reading too. they shoudnt see any error though". Until teammates update, their old skills still READ the
board; now only Owner/Editors can read it (db rules `read: "admin"`). Non-editors opening the page see only the "Paused"
notice (no lists, no red status). Originals: `_originals/2026-11-03/board-lock-read/`.

## 2026-11-03 — Winners Board paused: rating/feedback loop unplugged (branch `board-pause`)
Logged before editing. Priestley: "Can we somehow unplug the rating or feedback system? We might need a new way to refine the
system." → pause, freeze the page (read-only, data kept). Reversible: one switch (`PAUSED` in WINNERS-BOARD.md + the page).
Originals: `_originals/2026-11-03/board-pause/`.

## 2026-11-03 — Bible sync to 1793728650-5a0d: offer CTAs replace "Get Started Now" (branch `bible-sync-5a0d`)
Logged before editing. Justin's update: "Get Started Now" is banned (lead with the offer, "Save Up to N%"); "Ships Free From
Pharmacy" added as a CTA on every product; standard disclaimer filled in where the bible said "Disclaimer pending"; landing pages
filled in; two new standards (nothing obscures product/CTA/text, incl. a footer gradient; consistent capitalization in a set).
Priestley approved the sync including Restora-Z (2026-11-03). Originals: `_originals/2026-11-03/bible-sync-5a0d/`.
- `core/claude/creative-bible.md` re-synced (`bible_sync.py --write`); `global-rules.md` + `everlife-gates.md` carry the three new
  standards; `change-requests.md` row; REFS.md H8 note (its "Get Started Now" button is layout only).
- Every skill's `product-bible.md`: a "CTA update" block at the top (wins over older CTA lists), VERBATIM sections re-copied (10
  swapped whole; PT-141, Restora-Z, Sermorelin, Sermorelin GHK patched line by line; BPC-157's verbatim is the docx, left as is),
  "Get Started Now" rows marked ❌, new CTA rows screened.
- Default CTA per skill: the bible's offer CTA where it has a % (GLP-1 59, NAD+ 62, GHK Cream 75, Lovara 45, PT-141 23, Sermorelin
  65, Sermorelin GHK 47, Wolverine 39; Spark 51 PROVISIONAL, its CTA list is still Pending approval; MOTS-c 40 from its doc).
  "Ships Free From Pharmacy" where the bible % is a placeholder (BPC-157, Epithalon, Restora-Z, Spartan) and for Titan-Rx (offer
  still [VERIFY CURRENT]). SKILL.md CTA questions updated (Epithalon, GLP-1, MOTS-c, NAD+, Spark, Spartan, Titan-Rx, Wolverine).
- Disclaimer now on the bible pages for Epithalon, MOTS-c, GHK Cream (same text as product.json, `--check` ✅): provisional flags
  retired. Landing pages filled (BPC-157, GHK Cream, GLP-1, Spark, Wolverine). Sermorelin GHK: "growth hormone" lower-cased per bible.
- Smoke 62/62.
- **Then bible 1793730765-9d0d (same day, same branch, Priestley OK):** the **focal-point mix** replaces "the pill is the hero, not the
  bottle": 50% pill-focused / 25% bottle-focused / 25% person-focused. Gates, global rules, `creative-system.md` §1 (batch table
  Focal column; batch of 4 = 2/1/1), `ultra-premium.md`, Hook Engine; a FOCAL-POINT MIX banner in all 15 skills' `image-batch.md`
  (old "tablet is the hero" lines now apply to pill-focused slots only); SKILL.md product-truth lines and style notes. Products
  without a pill (vials, GHK pump): 75% product-focused / 25% person-focused. Smoke 62/62.
- **Justin's answers (2026-11-03, via Priestley):** (1) "Yes that would be correct. For non pill products the vial should be 75%"
  → 75/25 confirmed, provisional flags removed. (2) men in pill/bottle slots count toward the hardcore share: "That is fine."
  (3) "Videos and statics should really be the same in the sense of how we're presenting products" → videos use the same split.

## 2026-11-03 — Winners Board: finished ads only (branch `board-no-briefs`)
Logged before editing. BERNS's Claude wrote 10 Sermorelin GHK "BRIEF ONLY: image not made yet" entries with placeholder "Good"
ratings; Priestley approved deleting them (done) and closing the gap. Originals: `_originals/2026-11-03/board-no-briefs/`.
- `WINNERS-BOARD.md` §5: entries only for finished ads with a preview; never briefs, plans or placeholder ratings. §4: skip image
  entries without a preview when reading history.
- `board-page.html`: image entries without a preview are hidden and never counted (the entry count shows how many are hidden).

## 2026-11-03 — Team logs: Activity & Spend Log, Copy Ledger, Prompt & Outcome Log (branch `team-logs`)
Logged before editing. Priestley's decisions (2026-11-03): three separate shared pages next to the Winners Board; the Activity &
Spend Log is read only by Priestley + leads (Editors), each operator writes only their own runs; the Copy Ledger and the Prompt &
Outcome Log are read by the whole team; the learning report runs only when someone asks. Jeremy's ask behind the prompt log:
"what they put in can dictate what comes out from the automated system … anything we can learn on that.. and then automate for
better prompting is most likely helpful". Originals: `_originals/2026-11-03/team-logs/`.
- `core/team-logs/`: `TEAM-LOGS.md` (URLs, schemas, when Claude reads and writes each, run_id / ad_id, pending-file fallback,
  learning report on request) and the three page sources.
- Wiring: `creative-system.md`, `WINNERS-BOARD.md` cross-link, one line in 14 skills' `image-batch.md` and `finishing.md` (not
  Restora-Z: follow-up), `adapt-checklist.md`. Local ledgers (`style-ledger.jsonl`, `proof-ledger.jsonl`, copy logs) stay as the
  fallback; scripts never call the network. `pick_styles.py --skip <codes>` draws the team's recent styles last (smoke check added).
- Copy Ledger seeded with 125 ads from Priestley's local copy logs (8 products; `imported: true`). Restora-Z's two skill lines are a
  follow-up for Priestley's OK.
- **What each generation was built from** (Priestley: "will our logs see if we are using winners or other references?"): `gen.ref`
  = `{type, id, parent_ad_id, changed}`, type one of board_winner · meta_winner · style_board · hardcore_ref · product_example ·
  outside · hook_engine · none. Prompt log page: "Built from" filter, column and summary tile; the learning report compares by type.
- **Person filter** on the Copy Ledger and the Prompt log (Priestley): one option per person who wrote rows (account names); the
  Copy Ledger also offers "Imported (old copy logs)".

## 2026-11-02 — Hardcore men: shirtless / bodybuilder casting for the men's-muscle products, 40% of random slots (branch `hardcore-men-40`)
Jeremy's direction (via Mitansh): bodybuilding / men's-muscle products recommend intense, shirtless, hardcore models and images,
and in random mode 40% of images are hardcore. New `core/references/hardcore-men.md` (the rule, the cast, the prompt line, what
still applies) + `hardcore-men.json` (products: sermorelin, sermorelin-ghk, bpc-157, wolverine, spartan; share 0.4).
`pick_styles.py` gains `--audience men|women|both` and tags floor(0.4×men's slots) + a 40% chance of one more as `HARDCORE`
(averages exactly 40%; women's slots never). Overrides removed or rewritten: gates Sermorelin "fit, mature, not bodybuilders";
Hook Engine §8 no-shirtless/no-flexing (exception for these products); Hook Bank Sermorelin / Sermorelin GHK limits; Wolverine and
Spartan hook-bank "clothed" limits; Sermorelin + Sermorelin GHK prompt templates, video CAST lines, closing guards, QA checks
and style guardrails; SGHK `product.json` "never: bodybuilder physiques"; "bodybuilder bodies" dropped from the BPC/Wolverine/
Spartan style Hard-NO lists. A 💪 banner tops every file of the five skills. New-product checklist: TRT, Tesamorelin and
Tesamorelin/Ipamorelin opt in when built. Kept: no before/after, no body comparison, no body-composition claims, product hero.

## 2026-11-02 — Titan-Rx skill brought up to date with main before merging (branch `titan-rx-skill`)
Merged main (#23–#30; `regression.py` and `ultra-premium.md` conflicts with GHK/Epithalon resolved by hand: each product's
test block keeps its own closing line, the vial row takes Epithalon and the tablet row Titan-rx, both palette rows kept) and
gave the skill what those PRs gave the other skills (from its Spark template): the AI Avatar "ALL on Creatify" line, the
15-style Mood override, the no-smear + show-first banner, the proof split (images + videos), and the Winners Board steps.
Smoke 61/61.

## 2026-11-02 — Epithalon skill brought up to date with main before merging (branch `epithalon-skill`)
Merged main (#23–#29) and gave the skill what those PRs gave the other skills (from its MOTS-c template): the AI Avatar
"ALL on Creatify" line, the 15-style Mood override, the no-smear + show-first banner, the proof split (images + videos), and
the Winners Board read-first and rate steps. Smoke 57/57.

## 2026-11-02 — GHK-Cu Cream skill brought up to date with main before merging (branch `ghk-cream-skill`)
Merged main (#23–#28) and gave the skill what those PRs gave the other skills (from its Lovara template): the AI Avatar
"ALL on Creatify" line, the 15-style Mood override, the no-smear + show-first banner, the proof split (images + videos), and
the Winners Board read-first and rate steps. Smoke 53/53.

## 2026-11-02 — Bible sync to 1793655503-c3e7: captions on every video, kept out of the safe zones (branch `bible-sync-c3e7`)
Logged before editing. Justin's change (Standards 02 + 04), no product page or disclaimer changed: "Every video carries on-screen
captions for all spoken audio. Captions stay clear of Meta's safe zones"; the Safe zones list now names captions too.
- `everlife-gates.md` §5 + §6. No tool change: `full_layout.py` / `premium_finish.py` already caption every spoken line inside
  the safe band (above the Reels profile corner); animated stills have no audio. Originals: `_originals/2026-11-02/bible-sync-c3e7/`.
- Note: the bible still says 60% trust / 40% count "set separately"; PR #27's 42/28/30 split awaits Justin.

## 2026-11-02 — AI Avatar videos run 100% on Creatify, 0 Higgsfield (branch `all-creatify-avatar`, Mitansh)
Mitansh: "please add this a new rule for all the skills! That AI Avatar videos, always goes to creatify for everything!!! No
higgsfield needed at all!" Proven the same day on Wolverine "Two Peptides. One Mission." (10 s: 17.45 Creatify, 0 Higgsfield).
Originals: `_originals/2026-11-02/all-creatify-avatar/`.
- `core/references/ai-avatar-video.md`: ⛔ ALL-CREATIFY banner on top; presenter = Creatify Model Playground
  `bytedance/seedance-2.5/image-to-video` (480p, generate_audio, exact quoted lines + pronunciation; Step 4 rewritten, no
  `higgsfield` commands); music step added (`composer_generate_music`, Lyria 3 Pro, 0.8/take, hit at 0.0 s, ducked under the VO
  with ffmpeg `sidechaincompress`); costs restated in Creatify (10 s ≈ 17, 15 s ≈ 22).
- All 12 product skills' SKILL.md AI Avatar line + `everlife-new-product`: "ALL on Creatify, 0 Higgsfield"; the 52.5 Higgsfield
  cost and the Marketing Studio registration step removed from that option.
- `core/tools/premium_finish.py` (Quiet Luxe): the sub-label is no longer title-cased when it contains digits
  ("BPC-157 / TB-500" had rendered as "Bpc-157 / Tb-500").
- Lessons: Wolverine (Seedance-on-Creatify presenter, `bgvideo --dx`, caps-auto check, strong men's music picked: hip-hop / hard-rock
  walk-out) and Spartan Stack batch 1 ("no theyre great": styles, `mirror_fit_916 --strip 6` / `--align right`, benefit pool spent).

## 2026-11-02 — Bible sync to 1793655261-6ce8: product always in focus, hook said AND shown (branch `bible-sync-6ce8`)
Logged before editing. Justin's change to Standards 02 (creative direction), no product page or disclaimer changed:
"The product is always in focus, in every static and video asset"; video: "The hook or key benefit is both said (voiceover or
talent) and shown on screen within the first 2–3 seconds" (was "the hook lands in the first 2.5 seconds or less") and "The
product is always in focus whenever it's on screen — never soft, blurred or racked out of focus."
- `everlife-gates.md` §5 hook line and §3 standards; `creative-system.md` §3 multiples line (blur only on background repeats,
  never the hero; flagged for Justin); change-requests log. Originals: `_originals/2026-11-02/bible-sync-6ce8/`.

## 2026-11-02 — Shared style library, Surprise-me Mood, no-smear finishing (PR #24, Mitansh; logged after merge)
Entry added after the merge (the PR had none). Priestley approved the PR and its Restora-Z lines (2026-11-02).
- `core/references/style-library/`: the 15 Drive styles (Justin's folder), boards, refs, `STYLES.md` with a never-copy list per
  style, `styles.json`; `core/scripts/pick_styles.py` ("Surprise me", skips the product's last two batches).
- Every skill's image Mood question: "🎲 Surprise me" / "📚 Pick from the 15 styles" + the product's top two moods.
- `reposition_916.py` banned (smeared edges); `core/tools/mirror_fit_916.py` is the free fix. Show every result before any re-roll.
- New Hard NO, every product: no incoming-call screens, no Accept / Decline buttons.

## 2026-11-02 — Trust callouts on 60% of graphics, customer count on 40% (branch `trust-callouts`)
Logged before editing. Bible sync to version 1793650290-a4dd (Justin, Standards 01 + 02 · 06): "Trust callouts (Trustpilot,
doctor-prescribed, free shipping from pharmacy) go on 60% of graphics, not every one. 'Over 100,000 happy customers' goes on 40%."
It replaces "Every ad carries visible social proof". Reason given: graphics looked cluttered. Priestley asked for the fix on its
own branch. Originals: `_originals/2026-11-02/trust-callouts/`.
- **Images and videos** (Priestley: "it's for videos too"): `full_layout.py`, `premium_finish.py`, `styles.py` and
  `animate_still.py` take the proof from copy.json `"proof"` (or `--proof`); the end cards lost their own count line, the
  footer carries the one proof. `core/scripts/proof_next.py` keeps each product's video split near 60/40
  (ledger `~/Everlife-Creative/proof-ledger.jsonl`). 11 skills' `finishing.md` say so (not Restora-Z).
- **Split per batch, complementary:** every ad carries exactly one proof element, the trust row (~60%) or the customer-count
  line (~40%), so no ad is left with none (keeps the gates' social-proof check true; flagged for Justin to confirm).
- **`finish_batch.py --proof trust|count|none`** (default `trust`, the old footer, with a reminder), and
  `finish_batch.py --proof-plan N` prints which ads of an N-ad batch get which. Same value on an ad's 4:5 and 9:16.
- Rules + gates (`global-rules.md`, `everlife-gates.md`), `creative-system.md`, and one line in 11 skills' `image-batch.md`
  (not Restora-Z: it keeps the trust row on every ad until Priestley OKs the change).
- **Same footer size on every creative** (Justin, forwarded by Mitansh, same day): new `core/tools/standard_footer.py`. Trust row
  990 px wide; disclaimer Inter Medium 18 px, exactly 2 lines (the largest size at which every product's disclaimer fits 2 lines;
  Restora-Z's is the longest), refused rather than shrunk if one ever needs 3. Used by `finish_batch.py` (images, was 21 px /
  3 lines), `finish_modern.py` (was 24 px), `full_layout.py` and `premium_finish.py` (video endings, were 21–25 px, 2–3 lines,
  row 768–1000 px). Replaces the 2026-10-29 note "keep 21 px over the bible's 2-line rule": the bible's 2-line rule now holds.
- **`core/references/change-requests.md`** (new, Priestley: "keep a record of changes he tells us to do"): who asked for each
  change, their words, what changed.

## 2026-11-02 — Winners Board v3: bigger previews, click to enlarge (branch `winners-board`)
Logged before editing. Priestley approved: reviewers judge the ad on the board itself, so previews must be big enough to read
the headline, proof row and disclaimer. Originals: `_originals/2026-11-02/winners-board-previews/` (incl. the v2 page source).
- **Page:** larger thumbnails (160 px; 120 px on phones); tap one to open the ad full size in a viewer with its rating, reviews
  and a "Review" button. The page source now lives in the repo: `core/winners-board/board-page.html` (republish it to the same
  board URL; never as a new artifact).
- **`make_preview.py`:** default width 480 → 720 px, target 40 → 80 KB. Board room drops from ~1,800 to ~900 previews; the
  housekeeping rule in WINNERS-BOARD.md §6 is unchanged (export, then drop previews of retired ads older than 60 days).

## 2026-11-02 — Winners Board v2: reviewer features (branch `winners-board`)
Logged before editing. Priestley approved reviewer features: 7 operators write entries through their Claude; 4 reviewers use
the page in a browser as Contributors. Same board URL, republished in place (stored data kept). Originals:
`_originals/2026-11-02/winners-board-reviews/` (incl. the v1 page source).
- **Page:** "Review" on every card (Winner/Good/Weak/Kill + feedback, one per reviewer, editable), reviews listed under the ad;
  a "To review" view (no review yet / not reviewed by me); per-product feedback notes; ad preview thumbnails; each card says what
  decided its rating ("Meta" / "Reviewers 3–1" / "Operator"). Products added: Epithalon, GHK cream, Titan-Rx.
- **Combining rule:** newest Meta verdict → else reviewers' majority (newest review per reviewer; a tie goes to the lower rating)
  → else the operator's rating.
- **Previews:** a ~480 px JPEG as a data URL in a small sub-document under the entry (`…/<entry id>/preview/img`), written by
  the operator's Claude from a JSON file (`file_path`), so base64 never passes through the conversation.
- **`core/winners-board/WINNERS-BOARD.md`:** schema (review, product_note, preview), §4 also reads reviews + notes and summarises
  recurring points as guidance only, §5 attaches the preview. Per-skill lines unchanged (they point at the doc).

## 2026-11-02 — Winners Board: one shared rating store for hooks + image ads (branch `winners-board`)
Logged before editing. Priestley's decisions: one shared board for hooks and images; scale **Winner / Good / Weak / Kill**
(AskUserQuestion shows max 4 options; one question per ad); Winner → one later slot mutates its recipe (exactly one variable);
Good → quality bar; Weak/Kill → retired for that product; Meta results override opinion; teammates get Contributor access.
Originals: `_originals/2026-11-02/winners-board/`.
- **Board** (claude.ai artifact, private, owner Priestley): https://claude.ai/artifact/QiQsRZvDdTTsKmsuVDG52M. `db` rules: everyone
  with access reads; each rater writes only `data/users/<own id>` and `raters/<own id>`; Editors/Owner edit or delete anyone's.
  Empty at launch (no seeded entries).
- **New** `core/winners-board/WINNERS-BOARD.md`: URL, access, schema, read protocol (last 15, winner mutation, retired skip,
  median bar), write protocol, rating question, image + hook recipe fields, fallback when the board is unreachable.
- **New** `core/winners-board/HOOK-ENGINE-SWITCH.md`: proposal for Mitansh to move the Hook Ladder ledger to the board.
  `core/hook-engine/` is NOT edited.
- **Image loop:** every product's `references/image-batch.md` (except Restora-Z) reads the board before the batch table and rates
  the batch after it (Sermorelin + Sermorelin GHK had no "After the batch" section: a short §4 is added at the end).
  `skills/everlife-new-product/references/adapt-checklist.md` §3: new skills inherit both steps.
- **Follow-up (needs Priestley's OK):** the same two lines for `skills/everlife-restora-z/references/image-batch.md`.

## 2026-11-02 — New skill: GHK-Cu Cream (`skills/everlife-ghk-cream/`, branch `ghk-cream-skill`)
Logged before editing. Built with `everlife-new-product` from the **Lovara** template (women 30–55, product-led; the builder's
default suggestion was BPC-157, a men's vial skill, which doesn't fit a women's topical cream). Bible page "## GHK-Cu Cream".
Originals: `_originals/2026-11-02/ghk-cream/`.
- **Disclaimer: PROVISIONAL.** The bible page says "Disclaimer pending"; on Priestley's instruction (2026-11-02) the skill uses the
  standard ad disclaimer, verbatim the same string as MOTS-c, with a `_disclaimer_status` note. Jeremy to confirm.
- **Naming:** "GHK-Cu Cream" only as the H2 product name; on FB / GL / TK the name is "GHK Peptide Cream"; never "-Cu" or
  "copper peptide" anywhere else in creative.
- **Render:** the strength-free pump bottle (`GHK-PEPTIDE CREAM.webp`); the 0.5% and 2% versions are not used (the bible names no
  strength). Form = topical cream in an airless pump; there is no tablet.
- Shared files touched: `core/tests/regression.py` (the product's smoke block), `core/references/ultra-premium.md` (its row).
- Not done (needs an outside service or a person): Higgsfield Marketing Studio registration; the first 4-image test batch.

## 2026-11-02 — Epithalon skill: built from everlife-mots-c, vial (branch `epithalon-skill`)
Logged before editing. The form and render arrived (Priestley via the coordinator): compounded Rx **vial**, render
`asset-library/VIALS/EPITHALON/EPITALON 10MG-ML 5ML VIAL (screenshot 2026-11-02).jpg` (592×1280 screenshot on white; looked at:
clear glass, silver cap, teal label EVERLIFE / EPITALON / 10MG/ML / RX ONLY / 5ML). Template `everlife-mots-c` (vial pattern).
Originals: `_originals/2026-11-02/epithalon/`.
- **New `skills/everlife-epithalon/`** (`new_product.py create … --template everlife-mots-c --form vial --pending-disclaimer`), then
  adapted per `adapt-checklist.md` §2–§3b from `EPITHALON-DRAFT.md` (which is folded in and removed): product facts + pre-screen,
  product.json/product.env, cut-out PNG + `_ref.jpg` on white, RENDERS.md, SKILL.md, image-batch, video-prompting, finishing,
  personas, lessons, reference guide, direction, animated still, styles, hook bank. MOTS-c's borrowed winners and its Creatify
  project are not carried over; the style boards (shared library thumbnails, all products) are kept.
- **Render:** cut-out checked on green (clean edges, clear glass kept); source is a screenshot, a full render is on the wish list.
- **Tests:** `regression.py smoke` 47/47 (Epithalon: static with the provisional disclaimer, wrong-disclaimer refusal, end cards in
  default + tiktok looked at: the vial clears the headline, no `pill_end_scale` needed); preflight 10 ✅, 1 open (Marketing Studio
  registration: not done, needs Priestley's OK).
- **Disclaimer PROVISIONAL** (Priestley, 2026-11-02): the standard ad disclaimer, verbatim from MOTS-c; bible still "Disclaimer
  pending"; Jeremy to confirm.
- **Spelling open question (Justin):** bible "Epithalon", vial label "EPITALON". Copy uses "Epithalon"; `keep_case` holds both;
  the label is never edited.
- **Sleep lines ❌** (the page's Hard NO wins over its own sleep benefits/audience line); offer and LP still [PLACEHOLDER].
- **Shared files touched (one row/block each):** `core/references/ultra-premium.md` (Epithalon row in "Per product"),
  `core/tests/regression.py` (Epithalon smoke block, Lovara pattern).

## 2026-11-02 — Epithalon skill: pre-build draft only (branch `epithalon-skill`)
Logged before editing. Priestley asked to prepare the Epithalon skill as far as possible without the product render or the form
(vial / tablet / capsule…), which he will provide. Nothing was scaffolded: `new_product.py inspect` reports the form UNKNOWN and no
render exists (asset library, `~/Downloads` incl. zips, `~/Desktop`), and the bible does not name a form, so `create` was NOT run
and no template was chosen. Original backed up: `_originals/2026-11-02/epithalon/CHANGELOG.md`.
- **Added `EPITHALON-DRAFT.md`** (worktree root): the bible facts, the compliance pre-screen of every headline, benefit, CTA,
  offer and proof line, the proposed `product.json` values, a draft art direction, a draft `hook-bank.md` (8 hooks, bridges = exact
  ✅ lines) and the list of what is missing. To be folded into the skill and deleted once the form and render arrive.
- **Disclaimer PROVISIONAL** (Priestley, 2026-11-02): the standard ad disclaimer, verbatim from `skills/everlife-mots-c/product.json`;
  the bible page still says "Disclaimer pending". Jeremy to confirm.
- **Contradiction flagged for Justin:** the page's audience line and two quick-hit benefits are about sleep, but its creative
  direction and Hard NO forbid sleep/overnight messaging (DSIP's territory). The Hard NO wins: the sleep lines are ❌ until fixed.
  Offer and landing page are [PLACEHOLDER]; all four headlines are ⏳ pending.

## 2026-11-02 — New skill: Titan-rx (branch `titan-rx-skill`)
Logged before editing. Priestley asked for a Titan-rx ad skill (men's once-daily 3-in-1 performance capsule: Tadalafil +
Vardenafil + L-Arginine, men 40–65+). Built with `everlife-new-product` (`create "Titan-rx" --template everlife-spark --form capsule`).
Template: **Spark** instead of the builder's default PT-141, because Spark (itself built from PT-141) already carries the Hook
Engine, hook bank, Ultra premium and AI Avatar options and the intimate-wellness 3-in-1 flow; adapted to men-only, one oral capsule
taken daily (no sublingual, no on-demand / timing language) and per-ingredient claims (each claim only on its own ingredient).
Originals: `_originals/2026-11-02/titan-rx/`.
- New: `skills/everlife-titan-rx/` (SKILL.md, product.json/env, renders + RENDERS.md, product-bible extract with pre-screen,
  hook-bank, image-batch, video-prompting, finishing, personas, reference-guide, lessons, reviews, styles).
- `core/references/ultra-premium.md`: Titan-rx row in "Per product".
- `core/tests/regression.py`: Titan-rx smoke block (Lovara pattern). Smoke 43/43 before, 47/47 after; `bible_sync --check` ✅.
- Name on creative "Titan-Rx" (bible CTA spelling; label TITAN-RX; `bible_section` = "Titan-rx"); `pill_end_scale` 0.85 (wide
  horizontal capsule, checked on default + tiktok end cards).
- Open: "Save up to 49%" [VERIFY CURRENT] not used; ingredient claims "Enhances…" / "Boosts…" ⚠ Jeremy; ED headlines ⏳;
  Marketing Studio registration still to do; first paid test batch not run.

## 2026-11-02 — Fix: preflight read only the digits of the bible version (branch `fix-bible-version`)
Logged before editing. Found after #21: preflight showed "version 1793642193-" for `1793642193-f927`, because its pattern
`version [0-9-]*` stops at letters (earlier versions such as `…-2416` happened to be all digits). The every-session check would
then always see a difference from the live version and warn "Justin updated the bible" when he hadn't. `core/scripts/preflight.sh`
now reads `version [0-9a-f-]*`. Originals: `_originals/2026-11-02/fix-bible-version/`.

## 2026-11-02 — Bible sync to 1793642193-f927: Spartan/Wolverine un-swapped, PT-141 lines removed (branch `bible-sync-f927`)
Logged before editing. Priestley: "go ahead with the sync and merge". Justin's version f927 (after 1793640737-714c) fixes the
Spartan/Wolverine swap: **Spartan Stack (BPC-157/KPV/TB500)** and **Wolverine Stack (BPC-157/TB500)** now match the vial labels.
It also moves the Ambien comparison into Restora-Z (layout only; the Restora-Z skill is unchanged) and drops three PT-141 lines.
Originals: `_originals/2026-11-02/bible-sync-f927/`.
- `core/claude/creative-bible.md` → version 1793642193-f927 (`bible_sync.py --write`).
- **Spartan + Wolverine:** `product.json` `bible_section` = the new headings; the PROVISIONAL swap is removed everywhere (SKILL.md,
  video-prompting, image-batch, lessons, RENDERS, product.json); `product-bible.md` rebuilt from each product's own page (facts,
  pre-screen, VERBATIM). Lines the swap had borrowed from the other stack are replaced with the product's own ✅ lines
  (reference-guide, hook-bank, styles, video copy example, lessons). Setup questions and end-card rows were already right.
- **Wolverine (Justin's new content):** talent 30–45, "Wolverine Stack" + "BPC-157 / TB-500" on every design, "Save up to 39%",
  Hard NO "No direct claims", hooks / headlines ⏳, new benefits screened (Tissue Repair, Joint Comfort ⚠ Jeremy).
- **Held for Justin:** "Supports Healthy Inflammatory Balance" (KPV's benefit) sits on Wolverine, which has no KPV: not used by
  either skill until he answers.
- **PT-141:** "Gentle on the Vascular System", "Helps Wake Up the Want" and "Sublingual or Nasal Spray Desire Support" are no longer
  on the page: ❌ removed (Justin to confirm it was deliberate; the spray/tablet line was the only mention of the two forms).

## 2026-11-02 — Bible sync to Justin's version 1793638690-e4ca (branch `bible-sync-2026-11-02`)
Logged before editing. Priestley: "Lets merge the arousal sync. Check if anything else has been updated since then." Repo copy
was `1793291361-2416`. Justin's changes since: a new Hard NO "Never use 'arousal' or any form of it" (Lovara, PT-141, Spark,
Titan-rx), with the arousal lines reworded; "Supports Sleep Quality + Recovery" removed from Sermorelin (men, women); the Wolverine
page rewritten. Originals: `_originals/2026-11-02/bible-sync/`.
- `core/claude/creative-bible.md`: written by `bible_sync.py --write` (version 1793638690-e4ca).
- **PT-141:** default end-card row, video copy example, facts line and both authority style cards no longer say "arousal" (now
  "Supports Central Desire Pathways", the bible's new line); VERBATIM lines re-copied; pre-screen: the new lines screened ✅ /
  weak, any "arousal" form ❌.
- **Lovara:** VERBATIM block re-copied; "Women's Desire Blend" (still ⚠ "Exclusive") and the Tadalafil claim "…comfort and
  responsiveness" (✅ on Tadalafil only) replace the arousal wording; any "arousal" form ❌.
- **Spark:** VERBATIM block re-copied; the mechanism-map card no longer says "arousal signaling"; any "arousal" form ❌.
- **Sermorelin:** "Supports Sleep Quality + Recovery" ❌ (removed from the bible), dropped from the clean benefit pool and VERBATIM.
- **Wolverine:** VERBATIM block re-copied; "Save up to 39%" is now on the bible page (no longer landing-page only). NOT applied:
  the new "include 'BPC-157 / KPV / TB-500' on every design", hooks and benefits. The page still describes three peptides with
  KPV, while the Wolverine vial label reads BPC-157 + TB-500; waiting for Justin to settle which is right (review page item 2).

## 2026-11-02 — "Ultra premium, product only" in every product skill (branch `ultra-premium-all-products`)
Mitansh: every product, vials or not, offers the ultra-premium look. Docs only, no tool code changed.
- New `core/references/ultra-premium.md`: the one definition (Hims/Ro codes, staging refs per form: vial-refs for vials, Hims tiles
  for tablets / bottles / sprays), the gates it never relaxes (tablet hero, product name big, 50+ legibility, women's palette,
  footer adds logo + proof + disclaimer), a field-colour row per product, QA additions.
- Vial skills (BPC-157, MOTS-c, Spartan, Wolverine, NAD+, GLP-1): the existing option now points at the shared spec.
- GLP-1, NAD+: the option added to SKILL.md Round 2 (where their mood question lives); image-batch.md no longer re-asks a
  "Round 3" mood question (a BPC-157 leftover that also asked audience / people).
- PT-141, Spark, Lovara: the option added to the Round 2 mood question.
- Restora-Z, Sermorelin, Sermorelin GHK: a new "Look" question in the image round (Standard / Ultra premium).
- `everlife-new-product`: new skills must offer it.
- **Same branch: "🧑‍💼 AI Avatar Video" in every product skill.** `core/references/ai-avatar-video.md` says "every product skill,
  from 2026-10-30", but only BPC-157, PT-141, Restora-Z, Sermorelin and Sermorelin GHK offered it. Added to "What are we making?"
  in GLP-1, NAD+, Spark, Lovara, MOTS-c, Spartan, Wolverine, each with a bullet naming that product's casting, hero form and
  banned settings (Spartan / Wolverine: "Video ad or animated still" merged to stay within 4 options, as BPC-157 does).
  Lovara's "once the shared avatar format exists" note replaced (it exists; ≥ 2 avatar videos per video batch, Jeremy 30 Oct).
  `everlife-new-product`: required rule (checklist §3) + test 6. All 12 products are registered in Marketing Studio (2026-11-02).
- Review fix: `ultra-premium.md` women's palette: pinks / tans / beige only for GHK-Cu Cream and Glow Stack; other women's runs follow
  the bible (pinks, tans, warm neutrals, white, teal) and may let the product's own colour lead (Mitansh). GLP-1's note unchanged.

## 2026-11-02 — Fix: the new-product skill's `core` link (would stop everyone's update) (branch `fix-core-link`)
Logged before editing. Found right after #17: every skill reaches the toolkit through a committed `skills/<skill>/core` →
`../../core` link, but `everlife-new-product` arrived without it. `install.sh` creates it, git sees an untracked file, and
the next `update.sh` refuses ("This copy has local changes"). Originals: `_originals/2026-11-02/fix-core-link/`.
- `skills/everlife-new-product/core` committed (the same link as every other skill).
- `core/scripts/update.sh`: before the local-changes check, removes an UNtracked `skills/*/core` link that points to
  `../../core` (install.sh re-creates it after the pull), so a teammate who updated between #17 and this fix isn't stuck.

## 2026-11-02 — Three older branches brought to main: new-product builder, stricter 9:16 check, Sermorelin render notes (branch `older-three`)
Logged before editing. Priestley: "go ahead with all three, skip avatar" (`avatar-format` is not merged: Mitansh's #14 is
the avatar format in use). Merged onto today's main: `sermorelin` (500 mcg render doc fix), `new-product-skill` (the
builder that scaffolded the 7 new products), `safezone-sides` (finish_batch 9:16 refuses the ad's own type under the logo,
and type/product in the Reels side bands with `--fit none`). Plus: `skills/everlife-sermorelin/product.env` comments no
longer say the 1000 bottle and tablet are "NOT YET ADDED" (both are in `assets/`, see `MISSING_RENDERS.md`); and the
builder's `references/adapt-checklist.md` gets §3b, the lessons from building the 7 products (template leftovers are words,
form rules, real renders in product.env, kicker, Hook Engine + hook bank, Marketing Studio, stale "nothing yet" notes).
Originals: `_originals/2026-11-02/older-three/`.

## 2026-11-02 — Bible sync: every session checks, edit-access people sync, weekly job planned (branch `followup-7-hooks`)
Logged before editing. Priestley: Justin is the only one who edits the live bible; the team just has to use his latest. Decisions:
an unsynced change → **warn and continue** with the current approved lines; the **weekly automatic check** is documented
but NOT active (Priestley: "skip weekly job for now"; needs GitHub connected to the Claude account and a test that a cloud
job can read the artifact). Found while
building: the Artifact tool returns the full page only to people with edit access ("writer"); viewers get a summary, so
teammates check the **version**, and only edit-access people (later also the weekly job, if switched on) run the full sync.
Originals: `_originals/2026-11-02/bible-sync/`.
- `core/scripts/bible_sync.py`: names the skills each changed section affects (global sections = every skill); `--repo-version`
  prints the repo copy's version for the session check; `--write` refuses on `main` (a branch + PR only).
- `core/scripts/preflight.sh`: after the bible line, tells Claude to run the live-version check (read-only).
- `core/claude/everlife-team.md`: the "Check the bible" note becomes the session check + sync steps.
- New `core/references/bible-sync.md`: the whole process in plain words (who does what, the check, the sync, the weekly job).
  Linked from `README.md` and `ONBOARDING.md`.

## 2026-11-02 — Follow-up to #13 / #14: Hook Engine for the 7 new products, GLP-1 settings, one bible for everyone (branch `followup-7-hooks`)
Logged before editing. Priestley: "prepare the follow-up locally". Built on main + PR #14 (Hook Engine); merge after #14.
Originals: `_originals/2026-11-02/followup-7/`.
- **Hook Engine in the 7 new skills** (Lovara, Spark, GLP-1, NAD+, Spartan, Wolverine, MOTS-c): a "Hook Engine (mandatory for
  every video)" section before Step 0, pointing to `core/hook-engine/HOOK-ENGINE.md` (the path every install has; PR #14's
  `~/.claude/everlife/hook-engine/` is not created by `install.sh`) and to a new per-skill `references/hook-bank.md` (8 starting
  hooks each, the product's limits first, every bridge a ✅ line from its `product-bible.md`). The shared `HOOK-BANK.md` is not
  edited. Each section also carries the creative-system §0 rule: the VO says "<Product> by Everlife" by ~3 s, with pronunciation.
- **GLP-1 `product.env`**: scaffold placeholders replaced (`glp-1_bottle.png` → `glp1_semaglutide_vial.png`, renders list =
  the four real files, name "GLP-1", output folder `output/GLP-1`, which already exists). Preflight failed on it.
- **One bible for everyone**: `install.sh` no longer keeps a separate `~/.claude/everlife/creative-bible.md` (it said "✅ kept
  your own copy", so that teammate read an old bible forever); it moves it to `~/.claude/everlife/_originals/` and links the
  repo copy. `preflight.sh` checks that file equals this repo's copy and prints the bible version (❌ with the fix if not).

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

## 2026-10-30 — Gates: 9:16 safe band matches the bible's Meta safe zones (y 144–1385) (branch safe-band-1385)
Logged before editing. Priestley approved ("Sure do it"). The gates said "y 143–1275", a number carried over from the first
Restora-Z layer builder (27 Oct) with no source. The bible's "Safe zones" page (Meta's 9:16 layout: top 144 px, Reels left/right
156 px, bottom 535 px, lower-left 219×169 profile corner) gives y 144–1385, which `core/tools/safezones.py` has enforced for
images and videos since 29 Oct (creative lead's Reels reference; Mitansh confirmed for every product).
- `core/claude/everlife-gates.md` (section 6): the safe band now reads x 156–924, y 144–1385, minus the Reels profile corner
  x 156–375 × y 1216–1385, with the footer exceptions already in the tools (proof row may run x 39–1041 and cross the corner).
- Also changed outside the repo: Priestley's `~/.claude/CLAUDE.md` (same line; original in `~/.claude/everlife/_originals/2026-10-30/`).
- Not changed: the comment in `core/tools/build_layers.py` (legacy Restora-Z builder, no effect on output).
Original in `_originals/2026-10-30/safe-band/`.

## 2026-11-02 — MOTS-c: BPC-157 template leftovers removed (branch `mots-c-skill`)
Logged before editing. Priestley: "yes start with MOTS-c". The skill was scaffolded from BPC-157 and still carried its recovery
and gym wording, which would leak into scripts and prompts. Rewritten from `direction.md` (energy and endurance, never physique)
and the ✅ lines of `product-bible.md` only; no new claims. Originals: `_originals/2026-11-02/motsc-leftovers/`.
- `video-prompting.md`: hook and authority examples, copy example, banned-word list, offer line ("Save up to 40%"), cast
  wardrobe, winners note (borrowed winners exist in `winners/winners.md`).
- `styles/` (INDEX, 1–5): recovery, tissue, joint, ice-bath and gym-bag sub-styles become energy and endurance ones; 2E mechanism
  map = mitochondria → energy → endurance (✅ lines); the "slate vial" becomes the MOTS-c vial (lemon-yellow label).
- `image-batch.md`: the "Hardcore gym" and "Boxing gym" moods become "Outdoor endurance at dawn" and "Everyday energy"
  (direction.md); type-table notes no longer say "recovery category" or "gym signage".
- `finishing.md`: article kicker default is "CELLULAR ENERGY" (product.json `kicker_default`), not "RECOVERY".
- `animated-still.md`: gym environment moves (chalk, rubber floor, barbell) become dawn, water and road ones.
- `lessons.md`: stale BPC-157 notes fixed (pronunciation, caption spelling, "add BPC-157 lessons", GHK-Cu line); the BPC-157
  batch lessons are kept as tool lessons and labelled; the "blurred plate is the default 9:16 look" lesson is marked superseded
  by the 2026-10-29 "0 blurring" finishing rule.
- Kept on purpose: provenance notes ("adapted from BPC-157"), the shared `../everlife-bpc-157/references/vial-refs/` staging folder.

## 2026-10-30 — MOTS-c: clean-up after test-1 (branch `mots-c-cleanup`, from `mots-c-skill`)
Logged before editing. Priestley: "yes, do the MOTS-c clean-up now". The skill still carried "⛔ BLOCKED / finisher refuses"
text from before 938e44f, and "no offer" from before c81cde5, which contradicted SKILL.md. Made on its own branch (this
session cannot write to the mots-c worktree); fast-forward `mots-c-skill` to it.
- `references/image-batch.md`, `video-prompting.md`, `finishing.md`, `lessons.md`, `product-bible.md` (facts bullet + label
  note), `product.json` (`_disclaimer_status`): the ⛔ disclaimer blocks become the ⚠ PROVISIONAL note (drafts allowed; flag
  every asset "provisional disclaimer: Jeremy to confirm").
- Offer "Save up to 40%" (Creative Messaging doc) wired in: image-batch hard stops + F6 enabled; `personas.md`,
  `reference-guide.md`, `winners/winners.md` no longer say "no offer yet".
- Headline tiers in image-batch: Tier A = the doc's ✅ headlines (was: ⏳ bible headlines).
- Label note resolved: the website (staging H2 page) says "10 mg/mL · 5 mL Vial" = the render; the doc's "2 mg/mL" is wrong.
- `assets/creatify.json`: project 744fcca3-1910-4289-8adb-2454e71b8c0b + vial asset (created by test-1).
- `lessons.md`: test-1 lessons (9:16 overshoot, footer fade on CTAs, side band, edge fill only on plain backgrounds).
Originals in `_originals/2026-10-30/motsc-cleanup/`.

## 2026-10-30 — MOTS-c: PROVISIONAL ad disclaimer = the standard text (branch `mots-c-skill`)
Logged before editing. Priestley: "then use it for now". The bible's MOTS-c page still says "Disclaimer pending" and the
Creative Messaging doc only has the website FDA statement, so MOTS-c uses the **standard ad disclaimer** (verbatim on the
Spark, Spartan, Wolverine and most other bible pages) as a stopgap:
"AI-generated depictions and simulated portrayals used for illustrative advertising purposes. Not actual patients or medical
providers. Disclaimer: Individual results may vary. Doctor-prescribed compounded prescription."
- `product.json`: disclaimer set to that text; `_disclaimer_status` = PROVISIONAL, pending Jeremy.
- `SKILL.md` + `references/product-bible.md`: the ⛔ block becomes a ⚠ PROVISIONAL note: drafts allowed; every MOTS-c asset is
  flagged "provisional disclaimer: Jeremy to confirm" in the session hand-off; nothing goes live until he confirms.
- `core/tests/regression.py`: the MOTS-c check now expects finish_batch to render with the provisional text (was: refuse).
- Known: `bible_sync.py --check` will report MOTS-c as not matching its bible page until the bible gets a disclaimer.
Originals in `_originals/2026-10-30/motsc-provisional-disclaimer/`.

## 2026-10-30 — MOTS-c: Creative Messaging doc added as the approved copy source (branch `mots-c-skill`)
Logged before editing. Priestley: "I have a new doc for MOTS-c, we should use that"
(`motsc-creative-messaging-ranked-all-headlines.docx`; copy + text in `_originals/2026-10-30/motsc-messaging-doc/`).
- `references/product-bible.md`: new top section "APPROVED UPDATE — MOTS-c Creative Messaging" (verbatim) that wins over the
  older bible copy where they differ (same pattern as Justin's Sermorelin GHK doc); the bible extract stays below it. New
  pre-screen of all 47 headlines, 9 benefits, 6 CTAs, offer and proof against the global Hard NOs: 36 ✅, 10 ⚠ Jeremy
  ("upgrade / activated / optimized" outcome lines, "Help Your Metabolism Work", "Your Cells Need This", "Support
  Exercise-Like Signaling"), 1 ❌ ("Support Lean Body Goals": body composition, also banned by the doc itself).
- `SKILL.md`: headlines now come from the doc (✅ lines are Tier A); offer "Save up to 40%"; CTA list + "See How It Works";
  the doc's direction (balance men and women, include everyday non-workout concepts, lead with a hook, "MOTS-c" spelling).
- Still BLOCKED: the doc's disclaimer is the website's FDA/supplement statement, marked "confirm for ad use", with no AI
  disclosure. product.json stays empty → finishers refuse. Needs Jeremy's ad disclaimer.
- Flagged, not changed: the doc lists "2 mg/mL | 10 mg per 5 mL vial"; the vial render on file reads "10MG/ML · 5ML". One of
  them is wrong: confirm the render against the website before any ad (strength never appears in copy either way).
  The doc's URL is a staging page (not a live landing page).

## 2026-10-30 — MOTS-c: borrowed winners (branch `mots-c-skill`)
Logged before editing. Priestley: "for MOTS-c, I was told to take inspiration from NAD+, GLP-1 and GHK for winners". New
`references/winners/winners.md`: borrowed cards from the NAD+ (cellular energy), GLP-1 (metabolic) and Sermorelin GHK (all
audiences) winners, each with take / swap (the MOTS-c vial, "MOTS-C" big) / never copy. NAD+ and GLP-1 winners are linked by their
full files in `~/Everlife-Creative/reference-ads/` (their skills live on other branches until merged); GHK by its skill path.
The skill stays blocked (disclaimer pending); this is setup only.

## 2026-10-30 — MOTS-c skill setup, BLOCKED (branch `mots-c-skill`, from `main` 4ee62c6)
Logged before editing. New product skill `skills/everlife-mots-c/` (metabolic peptide, vial, active adults 30–55), scaffolded with
the new-product builder's new `--pending-disclaimer` option from the `everlife-bpc-157` template. Bible checked first: no changes.
**⛔ The bible's MOTS-c disclaimer is "Disclaimer pending"**: product.json carries an empty disclaimer + `_disclaimer_status`, so
every finisher refuses (core/tools/product.py) until Jeremy's verbatim text is in the bible. Vial render from Priestley's download
(`asset-library/VIALS/MOTS-C/MOTS-C VIAL.jpg`, small: 269×559). Also PENDING: all 5 headlines (⏳), both offers ([PLACEHOLDER]).
Setup only: no credits, no push, no PR until every skill is tested.
- Adapted from BPC-157 (originals in `_originals/2026-10-30/skills/everlife-mots-c/`): men and women 30–55, energy + endurance never
  physique, the metabolic-category body-composition Hard NOs up front, "Supports Glucose Metabolism" ⚠ Jeremy, new
  `references/direction.md` (replaces the BPC-157 men's direction), new personas (Distance Dan, Cycling Carla), no offer framework.
  Still recovery-flavoured (fill later): styles 1–5 examples, lessons history (a MOTS-c note at the top says direction.md wins).
- `core/tests/regression.py`: MOTS-c check = finish_batch REFUSES it while the disclaimer is pending (no file written). Smoke 19/19.

## 2026-11-02 — NAD+: BPC-157 template leftovers removed (branch `nad-skill`)
Logged before editing. Priestley: "Yes, do all one by one". The skill was scaffolded from BPC-157 and still carried its recovery,
gym and vial-only rules. Rewritten from `direction.md`, `assets/RENDERS.md` and the ✅ lines of `product-bible.md` only; no new
claims. Originals: `_originals/2026-11-02/nad-leftovers/`.
- **Form fix (blocking):** the video PRODUCT block said "attached vial reference … no capsules or pills anywhere" and the QA lines in
  `finishing.md` / `image-batch.md` said "no capsules or pills anywhere", which would reject every NAD+ tablet ad. Now form-aware:
  sublingual = bottle + exactly one NAD+ tablet (the hero); injection = the vial alone, a still object.
- `styles/6-lifestyle-identity.md`: the "Hardcore gym, tattooed bodybuilder, shirtless" and Pilates sub-styles (BPC-157 brief)
  become NAD+ ones from direction.md (bright morning desk, first coffee, the walk, burnout to back on), each with a ✅ headline.
- `video-prompting.md`: authority examples, copy example, banned-word list, cast wardrobe.
- `styles/` INDEX, 1–5: recovery, tissue, joint, ice-bath and gym sub-styles become clear-head / steady-energy ones; 2E mechanism
  map = cellular energy → focus → healthy aging (✅ lines).
- `image-batch.md`: gym moods become "Bright morning" and "Focused dark" (direction.md palette options); type-table notes; the
  women's "never green" accent rule removed (the pinks/tans rule is only for GHK-Cu Cream and Glow Stack; NAD+'s accent is green).
- `finishing.md`: article kicker default is "CELLULAR ENERGY" (product.json), not "RECOVERY".
- `animated-still.md`: gym environment moves become morning-light ones.
- `lessons.md`: the "BPC-157-specific risks" section (incl. "men must look hardcore", "only one product image, the vial",
  "3 mg/mL vial", "404 page", "PT-141 disclaimer") is rewritten as NAD+ risks; stale BPC-157 notes fixed; the blurred-plate
  9:16 lesson marked superseded.
- Kept on purpose: provenance notes, the shared `vial-refs/` staging folder, "Bounce Back From Burnout" (a ✅ NAD+ headline).

## 2026-10-30 — NAD+: Emily's winners (branch `nad-skill`)
Logged before editing. Emily's Drive folder "NAD Winners" (downloaded by Priestley): 4 statics (Base09, Base41, Base81, Base83;
4:5 + 9:16), dated 25 Sep – 22 Oct 2026. Full files in `~/Everlife-Creative/reference-ads/NAD-winners-2026-10-30/` (not in git).
`references/winners/winners.md` rewritten with a card per winner + previews. Open questions logged there (packaging boxes in the
winners vs our bottle render; held ⚠ lines used in live winners; a strength on Base09).

## 2026-10-30 — NAD+ skill setup (branch `nad-skill`, from `main` 4ee62c6)
Logged before editing. Priestley: GLP-1 and NAD+ (the plain NAD+ page, not Optima NAD+). New skill `skills/everlife-nad/` (cellular
energy, focus, healthy aging; adults 30–65+, all audiences), scaffolded with the new-product builder from `everlife-bpc-157` and
adapted like GLP-1 (two forms). Bible checked first: no changes; NAD+ disclaimer ✅. Two forms (bible: "lead with the choice"):
sublingual tablet (green bottle + green tablet) and injection (green vial), all from the asset library, looked at. The NAD+ nasal
spray render is left out (no spray form in the bible).
- Pre-screen: page lines that clash with the global rules held ⚠ for Jeremy (same decision as GLP-1): "Boost(s)…" (global:
  "supports", never "boosts"), "Reduces Fatigue + Brain Fog" (treatment-like), "Supports DNA Repair" (medical-style), "What
  Celebrities and CEOs Are Using…" / "Trusted by Entrepreneurs and Athletes" (unsourced authority).
- Bible rules built in: "injection" may be named, never shown with a needle; never "needle free" (say "easy sublingual delivery");
  voiceovers say "N-A-D plus"; strengths (200 mg / 1000 mg) never in copy.
- Adapted from BPC-157 (originals in `_originals/2026-10-30/skills/everlife-nad/`): two forms in product.json (sublingual / injection;
  the vial cut out from the asset-library JPG), new `references/direction.md`, personas Priya (38) and Tom (58), `references/winners/`
  (Base09 from the Meta export; file not on hand), all 42 lines screened (6 ⚠, 10 weak). `core/tests/regression.py` (original in
  `_originals/2026-10-30/core/tests/`): 4 NAD+ checks (disclaimer, wrong disclaimer refused, end cards for both forms, looked at
  both). Smoke 22/22. `bible_sync --check`: NAD+ ✅.
Setup only: no credits, no push, no PR until every skill is tested.

## 2026-11-02 — GLP-1: BPC-157 template leftovers removed (branch `glp1-skill`)
Logged before editing. Priestley: "Yes, do all one by one". The skill was scaffolded from BPC-157 and still carried its recovery
and gym wording. Rewritten from `direction.md`, `assets/RENDERS.md` and the ✅ lines of `product-bible.md` only; no new claims.
Originals: `_originals/2026-11-02/glp1-leftovers/`.
- `styles/6-lifestyle-identity.md`: the "Hardcore gym, tattooed bodybuilder, shirtless" and Pilates sub-styles (BPC-157 brief)
  become GLP-1 ones from direction.md (calm breakfast, fridge plan, quiet evening, daylight walk), each with a ✅ headline.
- `video-prompting.md`: authority examples, copy example (now with the price line), banned words (weight numbers, melt/burn,
  body areas, drug brands, "compounded"), cast wardrobe; PRODUCT block names the chosen vial (navy semaglutide / green tirzepatide).
- `styles/` INDEX, 1–5: recovery, tissue, joint, ice-bath and gym sub-styles become calm-control ones; 2E mechanism map =
  appetite → food noise → one plan (✅ lines).
- `image-batch.md`: gym moods become "Bright kitchen" and "Calm evening"; type-table notes; the women's "never green" accent rule
  removed (only for GHK-Cu Cream and Glow Stack; tirzepatide's accent is green).
- `finishing.md`: article kicker default is "WEIGHT MANAGEMENT" (product.json), not "RECOVERY".
- `animated-still.md`: gym environment moves become morning-light ones.
- `lessons.md`: the "BPC-157-specific risks" section (incl. "men must look hardcore", "3 mg/mL vial", "404 page", "PT-141
  disclaimer") rewritten as GLP-1 risks; stale BPC-157 notes fixed; the blurred-plate 9:16 lesson marked superseded.
- Kept on purpose: provenance notes, the shared `vial-refs/` staging folder, "no capsules or pills" (GLP-1 is vials only).

## 2026-10-30 — GLP-1: Emily's winners (branch `glp1-skill`)
Logged before editing. Emily's Drive folder "GLP1 Winners" (downloaded by Priestley): 3 statics (Base186, Base193, Base204; 4:5 +
9:16, made 30 Sep 2026; not in the Meta export, so no numbers yet). Full files in
`~/Everlife-Creative/reference-ads/GLP1-winners-2026-10-30/` (not in git).
- New `references/winners/` (cards + previews).
- All three show both vials side by side. The skill's "one form per ad" was Claude's own rule, not the bible's → both vials together
  now allowed (Priestley's "follow bible" principle). Scales stay out (they imply the weight-loss outcome Priestley held for
  Jeremy); listed as an open question.

## 2026-10-30 — GLP-1 skill setup (branch `glp1-skill`, from `main` 4ee62c6)
Logged before editing. Priestley: "we need to add two more products: GLP-1, NAD+". New skill `skills/everlife-glp-1/` (weight
management, adults 30–60, all audiences), scaffolded with the new-product builder from `everlife-bpc-157` (vial handling) and
adapted like MOTS-c (all audiences, strictest body-composition rules). Bible checked first: no changes; GLP1 disclaimer ✅ (its own
wording). Two forms: compounded semaglutide vial and compounded tirzepatide vial (asset library, looked at both).
- Priestley's decision: the page's weight-loss outcome lines ("Up to 20% Weight Loss", "Drop the Weight and Keep It Off"…) clash with
  the global no-body-composition / no-guaranteed-outcome rules → ⚠ held for Jeremy, used only with explicit OK. Ads lead with
  appetite, food noise, one price and provider-guided care.
- Bible rules built in: "compounded" before semaglutide/tirzepatide always; "GLP-1" as the umbrella in headers; every ad says "one
  price" or "no surprise price increases".
- `core/scripts/bible_sync.py`: the "bible_section" commit (from `spartan-skill`) cherry-picked, because the bible names it "GLP1".
- Adapted from BPC-157 (originals in `_originals/2026-10-30/skills/everlife-glp-1/`): two forms in product.json (semaglutide /
  tirzepatide), new `references/direction.md` (calm control, never a body), personas Maria (41, the bible's core demo) and Ron (56),
  every pre-screen line screened (7 ⚠ weight-loss lines, 2 weak). `core/tests/regression.py`: 4 GLP-1 checks (disclaimer, wrong
  disclaimer refused, end cards for both vials, looked at both). Smoke 22/22. `bible_sync --check`: GLP-1 ✅.
Setup only: no credits, no push, no PR until every skill is tested.

## 2026-11-02 — Spartan Stack: BPC-157 template leftovers removed (branch `spartan-skill`)
Logged before editing. Priestley: "Yes, do all one by one". Recovery and hardcore-gym wording is correct for this product and stays.
Fixed only what belongs to BPC-157: its copy lines, its vial facts and its colour. Originals: `_originals/2026-11-02/spartan-leftovers/`.
- BPC-157's own headlines used as examples (not on any Spartan page: "Don't Let Recovery Be the Bottleneck", "Built to Bounce Back",
  "Train Hard. Recover Smarter." as Tier A, the BPC-157 Men hook list, "Recovery an afterthought?", "Ice Baths Have Limits." …) replaced
  with Spartan lines from `product-bible.md` (⏳ headlines marked as needing an OK; ✅ PROVISIONAL benefits) in `video-prompting.md`,
  `reference-guide.md`, `image-batch.md`, `mens-direction.md`, `styles/1, 3, 6`.
- The "slate" vial / slate-blue accent → the Spartan vial's mustard gold (`assets/RENDERS.md`).
- `video-prompting.md`: offers "none in the bible yet" → none settled (Ronnel); borrowed winners exist; "repair (except the approved
  benefit line)" → no repair line exists for Spartan.
- `lessons.md`: BPC-157 risk section re-checked for Spartan (vial label, men only, no landing page on file, disclaimer source);
  pronunciation and caption spellings; blurred-plate 9:16 lesson marked superseded.
- NOT changed (open decision): the angle questions, style 2E and image-batch benefit examples quote the unswapped Spartan page,
  while the pre-screen table uses the PROVISIONAL swapped page. Waiting on the bible owner / Jeremy for the swap.

## 2026-10-30 — Spartan Stack: PROVISIONAL swap + headlines, gate lifted (branch `spartan-skill`)
Logged before editing. Bible-updates hand-off §6 proposed it; Priestley approved (reverses his earlier "wait for the bible fix").
Cause of the swap (team): the NEW Product Benefits Doc has the two stacks' labels flipped. PROVISIONAL — Jeremy to confirm.
- `references/product-bible.md`: pre-screen now uses the Wolverine page's benefit lines (the 3-peptide ones, incl. "Supports Healthy
  Inflammatory Balance" for KPV); "3 Peptides. One Recovery Protocol." moved here; provisional headlines "One Dose. Three Peptides. No
  Weak Links." and "Recovery, Fortified". Offer stays out (39/46/XX% disagree; Ronnel to confirm).
- `SKILL.md`, `image-batch.md`, `video-prompting.md`: the ⛔ gate becomes a ⚠ PROVISIONAL note; ingredients may be named together as
  on the label; "inflammation" allowed only in the exact KPV line. `product.json`: `_blocked` → `_provisional`.
Originals in `_originals/2026-10-30/stack-provisional/spartan/`.

## 2026-10-30 — Spartan Stack: labels confirmed, waiting for the bible fix (branch `spartan-skill`)
Priestley shared marked-up label crops: the vial labels are correct (Spartan = BPC-157 / KPV / TB-500; Wolverine = BPC-157 +
TB-500). The bible has the two stack pages swapped. Decision: wait for the bible fix (no partial unblock). The block wording in
SKILL.md, image-batch.md, video-prompting.md, product.json `_blocked`, RENDERS.md and product-bible.md now says so, with the steps to
take once the live bible is corrected.

## 2026-10-30 — Spartan Stack: borrowed winners (branch `spartan-skill`)
Logged before editing. Emily: "Wolverine, Spartan and MOTS-c use GHK and Sermorelin visuals instead. Rugged manly men." Priestley
approved. New `references/winners/winners.md`: 5 statics + 2 videos from the Sermorelin / Sermorelin GHK men's winners (CPA-ranked),
linked, not copied; per card what to take, what to swap (the vial as hero, "SPARTAN STACK" big) and what never to copy
(body-composition, injury, comparison and price lines, old ratings). SKILL.md points to it; "spin a winner" uses it.

## 2026-10-30 — Spartan Stack skill setup (branch `spartan-skill`, from `main` 4ee62c6)
Logged before editing. New product skill `skills/everlife-spartan/` (recovery stack, vial, active men 25–55), scaffolded with the
new-product builder from the `everlife-bpc-157` template. Bible checked first: no changes; Spartan disclaimer ✅. Vial render from
Priestley's download (filed as `asset-library/VIALS/SPARTAN/SPARTAN VIAL.jpg`). **⛔ Generation blocked:** the vial label
(BPC-157 / KPV / TB-500, three peptides) contradicts the bible page (BPC-157/TB500, "Two-Peptide Recovery Stack"); Wolverine is the
mirror image. Needs confirmation (Justin/Jeremy) before any ad. Also PENDING: all 4 headlines (⏳), offer ([PLACEHOLDER]).
Setup only: no credits, no push, no PR until every skill is tested.
- Adapted from BPC-157 (originals in `_originals/2026-10-30/skills/everlife-spartan/`): men 25–55 only (women's persona and
  direction removed), bible creative direction (rugged, fight imagery without blood/gore, no animal death, "Spartan Stack" in every
  asset), no offer framework, approved benefits as Tier A headlines (all bible headlines ⏳), no ingredient list in copy, "SPARTAN"
  big / never "by Everlife" on images, the ⛔ label gate in SKILL.md, image-batch, video-prompting and product.json `_blocked`.
- `core/tests/regression.py`: 4 Spartan checks (static disclaimer, wrong disclaimer refused, end cards default + tiktok, looked at
  both; short row labels after a tiktok collision). Smoke 22/22.
- `core/scripts/bible_sync.py` (original in `_originals/2026-10-30/core/scripts/`): `--check` now also reads an optional
  `"bible_section"` in product.json (the stacks' bible headings carry their ingredients, e.g. "Spartan Stack (BPC-157/TB500)").
  Spartan's product.json sets it. One commit, cherry-picked unchanged onto the other stack branches so merges stay clean.

## 2026-11-02 — Wolverine Stack: BPC-157 template leftovers removed (branch `wolverine-skill`)
Logged before editing. Priestley: "Yes, do all one by one". Recovery and hardcore-gym wording is correct for this product and stays.
Fixed only what belongs to BPC-157: its copy lines, its vial facts and its colour. Originals: `_originals/2026-11-02/wolverine-leftovers/`.
- BPC-157's own headlines used as examples (not on any Wolverine page: "Don't Let Recovery Be the Bottleneck", "Built to Bounce Back",
  "Train Hard. Recover Smarter." as Tier A, the BPC-157 Men hook list, "Recovery an afterthought?", "Ice Baths Have Limits." …) replaced
  with Wolverine lines from `product-bible.md` (⏳ / ⚠ headlines marked as needing an OK; ✅ PROVISIONAL benefits) in
  `video-prompting.md`, `reference-guide.md`, `image-batch.md`, `mens-direction.md`, `styles/1, 3, 5, 6`.
- The "slate" vial / slate-blue accent → the Wolverine vial's matte black and gold (`assets/RENDERS.md`).
- `video-prompting.md`: offers "none in the bible yet" → "Save up to 39%" (⚠ PROVISIONAL); borrowed winners exist.
- `lessons.md`: BPC-157 risk section re-checked for Wolverine (vial label, offer, men only, no landing page on file, disclaimer
  source); pronunciation and caption spellings; blurred-plate 9:16 lesson marked superseded.
- NOT changed (open decision): lines that depend on the swapped Spartan / Wolverine bible pages. Waiting on the bible owner / Jeremy.

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

## 2026-11-02 — Lovara: stale "nothing yet" notes fixed (branch `lovara-skill`)
Logged before editing. Priestley: "Yes, do all one by one" (template-leftover pass). Lovara's PT-141 / Sermorelin mentions are
attributed lessons and stay. Fixed three statements that were true at scaffolding and are not now. Originals:
`_originals/2026-11-02/lovara-stale/`.
- `lessons.md`: "No Lovara ads have been made" → batches 1 and 2 (2026-10-30) exist, lessons at the bottom.
- `video-prompting.md`: "No Lovara video winners" → V18, V26, V32 in `winners/winners.md`.
- `reference-guide.md`: "our own Lovara winners (none on file yet)" → points to `winners/winners.md`.
- Not changed: no pronunciation for "Lovara" is on file; add it once the team confirms how it is said.

## 2026-10-30 — Lovara: Emily's winners (branch `lovara-skill`)
Logged before editing. Emily's Drive folder "Lovara" (downloaded by Priestley): 3 statics (360555 A2/A3, Base161), 3 videos
(Video 32, 26, 18) and her note listing the all-time winners whose files she could NOT find (INT24 120 sales, INT4 112, INT13 95,
INT17 77…). Full files in `~/Everlife-Creative/reference-ads/Lovara-winners-2026-10-30/` (not in git).
- New `references/winners/`: winners.md (Emily's full ranking + a card per file: take / never copy) + small previews.
- SKILL.md points to it. No rule changes: several of these winners break today's rules (lingerie, bed/bedroom, per-ingredient
  benefit claims, 4.8 / 50,000 / 70,000 proof): they are format references only.
- Couples (Priestley: "Follow bible for now"): the skill's own "no couples" was stricter than the bible. Replaced with the bible's
  wording: "no generic stock-style couples", "product imagery led", "no bedroom scenes" (SKILL.md, image-batch.md,
  video-prompting.md, winners.md). "Couples in bed" stays banned (bedroom).

## 2026-10-30 — Lovara skill (branch `lovara-skill`, from `main` 4ee62c6)
Logged before editing. New product skill `skills/everlife-lovara/` (women's intimacy support, women 30–55), built per
the plan doc "New Product Skills: Build Plan" (https://claude.ai/artifact/8y75Kmn6hUKtSsoTLzxhaf), recipe "How to build
one product skill". Bible checked first: `bible_sync.py` against the live bible = no changes since the 30 Oct sync.
- Template: a copy of `skills/everlife-pt-141/` (intimate wellness), adapted to Lovara; `core -> ../../core` link kept.
- `product.json` / `product.env`: id `lovara`, verbatim bible ad disclaimer, renders listed but **not on file** (form
  not stated in the bible; PMG samples show a pink tablet) → `assets/MISSING_RENDERS.md`; generation blocked until added.
- `references/product-bible.md`: the bible's Lovara section verbatim + a compliance pre-screen (for Jeremy).
- Skill files adapted: women-only audience, tasteful product-led creative (no beds/bedroom), women's colours, each
  ingredient claim only on its own ingredient, today's image rules (no "by Everlife", name big, a different person per ad).
- Open: renders + form; Justin (ingredient list, "Support Your Spark" CTA); Jeremy (⚠ lines); winners; landing page.
- No credits spent. No push/PR until the tests pass and a real test batch looks right.
- Done (free steps): skill files written (SKILL.md, product.json/env, bible extract + pre-screen, image-batch, video-prompting,
  finishing, lessons, personas, reference-guide, reviews, styles ×7; PT-141 renders/winners/team refs/reviews removed, generic
  style boards kept). Statics default to product-only (Mitansh's PT-141 verdict on GPT Image people statics).
- `core/tests/regression.py` (original in `_originals/2026-10-30/core/tests/`): 3 Lovara checks (static finish with its disclaimer,
  wrong disclaimer refused, video refused while `lovara_bottle.png` is missing). Smoke 18/18 before, 21/21 after.
- `bible_sync.py --check`: Lovara ✅. Pre-existing, not ours: BPC-157's disclaimer is not in the bible ("Disclaimer pending").
- Preflight: 8 passed, 3 to fix (both renders missing; Marketing Studio registration needs them). Creatify project not created yet
  (it imports the renders).
- Then (same day): Priestley downloaded the asset library's TABLETS/CAPSULES folder (→ `~/Everlife-Creative/asset-library/`) and the
  PMG Ad folder (→ `~/Everlife-Creative/reference-ads/`). **Lovara is an oral capsule (30 per bottle), not a tablet.** Added
  `assets/lovara_bottle.png` (+ `_ref.jpg` on white) and `assets/lovara_capsule.png` (cut out from the JPG on white); looked at both.
  `MISSING_RENDERS.md` → `RENDERS.md` (with the bottle wording for prompts); "tablet" → "capsule" across the skill (originals in
  `_originals/2026-10-30/skills/everlife-lovara/`). `product.json`: `pill_end_scale` 0.36 (the tall capsule covered the end-card
  headline at full size). Regression: the "video refused without renders" check replaced by Lovara end-card renders (default + tiktok):
  smoke 22/22. Preflight 9/10 (only Marketing Studio registration open, optional, for UGC).
- Test batch-1 (4 statics, 4:5, product-only, 5 Creatify credits approved by Priestley): `assets/creatify.json` (the Lovara
  Creatify project + imported bottle/capsule) and `references/lessons.md` (batch-1 lessons appended). All 4 pass QA after one
  reposition fix on L4 (benefit lines under the footer). Gap flagged: `finish_batch` checks text under the footer only at 9:16.

## 2026-11-02 — Spark: stale "no ads yet" note fixed (branch `spark-skill`)
Logged before editing. Priestley: "Yes, do all one by one" (template-leftover pass). Spark's PT-141 / spray mentions are already
labelled as template history and stay. `lessons.md`: "No Spark ads have been made" → batches 1–3 (2026-10-30) exist.
Originals: `_originals/2026-11-02/spark-stale/`. Not changed (open decision for Priestley): the "3D-animated couple story" style
in SKILL.md vs the team's rejection of cartoon characters.

## 2026-10-30 — Spark: PROVISIONAL CTA "Get Started Now" (branch `spark-skill`)
Logged before editing. Bible-updates hand-off §6 (other session) proposed it; Priestley approved. All four bible CTAs are still
⏳ Pending approval; "Get Started Now" is already an approved (✅) CTA on the MOTS-c, GLP-1 and NAD+ pages, so it becomes Spark's
provisional default. PROVISIONAL — Jeremy to confirm; every asset's SESSION.md says so.
- `SKILL.md` (rule 3, CTA gate, round-1 CTA question), `references/product-bible.md` (pre-screen), `references/image-batch.md`.
Originals in `_originals/2026-10-30/spark-provisional-cta/`.

## 2026-10-30 — Spark: Emily's winners + tablet-hero / warm-default update (branch `spark-skill`)
Logged before editing. Emily shared the Spark winners (Drive "Spark - Oct-30-2026": 7 statics in 1:1 + 9:16, 3 videos in 4:5 +
9:16); full files in `~/Everlife-Creative/reference-ads/Spark-winners-2026-10-30/` (not in git). Priestley approved the update after
the test batch showed the bottle dominating (bible Standards 03: "the pill or tablet is the hero, not the bottle") and asked what the
bible says on colour (no Spark direction; global "warm, sun-lit"). Originals in `_originals/2026-10-30/skills/everlife-spark/`.
- `references/winners/`: winners.md rewritten with a card per winner (what to take, what never to copy) + small previews.
- `references/image-batch.md`, `SKILL.md`: tablet hero (larger than the bottle, in front), the winners' "big SPARK + huge tablet +
  three icon pills" framework, warm-and-light default mood (dark is an option), "spin a winner" points at the cards.
- `references/video-prompting.md`, `references/lessons.md`, `references/personas.md`: 3D-animated couple videos are an option for
  Spark (2 of its 3 winning videos), replacing the inherited PT-141 "no cartoons" lesson for this product only.

## 2026-10-30 — Spark skill setup (branch `spark-skill`, from `main` 4ee62c6)
Logged before editing. New product skill `skills/everlife-spark/` (PT-141 + Apomorphine + Tadalafil, sublingual tablet,
men and women 30–65+), scaffolded with the new-product builder (`new-product-skill` branch, run from a scratch copy) from the
`everlife-pt-141` template. Bible checked first: no changes since the 30 Oct sync; Spark disclaimer ✅. Renders from the asset
library (`TABLETS-CAPSULES/SPARK/`), looked at both. Gaps left PENDING: CTAs (all 4 pending approval), ED headlines (pending,
Jeremy). Product Hard NO: never tie a benefit to one ingredient. Setup only: no credits, no push, no PR until every skill is tested.
- Adapted from the PT-141 template (originals in `_originals/2026-10-30/skills/everlife-spark/`): one form (sublingual tablet), men +
  women, combo-only ingredient rule, CTA gate (all 4 ⏳; the user OKs one per session), "SPARK" big / never "by Everlife" on images,
  4:5 default + Lovara's layout block, product-only by default, no palette limit (≥1 dark ad per batch), offer Save up to 51%.
- `references/product-bible.md`: product facts + a filled compliance pre-screen (ED headlines ⏳ + ⚠ Jeremy). `references/winners/
  winners.md` from the Meta export (Base04/08/14 lead, one video; creative files not on hand). `assets/RENDERS.md` bottle wording;
  `assets/creatify.json` stub (project made on the first run).
- `core/tests/regression.py` (original in `_originals/2026-10-30/core/tests/`): 4 Spark checks (static disclaimer, wrong disclaimer
  refused, end cards default + tiktok, looked at both). Smoke 22/22. `bible_sync --check`: Spark ✅. Preflight 8/10 (Marketing Studio
  registration optional for UGC; venv flag only because the run pointed at the repo tools).
- Test batch (14 Creatify credits, approved by Priestley; CTA "Explore Spark" OK'd for the test, ⏳ for Jeremy): `assets/creatify.json`
  (project), `references/lessons.md` (native 9:16 failed 4/4 on safe zones; 4:5 → compose916 → `--fit trusted` passed 4/4; 2/4
  4:5 raws needed a fix for product under the footer). Results in `~/Everlife-Creative/output/Spark/2026-10-30_batch-2-4x5/SESSION.md`.
  The finisher gap it exposed is fixed on its own branch (`safezone-sides`).

## 2026-10-30 — New-product builder: `--pending-disclaimer` (branch `new-product-skill`)
Logged before editing. Priestley: set every product up now and fill gaps later. `scripts/new_product.py create … --pending-disclaimer`
scaffolds a product whose bible disclaimer is pending, blocked: product.json gets an empty disclaimer + `_disclaimer_status`, and
`core/tools/product.py` already refuses to finish anything for it. Used for MOTS-c (`mots-c-skill`). SKILL.md rule 2 notes the
exception. Original in `_originals/2026-10-30/skills/everlife-new-product/`.

## 2026-10-30 — New-product skill builder (branch `new-product-skill`, from `main` 4ee62c6)
Logged before editing. New skill `skills/everlife-new-product/` (Priestley: "a skill to smoothly ask us questions on making a new
skill for the next product"): it turns the plan doc's recipe ("How to build one product skill",
https://claude.ai/artifact/8y75Kmn6hUKtSsoTLzxhaf) into a guided, bible-first flow: pick the product → one summary card read from the
synced bible, the local asset library, the reference ads and the Meta winners export → ask only about gaps (template, form, missing
renders, flagged copy errors) → scaffold the skill on its own branch → adapt → test → stop at the two human gates (the first paid test
batch, the PR). Worked example: the Lovara build on branch `lovara-skill` (same day).
- `skills/everlife-new-product/SKILL.md` (the flow), `references/human-inputs.md` (what only people can provide),
  `references/templates.md` (which skill to copy), `references/adapt-checklist.md` (every file to adapt and the rules every new
  product inherits), `scripts/new_product.py` (`inspect` = the summary card; `create` = the scaffold: copy, strip the template's
  product files, product.json/env with the verbatim disclaimer, the bible extract, renders from the asset library, copy-log seed).
- Not a product skill: no product.json (bible_sync and the shared tools skip it). No shared code changed. No credits.

## 2026-10-30 — 9:16 safe-zone check: side bands + logo overlap (branch `safezone-sides`, from `main` 4ee62c6)
Priestley's Spark 9:16 safe-zone test showed `finish_batch.py` only checked the bottom (content under the proof row): three raws
with headline/CTA/product in the Reels side bands and one with the ad's own name under the Everlife logo all passed. Approved by
Priestley ("Yes, on its own branch"). Original in `_originals/2026-10-30/core/tools/finish_batch.py`.
- 9:16, unless `--fit force`: refuse when the ad's own type/product sits under the logo (edge "busy" > 0.12).
- 9:16 with `--fit none`: refuse when the left/right Reels band (outside x 156–924) has type or product (edge density > 0.09);
  warn above 0.05. Calibrated on the 4 Spark raws + 20 Sermorelin r3 raws: all 4 Spark raws refused with the right reason (S1
  bottom, S2/S4 left band, S3 logo); the Sermorelin logo refusals were checked by eye and are real (their name runs into the logo
  area). `--fit trusted` (compose916 / reposition outputs) keeps the logo check and skips the side check (geometry is known).
- Smoke 18/18. Videos (full_layout) do not use this path; animate_still checks only its first frame.
- Not changed: earlier finals already made from older raws (e.g. Sermorelin W1/GHK W2 have type or faces in the bands).

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
- 2026-10-30: MANDATORY "<Product> by Everlife" in every video VO + intro (creative-system §0; golden rule 0 in restora-z, bpc-157, pt-141).
- 2026-10-30: 🧑‍💼 AI Avatar Video option in all 5 skills → core/references/ai-avatar-video.md + core/tools/avatar_video.py (broll/shift/animatic/key/composite/caps/sheet).
