#!/usr/bin/env python3
"""Claude Code hooks that make team logging automatic (TEAM-LOGS.md §7). Installed by install.sh into ~/.claude/settings.json.

  teamlog_hook.py capture   PostToolUse: every paid Creatify / Higgsfield generation call (MCP tool, or the higgsfield /
                            creatify CLI through Bash) is appended to ~/Everlife-Creative/teamlog-auto.jsonl with its exact
                            input, whatever Claude does. Never blocks, never calls the network.
  teamlog_hook.py stop      Stop: if this session made more paid generations than `teamlog.py gen` logged since the first one,
                            or its job folders hold records never sent to the pages (`teamlog.py sent`) or finished ads of a
                            closed run never posted to Ad Review (`teamlog.py posted`), Claude is sent back once to do it
                            (decision "block"). The second time it lets the turn end and warns the user, so a session can never
                            get stuck. Local files only: no network, no tokens unless something is missing.

  teamlog_hook.py start     SessionStart: warns the user (never blocks) when the capture or Stop hook is missing from
                            ~/.claude/settings.json or points at a script that no longer exists, so nobody works unprotected.

All read the hook payload (JSON) on stdin and stay silent for every other tool and every non-Everlife session.
"""
import datetime, glob, hashlib, json, os, re, sys

HOME = os.path.expanduser(os.environ.get("EVERLIFE_CREATIVE", "~/Everlife-Creative"))
AUTO = os.path.join(HOME, "teamlog-auto.jsonl")      # raw capture, one line per paid generation call
INDEX = os.path.join(HOME, "teamlog-index.jsonl")    # one line per `teamlog.py gen` record (written by teamlog.py)

SERVER = re.compile(r"creatify|higgsfield", re.I)
# Tool names that spend credits (generation, edits, renders). Reads, quotes, status and listing calls never match.
PAID = re.compile(r"generate|edit_image|voice_line|upscale|outpaint|reframe|remove_background|motion_control|dubbing|"
                  r"voice_change|create_voice|execute_preset|shorts_studio_create|build_ai_influencer|playground_generate|"
                  r"apps_invoke|scene_builder_3d_generate", re.I)
NOT_PAID = re.compile(r"cost|quote|status|list|get_|_get|show_|balance|billing|describe|prepare|explore", re.I)
BASH_PAID = re.compile(r"\bhiggsfield\s+generate\s+create\b|\bmodel_playground_generate\b|\bcreatify\b.*\bgenerate\b")


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def is_paid(tool, tin):
    if tool == "Bash":
        return bool(BASH_PAID.search(str((tin or {}).get("command", ""))))
    return tool.startswith("mcp__") and bool(SERVER.search(tool)) and bool(PAID.search(tool.split("__")[-1])) \
        and not NOT_PAID.search(tool.split("__")[-1])


def slim(v, depth=0):
    """Keep prompts whole; shorten base64 blobs and very long non-prompt strings so the file stays small."""
    if isinstance(v, dict):
        return {k: (v[k] if re.search(r"prompt|text|script|caption|dialogue", k, re.I) and isinstance(v[k], str) else slim(v[k], depth + 1))
                for k in v}
    if isinstance(v, list):
        return [slim(x, depth + 1) for x in v[:50]]
    if isinstance(v, str) and (v.startswith("data:") or len(v) > 4000):
        return v[:200] + f"… [{len(v)} chars]"
    return v


def credits(resp):
    """The first number under a key that looks like a credit cost, anywhere in the tool response."""
    found = []
    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if re.search(r"credit|cost", k, re.I) and isinstance(v, (int, float)):
                    found.append(v)
                else:
                    walk(v)
        elif isinstance(x, list):
            for y in x:
                walk(y)
        elif isinstance(x, str) and x.strip().startswith(("{", "[")):
            try:
                walk(json.loads(x))
            except ValueError:
                pass
    walk(resp)
    return found[0] if found else None


def lines(path):
    if not os.path.exists(path):
        return []
    out = []
    for ln in open(path, encoding="utf-8"):
        try:
            out.append(json.loads(ln))
        except ValueError:
            pass
    return out


def capture(p):
    tool, tin = p.get("tool_name", ""), p.get("tool_input") or {}
    if not is_paid(tool, tin):
        return
    os.makedirs(HOME, exist_ok=True)
    rec = {"at": now(), "session_id": p.get("session_id", ""), "cwd": p.get("cwd", ""), "tool": tool,
           "input": slim(tin), "credits": credits(p.get("tool_response"))}
    with open(AUTO, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def stop(p):
    sid = p.get("session_id", "")
    mine = [r for r in lines(AUTO) if r.get("session_id") == sid and sid]
    if not mine:
        return
    first = min(datetime.datetime.fromisoformat(r["at"]) for r in mine) - datetime.timedelta(minutes=10)
    def since(r):   # a gen record may be written just before its call is sent: allow 10 minutes
        try:
            return datetime.datetime.fromisoformat(r.get("at", "")) >= first
        except ValueError:
            return False
    logged = [r for r in lines(INDEX) if since(r)]
    missing = len(mine) - sum(int(r.get("count") or 1) for r in logged)   # a light (maintenance) record covers several calls
    unsent, unposted = backlog({r.get("job") for r in logged if r.get("job")})
    if missing <= 0 and not unsent and not unposted:
        return
    todo, short = [], []
    if missing > 0:
        tools = ", ".join(sorted({r["tool"].split("__")[-1] if r["tool"] != "Bash" else "Bash CLI" for r in mine}))
        todo.append(f"this session made {len(mine)} paid generation(s) ({tools}) but {missing} are not logged with "
                    f"`core/scripts/teamlog.py gen`/`gens` (exact inputs captured in {AUTO}, session {sid[:8]}): log them")
        short.append(f"{missing} generation(s) not logged")
    if unsent:
        todo.append(f"{sum(unsent.values())} logged record(s) were never sent to the pages: run `teamlog.py pending <job>` "
                    f"({', '.join(unsent)}), send one ArtifactData batch per page, then `teamlog.py sent <job> --all`")
        short.append(f"{sum(unsent.values())} record(s) not sent")
    if unposted:
        todo.append(f"{sum(unposted.values())} finished ad(s) are not on Ad Review (AD-REVIEW §4): post them, then "
                    "`teamlog.py posted <job> <ad_id…>`")
        short.append(f"{sum(unposted.values())} ad(s) not posted")
    if p.get("stop_hook_active"):
        print(json.dumps({"systemMessage": "⚠ Team logs: " + "; ".join(short) + f" (raw copy kept in {AUTO})."}))
        return
    print(json.dumps({"decision": "block", "reason": "Team logs: " + "; ".join(todo) + ". If a page can't be reached, append to "
                      "the pending file and mark them with --queued. Then finish."}))


def digest(rec):   # same as teamlog.digest
    return hashlib.sha1(json.dumps(rec, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:12]


def backlog(jobs):
    """{job: n} records not sent (new or changed since `teamlog.py sent`) and {job: n} finished ads of closed runs not posted."""
    unsent, unposted = {}, {}
    for job in jobs:
        d = os.path.join(job, "teamlog")
        if not os.path.isdir(d):
            continue
        load = lambda n: json.load(open(os.path.join(d, n))) if os.path.exists(os.path.join(d, n)) else {}
        sent, posted = load(".sent.json"), load(".posted.json")
        recs = {}
        for f in glob.glob(os.path.join(d, "*.json")):
            try:
                recs[os.path.basename(f)[:-5]] = json.load(open(f))
            except ValueError:
                pass
        n = sum(1 for doc, r in recs.items() if (sent.get(doc) or {}).get("digest") != digest(r))
        closed = {r.get("run_id") for r in recs.values() if r.get("type") == "run"}
        ads = {r.get("ad_id") for r in recs.values() if r.get("type") == "gen" and not r.get("light")
               and r.get("run_id") in closed and (r.get("qa") or {}).get("pass")}
        name = os.path.basename(job.rstrip("/"))
        if n:
            unsent[name] = n
        if ads - set(posted):
            unposted[name] = len(ads - set(posted))
    return unsent, unposted


def start(p):
    settings = os.path.expanduser("~/.claude/settings.json")
    try:
        hooks = json.load(open(settings)).get("hooks", {})
    except (OSError, ValueError):
        hooks = {}
    problems = []
    for ev, mode in (("PostToolUse", "capture"), ("Stop", "stop")):
        cmds = [x.get("command", "") for e in hooks.get(ev, []) for x in e.get("hooks", []) if "teamlog_hook.py" in x.get("command", "")]
        if not any(c.rstrip().endswith(mode) for c in cmds):
            problems.append(f"the {mode} hook is not installed")
        for c in cmds:
            m = re.search(r'"([^"]*teamlog_hook\.py)"', c)
            if m and not os.path.exists(m.group(1)):
                problems.append(f"the {mode} hook points at a missing script ({m.group(1)})")
    if problems:
        print(json.dumps({"systemMessage": "⚠ Team logs: " + "; ".join(sorted(set(problems))) + ". Paid generations will not be captured. "
                          "Fix: bash <repo>/core/scripts/update.sh, then restart Claude Code."}))


def main():
    try:
        p = json.load(sys.stdin)
    except ValueError:
        return
    try:
        {"capture": capture, "stop": stop, "start": start}[sys.argv[1]](p)
    except Exception as e:   # a logging hook must never break the session
        print(json.dumps({"systemMessage": f"team-log hook skipped: {e}"}))


if __name__ == "__main__":
    main()
