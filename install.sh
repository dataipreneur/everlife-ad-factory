#!/usr/bin/env bash
# Links every product skill in this repo into ~/.claude/skills/ so `git pull` updates them in place.
# An existing (non-linked) copy of a skill is moved to ~/.claude/skills-backup/ first, never deleted.
#   bash install.sh
set -e
REPO="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.claude/skills"
BACKUP="$HOME/.claude/skills-backup"
mkdir -p "$DEST"

for skill in "$REPO"/skills/*/; do
  name="$(basename "$skill")"
  target="$DEST/$name"
  if [ -L "$target" ]; then
    rm "$target"
  elif [ -e "$target" ]; then
    mkdir -p "$BACKUP"
    mv "$target" "$BACKUP/$name-$(date +%Y%m%d-%H%M%S)"
    echo "… moved old copy of $name to $BACKUP/"
  fi
  ln -s "${skill%/}" "$target"
  echo "✅ $name → ${skill%/}"
done

echo
echo "Next: run each skill's preflight once to install the shared finishing toolkit, e.g."
echo "  bash ~/.claude/skills/everlife-restora-z/core/scripts/preflight.sh --install"
