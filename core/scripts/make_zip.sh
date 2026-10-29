#!/usr/bin/env bash
# Build the zip handed to teammates who install without GitHub (see ONBOARDING-ZIP.md).
# Packs a committed version (default: main) with git archive: no .git, no _originals or other untracked files, and the
# skills' core links kept as links. Writes a VERSION file inside so a zip install can say which version it runs.
#   bash core/scripts/make_zip.sh [ref] [out-dir]      e.g. bash core/scripts/make_zip.sh main ~/Desktop
set -e
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
REF="${1:-main}"
OUT="${2:-$HOME/Desktop}"
cd "$REPO"
git rev-parse --verify -q "$REF" >/dev/null || { echo "❌ unknown version '$REF'"; exit 1; }
SHA="$(git rev-parse --short "$REF")"
DATE="$(git log -1 --format=%cd --date=format:%Y-%m-%d "$REF")"
NAME="everlife-ad-factory_${DATE}_${SHA}.zip"
TMP="$(mktemp -d)"
printf '%s %s (%s)\n' "$DATE" "$SHA" "$(git log -1 --format=%s "$REF")" > "$TMP/VERSION"
git archive --format=zip --prefix=everlife-ad-factory/ \
  --add-file="$TMP/VERSION" -o "$OUT/$NAME" "$REF" 2>/dev/null \
  || { git archive --format=tar --prefix=everlife-ad-factory/ "$REF" | (cd "$TMP" && tar -x) \
       && cp "$TMP/VERSION" "$TMP/everlife-ad-factory/" && (cd "$TMP" && zip -qry "$OUT/$NAME" everlife-ad-factory); }
rm -rf "$TMP"
echo "✅ $OUT/$NAME ($(du -h "$OUT/$NAME" | cut -f1)), version $DATE $SHA"
echo "   Contains the creative bible and gates: send it only to Everlife teammates."
