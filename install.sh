#!/usr/bin/env bash
# Links every product skill in this repo into ~/.claude/skills/ so `git pull` updates them in place.
# An existing (non-linked) copy of a skill is moved to ~/.claude/skills-backup/ first, never deleted.
# Also (each step skipped when already done; files are backed up, never replaced):
#   - adds the EverlifeMD creative gates + team notes to ~/.claude/CLAUDE.md as one managed import block
#   - links the creative bible to ~/.claude/everlife/creative-bible.md when there is none
#   - adds a short list of read-only commands to Claude Code's allow list (nothing that spends credits)
#   bash install.sh
set -e
REPO="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.claude/skills"
BACKUP="$HOME/.claude/skills-backup"
STAMP="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$DEST"

for skill in "$REPO"/skills/*/; do
  name="$(basename "$skill")"
  target="$DEST/$name"
  # a skill reaches the shared toolkit through skills/<name>/core -> ../../core; some unzip tools flatten that link
  if [ ! -L "${skill}core" ] || [ ! -d "${skill}core/tools" ]; then
    rm -rf "${skill}core" && ln -s ../../core "${skill}core" && echo "… repaired the core link in $name"
  fi
  if [ -L "$target" ]; then
    rm "$target"
  elif [ -e "$target" ]; then
    mkdir -p "$BACKUP"
    mv "$target" "$BACKUP/$name-$STAMP"
    echo "… moved old copy of $name to $BACKUP/"
  fi
  ln -s "${skill%/}" "$target"
  echo "✅ $name → ${skill%/}"
done

# Creative gates: one managed block in ~/.claude/CLAUDE.md that imports the repo's files (updated by git pull)
CMD="$HOME/.claude/CLAUDE.md"
BEGIN="# >>> everlife-ad-factory (managed by install.sh, do not edit inside) >>>"
END="# <<< everlife-ad-factory <<<"
BLOCK="$BEGIN
@$REPO/core/claude/everlife-gates.md
@$REPO/core/claude/everlife-team.md
$END"
if [ -f "$CMD" ] && grep -qF "$BEGIN" "$CMD"; then
  python3 - "$CMD" "$BEGIN" "$END" "$BLOCK" <<'EOF'
import sys
p, b, e, block = sys.argv[1:]
s = open(p).read()
i, j = s.index(b), s.index(e) + len(e)
open(p, "w").write(s[:i] + block + s[j:])
EOF
  echo "✅ creative gates already in $CMD (block refreshed)"
elif [ -f "$CMD" ] && grep -q "EverlifeMD Creative Gates" "$CMD"; then
  echo "✅ creative gates already written into $CMD by hand (left as is)"
else
  if [ -f "$CMD" ]; then cp "$CMD" "$CMD.backup-$STAMP"; echo "… backed up $CMD"; fi
  printf '\n%s\n' "$BLOCK" >> "$CMD"
  echo "✅ creative gates added to $CMD"
fi

# Creative bible: the gates point to ~/.claude/everlife/creative-bible.md
BIB="$HOME/.claude/everlife/creative-bible.md"
mkdir -p "$(dirname "$BIB")"
if [ -L "$BIB" ] || [ ! -e "$BIB" ]; then
  ln -sfn "$REPO/core/claude/creative-bible.md" "$BIB"
  echo "✅ creative bible linked → $BIB"
else
  echo "✅ creative bible: kept your own copy at $BIB (the repo copy is $REPO/core/claude/creative-bible.md)"
fi

# Read-only commands Claude may run without asking (fewer permission prompts). Never generation or spending.
python3 - "$HOME/.claude/settings.json" "$STAMP" <<'EOF'
import json, os, shutil, sys
p, stamp = sys.argv[1:]
SAFE = [
    "Bash(ls:*)", "Bash(open:*)",
    "Bash(higgsfield workspace list:*)", "Bash(higgsfield account:*)", "Bash(higgsfield generate cost:*)",
    "Read(~/Everlife-Creative/**)", "Read(~/.claude/skills/**)", "Read(~/.claude/everlife/**)",
    "mcp__plugin_creatify-ad-agent_creatify-ad-agent__composer_billing_state",
    "mcp__plugin_creatify-ad-agent_creatify-ad-agent__composer_task_status",
]
d = {}
if os.path.exists(p):
    try:
        d = json.load(open(p))
    except ValueError:
        print(f"… {p} is not valid JSON: allow list not changed"); sys.exit(0)
allow = d.setdefault("permissions", {}).setdefault("allow", [])
new = [r for r in SAFE if r not in allow]
if not new:
    print("✅ read-only commands already allowed"); sys.exit(0)
if os.path.exists(p):
    shutil.copy(p, f"{p}.backup-{stamp}")
allow.extend(new)
os.makedirs(os.path.dirname(p), exist_ok=True)
json.dump(d, open(p, "w"), indent=2)
print(f"✅ {len(new)} read-only commands added to Claude Code's allow list")
EOF

echo
echo "Next: install the shared finishing toolkit once (or run core/scripts/update.sh, which does everything):"
echo "  bash ~/.claude/skills/everlife-restora-z/core/scripts/preflight.sh --install"
