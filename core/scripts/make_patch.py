#!/usr/bin/env python3
"""Build a small patch zip of what changed between two versions, for teammates who install from a zip (no git).

  python3 core/scripts/make_patch.py <from> [<to>=main] [--out ~/Desktop]

<from> is the version the teammates have now: a git ref, or the short sha on the VERSION line of the zip they got
(e.g. e79c3f5). The patch carries only the files that differ, each with a SHA-256, and is applied by
`core/scripts/apply_patch.py` (the "apply the patch" phrase in everlife-team.md). A patch only applies on top of exactly <from>.
Run it on a git copy, after `git pull` on main. Symlinks and files over 5 MB are not patched: send a full zip (make_zip.sh).
"""
import argparse, datetime, hashlib, json, os, subprocess, sys, zipfile

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
MAX_FILE = 5 * 1024 * 1024
SKIP = (".git/", ".claude/", "_originals/")
CODE = (".py", ".sh", ".command")


def git(*args, text=True):
    r = subprocess.run(["git", "-C", REPO, *args], capture_output=True)
    if r.returncode:
        sys.exit(f"❌ git {' '.join(args)}: {r.stderr.decode().strip()}")
    return r.stdout.decode().strip() if text else r.stdout


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", metavar="from")
    ap.add_argument("dst", metavar="to", nargs="?", default="main")
    ap.add_argument("--out", default="~/Desktop")
    a = ap.parse_args()
    src = git("rev-parse", "--verify", a.src + "^{commit}")
    dst = git("rev-parse", "--verify", a.dst + "^{commit}")
    if src == dst:
        sys.exit("ℹ️  from and to are the same version: nothing to patch.")
    if subprocess.run(["git", "-C", REPO, "merge-base", "--is-ancestor", src, dst]).returncode:
        sys.exit(f"❌ {a.src} is not an ancestor of {a.dst}: a patch only goes forward. Build a full zip with make_zip.sh.")
    raw = git("diff", "--raw", "-z", "--no-renames", src, dst, text=False).split(b"\0")
    files, problems, i = [], [], 0
    while i + 1 < len(raw) and raw[i]:
        meta = raw[i].decode().lstrip(":").split()
        path = raw[i + 1].decode()
        i += 2
        omode, nmode, osha, nsha, st = meta[0], meta[1], meta[2], meta[3], meta[4][0]
        if path.startswith(SKIP):
            continue
        if "120000" in (omode, nmode) or "160000" in (omode, nmode) or st == "T":
            problems.append(f"{path}: symlink / submodule / type change")
            continue
        entry = {"path": path, "action": {"A": "add", "M": "modify", "D": "delete"}[st],
                 "mode": "755" if nmode == "100755" else "644"}
        if st in "MD":
            old = subprocess.run(["git", "-C", REPO, "cat-file", "blob", osha], capture_output=True).stdout
            entry["base_sha256"] = sha(old)
        if st in "AM":
            blob = subprocess.run(["git", "-C", REPO, "cat-file", "blob", nsha], capture_output=True).stdout
            if len(blob) > MAX_FILE:
                problems.append(f"{path}: {len(blob) // 1024} KB is over the 5 MB limit")
                continue
            entry["sha256"], entry["size"], entry["_data"] = sha(blob), len(blob), blob
        files.append(entry)
    if problems:
        sys.exit("❌ This change cannot go in a patch (send a full zip with make_zip.sh):\n   " + "\n   ".join(problems))
    if not files:
        sys.exit("ℹ️  Nothing to patch: the two versions differ only in untracked areas.")
    short_src, short_dst = git("rev-parse", "--short", src), git("rev-parse", "--short", dst)
    date = git("log", "-1", "--format=%cd", "--date=format:%Y-%m-%d", dst)
    subject = git("log", "-1", "--format=%s", dst)
    paths = [f["path"] for f in files]
    manifest = {
        "format": 1, "from": short_src, "to": short_dst, "date": date, "subject": subject,
        "version_line": f"{date} {short_dst} ({subject})",
        "code_files": sorted(p for p in paths if p.endswith(CODE)),
        # new skills are linked, and hooks / the installer are wired, only by install.sh
        "install_needed": any(p == "install.sh" or p.startswith("core/hooks/") or
                              (p.startswith("skills/") and p.endswith("/SKILL.md") and f["action"] == "add")
                              for p, f in zip(paths, files)),
        "files": [{k: v for k, v in f.items() if k != "_data"} for f in files],
    }
    out = os.path.join(os.path.expanduser(a.out), f"everlife-patch_{short_src}_to_{short_dst}.zip")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("PATCH.json", json.dumps(manifest, indent=1))
        for f in files:
            if f["action"] != "delete":
                z.writestr("files/" + f["path"], f["_data"])
    n = {k: sum(1 for f in files if f["action"] == k) for k in ("add", "modify", "delete")}
    print(f"✅ {out} ({os.path.getsize(out) // 1024} KB): {n['modify']} changed, {n['add']} new, {n['delete']} removed")
    print(f"   Applies on top of {short_src} (the VERSION line of their zip) and brings them to {short_dst}.")
    if manifest["code_files"]:
        print(f"   Includes {len(manifest['code_files'])} script(s): " + ", ".join(manifest["code_files"][:6]) +
              (" …" if len(manifest["code_files"]) > 6 else ""))
    if manifest["install_needed"]:
        print("   Teammates must run install.sh / update.sh after applying (new skill or hook changes).")
    print("   Send it only to Everlife teammates. Anyone on another version needs a patch built from THEIR version, or a full zip.")


if __name__ == "__main__":
    main()
