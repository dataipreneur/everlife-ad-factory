#!/bin/bash
# pack.sh <work dir> <out folder> <source tag 4x5|9x16> <target tag 9x16|4x5>
# Copies every finished pair into <out> as imageN_<src>.png + imageN_<target>.png (N = number in the work id) + key.txt.
W="$1"; O="$2"; S="$3"; T="$4"; mkdir -p "$O"; : > "$O/key.txt"; cd "$W"
while IFS=$'\t' read n f; do i=$((10#${n//[!0-9]/})); [ -f final/${n}_$T.png ] || continue
  cp src/$n.png "$O/image${i}_$S.png"; cp final/${n}_$T.png "$O/image${i}_$T.png"; echo "image${i} = $f" >> "$O/key.txt"; done < map.tsv
echo "$(ls "$O" | grep -c "_$T.png") pairs in $O"; open "$O"
