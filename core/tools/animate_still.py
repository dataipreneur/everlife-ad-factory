"""Animated still: lay the Everlife logo + proof footer (finish_batch rules) on EVERY frame of a short Seedance clip that was
generated from a batch raw, so the brand layers stay crisp while the scene moves.

Flow (skill: references/animated-still.md): approved static → its RAW (gen/*.png) → Seedance image-to-video, 8 s, 9:16
(start_image = the raw; subtle motion; text and product still) → this tool → FINAL_<n>_anim8s_9x16.mp4.

usage: animate_still.py <seedance.mp4> <out.mp4> --product <id> [--ratio 9:16] [--fps 24] [--shift auto|<px>] [--tone auto|dark|light]
The first frame decides tone and shift (and must pass the safe-area check); every frame then gets the same layers.
"""
import argparse, os, subprocess, sys, tempfile, glob

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
import finish_batch as fb  # noqa: E402


def ffmpeg():
    cands = glob.glob(os.path.expanduser("~/Everlife-Creative/tools/venv/lib/python*/site-packages/imageio_ffmpeg/binaries/ffmpeg-*"))
    return cands[0] if cands else "ffmpeg"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("out")
    ap.add_argument("--product", required=True); ap.add_argument("--ratio", default="9:16", choices=fb.SIZES)
    ap.add_argument("--fps", type=int, default=24); ap.add_argument("--shift", default="auto"); ap.add_argument("--tone", default="auto")
    ap.add_argument("--proof", default="", choices=["", "trust", "count", "none"],
                    help="this creative's one proof (bible 2026-11-02: trust ~42%%, badge + count ~28%%, none ~30%%; core/scripts/proof_next.py)")
    a = ap.parse_args()
    if a.proof:
        fb.PROOF = a.proof
    else:
        print("ℹ️  no --proof given: trust row. Split 2026-11-02: trust ~42% / badge + count ~28% / none ~30% (core/scripts/proof_next.py).")
    import product
    PR = product.load(a.product); disclaimer = PR["disclaimer"]
    FF = ffmpeg()
    W, H = fb.SIZES[a.ratio]
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([FF, "-v", "error", "-y", "-i", a.video, "-vf", f"fps={a.fps},scale={W}:{H}:flags=lanczos", f"{tmp}/f_%05d.png"], check=True)
        frames = sorted(glob.glob(f"{tmp}/f_*.png"))
        if not frames: raise SystemExit("❌ no frames extracted")
        first, info = fb.finish(frames[0], a.ratio, disclaimer, a.tone, a.shift, "none")   # may refuse (exit 2): fix the raw, not the video
        first.save(frames[0])
        tone, shift = info["tone"], info["shift"]
        for f in frames[1:]:
            img, _ = fb.finish(f, a.ratio, disclaimer, tone, str(shift), "force")
            img.save(f)
        os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
        has_audio = subprocess.run([FF, "-v", "error", "-i", a.video, "-map", "0:a:0", "-f", "null", "-"], capture_output=True).returncode == 0
        cmd = [FF, "-v", "error", "-y", "-framerate", str(a.fps), "-i", f"{tmp}/f_%05d.png"]
        if has_audio: cmd += ["-i", a.video, "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-shortest"]
        cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", a.out]
        subprocess.run(cmd, check=True)
    print(f"done {a.out}  frames={len(frames)} fps={a.fps} tone={tone} shift={shift}px footer @ y {info['fy']}–{info['fy'] + info['foot_h']}")


if __name__ == "__main__":
    main()
