#!/usr/bin/env python3
"""Both-sizes check for one image batch (the same maths the Stop hook uses).

    batch_check.py <job folder>                 # ✅ complete / ❌ list of what is owed; exit 1 while anything is owed
    batch_check.py <job folder> --release "<reason>"   # the user stopped the batch on purpose: stop nagging, record why
                                                       # (also releases the next-batch questionnaire for that batch)

A batch = <job>/deal.json (slots × ratios owed) · <job>/renders.jsonl (what was fired, written by the hook) ·
FINAL_<slot>_<world>_1080x1920 / _1080x1350 files (what was finished). `teamlog.py close` and Ad Review posting call this first.
"""
import datetime, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks"))
from batch_hook import status, fmt, ASKED  # noqa: E402


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    job = os.path.expanduser(sys.argv[1])
    if "--release" in sys.argv:
        why = sys.argv[sys.argv.index("--release") + 1] if len(sys.argv) > sys.argv.index("--release") + 1 else "released"
        with open(os.path.join(job, ".batch-released"), "w") as f:
            f.write(f"{datetime.datetime.now().isoformat(timespec='seconds')} {why}\n")
        print(f"released: {os.path.basename(job)} ({why}); the Stop hook no longer asks for it"); return
    st = status(job)
    if st is None:
        print(f"❌ no deal.json in {job}: deal the batch first (deal_worlds.py … --json > deal.json)"); sys.exit(1)
    if st["released"]:
        print(f"⚪ {os.path.basename(job)}: released on purpose (see .batch-released)"); return
    if not st["owed_fire"] and not st["owed_finish"]:
        print(f"✅ {os.path.basename(job)}: {st['n']} ads × 2 sizes = {2 * st['n']} finished images")
        if os.path.exists(os.path.join(job, ASKED)): print("✅ next-batch questionnaire asked (next_asked.json)")
        else: print("❗ next-batch questionnaire owed: ask it before the turn ends (image-flow.md §9); the Stop hook blocks until then")
        return
    if st["owed_fire"]: print("❌ not generated: " + fmt(st["owed_fire"]))
    if st["owed_finish"]: print("❌ generated but not finished (no FINAL file): " + fmt(st["owed_finish"]))
    sys.exit(1)


if __name__ == "__main__":
    main()
