# Everlife creative skills

Claude Code skills that make compliant EverlifeMD ads, one skill per product, all sharing one toolkit.

```
core/                         shared by every product skill
  scripts/                    preflight.sh (reads the skill's product.env), finish_image.py
  tools/                      video + static finishing toolkit, fonts, footer art, logo
  references/                 global-rules.md, static-refs/ (generic reference ads by framework)
skills/
  everlife-restora-z/         one folder per product
    SKILL.md                  the producer flow
    product.env               product name, renders, output folder, copy log
    assets/                   real bottle + pill renders, Creatify project, copy-log seed
    references/               product bible, reviews, styles + boards, prompting, finishing, lessons
    core -> ../../core        link to the shared toolkit (committed to git)
install.sh                    links every skill into ~/.claude/skills/
```

## Setup (each person, once)
1. `git clone <repo-url> ~/everlife-creative-skills`
2. `bash ~/everlife-creative-skills/install.sh` (links the skills; an older unlinked copy is moved to `~/.claude/skills-backup/`)
3. `bash ~/.claude/skills/everlife-restora-z/core/scripts/preflight.sh --install`
4. Higgsfield: `higgsfield auth login`, Everlife workspace. Creatify: connect the creatify-ad-agent plugin.

## Day to day
- Get the latest: `git pull`. If anything under `core/tools/` changed, run preflight `--install` again (it copies the toolkit to `~/Everlife-Creative/tools`).
- Change something: `git checkout -b <short-name>` → edit → `git commit` → `git push` → open a pull request → the other person reviews and merges.
- Changes to `core/` affect every product: test with at least one product skill before merging.
- Changes to a bible, disclaimer or claim file need Jeremy's sign-off before merge.

## Adding a product skill
1. Copy `skills/everlife-restora-z/` to `skills/everlife-<product>/` (keep the `core` link).
2. Replace: `SKILL.md` name/description/product wording, `product.env`, `assets/` renders (from the Drive asset library, checked against the website), `references/product-bible.md` (from the creative bible), and rewrite the Restora-specific copy in `references/` (styles, prompting, image-batch, finishing, lessons, reviews).
3. The product must have an ad disclaimer on file in the creative bible (Part A products only); otherwise the skill stops at the compliance gate.
4. `bash install.sh`, then run its preflight.

## Known Restora-specific bits still in core (fix before a second product ships)
- `core/tools/build_layers.py`: Restora disclaimer, benefits, CTA, ingredient claims and render names are hard-coded constants.
- `core/tools/composite.py` and `full_layout.py`: default paths point at `~/.claude/skills/everlife-restora-z/` (assets, reviews.json).
- `core/tools/finish_modern.py`, `review_burst.py`, `styles.py`, `core/scripts/finish_image.py`: Restora-Z / sleep defaults and examples.
- Copy logs live per person in `~/Everlife-Creative/`; they are not shared through git.
