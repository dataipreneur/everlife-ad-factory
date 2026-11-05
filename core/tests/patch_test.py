#!/usr/bin/env python3
"""End-to-end test of make_patch.py + apply_patch.py on this repo's own history (no network, no credits).

  python3 core/tests/patch_test.py <work-dir> [<from-ref> [<to-ref>]]

Builds a 'zip install' of <from-ref> (git archive + a VERSION line, like make_zip.sh), makes the patch, applies it, and checks
the result is identical to a 'zip install' of <to-ref>. Then the refusals: wrong version, hand-edited file, damaged patch,
path traversal, git copy; and that re-applying is a no-op.
"""
import hashlib, json, os, shutil, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
WORK = os.path.abspath(sys.argv[1])
FROMS = (sys.argv[2] if len(sys.argv) > 2 else "56338a6").split(",")   # one version, or several: ONE patch must fit them all
FROM = FROMS[0]
TO = sys.argv[3] if len(sys.argv) > 3 else "e79c3f5"
results = []


def check(name, ok, extra=""):
    results.append(ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else f"  {extra}"))


def run(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True, check=True).stdout.strip()


def install_of(ref, name):
    """A zip-style copy of ref: git archive, no .git, plus the VERSION line make_zip.sh writes."""
    d = os.path.join(WORK, name)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    arc = subprocess.Popen(["git", "-C", REPO, "archive", "--format=tar", ref], stdout=subprocess.PIPE)
    subprocess.run(["tar", "-x", "-C", d], stdin=arc.stdout, check=True)
    arc.wait()
    date = git("log", "-1", "--format=%cd", "--date=format:%Y-%m-%d", ref)
    open(os.path.join(d, "VERSION"), "w").write(f"{date} {git('rev-parse', '--short', ref)} ({git('log', '-1', '--format=%s', ref)})\n")
    return d


def tree(d):
    out = {}
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x not in ("_originals",)]
        for f in files + [x for x in dirs if os.path.islink(os.path.join(root, x))]:
            p = os.path.join(root, f)
            rel = os.path.relpath(p, d)
            if rel == "VERSION":
                continue
            out[rel] = ("link", os.readlink(p)) if os.path.islink(p) else ("file", hashlib.sha256(open(p, "rb").read()).hexdigest(), os.access(p, os.X_OK))
    return out


shutil.rmtree(WORK, ignore_errors=True)
os.makedirs(WORK)
base, want = install_of(FROM, "base"), install_of(TO, "want")
rc, out = run(sys.executable, os.path.join(REPO, "core/scripts/make_patch.py"), ",".join(FROMS), TO, "--out", WORK)
print(out.strip())
patch = [os.path.join(WORK, f) for f in os.listdir(WORK) if f.startswith("everlife-patch_")]
check("make_patch builds a patch", rc == 0 and len(patch) == 1, out)
patch = patch[0]
apply = os.path.join(REPO, "core/scripts/apply_patch.py")

rc, out = run(sys.executable, apply, patch, "--repo", base, "--dry-run")
check("dry run changes nothing", rc == 0 and tree(base) == tree(install_of(FROM, "base_copy")), out)

rc, out = run(sys.executable, apply, patch, "--repo", base)
print(out.strip())
check("apply succeeds", rc == 0, out)
bt, wt = tree(base), tree(want)
diff = sorted(set(bt) ^ set(wt)) + [k for k in bt if k in wt and bt[k] != wt[k]]
check("patched copy is identical to a fresh install of the new version", not diff, str(diff[:8]))
check("VERSION line updated", open(os.path.join(base, "VERSION")).read() == open(os.path.join(want, "VERSION")).read())
check("originals backed up", os.path.isdir(os.path.join(base, "_originals")))

rc, out = run(sys.executable, apply, patch, "--repo", base)
check("applying again is a no-op", rc == 0 and "Already applied" in out, out)

# wrong version: an older copy
older = install_of(git("rev-parse", FROM + "~1"), "older")
before = tree(older)
rc, out = run(sys.executable, apply, patch, "--repo", older)
check("wrong version is refused, nothing changed", rc != 0 and "Wrong patch" in out and tree(older) == before, out)

# hand-edited file
edited = install_of(FROM, "edited")
manifest = json.loads(zipfile.ZipFile(patch).read("PATCH.json"))
victim = next(f["path"] for f in manifest["files"] if f["action"] == "modify")
open(os.path.join(edited, victim), "a").write("\nlocal edit\n")
before = tree(edited)
rc, out = run(sys.executable, apply, patch, "--repo", edited)
check("a hand-edited file is a conflict, nothing changed", rc != 0 and victim in out and tree(edited) == before, out)
rc, out = run(sys.executable, apply, patch, "--repo", edited, "--force")
check("--force overwrites it and keeps the original", rc == 0 and os.path.exists(os.path.join(edited, "_originals")), out)

# damaged patch
damaged = os.path.join(WORK, "damaged.zip")
with zipfile.ZipFile(patch) as zin, zipfile.ZipFile(damaged, "w") as zout:
    done = False
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename.startswith("files/") and not done:
            data, done = data + b"x", True
        zout.writestr(item, data)
fresh = install_of(FROM, "fresh")
before = tree(fresh)
rc, out = run(sys.executable, apply, damaged, "--repo", fresh)
check("a damaged patch is refused (checksum)", rc != 0 and "checksum" in out and tree(fresh) == before, out)

# path traversal
evil = os.path.join(WORK, "evil.zip")
em = dict(manifest, files=[{"path": "../outside.txt", "action": "add", "mode": "644", "sha256": hashlib.sha256(b"x").hexdigest(), "size": 1}])
with zipfile.ZipFile(evil, "w") as z:
    z.writestr("PATCH.json", json.dumps(em))
    z.writestr("files/../outside.txt", b"x")
rc, out = run(sys.executable, apply, evil, "--repo", fresh)
check("path traversal is refused", rc != 0 and "not allowed" in out and not os.path.exists(os.path.join(WORK, "outside.txt")), out)

# Windows copy: every text file (and VERSION) has CRLF line endings
win = install_of(FROM, "win")
for root, _, fs in os.walk(win):
    for f in fs:
        p = os.path.join(root, f)
        if os.path.islink(p) or "_originals" in p:
            continue
        b = open(p, "rb").read()
        if b"\0" not in b and b"\r\n" not in b:
            open(p, "wb").write(b.replace(b"\n", b"\r\n"))
rc, out = run(sys.executable, apply, patch, "--repo", win)
check("a CRLF (Windows) copy applies with no false conflicts", rc == 0 and "refused" not in out, out)


def tree_norm(d):
    t = {}
    for k, v in tree(d).items():
        if v[0] == "file":
            b = open(os.path.join(d, k), "rb").read()
            v = ("file", hashlib.sha256(b if b"\0" in b else b.replace(b"\r\n", b"\n")).hexdigest(), v[2])
        t[k] = v
    return t


check("CRLF copy equals a fresh install apart from line endings", tree_norm(win) == tree_norm(want))
patched_md = os.path.join(win, victim)
b = open(patched_md, "rb").read()
check("patched files keep CRLF (the next patch still matches)", b.count(b"\r\n") == b.count(b"\n") and b"\r\n" in b)
check("VERSION keeps CRLF", b"\r\n" in open(os.path.join(win, "VERSION"), "rb").read())

# every other version the patch was built for applies too, and ends identical to a fresh install of the new version
for other in FROMS[1:]:
    cp = install_of(other, "other_" + other)
    rc, out = run(sys.executable, apply, patch, "--repo", cp)
    check(f"the same patch applies on {other}", rc == 0, out)
    check(f"{other} ends identical to a fresh install of the new version", tree(cp) == wt, str(sorted(set(tree(cp)) ^ set(wt))[:6]))
    again = install_of(other, "other_edit_" + other)
    mf = [f for f in manifest["files"] if f["action"] == "modify"]
    if mf:
        open(os.path.join(again, mf[-1]["path"]), "a").write("\nlocal edit\n")
        rc, out = run(sys.executable, apply, patch, "--repo", again)
        check(f"a hand-edited file is still a conflict on {other}", rc != 0 and mf[-1]["path"] in out, out)

# a version that is not in the list is refused
if len(FROMS) > 1:
    outsider = install_of(git("rev-parse", FROM + "~1"), "outsider")
    rc, out = run(sys.executable, apply, patch, "--repo", outsider)
    check("a version outside the list is refused", rc != 0 and "Wrong patch" in out and FROMS[0] in out and FROMS[1] in out, out)

# git copy
os.makedirs(os.path.join(fresh, ".git"))
rc, out = run(sys.executable, apply, patch, "--repo", fresh)
check("a git copy is refused", rc != 0 and "git" in out, out)

print(f"{sum(results)}/{len(results)} passed")
sys.exit(0 if all(results) else 1)
