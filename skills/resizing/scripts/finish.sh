#!/bin/bash
# finish.sh <work dir> <ratio 9:16|4:5> <product id> [ids...]
# For each id in assets.tsv (id<TAB>asset<TAB>proof) whose raw/<id>.png exists: finish_batch AS IS (--shift 0, never moves the
# image: a shift fills the gap with a blurred strip, Mitansh 2026-11-04) with the same proof as the source.
# Output final/<id>_<WxH>.png. Prints ok / FAIL (with the reason) per ad; a FAIL = drop the footer (free) or re-roll the raw.
W="$1"; R="$2"; P="$3"; shift 3; cd "$W" || exit 1
T=~/Everlife-Creative/tools; PY=$T/venv/bin/python; tag=${R/:/x}
grep -v '^$' assets.tsv | while IFS=$'\t' read n a p; do
  [ $# -gt 0 ] && [[ ! " $* " =~ " $n " ]] && continue
  [ -f raw/$n.png ] || { echo "$n no raw yet"; continue; }
  msg=$($PY $T/finish_batch.py raw/$n.png final/${n}_$tag.png --ratio $R --product $P --fit trusted --proof $p --shift 0 2>&1)
  if [ $? -eq 0 ]; then echo "$n ok (proof $p)"; else echo "$n FAIL: $(echo "$msg" | grep -E '❌|refus|busy' | head -1 | cut -c1-160)"; fi
done
