#!/usr/bin/env python3
"""Both-sizes + layout gate for image batches (Claude Code hooks; installed by install.sh). Mitansh 2026-11-05:
"how is it guaranteed that for every skill Claude will one-shot 10 images in 1 batch, 5 for each side?" → this file.

  batch_hook.py gate    PreToolUse on image-generation tools: an Everlife image prompt is REFUSED unless it carries the
                        STRICT LAYOUT block and the batch reference line the template adds at the end:
                          Reference only, never render: everlife slot=3 ratio=9:16 product=pt-141 job=<batch folder>
                        (ratio must match the layout block). Other generations (video, avatars, non-Everlife) pass untouched.
  batch_hook.py fired   PostToolUse: records every fired (slot, ratio) in <job>/renders.jsonl.
  batch_hook.py stop    Stop: for every batch touched today, compares deal.json (slots × ratios owed) with renders fired and
                        FINAL_<slot>_*_1080x1920 / _1080x1350 files finished. Anything owed → Claude is sent back once
                        (decision "block") with the exact list; the second time it lets the turn end and warns the user.
                        A batch the user abandoned is released with `batch_check.py <job> --release "<reason>"`.

Independent of the team-log pause (a paused log never means half a batch). Local files only, no network.
"""
import datetime, glob, json, os, re, sys

HOME = os.path.expanduser(os.environ.get("EVERLIFE_CREATIVE", "~/Everlife-Creative"))
OUT = os.path.join(HOME, "output")
REF = re.compile(r"Reference only, never render: everlife slot=(\d+) ratio=(9:16|4:5|1:1) product=([a-z0-9-]+) job=(\S+)")
IMAGE_TOOL = re.compile(r"model_playground_generate|edit_image|gpt[-_]image|image_generate|generate_image", re.I)
SIZES = {"9:16": "1080x1920", "4:5": "1080x1350", "1:1": "1080x1080"}


def strings(v, out=None):
    out = [] if out is None else out
    if isinstance(v, dict):
        for x in v.values(): strings(x, out)
    elif isinstance(v, list):
        for x in v: strings(x, out)
    elif isinstance(v, str): out.append(v)
    return out


def find_ref(tin):
    for s in strings(tin):
        m = REF.search(s)
        if m: return m.group(1), m.group(2), m.group(3), os.path.expanduser(m.group(4)), s
    return None


def is_everlife_image(tool, tin):
    if not IMAGE_TOOL.search(tool or ""): return False
    txt = "\n".join(strings(tin))
    return "Everlife" in txt or "STRICT LAYOUT" in txt or "everlife slot=" in txt


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": reason}}))


def gate(p):
    tool, tin = p.get("tool_name", ""), p.get("tool_input", {}) or {}
    if not is_everlife_image(tool, tin): return
    ref = find_ref(tin)
    txt = "\n".join(strings(tin))
    if not ref:
        return deny("Everlife image prompt without its batch reference line. Every image prompt ends with: "
                    "'Reference only, never render: everlife slot=<n> ratio=<9:16|4:5> product=<id> job=<batch folder>' "
                    "(core/references/image-flow.md §4). Deal the batch first (deal_worlds.py → <job>/deal.json), then send both sizes.")
    slot, ratio, product, job, _ = ref
    if "STRICT LAYOUT" not in txt:
        return deny(f"Slot {slot} {ratio}: the prompt has no STRICT LAYOUT block (core/references/prompt-layout-zones.md). Add it and resend.")
    if f"STRICT LAYOUT ({ratio}" not in txt:
        return deny(f"Slot {slot}: the reference says ratio={ratio} but the STRICT LAYOUT block is for another ratio. One prompt per ratio, each with its own block.")
    deal = os.path.join(job, "deal.json")
    if not os.path.exists(deal):
        return deny(f"No deal.json in {job}. Run core/scripts/deal_worlds.py --product {product} --n N … --json > {deal} first; the batch is owed from that manifest.")
    try:
        slots = {str(s["slot"]) for s in json.load(open(deal))}
    except Exception:
        slots = set()
    if slots and slot not in slots:
        return deny(f"Slot {slot} is not in {deal} (slots {', '.join(sorted(slots, key=int))}). Re-roll an existing slot; never add a size-less extra.")


def fired(p):
    tool, tin = p.get("tool_name", ""), p.get("tool_input", {}) or {}
    if not is_everlife_image(tool, tin): return
    ref = find_ref(tin)
    if not ref: return
    slot, ratio, product, job, _ = ref
    os.makedirs(job, exist_ok=True)
    with open(os.path.join(job, "renders.jsonl"), "a") as f:
        f.write(json.dumps({"ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "slot": int(slot),
                            "ratio": ratio, "product": product, "tool": tool}) + "\n")


def status(job):
    """→ dict(owed_fire=[(slot,ratio)], owed_finish=[(slot,ratio)], n, released)"""
    deal = os.path.join(job, "deal.json")
    if not os.path.exists(deal): return None
    try: slots = json.load(open(deal))
    except Exception: return None
    rel = os.path.join(job, ".batch-released")
    if os.path.exists(rel): return {"owed_fire": [], "owed_finish": [], "n": len(slots), "released": True}
    firedset = set()
    rp = os.path.join(job, "renders.jsonl")
    if os.path.exists(rp):
        for ln in open(rp):
            try: r = json.loads(ln); firedset.add((int(r["slot"]), r["ratio"]))
            except Exception: pass
    finals = set()
    for f in glob.glob(os.path.join(job, "**", "FINAL_*"), recursive=True):
        m = re.search(r"FINAL_(\d+)_.*_(1080x\d+)", os.path.basename(f))
        if m:
            for ratio, wh in SIZES.items():
                if m.group(2) == wh: finals.add((int(m.group(1)), ratio))
    owed_fire, owed_finish = [], []
    for s in slots:
        for ratio in s.get("ratios", ["9:16", "4:5"]):
            key = (int(s["slot"]), ratio)
            if key not in firedset and key not in finals: owed_fire.append(key)
            elif key not in finals: owed_finish.append(key)
    return {"owed_fire": owed_fire, "owed_finish": owed_finish, "n": len(slots), "released": False}


def active_jobs(hours=14):
    cutoff = datetime.datetime.now().timestamp() - hours * 3600
    jobs = []
    for deal in glob.glob(os.path.join(OUT, "*", "*", "deal.json")):
        job = os.path.dirname(deal)
        newest = max(os.path.getmtime(x) for x in [deal] + glob.glob(os.path.join(job, "renders.jsonl")))
        if newest >= cutoff: jobs.append(job)
    return jobs


def fmt(pairs):
    by = {}
    for s, r in pairs: by.setdefault(r, []).append(str(s))
    return "; ".join(f"{r} for slot(s) {', '.join(sorted(v, key=int))}" for r, v in sorted(by.items()))


def stop(p):
    todo = []
    for job in active_jobs():
        st = status(job)
        if not st or st["released"]: continue
        rp = os.path.join(job, "renders.jsonl")
        if not os.path.exists(rp) and not st["owed_finish"]: continue   # dealt but never started: nothing owed yet
        parts = []
        if st["owed_fire"]: parts.append("not generated: " + fmt(st["owed_fire"]))
        if st["owed_finish"]: parts.append("generated but not finished (no FINAL file): " + fmt(st["owed_finish"]))
        if parts: todo.append(f"{os.path.basename(job)}: " + " · ".join(parts))
    if not todo: return
    nag = os.path.join(HOME, ".batch-stop-nag")
    sid = p.get("session_id", "")
    seen = open(nag).read() if os.path.exists(nag) else ""
    if sid and sid in seen:
        print(json.dumps({"systemMessage": "⚠ Batch incomplete: " + " | ".join(todo) + ". Every ad needs both sizes, finished. "
                          "Finish it next turn, or release it with core/scripts/batch_check.py <job> --release '<reason>'."}))
        return
    open(nag, "a").write(sid + "\n")
    print(json.dumps({"decision": "block", "reason": "Both-sizes gate: " + " | ".join(todo) + ". Every ad is owed in 9:16 AND 4:5, "
                      "finished with finish_batch.py (FINAL_<slot>_<world>_1080x1920 / _1080x1350). Generate / finish what is missing now "
                      "(same slots, same worlds). If the user stopped the batch on purpose: core/scripts/batch_check.py <job> --release '<their words>'."}))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        p = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    except Exception:
        p = {}
    try:
        {"gate": gate, "fired": fired, "stop": stop}.get(cmd, lambda p: None)(p)
    except Exception as e:   # a hook must never break the session
        print(json.dumps({"systemMessage": f"batch hook skipped: {e}"}))


if __name__ == "__main__":
    main()
