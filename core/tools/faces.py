"""Where are the heads? Samples a clip and returns head boxes over time, so overlays can stay off faces.
heads(clip, ff, fps=4, zoom=1.0) -> list of (t, [(x0, y0, x1, y1), ...]) in 1080x1920 output coordinates.
A head box = detected face expanded upward (hair/forehead) and sideways."""
import subprocess
import numpy as np
import cv2

_W, _H = 540, 960   # analysis size (half of 1080x1920)


def heads(clip, ff, fps=4, zoom=1.0):
    zw, zh = int(_W * zoom) // 2 * 2, int(_H * zoom) // 2 * 2
    vf = f"fps={fps},scale={zw}:{zh},crop={_W}:{_H}:(iw-{_W})/2:0"
    raw = subprocess.run([ff, "-v", "error", "-i", clip, "-vf", vf, "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                         capture_output=True, check=True).stdout
    n = len(raw) // (_W * _H)
    frames = np.frombuffer(raw[: n * _W * _H], np.uint8).reshape(n, _H, _W)
    front = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    prof = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
    out = []
    for i, g in enumerate(frames):
        g = cv2.equalizeHist(g)
        found = []
        for det in (front, prof):
            for (x, y, w, h) in det.detectMultiScale(g, 1.1, 6, minSize=(40, 40)):
                # head = face box grown 60% upward (hair) and 20% each side; scaled x2 to output coordinates
                found.append((int((x - 0.2 * w) * 2), int((y - 0.6 * h) * 2), int((x + 1.2 * w) * 2), int((y + h) * 2)))
        out.append((i / fps, found))
    return out


def blocked_windows(head_track, box, fps=4, pad=0.35, merge=0.6):
    """Time windows where any head overlaps `box` (x0,y0,x1,y1). Padded and merged."""
    raw = [t for t, hs in head_track if any(not (h[2] <= box[0] or h[0] >= box[2] or h[3] <= box[1] or h[1] >= box[3]) for h in hs)]
    step = 1 / fps + 1e-6
    hits = [t for t in raw if any(abs(t - u) <= step and u != t for u in raw)]   # 2+ samples in a row: ignore one-off false detections
    wins = []
    for t in hits:
        s, e = max(0, t - pad), t + 1 / fps + pad
        if wins and s - wins[-1][1] <= merge:
            wins[-1][1] = max(wins[-1][1], e)
        else:
            wins.append([s, e])
    return [(round(s, 2), round(e, 2)) for s, e in wins]
