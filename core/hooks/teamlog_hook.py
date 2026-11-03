#!/usr/bin/env python3
"""Claude Code hooks that make team logging automatic (TEAM-LOGS.md §7). Installed by install.sh into ~/.claude/settings.json.

  teamlog_hook.py capture   PostToolUse: every paid Creatify / Higgsfield generation call (MCP tool, or the higgsfield /
                            creatify CLI through Bash) is appended to ~/Everlife-Creative/teamlog-auto.jsonl with its exact
                            input, whatever Claude does. Never blocks, never calls the network.
  teamlog_hook.py stop      Stop: if this session made more paid generations than `teamlog.py gen` logged since the first one,
                            Claude is sent back once to log them (decision "block"). The second time it lets the turn end and
                            warns the user, so a session can never get stuck.

Both read the hook payload (JSON) on stdin and stay silent for every other tool and every non-Everlife session.
"""
import datetime, json, os, re, sys

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
    missing = len(mine) - len(logged)
    if missing <= 0:
        return
    tools = ", ".join(sorted({r["tool"].split("__")[-1] if r["tool"] != "Bash" else "Bash CLI" for r in mine}))
    msg = (f"Team logs: this session made {len(mine)} paid generation(s) ({tools}) but only {len(logged)} were logged with "
           f"`core/scripts/teamlog.py gen`. Their exact inputs were captured automatically in {AUTO} (session {sid[:8]}). "
           "Log the missing ones now (teamlog.py gen per generation, prompt text from that file, then qa / copy / proof / run and "
           "`teamlog.py close <job>`), send them to the logs, then finish. If the logs can't be reached, use the pending file.")
    if p.get("stop_hook_active"):
        print(json.dumps({"systemMessage": f"⚠ {missing} paid generation(s) in this session are still not in the team logs "
                                           f"(raw copy kept in {AUTO})."}))
        return
    print(json.dumps({"decision": "block", "reason": msg}))


def main():
    try:
        p = json.load(sys.stdin)
    except ValueError:
        return
    try:
        {"capture": capture, "stop": stop}[sys.argv[1]](p)
    except Exception as e:   # a logging hook must never break the session
        print(json.dumps({"systemMessage": f"team-log hook skipped: {e}"}))


if __name__ == "__main__":
    main()
