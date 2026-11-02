# Keeping everyone on the latest creative bible

**Goal:** Justin updates the bible; every teammate's Claude makes ads from his latest version, and nobody works from old
rules without knowing. Decided by Priestley, 2026-11-02.

## Where the bible lives

```
Justin's live bible (claude.ai page)          ← the source. Only Justin edits it.
        │  synced in by bible_sync.py (on a branch, through a PR)
        ▼
core/claude/creative-bible.md                 ← the repo copy. Everyone's gates read it
        │                                       (linked to ~/.claude/everlife/creative-bible.md).
        ▼
skills/everlife-<product>/references/product-bible.md  + product.json
                                              ← each product's extract: the lines it may use (✅ / ⚠ / ❌)
                                                and its disclaimer. Ads are written from THIS.
```

Live page: https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG (visible to the Everlife org).

## Who does what

| Who | What |
|---|---|
| **Justin** | Edits the live bible. The only person who does. |
| **Every teammate's Claude** | Checks at the start of every product session whether Justin's page is newer (automatic). |
| **Someone with edit access** (Priestley, Justin, anyone they give edit rights to) | Runs **"Sync the bible"** when a change is found. |
| **The weekly job** (on Priestley's account) | Checks every week, even if nobody opens a session. |
| **Jeremy** | Approves sync PRs that change claims, disclaimers or approvals. |
| **Everyone** | Gets the synced version on their next update (`update.sh`). All on the same version. |

## 1. The check at the start of every session (automatic, read-only)

When any product skill starts, preflight shows the bible version and asks Claude to compare it with the live page:

- `✅ Creative bible = this repo's copy (version …)`: this computer reads the same bible as the repo. A ❌ here means an old
  separate copy; the fix is to run `install.sh`, which moves it to `~/.claude/everlife/_originals/` and links the repo's.
- Claude reads the live page and compares its **version** with the repo copy's:
  - **Same** → "Bible: up to date".
  - **Different** → "⚠ Justin updated the bible since the last sync; using this skill's current approved lines." **The
    work carries on** with the lines already approved (decision: warn, never block), and someone should sync the same day.
  - **Can't read it** (offline, no access) → Claude says so and carries on.

It writes nothing, so it never breaks anyone's updates. Teammates with view-only access see the version but not the
details: that is enough for the warning.

## 2. "Sync the bible" (someone with edit access)

Just ask Claude: **"sync the bible"**. Claude then:

1. Reads the live page (the full page is only returned to people with edit access) and makes a **new branch**
   (`bible-sync-<date>`). Never on `main`: the script refuses to write there, because a change on `main` stops
   `update.sh` from updating that computer.
2. Runs `core/scripts/bible_sync.py <saved page> --check`. It lists every changed line per section and **which product
   skills each section affects** (global sections = every skill), plus any disclaimer that no longer matches.
3. Writes the new repo copy (`--write`).
4. For every skill on the list: re-copies the product's VERBATIM block in `references/product-bible.md` word for word,
   marks new or changed lines **"NEW, not screened"**, screens them against the global rules (✅ / ⚠ / ❌, the same way the
   pre-screen table was made), and updates `product.json`'s disclaimer if Justin changed it (`--check` must then show ✅).
5. Logs it in `CHANGELOG.md` and opens a **PR** with the plain-words list of what changed.
6. Jeremy signs off when claims, disclaimers or approvals changed; then it is merged and everyone updates.

Until a line is screened, the skills treat it like ⚠: never used without an explicit OK.

## 3. The weekly check (automatic)

A scheduled job on Priestley's account reads the live page once a week and compares versions with the repo's `main`. If
Justin changed it, it prepares the sync (step 2) on a branch and opens the PR for review. If nothing changed, it does
nothing. It never merges by itself.

## Commands (for whoever maintains this)

```
python3 core/scripts/bible_sync.py --repo-version            # the repo copy's version
python3 core/scripts/bible_sync.py <saved page.html>         # what changed, and which skills it affects
python3 core/scripts/bible_sync.py <saved page.html> --check # also: does every product.json disclaimer match?
python3 core/scripts/bible_sync.py <saved page.html> --write # on a branch only: write the new repo copy
```

The Artifact tool's `read` saves the page as `artifact-<id>-<version>.html` in the current session's `tool-results/`
folder; the version in that file name is the live version.

## Never

- Never edit `core/claude/creative-bible.md` by hand.
- Never sync on `main`, and never on a teammate's own copy outside a branch.
- Never use a new bible line in an ad before it is screened (or explicitly approved as ⚠ and flagged for Jeremy).
