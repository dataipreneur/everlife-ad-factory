#!/usr/bin/env bash
# Everlife ad factory preflight (shared): checks every connection and tool, prints ✅ / ❌ with the fix.
# Run it through a product skill's core link so it finds that skill's product.env:
#   bash <skill-dir>/core/scripts/preflight.sh            # check only
#   bash <skill-dir>/core/scripts/preflight.sh --install  # also install the finishing toolkit (after the user agrees)
# (or set SKILL_DIR=<skill-dir> when running it from the repo directly)
SKILL="${SKILL_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
CORE="$SKILL/core"
if [ ! -f "$SKILL/product.env" ]; then
  echo "❌ No product.env in $SKILL (run via <skill-dir>/core/scripts/preflight.sh or set SKILL_DIR)"; exit 1
fi
. "$SKILL/product.env"
T="${EVERLIFE_TOOLS:-$HOME/Everlife-Creative/tools}"
OUT="$OUT_DIR"
LOG="$COPY_LOG"
ok=0; bad=0
pass() { echo "✅ $1"; ok=$((ok+1)); }
fail() { echo "❌ $1"; echo "   → fix: $2"; bad=$((bad+1)); }

echo "== $PRODUCT_NAME ad factory preflight =="
# 0. Make the skill available everywhere (project copy → ~/.claude/skills link; never replaces a real folder)
USKILL="$HOME/.claude/skills/$(basename "${SKILL%/}")"
if [ "$SKILL" != "$USKILL" ]; then
  mkdir -p "$HOME/.claude/skills"
  if [ ! -e "$USKILL" ]; then ln -s "$SKILL" "$USKILL" && pass "Skill linked into ~/.claude/skills (works from any folder)"
  elif [ -L "$USKILL" ] && [ "$(readlink "$USKILL")" != "$SKILL" ]; then ln -sfn "$SKILL" "$USKILL" && pass "Skill link updated → $SKILL"
  elif [ -L "$USKILL" ]; then pass "Skill already linked in ~/.claude/skills"
  else fail "An older, unlinked copy of this skill sits in $USKILL (Claude uses that one, not $SKILL)" \
            "bash <repo>/install.sh   (moves the old copy to ~/.claude/skills-backup/ and links this one)"; fi
else pass "Skill installed in ~/.claude/skills"; fi

# 1. Higgsfield CLI
if command -v higgsfield >/dev/null 2>&1; then
  pass "Higgsfield CLI installed ($(higgsfield version 2>/dev/null | head -1))"
  # 2. logged in + workspace
  WS=$(higgsfield workspace list 2>&1)
  if echo "$WS" | grep -qiE "not authenticated|session expired|login"; then
    fail "Higgsfield not logged in" "run:  ! higgsfield auth login"
  else
    SEL=$(echo "$WS" | awk '/✓/{print $2; for(i=1;i<=NF;i++) if($i ~ /^[0-9.]+$/) c=$i} END{}' | head -1)
    CRED=$(echo "$WS" | awk '/✓/{for(i=1;i<=NF;i++) if($i ~ /^[0-9]+(\.[0-9]+)?$/) c=$i; print c}' | head -1)
    if echo "$WS" | grep "✓" | grep -qi everlife; then
      pass "Workspace = Everlife (shared team credits: ${CRED:-?})"
      if [ -n "$CRED" ] && awk "BEGIN{exit !($CRED < 100)}"; then
        fail "Low credits (${CRED})" "tell the creative lead before generating"
      fi
    else
      fail "Selected workspace is '${SEL:-unknown}', not Everlife" "higgsfield workspace list → select the Everlife workspace (never spend personal credits)"
    fi
    # 3. Marketing Studio product
    PID=$(higgsfield marketing-studio products list --json 2>/dev/null | python3 -c "
import json,sys
try:
  d=json.load(sys.stdin); d=d.get('items',d) if isinstance(d,dict) else d
  print(next((p['id'] for p in d if p.get('title','').lower()=='$(echo "$PRODUCT_NAME" | tr '[:upper:]' '[:lower:]')'),''))
except Exception: print('')")
    if [ -n "$PID" ]; then
      pass "$PRODUCT_NAME registered in Marketing Studio (product id $PID)"
      echo "[\"$PID\"]" > "$SKILL/assets/product_ids.json"
    else
      fail "$PRODUCT_NAME not registered in Marketing Studio (needed for realistic UGC)" \
           "$(if [ -n "$PILL" ]; then echo "B=\$(higgsfield upload create \"$SKILL/assets/$BOTTLE\" --json | grep -oE '[0-9a-f-]{36}' | head -1); C=\$(higgsfield upload create \"$SKILL/assets/$PILL\" --json | grep -oE '[0-9a-f-]{36}' | head -1); higgsfield marketing-studio products create --title \"$PRODUCT_NAME\" --image \$B --image \$C"; else echo "B=\$(higgsfield upload create \"$SKILL/assets/$BOTTLE\" --json | grep -oE '[0-9a-f-]{36}' | head -1); higgsfield marketing-studio products create --title \"$PRODUCT_NAME\" --image \$B"; fi)"
    fi
  fi
else
  fail "Higgsfield CLI not installed" "run:  ! curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh   (then: ! higgsfield auth login)"
fi

# 4. Finishing toolkit
if [ "$1" = "--install" ]; then
  echo "… installing finishing toolkit into $T"
  mkdir -p "$T/assets"
  cp "$CORE"/tools/*.py "$T/" && cp -R "$CORE"/tools/assets/. "$T/assets/"
  [ -f "$T/assets/type_specimen.png" ] || cp "$SKILL/assets/type_specimen.png" "$T/assets/"
  [ -x "$T/venv/bin/python" ] || python3 -m venv "$T/venv"
  "$T/venv/bin/pip" -q install --disable-pip-version-check imageio-ffmpeg faster-whisper pillow numpy "opencv-python-headless==4.10.0.84" >/dev/null 2>&1
fi
if [ -f "$T/full_layout.py" ] && [ -f "$T/avatar_video.py" ] && [ -f "$T/finish_modern.py" ] && [ -f "$T/finish_batch.py" ] && [ -f "$T/assets/fonts/InstrumentSerif-Regular.ttf" ] && [ -f "$T/assets/proof_row_clear.png" ] && [ -f "$T/assets/footer/badge_dark.png" ]; then
  pass "Finishing scripts present ($T)"
else
  fail "Finishing scripts missing in $T" "bash \"$0\" --install"
fi
if [ -x "$T/venv/bin/python" ] && FF=$("$T/venv/bin/python" -c "import imageio_ffmpeg,faster_whisper,PIL;print(imageio_ffmpeg.get_ffmpeg_exe())" 2>/dev/null); then
  pass "Toolkit venv ready (ffmpeg + whisper + Pillow)"; echo "   FF=$FF"; echo "   PY=$T/venv/bin/python"
else
  fail "Toolkit venv missing or incomplete" "bash \"$0\" --install"
fi

# 5. Product renders
for f in $RENDERS; do
  [ -f "$SKILL/assets/$f" ] || fail "Missing render $f" "copy it from the Drive asset library ($DRIVE_FOLDER folder) into $SKILL/assets/"
done
if [ -n "$PILL" ]; then [ -f "$SKILL/assets/$BOTTLE" ] && [ -f "$SKILL/assets/$PILL" ] && pass "Real product renders present (bottle + pill)"
else [ -f "$SKILL/assets/$BOTTLE" ] && pass "Real product render present (bottle; this product has no pill/tablet render)"; fi
# 5a. Hidden junk under transparent pixels (Higgsfield shows it as a black/streaky background → wrong product in video)
if [ -x "$T/venv/bin/python" ]; then
  for f in "$BOTTLE" "$PILL"; do
    [ -n "$f" ] && [ -f "$SKILL/assets/$f" ] || continue
    J=$("$T/venv/bin/python" -I -c "
import sys
from PIL import Image, ImageFilter
import numpy as np
im = Image.open(sys.argv[1])
if im.mode != 'RGBA': print(0); sys.exit()
a = np.array(im); near = np.array(im.getchannel('A').filter(ImageFilter.MaxFilter(11))) > 0
t = a[(a[..., 3] == 0) & ~near][:, :3].astype(int)
print(int(100 * (((t.max(1) - t.min(1)) > 40) | (t.max(1) < 60)).mean()) if len(t) else 0)" "$SKILL/assets/$f" 2>/dev/null)
    [ "${J:-0}" -gt 20 ] && echo "⚠️  $f hides coloured/dark pixels under its transparent background (${J}%): Higgsfield may show them. Before registering it in Marketing Studio, set those pixels to white (visible pixels unchanged)."
  done
fi

# 5b. Product settings the shared tools read (product.json)
if PID=$(python3 -c "import json,sys; d=json.load(open(sys.argv[1])); [d[k] for k in ('id','name','renders','disclaimer','keep_case','review_highlight','reviews','kicker_default','split_titles','notify_app')]; print(d['id'])" "$SKILL/product.json" 2>/dev/null); then
  pass "product.json valid (product id: $PID; use \"product\": \"$PID\" in every copy.json)"
else
  fail "product.json missing or incomplete in $SKILL" "copy another skill's product.json and fill in this product's values (disclaimer verbatim from the bible)"
fi

# 6. Copy log + output folder
mkdir -p "$OUT"
if [ ! -f "$LOG" ]; then
  mkdir -p "$(dirname "$LOG")"
  if [ -f "$SKILL/assets/copy-log-seed.md" ]; then
    cp "$SKILL/assets/copy-log-seed.md" "$LOG"
    pass "Copy log seeded from the bundle ($(grep -c '^|' "$LOG") rows already used: $LOG)"
  else
    printf "# $PRODUCT_NAME copy log — lines already used (do not reuse)\n\n"'| Ad | Header | VO lines | End head | CTA |\n|---|---|---|---|---|\n' > "$LOG"
    pass "Copy log created ($LOG)"
  fi
else
  pass "Copy log found ($(grep -c '^|' "$LOG") rows)"
fi
pass "Output folder: $OUT"

# 7. Optional connectors (informational)
if claude mcp list 2>/dev/null | grep -qE "^creatify: .*Connected"; then pass "Creatify MCP (Model Playground) connected: Nano Banana 2.1 / Pro available for image batches"
else echo "ℹ️  Optional: Nano Banana batches need the Creatify MCP: claude mcp add --transport http --scope user creatify https://api.creatify.ai/mcp, then a new session and /mcp → sign in. GPT Image 2.5 works without it."; fi
echo "ℹ️  Optional: Google Drive connector (pull new renders / reference ads), Playwright browser (study reference videos)."

echo "== $ok passed, $bad to fix =="
[ $bad -eq 0 ]
