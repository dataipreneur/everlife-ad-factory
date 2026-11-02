# Proposal for Mitansh: move the Hook Ladder ledger to the Winners Board

**Status: PROPOSED, not applied.** `core/hook-engine/` is Mitansh's; nothing in it has been changed. This file lists the exact
edits for his review. Until he approves, the Hook Engine keeps using `~/Everlife-Creative/hook-ledger.jsonl` as written.

## Why
The ledger is a local file on each Mac, so teammate A's winners and retired hooks are invisible to teammate B: two people can
pitch the same retired hook, and "this product's last 15" means "my last 15". The Winners Board
(https://claude.ai/artifact/QiQsRZvDdTTsKmsuVDG52M, protocol in `core/winners-board/WINNERS-BOARD.md`) is one shared store that
every teammate's Claude reads before a batch and writes after it. Image batches already use it.

## What changes (proposed edits to `core/hook-engine/HOOK-ENGINE.md`)

### §4 "The Hook Ladder", the **Ledger** paragraph → replace with
> **Ledger:** the shared Winners Board (`core/winners-board/WINNERS-BOARD.md`), entries with `kind: "hook"`. Recipe fields:
> `family`, `mechanic`, `route`, `frame0`, `sound`; plus `score` (HOOK-10), `rating`, `status`, `job`, and Meta reports
> (`hook_rate`, CTR, CPA) as `type: "meta"` docs. If the board can't be reached, use its fallback (§7 of that file).

### §4 rating thresholds → the board's 4-point scale
| Today (5-point) | Board |
|---|---|
| "rated 5" → winner | **Winner** → `winner` |
| 4 Good, 3 OK | **Good** → `active` |
| "rated ≤ 2" → retired | **Weak** or **Kill** → `retired` |
Bar rules stay the same, read from the board: pitch only ≥ 8; the top pitched hook beats the median of this product's last 5
board scores (hooks only); one option from a family unused in the last 3; once a winner exists, one of the 3 options is a winner
mutation (exactly one of object, angle, cast, room, speed, sound); retired hooks are never pitched again for that product unless
asked; Meta results (best hook rate → winner, bottom quarter → retired) override the opinion rating.
Novelty point ⑥ ("0 if the same family+mechanic appears in this product's last 10 ledger lines") reads the board's last 10.

### §5 step 1 → replace "the product's last 15 ledger lines (create the ledger if missing)" with
> the product's last 15 hook entries on the Winners Board (WINNERS-BOARD.md §4; across all teammates)

### §8 "After each video" → replace steps 1–2 with
> 1. AskUserQuestion "Rate the hook": **Winner / Good / Weak / Kill** (descriptions as in WINNERS-BOARD.md §5).
> 2. Write the entry to the Winners Board (`kind: "hook"`, recipe, `score`, `rating`, `job`; WINNERS-BOARD.md §5).
Steps 3–4 unchanged.

## One-time migration (optional, after approval)
Each teammate with a local `~/Everlife-Creative/hook-ledger.jsonl` asks Claude to import it: one board entry per line, `kind:
"hook"`, rating mapped 5 → winner, 4/3 → good, 2 → weak, 1 → kill, `status` from that rating, `meta_hook_rate` → a `type: "meta"`
doc, `source: "ledger-import"`. Keep the local file as a backup; stop appending to it.

## Open questions for Mitansh
1. Is losing "3 OK" as a separate grade acceptable (it merges into Good)? AskUserQuestion shows at most 4 options.
2. Should the "median of the last 5" bar move to "last 15" to match the image side, or stay at 5 for hooks?
3. Who sets the Meta verdict for hooks (the media buyer pasting results, or a fixed hook-rate threshold per product)?
