# Everlife ad factory

Claude Code skills that make compliant EverlifeMD ads, one skill per product, all sharing one toolkit.

```
core/                         shared by every product skill
  scripts/                    preflight.sh (reads the skill's product.env), finish_image.py
  tools/                      video + static finishing toolkit (product-neutral), fonts, footer art, logo
    product.py                loads a product's product.json; every tool uses it
  references/                 global-rules.md, static-refs/ (generic reference ads by framework)
  tests/regression.py         before/after check for core changes (+ fixtures/)
skills/
  everlife-restora-z/         one folder per product
  everlife-sermorelin-ghk/  (transparent bottle still missing: see its assets/MISSING_RENDERS.md)
  everlife-sermorelin/      plain Sermorelin, NOT Sermorelin GHK (1000 mcg renders in; 500 mcg missing: see its assets/MISSING_RENDERS.md)
    SKILL.md                  the producer flow
    product.json              everything the shared tools need to know about the product (data only)
    product.env               product name, renders, output folder, copy log (read by preflight)
    assets/                   real bottle + pill renders, Creatify project, copy-log seed
    references/               product bible, reviews, styles + boards, prompting, finishing, lessons
    core -> ../../core        link to the shared toolkit (committed to git)
core/claude/                  everlife-gates.md + everlife-team.md (imported into ~/.claude/CLAUDE.md), creative-bible.md
core/scripts/update.sh        "update my ad tools": pull, install, toolkit, checks
install.sh                    links every skill into ~/.claude/skills/ (+ gates, bible link, read-only allow list)
ONBOARDING.md                 Day-1 guide for non-technical teammates
```

## Setup (each person, once)
Non-technical teammates: follow `ONBOARDING.md` (GitHub route; one pasted prompt; Claude Code does the steps) or
`ONBOARDING-ZIP.md` (no GitHub: we send a zip built with `bash core/scripts/make_zip.sh main ~/Desktop`; new versions
are new zips). Both cover Mac and Windows (Windows runs everything inside WSL/Ubuntu; Apple fonts fall back to the
bundled Inter/Fraunces in `build_layers.font()`). Already running the original Restora-Z package (zip)? Follow `HANDOFF-MITANSH.md` instead: it checks your version, backs it up, tests the new
tools on your Mac before installing, and has a rollback.

1. `gh repo clone dataipreneur/everlife-ad-factory ~/everlife-ad-factory` (private repo: needs a GitHub invite)
2. `bash ~/everlife-ad-factory/core/scripts/update.sh`: links the skills (`install.sh`: an older unlinked copy is moved
   to `~/.claude/skills-backup/`), adds the creative gates (`core/claude/`) to `~/.claude/CLAUDE.md` as one managed
   import block, links the creative bible, allows a few read-only commands, installs the toolkit, runs every preflight.
3. Higgsfield: `higgsfield auth login`, Everlife workspace. Creatify: `claude plugin marketplace add
   creatify-ai/creatify-ad-agent-skill`, `claude plugin install creatify-ad-agent@creatify-ad-agent`, sign in via `/mcp`.

## Day to day
- Get the latest: `bash core/scripts/update.sh` (pull main → `install.sh` → toolkit `--install` → every preflight; stops
  if the copy has local edits). In that order: the tools find products through the linked skills in `~/.claude/skills`.
- The creative gates and bible live in `core/claude/`. Change them only through a PR with Jeremy's sign-off;
  everyone's Claude Code reads them. The **live bible** is the shared artifact
  https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG; `core/claude/creative-bible.md` is synced from it with
  `core/scripts/bible_sync.py` (ask Claude: "check the bible for updates"). Never edit the copy by hand.
- Change something: `git checkout -b <short-name>` → edit → `git commit` → `git push` → open a pull request → the other person reviews and merges.
- Changes to `core/` affect every product: run the before/after check before merging (below).
- Changes to a bible, disclaimer or claim file need Jeremy's sign-off before merge.

## Adding a product skill
1. Copy `skills/everlife-restora-z/` to `skills/everlife-<product>/` (keep the `core` link).
2. Write its `product.json` (copy another skill's and change the values; the disclaimer is the bible's, verbatim). No tool code changes: a new product is data only.
3. Replace: `SKILL.md` name/description/product wording, `product.env`, `assets/` renders (from the Drive asset library, checked against the website), `references/product-bible.md` (from the creative bible), and rewrite the Restora-specific copy in `references/` (styles, prompting, image-batch, finishing, lessons, reviews).
4. The product must have an ad disclaimer on file in the creative bible (Part A products only); otherwise the skill stops at the compliance gate.
5. `bash install.sh`, then run its preflight.

## How products are handled in the shared tools (since 2026-10-28)
The tools contain no product names. Every job's `copy.json` says which product it is (`"product": "<id>"`), and the tools
read the rest from `skills/everlife-<id>/product.json`: verbatim disclaimer, renders, name casing ("GHK", never "Ghk"),
review highlight and reviews file, legacy-layout defaults, whether a comparison layout is allowed, and the colours
`finish_modern.py` uses to keep type off the product (`product_zones`; a product without them is refused there, so use
`finish_batch.py`). A job without a product, or with a disclaimer that differs from product.json, is refused: the tools
never fall back to another product. `build_layers.py` run on its own is the old Restora-only builder (legacy).

## Before/after check for core changes
`core/tests/regression.py` renders a fixed set of jobs (every video look + review burst, every static finisher; Restora-Z
fixtures, no credits) and compares them pixel by pixel; `smoke` renders a second product and checks every guard.
```
T=~/Everlife-Creative/tools/venv/bin/python
git archive main core | tar -x -C /tmp/main                       # the version you're comparing against
$T -I core/tests/regression.py run /tmp/main/core /tmp/before
$T -I core/tests/regression.py run core /tmp/after
$T -I core/tests/regression.py compare /tmp/before /tmp/after     # Restora-Z must be identical unless intended
$T -I core/tests/regression.py smoke core /tmp/smoke              # all checks must pass
```
- Copy logs live per person in `~/Everlife-Creative/`; they are not shared through git.
