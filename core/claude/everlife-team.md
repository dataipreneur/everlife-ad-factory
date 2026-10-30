# Everlife ad tools: team notes (installed by everlife-ad-factory/install.sh)

- **"Update my ad tools"** (or "update the Everlife skills"): run `bash <repo>/core/scripts/update.sh`, where `<repo>` is
  the folder the `everlife-*` links in `~/.claude/skills` point to (two levels up from a skill folder). Show the
  ✅ / ❌ lines and explain every ❌ in plain words.
- **"Check my Everlife ad setup"**: run `bash ~/.claude/skills/<skill>/core/scripts/preflight.sh` for every
  `everlife-*` skill in `~/.claude/skills` (check only, never `--install` unless they agree) and explain every ❌.
- **Zip installs** (no `.git` folder in the repo): a new version comes as a new zip that replaces the whole folder
  (ONBOARDING-ZIP.md, "Getting a new version"); `update.sh` then re-links and checks. "Which version do I have?":
  read `VERSION` in the repo folder.
- **Windows (WSL/Ubuntu):** the tools run unchanged; to show a file or folder use `explorer.exe <path>` (or `wslview`)
  instead of macOS `open`; sign-in links open in the Windows browser; keep the repo in the Linux home, never under /mnt/c.
  Videos use the bundled open fonts (Inter, Fraunces) because Apple's fonts are missing.
- **The creative bible** lives as a shared claude.ai artifact, the source of truth:
  https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG (visible to the Everlife org). The skills read the repo copy,
  `core/claude/creative-bible.md` (linked to `~/.claude/everlife/creative-bible.md`), which is synced from it.
- **"Check the bible for updates"**: read the live bible with the Artifact tool (`read`, the link above; it saves the
  page's HTML locally and says where), then run `python3 <repo>/core/scripts/bible_sync.py <that html> --check` and
  report the changes per product in plain words, plus any skill whose disclaimer no longer matches. If anything changed:
  on a new branch, run it again with `--write`, update the affected skills' `references/product-bible.md`, log it in
  CHANGELOG.md, and open a PR (claims, disclaimers or approvals need Jeremy's sign-off before merge). Never edit
  `creative-bible.md` by hand.
- The people using these skills are often not technical: do the steps yourself, keep questions few and in plain words,
  and never ask them to edit files or code.
- Never spend credits (Creatify, Higgsfield) without an explicit approval that shows the cost. Shared Everlife team credits.
- Finished ads land in `~/Everlife-Creative/output/<Product>/`. Everything is a draft until creative review and
  Jeremy's compliance sign-off.
- Tools or setup broken: Mitansh. Compliance questions: Jeremy.
