"""Make a Winners Board preview document from a finished ad (FINAL_*.png / .jpg, or a video frame).

Usage (toolkit venv, isolated mode):
  $T/venv/bin/python -I core/winners-board/make_preview.py <FINAL image> <out.json> [--width 720]

Writes <out.json> = {"type": "preview", "data": "data:image/jpeg;base64,...", "w", "h", "bytes", "updatedAt"}:
the body of the board document `data/users/me/<entry doc_id>/preview/img`. Pass it to ArtifactData with `file_path`
so the base64 never goes through the conversation. Prints the small `preview` field to put on the entry itself.
Downscales to --width px (default 720), JPEG quality steps down until the file is <= 80 KB (hard stop 150 KB).
"""
import argparse, base64, io, json, sys
from datetime import datetime, timezone
from PIL import Image

TARGET = 80_000  # ~110 KB as base64: ~900 previews fit the 100 MB board database
HARD_MAX = 150_000  # a db document is capped at 256 KiB; base64 adds a third


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--width", type=int, default=720)
    a = ap.parse_args()

    im = Image.open(a.src)
    im = im.convert("RGB")
    if im.width > a.width:
        im = im.resize((a.width, round(im.height * a.width / im.width)), Image.LANCZOS)
    data = b""
    for q in (82, 75, 68, 60, 52, 45):
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        data = buf.getvalue()
        if len(data) <= TARGET:
            break
    if len(data) > HARD_MAX:
        sys.exit(f"preview still {len(data)} bytes; try --width 540")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    doc = {"type": "preview", "data": "data:image/jpeg;base64," + base64.b64encode(data).decode("ascii"),
           "w": im.width, "h": im.height, "bytes": len(data), "updatedAt": now}
    with open(a.out, "w") as f:
        json.dump(doc, f)
    print(json.dumps({"preview": {"w": im.width, "h": im.height, "bytes": len(data), "updatedAt": now}}))


if __name__ == "__main__":
    main()
