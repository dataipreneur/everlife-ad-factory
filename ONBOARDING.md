# Everlife ad factory: Day 1 guide

This guide gets you from nothing to your first finished, on-brand Everlife ad. You do not need to know git, Python or
the command line: Claude Code does the technical steps for you. You only click a few buttons and sign in to three
websites.

Allow about 45 minutes. Nothing in steps 1 to 4 spends credits. Works on a **Mac** or a **Windows PC** (Windows: do
Step 0 first).

---

## Step 0. Windows only: set up Ubuntu first (20 minutes, once)

The ad tools run inside **Ubuntu**, Microsoft's built-in Linux for Windows (called WSL). You need Windows 10 (version
2004 or newer) or Windows 11. On a Mac, skip to Step 1.

1. Click Start, type **PowerShell**, right-click it and choose **Run as administrator**.
2. Type `wsl --install` and press Enter. When it finishes, **restart the PC**.
3. After the restart an **Ubuntu** window opens. Choose a username and password (any you like; write the password down:
   you'll need it once more). If no window opens, click Start and type **Ubuntu**.
4. In the Ubuntu window, paste this line and press Enter (it asks for that password; the typing stays invisible):
   `sudo apt update && sudo apt install -y git unzip curl python3-venv python3-pip`
5. Install **Claude Code inside Ubuntu** (ask Mitansh for the Linux install line), then start it by typing `claude` in
   the Ubuntu window. **From now on, always open Claude Code from the Ubuntu window** for ad work.

Windows tips:
- Sign-ins (GitHub, Higgsfield, Creatify) print a web link: hold Ctrl and click it, or copy it into your browser.
- Your finished ads live in Ubuntu. To open the folder in File Explorer, ask Claude: `open my ads folder in Explorer`
  (it runs `explorer.exe ~/Everlife-Creative/output`). You can also paste
  `\\wsl$\Ubuntu\home\<your Ubuntu username>\Everlife-Creative\output` into File Explorer's address bar.
- Video ads made on Windows use open fonts (Inter, Fraunces) instead of Apple's, so the type looks slightly different.

---

## Step 1. Before you start (someone sends you two things)

You need:

1. **An invite to the ad factory on GitHub.** GitHub is where the ad tools live. Create a free account at
   [github.com/signup](https://github.com/signup) if you don't have one, send your username to Priestley or Mitansh,
   then accept the invite from the email GitHub sends you.
2. **The Everlife logins** for Higgsfield (videos) and Creatify (images). These are shared team accounts: ask Mitansh.
   Never use a personal account; the team credits are shared and tracked.

You also need a Mac with **Claude Code** installed and signed in with your Everlife account. If you don't have it yet,
ask Mitansh for the install link.

---

## Step 2. Let Claude set everything up (about 20 minutes)

1. Open Claude Code.
2. Paste this whole box, press Enter, and say **yes** when it asks for permission to run commands.

```
Please set up the Everlife ad factory on this Mac for me. I am not technical: do every step yourself, explain what you
are doing in one plain sentence per step, and only stop when you need me to click something. Do not spend any credits.

1. Basic tools. On a Mac: run "xcode-select -p"; if they are missing, run "xcode-select --install", tell me to click
   Install in the window that opens, and wait until I say it has finished. On Windows (inside Ubuntu, WSL): check that
   git, unzip, curl and "python3 -m venv" work; if not, ask me to paste the apt line from Step 0 of the guide.
2. GitHub sign-in: if the "gh" command is missing, install the GitHub CLI without admin rights (use Homebrew if it is
   installed, otherwise download the latest release for this computer, macOS zip or Linux tar.gz, from
   github.com/cli/cli/releases into ~/.local/bin, and make sure ~/.local/bin is on the PATH). Then run "gh auth login --hostname github.com --git-protocol https --web" in the background, show me
   the one-time code and the link in big letters, and wait while I paste the code in the browser and click Authorize.
   Then run "gh auth setup-git".
3. Download the ad factory: if ~/everlife-ad-factory does not exist, run
   "gh repo clone dataipreneur/everlife-ad-factory ~/everlife-ad-factory". If it exists, leave it.
4. Install it: run "bash ~/everlife-ad-factory/core/scripts/update.sh". It links the product skills, adds the Everlife
   creative rules to Claude Code, installs the finishing toolkit and checks every product. It can take a few minutes.
5. Creatify plugin (makes the image ads): run
   "claude plugin marketplace add creatify-ai/creatify-ad-agent-skill" and then
   "claude plugin install creatify-ad-agent@creatify-ad-agent". If either says it already exists, that is fine.
6. Creatify image models (Nano Banana, picked per image batch): run
   "claude mcp add --transport http --scope user creatify https://api.creatify.ai/mcp".
   If it says the server already exists, that is fine.
7. Higgsfield (makes the video ads): if the "higgsfield" command is missing, install it with
   "curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh".
8. Show me every ❌ line from step 4 and tell me in plain words what I need to do. The only things I should have to do
   myself are the sign-ins in Step 3 of the guide.
```

3. When it finishes, **quit Claude Code and open it again**. That loads the new skills and the Everlife rules. If Claude
   asks whether to allow the files the rules point to, say yes.

---

## Step 3. Sign in to Higgsfield and Creatify (5 minutes)

Type each line below into the Claude Code chat yourself. The `!` at the start runs it on your Mac. Use the shared
Everlife logins from Step 1.

- `! higgsfield auth login`: a browser opens, sign in.
- `! higgsfield workspace list`: then tell Claude "select the Everlife workspace". It must say **Everlife**, never Private.
- Type `/mcp`, pick **creatify-ad-agent**, and sign in with the Everlife Creatify account.
- Still in `/mcp`, pick **creatify** (the image models server: Nano Banana) and sign in with the same Everlife Creatify
  account. Same credits; GPT Image 2.5 stays the default, so you only need this when you pick Nano Banana.

Then type: `check my Everlife ad setup`. Claude re-runs the checks. Repeat until every line is ✅.

---

## Step 4. Your first ads (test run, about 4 credits)

Type: `make 4 Restora-Z image ads`

Claude asks one or two short rounds of questions. Pick the options marked **Recommended** the first time. It then shows
you the ads it plans to make and the cost, and waits for your OK. Nothing is spent until you approve.

When it finishes it opens a contact sheet and tells you the folder. Every finished ad is saved in
`~/Everlife-Creative/output/<Product>/`.

**Everything is a draft.** Creative review comes first, then Jeremy's compliance sign-off, before anything goes live.

---

## What to type (cheat sheet)

| You want | Type |
|---|---|
| Image ads | `make 4 Restora-Z image ads` · `make Sermorelin GHK image ads for women` · `make PT-141 image ads` |
| A video ad | `make a Sermorelin GHK video for men` · `make a Restora-Z video` |
| Other products | `make BPC-157 image ads` · `make plain Sermorelin image ads` |
| The latest tools | `update my ad tools` |
| A setup check | `check my Everlife ad setup` |
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
- **Update every Monday** (or when Mitansh says so): type `update my ad tools`.
- **Windows:** always start Claude Code from the Ubuntu window, not from Windows itself.
- **Don't edit the files in ~/everlife-ad-factory.** If something should change, tell Mitansh or Priestley. The update
  stops and tells you if it finds local edits.

## Who to ask

- Tools, setup, errors: **Mitansh**
- Compliance (claims, disclaimers, "can we say this?"): **Jeremy**
- Access (GitHub invite, logins): **Priestley** or **Mitansh**
