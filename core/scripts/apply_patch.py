#!/usr/bin/env python3
"""Apply an Everlife patch zip (built by make_patch.py) to a zip-installed copy of the ad factory.

  python3 core/scripts/apply_patch.py <patch.zip> [--dry-run] [--force] [--repo DIR]

Checks first, changes nothing unless every check passes:
  - the copy's VERSION must be one of the patch's `from` versions (the new version already applied → nothing to do);
  - every file in the patch matches its SHA-256 and sits inside the folder (no absolute paths, no "..", nothing through a symlink);
  - every file it replaces is still the original (a file you edited by hand is a conflict; --force overwrites it).
Replaced or deleted files are first copied to _originals/<date>/patch-<to>/. A git copy is refused: use `git pull` / update.sh.
"""
import argparse, datetime, hashlib, json, os, posixpath, shutil, sys, zipfile

BANNED = (".git/", ".claude/", "_originals/")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def norm(b):
    """Text compares line-ending neutral (a Windows unzip turns LF into CRLF); binary files compare as they are."""
    return b if b"\0" in b else b.replace(b"\r\n", b"\n")


def uses_crlf(path):
    try:
        b = open(path, "rb").read()
    except OSError:
        return False
    return b"\0" not in b and b"\r\n" in b


def same(a, b):
    return bool(a and b) and (a.startswith(b) or b.startswith(a))


def current(repo):
    try:
        parts = open(os.path.join(repo, "VERSION"), encoding="utf-8").readline().split()
        return parts[1] if len(parts) > 1 else ""
    except OSError:
        return ""


def die(msg, code=2):
    print(msg)
    sys.exit(code)


def safe(repo, rel):
    """True when rel stays inside repo and no existing part of the path is a symlink."""
    n = posixpath.normpath(rel)
    if n != rel or n.startswith(("/", "../")) or n == ".." or "\\" in rel or rel.startswith(BANNED):
        return False
    cur = repo
    for part in rel.split("/"):
        cur = os.path.join(cur, part)
        if os.path.islink(cur):
            return False
    return os.path.realpath(os.path.join(repo, rel)).startswith(os.path.realpath(repo) + os.sep)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("patch")
    ap.add_argument("--repo", default=os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..")))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="overwrite files you edited by hand")
    a = ap.parse_args()
    repo = os.path.realpath(a.repo)
    if os.path.exists(os.path.join(repo, ".git")):
        die("❌ This copy uses git: update it with `git pull` / update.sh, not a patch.")
    try:
        z = zipfile.ZipFile(a.patch)
        m = json.loads(z.read("PATCH.json"))
    except (OSError, KeyError, ValueError, zipfile.BadZipFile) as e:
        die(f"❌ {a.patch} is not a valid Everlife patch ({e}).")
    if m.get("format") not in (1, 2):
        die("❌ This patch was made by a newer tool: ask for a full zip.")
    have = current(repo)
    if same(have, m["to"]):
        print(f"✅ Already applied: this copy is at {m['to']}. Nothing to do.")
        return
    froms = m["from"] if isinstance(m["from"], list) else [m["from"]]
    fromtxt = " or ".join(froms)
    if not any(same(have, x) for x in froms):
        die(f"❌ Wrong patch for this copy. The patch goes from {fromtxt} to {m['to']}, but this copy is "
            f"{have or 'unknown (no VERSION file)'}. Ask for a patch built from {have or 'your version'}, or a full zip.")
    names, plan, bad, conflicts = set(z.namelist()), [], [], []
    for f in m["files"]:
        rel = f["path"]
        if not safe(repo, rel):
            bad.append(f"{rel}: path not allowed")
            continue
        target = os.path.join(repo, rel)
        data = None
        if f["action"] != "delete":
            if "files/" + rel not in names:
                bad.append(f"{rel}: missing from the patch")
                continue
            data = z.read("files/" + rel)
            if sha(data) != f["sha256"]:
                bad.append(f"{rel}: checksum mismatch (the patch is damaged or was changed)")
                continue
        now = sha(norm(open(target, "rb").read())) if os.path.isfile(target) else None
        bases = f.get("base_sha256")            # format 1: one checksum (or none for an add); format 2: a list, null = absent
        bases = bases if isinstance(bases, list) else [bases]
        if f["action"] == "delete":
            ok = now is None or now in bases
        else:
            ok = now == f["sha256"] or now in bases   # untouched old file, absent where the old version had none, or already the new file
        if not ok:
            conflicts.append(rel)
        plan.append((f, target, data, now))
    if bad:
        die("❌ Patch refused, nothing changed:\n   " + "\n   ".join(bad))
    if conflicts and not a.force:
        die("❌ Patch refused, nothing changed: these files were edited on this copy (or are not the version the patch expects):\n   "
            + "\n   ".join(conflicts) + "\n   Ask for a full zip, or re-run with --force to overwrite them (originals are kept).")
    todo = [p for p in plan if not (p[0]["action"] != "delete" and p[3] == p[0]["sha256"]) and not (p[0]["action"] == "delete" and p[3] is None)]
    print(f"Patch {fromtxt} → {m['to']} ({m['date']}): {m['subject']}")
    print(f"  {len(todo)} file(s) to write or remove, {len(plan) - len(todo)} already in place" + (f", {len(conflicts)} overwritten by --force" if conflicts else ""))
    for f, _, _, _ in todo[:25]:
        print(f"   {f['action']:7} {f['path']}")
    if len(todo) > 25:
        print(f"   … and {len(todo) - 25} more")
    if m.get("code_files"):
        print(f"  Includes {len(m['code_files'])} script(s): " + ", ".join(m["code_files"][:8]) + (" …" if len(m["code_files"]) > 8 else ""))
    if a.dry_run:
        print("Dry run: nothing was changed.")
        return
    bk = os.path.join(repo, "_originals", datetime.date.today().isoformat(), f"patch-{m['to']}")
    for f, target, data, now in todo:
        if now is not None:
            dest = os.path.join(bk, f["path"])
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(target, dest)
        if f["action"] == "delete":
            os.remove(target)
            d = os.path.dirname(target)
            while d != repo and os.path.isdir(d) and not os.listdir(d):
                os.rmdir(d)
                d = os.path.dirname(d)
        else:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            tmp = target + ".patch-tmp"
            if uses_crlf(target) and b"\0" not in data and b"\r\n" not in data:
                data = data.replace(b"\n", b"\r\n")   # keep this copy's line endings, so the next patch still matches
            open(tmp, "wb").write(data)
            os.chmod(tmp, 0o755 if f["mode"] == "755" else 0o644)
            os.replace(tmp, target)
    vf = os.path.join(repo, "VERSION")
    open(vf, "w", encoding="utf-8", newline="\r\n" if uses_crlf(vf) else "\n").write(m["version_line"] + "\n")
    print(f"✅ Patched to {m['version_line']}")
    if todo and any(p[3] is not None for p in todo):
        print(f"   Replaced files were saved in {bk}")
    if m.get("install_needed"):
        print("   ➜ This patch has new skills or hook changes: run `bash " + os.path.join(repo, "install.sh") + "` now (no credits).")
    print("   ➜ Quit Claude Code and open it again so the new rules load.")


if __name__ == "__main__":
    main()
