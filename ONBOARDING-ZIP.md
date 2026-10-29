# Everlife ad factory: Day 1 guide (zip version)

Use this guide if you received the ad tools as a **zip file** (for example `everlife-ad-factory_2026-10-29_abc1234.zip`).
You do not need a GitHub account, git, Python or the command line: Claude Code does the technical steps for you.

Allow about 40 minutes. Nothing in steps 1 to 4 spends credits.

**A Mac is required.** The tools don't run on Windows yet: talk to Mitansh first if you only have a Windows PC.

The zip contains Everlife's creative bible and compliance rules. Keep it to yourself: don't forward or upload it.

---

## Step 1. Before you start (someone sends you two things)

1. **The zip file**, from Priestley or Mitansh.
2. **The Everlife logins** for Higgsfield (videos) and Creatify (images). These are shared team accounts: ask Mitansh.
   Never use a personal account; the team credits are shared and tracked.

You also need **Claude Code** installed and signed in with your Everlife account. If you don't have it yet, ask Mitansh
for the install link.

---

## Step 2. Unzip it in the right place (2 minutes)

1. Double-click the zip in your Downloads folder. A folder called **everlife-ad-factory** appears.
2. Move that folder into your **home folder** (in Finder: Go → Home, or press Shift-Command-H), so it sits at
   `~/everlife-ad-factory`. It must stay there: the tools look for it in that exact place.

Don't rename the folder or move files around inside it.

---

## Step 3. Let Claude set everything up (about 20 minutes)

1. Open Claude Code.
2. Paste this whole box, press Enter, and say **yes** when it asks for permission to run commands.

```
Please set up the Everlife ad factory on this Mac for me. I am not technical: do every step yourself, explain what you
are doing in one plain sentence per step, and only stop when you need me to click something. Do not spend any credits.

1. Check that the folder ~/everlife-ad-factory exists and contains install.sh. If it is somewhere else (for example
   still in Downloads), tell me and help me move it to my home folder.
2. Apple developer tools: run "xcode-select -p". If they are missing, run "xcode-select --install", tell me to click
   Install in the window that opens, and wait until I say it has finished.
3. Install it: run "bash ~/everlife-ad-factory/core/scripts/update.sh". It links the product skills, adds the Everlife
   creative rules to Claude Code, installs the finishing toolkit and checks every product. It can take a few minutes.
4. Creatify plugin (makes the image ads): run
   "claude plugin marketplace add creatify-ai/creatify-ad-agent-skill" and then
   "claude plugin install creatify-ad-agent@creatify-ad-agent". If either says it already exists, that is fine.
5. Creatify image models (Nano Banana, picked per image batch): run
   "claude mcp add --transport http --scope user creatify https://api.creatify.ai/mcp".
   If it says the server already exists, that is fine.
6. Higgsfield (makes the video ads): if the "higgsfield" command is missing, install it with
   "curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh".
7. Show me every ❌ line from step 3 and tell me in plain words what I need to do. The only things I should have to do
   myself are the sign-ins in Step 4 of the guide.
```

3. When it finishes, **quit Claude Code and open it again**. That loads the new skills and the Everlife rules. If Claude
   asks whether to allow the files the rules point to, say yes.

---

## Step 4. Sign in to Higgsfield and Creatify (5 minutes)

Type each line below into the Claude Code chat yourself. The `!` at the start runs it on your Mac. Use the shared
Everlife logins from Step 1.

- `! higgsfield auth login`: a browser opens, sign in.
- `! higgsfield workspace list`: then tell Claude "select the Everlife workspace". It must say **Everlife**, never Private.
- Type `/mcp`, pick **creatify-ad-agent**, and sign in with the Everlife Creatify account.
- Still in `/mcp`, pick **creatify** (the image models server: Nano Banana) and sign in with the same Everlife Creatify
  account. Same credits; GPT Image 2.5 stays the default, so you only need this when you pick Nano Banana.

Then type: `check my Everlife ad setup`. Claude re-runs the checks. Repeat until every line is ✅.

---

## Step 5. Your first ads (test run, about 4 credits)

Type: `make 4 Restora-Z image ads`

Claude asks one or two short rounds of questions. Pick the options marked **Recommended** the first time. It then shows
you the ads it plans to make and the cost, and waits for your OK. Nothing is spent until you approve.

When it finishes it opens a contact sheet and tells you the folder. Every finished ad is saved in
`~/Everlife-Creative/output/<Product>/`. Your ads live there, not in the zip folder, so updates never touch them.

**Everything is a draft.** Creative review comes first, then Jeremy's compliance sign-off, before anything goes live.

---

## Getting a new version

When Mitansh sends a new zip:

1. Quit Claude Code.
2. Delete the old `everlife-ad-factory` folder from your home folder (your finished ads are elsewhere and stay safe).
3. Unzip the new zip and move the new `everlife-ad-factory` folder into your home folder, exactly like Step 2.
4. Open Claude Code and type `update my ad tools`. It re-links everything and runs the checks.
5. Quit Claude Code and open it again.

To see which version you have, type `which version of the ad tools do I have?` (it reads the VERSION file).

---

## What to type (cheat sheet)

| You want | Type |
|---|---|
| Image ads | `make 4 Restora-Z image ads` · `make Sermorelin GHK image ads for women` · `make PT-141 image ads` |
| A video ad | `make a Sermorelin GHK video for men` · `make a Restora-Z video` |
| Other products | `make BPC-157 image ads` · `make plain Sermorelin image ads` |
| A setup check | `check my Everlife ad setup` |
| After a new zip | `update my ad tools` |
| Your credits | `how many Creatify and Higgsfield credits are left?` |
| Something broke | paste the error and ask `what does this mean and how do I fix it?` |

Products with a skill today: **Restora-Z, Sermorelin GHK, plain Sermorelin, PT-141, BPC-157.** "Sermorelin" alone is
ambiguous: say "Sermorelin GHK" or "plain Sermorelin".

---

## Good to know

- **Credits are shared team money.** Claude always shows the cost and waits for your OK before generating. Image ads are
  about 1 credit each; a 15-second video is about 75.
- **Claims come only from the creative bible.** The skills will not invent claims, and they stop and tell you when a
  brief asks for something the rules don't allow. That's working as intended: ask Jeremy if you think the rule is wrong.
- **Don't edit the files in ~/everlife-ad-factory.** A new zip replaces the whole folder, so any edit is lost. If something
  should change, tell Mitansh or Priestley.

## Who to ask

- Tools, setup, errors, new versions: **Mitansh**
- Compliance (claims, disclaimers, "can we say this?"): **Jeremy**
- The zip and the logins: **Priestley** or **Mitansh**
