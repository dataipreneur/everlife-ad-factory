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
- **The creative bible** lives as a shared claude.ai artifact, the source of truth, edited only by Justin:
  https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG (visible to the Everlife org). The skills read the repo copy,
  `core/claude/creative-bible.md` (linked to `~/.claude/everlife/creative-bible.md`), which is synced from it, and
  each product's extract (`references/product-bible.md`, `product.json`). Full process: `core/references/bible-sync.md`.
- **Every session (preflight asks for it): the live-version check.** Read the live bible with the Artifact tool and
  compare its version with `bible_sync.py --repo-version`. Same → "Bible: up to date". Different → "⚠ Justin updated
  the bible since the last sync; using this skill's current approved lines", carry on (never block the work), and
  suggest a sync. Read-only: never write any file for this check.
- **"Sync the bible"** (needs edit access to the artifact: the full page is only returned to editors; viewers see a
  summary and can only do the version check). Never on `main` (`--write` refuses there): make a branch, run
  `bible_sync.py <saved html> --check`, then `--write`; for every skill the report lists, re-copy its VERBATIM block,
  mark new lines "NEW, not screened", screen them (✅ / ⚠ / ❌ against the global rules), update `product.json`'s
  disclaimer if it changed, log it in CHANGELOG.md, open a PR (claims, disclaimers or approvals need Jeremy's
  sign-off). Never edit `creative-bible.md` by hand.
- The people using these skills are often not technical: do the steps yourself, keep questions few and in plain words,
  and never ask them to edit files or code.
- Never spend credits (Creatify, Higgsfield) without an explicit approval that shows the cost. Shared Everlife team credits.
- Finished ads land in `~/Everlife-Creative/output/<Product>/`. Everything is a draft until creative review and
  Jeremy's compliance sign-off.
- Tools or setup broken: Mitansh. Compliance questions: Jeremy.
