# Everlife ad factory, version 2: update guide for the creative team

You already run version 1 (the Restora-Z and Sermorelin GHK skills). Version 2 adds the PT-141 skill, moves the
Everlife logo to the top of every static, and moves the proof footer (Trustpilot, Doctor Prescribed, Ships Free,
disclaimer) up into the Meta safe area so it is never hidden under the Reels "Learn more" button.

You do not need to know git or Python. Every step below is either "paste this into Claude Code" or "type this one line".
Nothing here spends credits.

---

## Step 1. Save your own tweaks first (5 minutes)

You changed a few things in your copy (for example the logo size). Those must not be lost, so Claude will list them.

1. Open Claude Code the way you do for ads.
2. Paste this whole box, press Enter, and say yes if it asks to read files:

```
Please help me make a list of every change that was made to my Everlife ad tools, so my team lead can copy those changes into the new version. I am not technical, so please do everything yourself and keep your questions to a minimum.

What to do:
1. Find my Everlife ad skills and tools on this computer. They are usually in ~/.claude/skills (folders starting with "everlife-") and in ~/Everlife-Creative/tools. Follow any shortcuts to the real folders.
2. Work out what the original files looked like. Look for a git history, an "_originals" folder next to CHANGELOG.md, the CHANGELOG.md itself, or any zip or backup of the install. If none of those exist, use the file dates and say that you did.
3. Find everything that is different from the original: numbers that changed (for example a logo size), words that changed in prompts or templates, new or replaced pictures and assets, and anything added to the lessons or copy-log files. For every change, record the exact old and new values.
4. Write it all into one file on my Desktop called my-ad-changes.md, with:
   - a short summary in plain English,
   - a table with one row per changed file: file, what changed in plain words, old value -> new value, why if you can tell, and when,
   - a list of new files or assets,
   - a list of anything you could not confirm.
5. Tell me when the file is ready and where it is.

Important: only read and write that one file. Do not change, delete, regenerate or upload anything, and do not spend any credits.
```

3. A file called `my-ad-changes.md` appears on your Desktop. Send it to Mitansh. He merges your tweaks into version 2.

---

## Step 2. Install version 2 (10 minutes, Claude does it)

Paste this box into Claude Code and press Enter. Say yes when it asks permission to run commands. It downloads the
new version, links the skills, and installs the finishing toolkit. Your old copy is moved to a backup folder, never deleted.

```
Please install version 2 of the Everlife ad factory for me. I am not technical: do each step yourself, show me the result of each step, and stop and explain if anything fails. Do not spend any credits.

1. If the folder ~/everlife-ad-factory does not exist, run:
   git clone https://github.com/dataipreneur/everlife-ad-factory.git ~/everlife-ad-factory
   If it already exists, run "git -C ~/everlife-ad-factory pull" instead.
2. Switch it to the version-2 branch: git -C ~/everlife-ad-factory checkout pt-141-skill && git -C ~/everlife-ad-factory pull
   (If Mitansh has said the branch is merged, use "main" instead of "pt-141-skill".)
3. Run: bash ~/everlife-ad-factory/install.sh
   It links three skills into ~/.claude/skills: everlife-restora-z, everlife-sermorelin-ghk, everlife-pt-141. If it says it moved an old copy to ~/.claude/skills-backup, that is expected.
4. Run: bash ~/.claude/skills/everlife-pt-141/core/scripts/preflight.sh --install
   This installs the shared finishing toolkit into ~/Everlife-Creative/tools. It may take a few minutes.
5. Run the preflight check for each skill and show me the ✅ / ❌ lines:
   bash ~/.claude/skills/everlife-restora-z/core/scripts/preflight.sh
   bash ~/.claude/skills/everlife-sermorelin-ghk/core/scripts/preflight.sh
   bash ~/.claude/skills/everlife-pt-141/core/scripts/preflight.sh
6. Run: claude mcp add --transport http --scope user creatify https://api.creatify.ai/mcp
   (If it says the server already exists, that is fine.)
7. For every ❌ line, tell me in plain words what I need to do. The only things I may have to do myself are logging in to Higgsfield and connecting the Creatify plugin (step 3 of the guide).
```

---

## Step 3. Log in to the two services (only if the preflight showed a ❌ for them)

Type these yourself in the Claude Code chat. The `!` at the start runs the command on your Mac.

- Higgsfield login: `! higgsfield auth login` and follow the browser window. Then `! higgsfield workspace list`
  and pick the **Everlife** workspace (shared team credits, never your personal ones).
- Creatify (images): the creatify-ad-agent plugin must be connected in Claude Code. If the preflight says it is missing,
  ask Mitansh for the plugin link; it is a one-time install.
- Creatify models (Nano Banana for image batches): paste this once, then type `/mcp`, pick **creatify** and approve the sign-in:
  `! claude mcp add --transport http --scope user creatify https://api.creatify.ai/mcp`
  (Step 2's install prompt already runs the add command for you; you only do the sign-in.)

Run step 2's preflight lines again until every line is ✅.

---

## Step 4. Make your first PT-141 batch (test run, about 4 credits)

In Claude Code, type: `make 4 PT-141 image ads`

Claude asks two short rounds of questions (form, hook angle, boldness, mood, how many). Pick the recommended answers
the first time. It then shows you a table of four ads to approve. Approving costs about 1 Creatify credit per image.

When it finishes it opens a contact sheet and tells you the folder:
`~/Everlife-Creative/output/PT-141/<date>_batch-<n>/` with `FINAL_*.png`, the raws and a `prompts.md`.

Everything is a draft: creative review first, then Jeremy's compliance sign-off, before anything goes live.

---

## What is different in version 2

- **PT-141 skill.** Nasal spray and sublingual tablet. Product-only premium statics (no people until the new people
  approach is approved). Copy comes only from the PT-141 bible page; every unflagged Tier A headline has now been used
  once, so new headlines need Jeremy.
- **Logo at the top** of every static, 311 px wide, dark on light scenes and cream on dark ones.
- **Proof footer inside the Reels safe area.** On 9:16 it now ends at 72% of the frame (y 1385) instead of the bottom
  edge, because the bottom of a Reel sits under Meta's button and caption. The image prompt keeps the product and
  headline in the top half; if a generation comes back too low, the finisher shifts it up, and if that is not enough
  it refuses and tells you to re-roll or do one reposition edit (1 credit).
- **Type and colour vary per ad.** No more same serif and purple accent five times in a row.
- **Shared tools read each product's product.json.** The disclaimer, renders and names come from the skill, so the
  tools never mix products up.

---

## If something goes wrong

- Paste the exact error into Claude Code and ask it to explain and fix it. It will not spend credits unless you approve a generation.
- To go back to version 1: your old skills are in `~/.claude/skills-backup/`. Ask Claude: "put my backed-up Everlife skills back".
- Anything else: message Mitansh with a screenshot.
