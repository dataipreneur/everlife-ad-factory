#!/usr/bin/env python3
"""Build a small patch zip of what changed between versions, for teammates who install from a zip (no git).

  python3 core/scripts/make_patch.py <from>[,<from2>,...] [<to>=main] [--out ~/Desktop]

<from> is the version(s) the teammates have now: a git ref, or the short sha on the VERSION line of the zip they got
(e.g. e79c3f5). Give every version in use, comma-separated (e.g. 2800e8d,40233f6): ONE patch then fits all of them.
The patch carries only the files that differ, each with a SHA-256 of the new file and of every old file it may replace, and is
applied by `core/scripts/apply_patch.py` (the "apply the patch" phrase in everlife-team.md). It applies on a copy whose VERSION
is any of the <from> versions, nothing else.
Run it on a git copy, after `git pull` on main. Symlinks and files over 5 MB are not patched: send a full zip (make_zip.sh).
"""
import argparse, hashlib, json, os, subprocess, sys, zipfile

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
MAX_FILE = 5 * 1024 * 1024
SKIP = (".git/", ".claude/", "_originals/")
CODE = (".py", ".sh", ".command")


def git(*args, text=True, check=True):
    r = subprocess.run(["git", "-C", REPO, *args], capture_output=True)
    if r.returncode and check:
        sys.exit(f"❌ git {' '.join(args)}: {r.stderr.decode().strip()}")
    out = r.stdout.decode() if text else r.stdout
    return (out.strip() if text else out) if not r.returncode else None


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob(ref, path):
    r = subprocess.run(["git", "-C", REPO, "cat-file", "blob", f"{ref}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", metavar="from", help="version(s) the team has, comma-separated")
    ap.add_argument("dst", metavar="to", nargs="?", default="main")
    ap.add_argument("--out", default="~/Desktop")
    a = ap.parse_args()
    dst = git("rev-parse", "--verify", a.dst + "^{commit}")
    srcs = []
    for ref in dict.fromkeys(x.strip() for x in a.src.split(",") if x.strip()):
        full = git("rev-parse", "--verify", ref + "^{commit}")
        if full == dst:
            sys.exit(f"ℹ️  {ref} is already the target version: leave it out of the list.")
        if subprocess.run(["git", "-C", REPO, "merge-base", "--is-ancestor", full, dst]).returncode:
            sys.exit(f"❌ {ref} is not an ancestor of {a.dst}: a patch only goes forward. Build a full zip with make_zip.sh.")
        srcs.append((ref, full))
    if not srcs:
        sys.exit("❌ give at least one <from> version.")
    paths, problems = {}, []
    for ref, full in srcs:
        raw = git("diff", "--raw", "-z", "--no-renames", full, dst, text=False).split(b"\0")
        i = 0
        while i + 1 < len(raw) and raw[i]:
            meta = raw[i].decode().lstrip(":").split()
            path = raw[i + 1].decode()
            i += 2
            if path.startswith(SKIP):
                continue
            if "120000" in meta[:2] or "160000" in meta[:2] or meta[4][0] == "T":
                problems.append(f"{path}: symlink / submodule / type change")
                continue
            paths[path] = True
    entries = []
    for path in sorted(paths):
        new = blob(dst, path)
        bases = [(sha(b) if (b := blob(full, path)) is not None else None) for _, full in srcs]
        if new is not None and len(new) > MAX_FILE:
            problems.append(f"{path}: {len(new) // 1024} KB is over the 5 MB limit")
            continue
        mode = "644"
        if new is not None:
            lt = git("ls-tree", dst, "--", path)
            mode = "755" if lt.startswith("100755") else "644"
        e = {"path": path, "mode": mode, "base_sha256": sorted(set(bases), key=lambda x: (x is None, x or ""))}
        if new is None:
            e["action"] = "delete"
        else:
            e["action"] = "modify" if any(b is not None for b in bases) else "add"
            e["sha256"], e["size"], e["_data"] = sha(new), len(new), new
        entries.append(e)
    if problems:
        sys.exit("❌ This change cannot go in a patch (send a full zip with make_zip.sh):\n   " + "\n   ".join(problems))
    if not entries:
        sys.exit("ℹ️  Nothing to patch: the versions differ only in untracked areas.")
    short_srcs = [git("rev-parse", "--short", full) for _, full in srcs]
    short_dst = git("rev-parse", "--short", dst)
    date = git("log", "-1", "--format=%cd", "--date=format:%Y-%m-%d", dst)
    subject = git("log", "-1", "--format=%s", dst)
    plist = [e["path"] for e in entries]
    manifest = {
        "format": 2, "from": short_srcs, "to": short_dst, "date": date, "subject": subject,
        "version_line": f"{date} {short_dst} ({subject})",
        "code_files": sorted(p for p in plist if p.endswith(CODE)),
        # new skills are linked, and hooks / the installer are wired, only by install.sh
        "install_needed": any(e["path"] == "install.sh" or e["path"].startswith("core/hooks/") or
                              (e["path"].startswith("skills/") and e["path"].endswith("/SKILL.md") and e["action"] == "add")
                              for e in entries),
        "files": [{k: v for k, v in e.items() if k != "_data"} for e in entries],
    }
    out = os.path.join(os.path.expanduser(a.out), f"everlife-patch_{'+'.join(short_srcs)}_to_{short_dst}.zip")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("PATCH.json", json.dumps(manifest, indent=1))
        for e in entries:
            if e["action"] != "delete":
                z.writestr("files/" + e["path"], e["_data"])
    n = {k: sum(1 for e in entries if e["action"] == k) for k in ("add", "modify", "delete")}
    print(f"✅ {out} ({os.path.getsize(out) // 1024} KB): {n['modify']} changed, {n['add']} new, {n['delete']} removed")
    print(f"   Applies on a copy whose VERSION is {' or '.join(short_srcs)} and brings it to {short_dst}.")
    if manifest["code_files"]:
        print(f"   Includes {len(manifest['code_files'])} script(s): " + ", ".join(manifest["code_files"][:6]) +
              (" …" if len(manifest["code_files"]) > 6 else ""))
    if manifest["install_needed"]:
        print("   Teammates must run install.sh / update.sh after applying (new skill or hook changes).")
    print("   Send it only to Everlife teammates, together with the current apply_patch.py.")
    print("   Anyone on a version that is not in the list needs a patch built for it, or a full zip.")


if __name__ == "__main__":
    main()
