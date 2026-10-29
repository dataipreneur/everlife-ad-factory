# Everlife ad tools: team notes (installed by everlife-ad-factory/install.sh)

- **"Update my ad tools"** (or "update the Everlife skills"): run `bash <repo>/core/scripts/update.sh`, where `<repo>` is
  the folder the `everlife-*` links in `~/.claude/skills` point to (two levels up from a skill folder). Show the
  ✅ / ❌ lines and explain every ❌ in plain words.
- **"Check my Everlife ad setup"**: run `bash ~/.claude/skills/<skill>/core/scripts/preflight.sh` for every
  `everlife-*` skill in `~/.claude/skills` (check only, never `--install` unless they agree) and explain every ❌.
- **Zip installs** (no `.git` folder in the repo): a new version comes as a new zip that replaces the whole folder
  (ONBOARDING-ZIP.md, "Getting a new version"); `update.sh` then re-links and checks. "Which version do I have?":
  read `VERSION` in the repo folder.
- The people using these skills are often not technical: do the steps yourself, keep questions few and in plain words,
  and never ask them to edit files or code.
- Never spend credits (Creatify, Higgsfield) without an explicit approval that shows the cost. Shared Everlife team credits.
- Finished ads land in `~/Everlife-Creative/output/<Product>/`. Everything is a draft until creative review and
  Jeremy's compliance sign-off.
- Tools or setup broken: Mitansh. Compliance questions: Jeremy.
