#!/usr/bin/env python3
"""One phrase: "sync the bible". The whole chain from Justin's page to every skill, checked, with nothing done by hand.

    bible_pipeline.py sync <saved.html> [--commit] [--release]
        1 guard + convert the saved live page → core/claude/creative-bible.md (bible_sync.py --write, refuses a weak parse)
        2 regenerate every product skill: references/bible.json, product-bible.md, product-brief.md, product.json disclaimer
        3 skill_lint.py (strict) + core/tests/bible_pipeline_test.py + core/tests/batch_gate_test.py
        4 report: version, sections changed → skills, NEW lines for Jeremy, retired lines, offers/CTAs that changed; CHANGELOG entry
        --commit   also commit on the current branch (never main)            ← only on Mitansh's go
        --release  also merge into main, push, and build the team patch         ← only on Mitansh's go
    bible_pipeline.py regen [--only a,b]      regenerate + lint after a hand edit (bible-screen.json, hard-stops.md, product-notes.md, product.json)
    bible_pipeline.py check                   regenerate into a temp dir and diff against the repo: exit 1 listing stale files (what a PR review runs)
    bible_pipeline.py newest                  print the newest saved live page (the Artifact tool saves it as artifact-<id>-<version>.html)

Never touches git unless --commit / --release is given. Any failure stops before the next step and leaves the files for inspection.
"""
import argparse, datetime, glob, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import bible_model as bm  # noqa: E402

PY = sys.executable
SAVED = os.path.expanduser("~/.claude/projects/*/*/tool-results/artifact-b393ddd4-*.html")   # the live bible artifact id
TEAM_VERSIONS = os.path.join(REPO, "core", "team-logs", "team-versions.json")


def run(cmd, check=True, **kw):
    r = subprocess.run(cmd, cwd=REPO, text=True, capture_output=True, **kw)
    if check and r.returncode != 0:
        sys.exit(f"❌ `{' '.join(os.path.basename(c) if i < 2 else c for i, c in enumerate(cmd))}` failed:\n{r.stdout[-3000:]}\n{r.stderr[-2000:]}")
    return r


def git(*args, check=True):
    return run(["git", *args], check=check)


def newest_saved():
    files = sorted(glob.glob(SAVED), key=os.path.getmtime, reverse=True)
    return files[0] if files else None


def regen(only=""):
    args = ["--only", only] if only else []
    r = run([PY, "-I", os.path.join(HERE, "build_product_bibles.py"), *args]); print(r.stdout.rstrip())
    r = run([PY, "-I", os.path.join(HERE, "build_product_briefs.py"), *args]); print("\n".join(l for l in r.stdout.splitlines() if l.startswith("❌")) or "✅ briefs regenerated")


def lint(strict=True):
    r = run([PY, "-I", os.path.join(HERE, "skill_lint.py")] + (["--strict"] if strict else []), check=False)
    print(r.stdout.rstrip())
    if r.returncode != 0:
        sys.exit("❌ lint failed: fix what it lists (usually `bible_pipeline.py regen`, or a hand file it names), then run again")


def tests():
    for t in ("bible_pipeline_test.py", "batch_gate_test.py"):
        p = os.path.join(REPO, "core", "tests", t)
        if not os.path.exists(p): continue
        r = run([PY, "-I", p], check=False)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""
        print(f"{'✅' if r.returncode == 0 else '❌'} {t}: {last}")
        if r.returncode != 0:
            sys.exit(r.stdout[-3000:] + "\n❌ tests failed: nothing merged")


def snapshot():
    """{skill: bible.json} before a sync, to report what changed per product."""
    out = {}
    for p in glob.glob(os.path.join(REPO, "skills", "everlife-*", "references", "bible.json")):
        try: out[p.split(os.sep)[-3]] = json.load(open(p, encoding="utf-8"))
        except Exception: pass
    return out


def changes(before, after):
    lines = []
    for skill in sorted(after):
        a, b = before.get(skill) or {}, after[skill]
        diff = []
        if (a.get("offer") or {}).get("pct") != (b.get("offer") or {}).get("pct") or (a.get("offer") or {}).get("status") != (b.get("offer") or {}).get("status"):
            diff.append(f"offer {(a.get('offer') or {}).get('pct')}/{(a.get('offer') or {}).get('status')} → {(b.get('offer') or {}).get('pct')}/{(b.get('offer') or {}).get('status')}")
        if a.get("cta_default") != b.get("cta_default"): diff.append(f"default CTA \"{a.get('cta_default')}\" → \"{b.get('cta_default')}\"")
        for f in ("ctas", "benefits_quick", "proof", "hard_nos"):
            add = [x for x in b.get(f, []) if bm.norm(x) not in {bm.norm(y) for y in a.get(f, [])}]
            rem = [x for x in a.get(f, []) if bm.norm(x) not in {bm.norm(y) for y in b.get(f, [])}]
            if add: diff.append(f"{f} +{add}")
            if rem: diff.append(f"{f} -{rem}")
        if bm.norm(a.get("disclaimer", "")) != bm.norm(b.get("disclaimer", "")) and a: diff.append("DISCLAIMER CHANGED (Jeremy)")
        new = [k for k, v in (b.get("screen") or {}).items() if "NEW" in v.get("status", "")]
        if new: diff.append(f"NEW lines to screen: {new}")
        if diff: lines.append(f"- **{b.get('name', skill)}:** " + "; ".join(diff))
    return lines


def changelog(version, prev, section_lines, change_lines):
    p = os.path.join(REPO, "CHANGELOG.md"); s = open(p, encoding="utf-8").read()
    entry = [f"## {datetime.date.today().isoformat()} — Bible sync to {version} (automatic: `bible_pipeline.py sync`)",
             f"Justin moved the live bible from {prev} to {version}. Every product skill was regenerated from it "
             "(references/bible.json, product-bible.md, product-brief.md, product.json disclaimer); nothing by hand.", ""]
    entry += section_lines or ["- No section changes reported by the diff."]
    entry += [""] + (change_lines or ["- No product copy changed (offers, CTAs, benefits, proof, hard NOs, disclaimers)."]) + [""]
    i = s.find("\n## ")
    s = s[:i + 1] + "\n".join(entry) + "\n" + s[i + 1:] if i >= 0 else s + "\n" + "\n".join(entry)
    open(p, "w", encoding="utf-8").write(s)


def cmd_sync(a):
    html = a.html or newest_saved()
    if not html or not os.path.exists(html):
        sys.exit("❌ no saved live page: read https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG with the Artifact tool first, then run again")
    m = re.search(r"artifact-[0-9a-f]+-(\d+-[0-9a-f]+)\.html$", os.path.basename(html))
    new_ver = m.group(1) if m else "unknown"
    prev = bm.version_of(open(bm.BIBLE, encoding="utf-8").read()) if os.path.exists(bm.BIBLE) else "none"
    print(f"live page: {os.path.basename(html)} (version {new_ver}); repo copy: {prev}")
    if new_ver == prev and not a.force:
        print("✅ already synced: the repo copy is this version. Nothing to do (use --force to regenerate anyway)."); return
    br = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if br in ("main", "master"):
        sys.exit("❌ on main: `git checkout -b bible-sync-" + new_ver.split("-")[-1] + "` first (the repo copy only changes on a branch)")
    if (a.commit or a.release) and git("status", "--short").stdout.strip():
        sys.exit("❌ the working tree has other changes: commit or stash them before a sync that commits")
    before = snapshot()
    r = run([PY, "-I", os.path.join(HERE, "bible_sync.py"), html, "--write"])
    section_lines = [l.strip() for l in r.stdout.splitlines() if l.startswith(("~ ", "+ NEW", "- REMOVED", "  "))]
    print(r.stdout.rstrip())
    regen()
    lint(strict=False)
    tests()
    after = snapshot(); change_lines = changes(before, after)
    print("\n== What changed for the products ==")
    print("\n".join(change_lines) or "- nothing in the product copy")
    changelog(new_ver, prev, [f"- {l}" for l in section_lines if l.startswith(("~", "+", "-"))], change_lines)
    print(f"\n✅ synced to {new_ver}: repo copy, 15 skills, briefs, lint, tests, CHANGELOG. Nothing committed." if not a.commit else "")
    if a.commit or a.release:
        git("add", "-A")
        git("commit", "-q", "-m", f"Bible sync to {new_ver}: skills regenerated from the bible\n\n" + "\n".join(change_lines))
        print(f"✅ committed on {br}")
    if a.release:
        release(br, new_ver)


def release(branch, version):
    git("checkout", "-q", "main"); git("pull", "-q", "--ff-only")
    git("merge", "-q", "--no-ff", "-m", f"Merge {branch}: bible sync to {version}", branch)
    git("push", "-q", "origin", "main")
    sha = git("rev-parse", "--short", "main").stdout.strip()
    versions = json.load(open(TEAM_VERSIONS)) if os.path.exists(TEAM_VERSIONS) else {"in_use": []}
    bases = [v for v in versions.get("in_use", []) if v != sha]
    if not bases:
        print(f"✅ main is {sha}. No team versions recorded in {TEAM_VERSIONS}: ask which VERSION each teammate has, then `build a patch`"); return
    r = run([PY, os.path.join(HERE, "make_patch.py"), ",".join(bases), "main", "--out", os.path.expanduser("~/Desktop")], check=False)
    print(r.stdout.rstrip()); print(r.stderr.rstrip())
    if r.returncode == 0:
        versions.setdefault("history", []).append({"date": datetime.date.today().isoformat(), "from": bases, "to": sha, "bible": version})
        versions["in_use"] = sorted(set(bases + [sha]))
        json.dump(versions, open(TEAM_VERSIONS, "w"), indent=1)


def cmd_regen(a):
    regen(a.only); lint(strict=False); print("✅ regenerated and linted")


def cmd_check(a):
    tmp = tempfile.mkdtemp(prefix="bible-check-")
    r = run([PY, "-I", os.path.join(HERE, "build_product_bibles.py"), "--out", tmp])
    stale = []
    for skill in sorted(os.listdir(tmp)):
        for f in ("bible.json", "product-bible.md"):
            a_, b_ = os.path.join(tmp, skill, "references", f), os.path.join(REPO, "skills", skill, "references", f)
            if not os.path.exists(b_) or open(a_, encoding="utf-8").read() != open(b_, encoding="utf-8").read():
                stale.append(f"skills/{skill}/references/{f}")
    shutil.rmtree(tmp)
    if stale:
        sys.exit("❌ generated files are stale (run `bible_pipeline.py regen` and commit):\n  " + "\n  ".join(stale))
    print("✅ every generated extract matches the synced bible")


def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("sync"); s.add_argument("html", nargs="?"); s.add_argument("--commit", action="store_true"); s.add_argument("--release", action="store_true"); s.add_argument("--force", action="store_true")
    r = sub.add_parser("regen"); r.add_argument("--only", default="")
    sub.add_parser("check"); sub.add_parser("newest")
    a = ap.parse_args()
    if a.cmd == "sync": cmd_sync(a)
    elif a.cmd == "regen": cmd_regen(a)
    elif a.cmd == "check": cmd_check(a)
    elif a.cmd == "newest": print(newest_saved() or "none")
    else: ap.print_help()


if __name__ == "__main__":
    main()
