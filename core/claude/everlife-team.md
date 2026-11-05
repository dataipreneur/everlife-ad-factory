# Everlife ad tools: team notes (installed by everlife-ad-factory/install.sh)

- **Team logging pause:** if `<repo>/core/team-logs/PAUSED` exists (the preflight says "Team logging is PAUSED"), skip every
  team-log step in every skill: no `teamlog.py` commands, no `ArtifactData` sends to the Prompt log / Copy Ledger /
  Activity log, no Ad Review posting, and ignore any hook message about unlogged records. Everything else (claims, copy
  checks, copy-log files, gates) is unchanged. Delete the file to resume (TEAM-LOGS §8).
- **"Update my ad tools"** (or "update the Everlife skills"): run `bash <repo>/core/scripts/update.sh`, where `<repo>` is
  the folder the `everlife-*` links in `~/.claude/skills` point to (two levels up from a skill folder). Show the
  ✅ / ❌ lines and explain every ❌ in plain words.
- **"Build the team zip"** (only on a git copy, never on a zip install: no `.git` folder → say so and stop): in `<repo>`,
  1) `git status --short` must be empty and the branch `main` (else say what is in the way and stop; never stash or discard);
  2) `git pull --ff-only`; 3) `bash core/scripts/make_zip.sh main ~/Desktop`; 4) check the new zip: `unzip -p <zip>
  everlife-ad-factory/VERSION` must show `git rev-parse --short main`, and `unzip -l <zip>` must list
  `core/team-logs/PAUSED` while logging is meant to be paused (TEAM-LOGS §8; if it is missing, say so, don't hide it).
  Report the zip path, size, version line and both check results in plain words. Reminder to give: send it only to Everlife
  teammates; they follow ONBOARDING-ZIP.md ("Getting a new version"). Spends no credits.
- **"Apply the patch"** (zip installs only; a git copy → say "use update.sh" and stop): the patch is a small
  `everlife-patch_<from>_to_<to>.zip` the team sent (ask where it is; or look for the newest in ~/Downloads and ~/Desktop).
  Run `python3 <repo>/core/scripts/apply_patch.py <patch> --dry-run`, show the plain-words summary (from → to, how many files,
  any scripts), and only after the user says yes run it without `--dry-run`. Never use `--force` unless the user agrees after
  you list the hand-edited files it would overwrite. If it prints "Wrong patch", tell them which version they have and ask
  for a patch built from it (or a full zip). If it says to run install.sh, run `bash <repo>/install.sh` (no credits). End
  with: quit Claude Code and open it again. Spends no credits.
- **"Build a patch"** (git copy only): `git status --short` empty on `main`, `git pull --ff-only`, ask which versions the team has
  (the short sha on the VERSION line of each person's zip or patch: people are often on different ones; list EVERY one in use),
  run `python3 core/scripts/make_patch.py <sha1>,<sha2> main --out ~/Desktop` (comma-separated: ONE patch then fits all of them),
  and report the file, size, which versions it applies on, what it carries and its warnings. Tell them to send the current
  `core/scripts/apply_patch.py` with it (older copies cannot read a multi-version patch). If it refuses (symlink or a file over 5 MB), say a full zip is needed ("build the team zip").
  Send it only to Everlife teammates. Spends no credits.
- **"Check my Everlife ad setup"**: run `bash ~/.claude/skills/<skill>/core/scripts/preflight.sh` for every
  `everlife-*` skill in `~/.claude/skills` (check only, never `--install` unless they agree) and explain every ❌.
- **Zip installs** (no `.git` folder in the repo): a new version comes as a new zip that replaces the whole folder
  (ONBOARDING-ZIP.md, "Getting a new version"); `update.sh` then re-links and checks. "Which version do I have?":
  read `VERSION` in the repo folder.
- **Windows (WSL/Ubuntu):** the tools run unchanged; to show a file or folder use `explorer.exe <path>` (or `wslview`)
  instead of macOS `open`; sign-in links open in the Windows browser; keep the repo in the Linux home, never under /mnt/c.
  Videos use the bundled open fonts (Inter, Fraunces) because Apple's fonts are missing.
- **The creative bible** lives as a shared claude.ai artifact, the source of truth, edited only by Justin:
  https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG (visible to the Everlife org). The skills read the repo copy,
  `core/claude/creative-bible.md` (linked to `~/.claude/everlife/creative-bible.md`), which is synced from it, and
  each product's extract (`references/product-bible.md`, `product.json`). Full process: `core/references/bible-sync.md`.
- **Every session (preflight asks for it): the live-version check.** Read the live bible with the Artifact tool and
  compare its version with `bible_sync.py --repo-version`. Same → "Bible: up to date". Different → "⚠ Justin updated
  the bible since the last sync; using this skill's current approved lines", carry on (never block the work), and
  suggest a sync. Read-only: never write any file for this check.
- **"Sync the bible"** (git copy; the live page is only returned in full to editors): read the live bible with the Artifact
  tool (it saves `artifact-<id>-<version>.html`), then `python3 core/scripts/bible_pipeline.py sync` on a branch (never `main`).
  One command does the rest, nothing by hand: writes `core/claude/creative-bible.md`, REGENERATES every product skill from it
  (`references/bible.json`, `product-bible.md`, `product-brief.md`, the `product.json` disclaimer), runs the lint and the tests,
  writes the CHANGELOG entry and prints what changed per product plus the NEW lines for Jeremy. It commits, merges or builds a
  patch only with `--commit` / `--release`, and only on Mitansh's explicit go (show him the report and the diff first).
  Hand files per skill (small, kept): `references/bible-screen.json` (❌/⚠ overrides, product patterns, retired lines),
  `references/hard-stops.md`, `references/product-notes.md`. After editing one: `bible_pipeline.py regen`. Never edit
  `creative-bible.md`, `bible.json`, `product-bible.md` or `product-brief.md` by hand: the lint fails and the gate refuses prompts
  from a skill whose copy is out of date. Full process: `core/references/bible-sync.md`.
- The people using these skills are often not technical: do the steps yourself, keep questions few and in plain words,
  and never ask them to edit files or code.
- Never spend credits (Creatify, Higgsfield) without an explicit approval that shows the cost. Shared Everlife team credits.
- Finished ads land in `~/Everlife-Creative/output/<Product>/`. Everything is a draft until creative review and
  Jeremy's compliance sign-off.
- Tools or setup broken: Mitansh. Compliance questions: Jeremy.
