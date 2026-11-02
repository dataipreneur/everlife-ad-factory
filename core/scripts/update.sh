#!/usr/bin/env bash
# "Update my ad tools" in one step: get the latest main, re-link the skills, re-install the finishing toolkit, check.
# Nothing here spends credits. Stops (changes nothing) if the repo has local edits.
# A copy installed from a zip (no git) skips the download step: unzip the new version over ~/everlife-ad-factory first.
#   bash <repo>/core/scripts/update.sh
set -e
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO"

# A skill's core link (skills/<skill>/core -> ../../core) that install.sh made but git doesn't track yet is not a local
# change: drop it (install.sh re-creates it after the pull), so it can't block the update or clash with the pulled link.
if [ -e "$REPO/.git" ]; then   # -e: .git is a folder in a clone, a file in a git worktree
  for l in skills/*/core; do
    [ -L "$l" ] && [ "$(readlink "$l")" = "../../core" ] && ! git ls-files --error-unmatch "$l" >/dev/null 2>&1 && rm "$l"
  done
fi

if [ ! -d "$REPO/.git" ]; then
  echo "ℹ️  This copy was installed from a zip: to get a newer version, unzip the new zip over $REPO, then run this again."
  echo "✅ version: $(cat "$REPO/VERSION" 2>/dev/null || echo unknown)"
elif [ -n "$(git status --porcelain)" ]; then
  echo "❌ This copy has local changes, so it was not updated:"
  git status --short
  echo "   → fix: ask Mitansh (or say \"show me my local changes\" to Claude first)"
  exit 1
else
  BR="$(git branch --show-current)"
  if [ "$BR" != "main" ]; then
    echo "… switching from branch '$BR' to main"
    git checkout -q main
  fi
  before="$(git rev-parse HEAD)"
  git pull -q --ff-only origin main
  after="$(git rev-parse HEAD)"
  if [ "$before" = "$after" ]; then echo "✅ already up to date ($(git log -1 --format='%h %s'))"
  else echo "✅ updated: $(git log --oneline "$before..$after" | wc -l | tr -d ' ') new change(s), now at $(git log -1 --format='%h %s')"; fi
fi

bash "$REPO/install.sh"
# one preflight --install copies the shared toolkit to ~/Everlife-Creative/tools; then check every product
first=""; fails=0
for s in "$REPO"/skills/*/; do
  [ -f "$s/product.env" ] || continue
  pf="$HOME/.claude/skills/$(basename "$s")/core/scripts/preflight.sh"
  if [ -z "$first" ]; then first="$s"; bash "$pf" --install || fails=$((fails+1))
  else bash "$pf" || fails=$((fails+1)); fi
  echo
done
if [ "$fails" -eq 0 ]; then echo "✅ every product checks out"
else echo "❌ $fails product check(s) have something to fix (see the ❌ lines above)"; exit 1; fi
