---
name: everlife-ads
description: The front door to the Everlife ad factory for the creative team. Use whenever someone wants ads but doesn't name a product, or says "make ads", "new batch", "what should I make today", "let's make some statics", "start", "help me make something", "I'm new, where do I start", or names a product the product skills don't cover. Asks ONE question (which product, with a recommendation), then hands over to that product's everlife-* skill, which runs the shared engine (core/references/image-flow.md). Not for videos of a named product (go straight to that skill).
---

# Everlife ads: start here

You are talking to a designer on the creative team. Assume they know nothing about skills, files, credits or rules. **You do
the heavy lifting; they answer one question and get a folder of finished ads.** Never ask them to edit files or run commands.

## 1. One question
`AskUserQuestion`, one question: **"Which product are we making ads for today?"** Options (first = ✨ Recommended), built like this:
1. The product that needs ads most: the one with the fewest finished ads on Ad Review in the last 7 days, or the one with the
   most reviewer flags to fix (`teamlog.py summary --product <id>` per product; skip the step silently if the pages are unreachable).
   Label "✨ <Product> (Recommended): <why in six words>".
2. Two more products the team hasn't touched this week.
3. "Something else" (they type the product; match it to a skill; if none exists, say so in one line and offer `everlife-new-product`).
Product skills: Restora-Z, Sermorelin, Sermorelin GHK, BPC-157, Wolverine Stack, Spartan Stack, PT-141, Lovara, Spark, Titan-Rx,
GLP-1, NAD+, MOTS-c, Epithalon, GHK Peptide Cream.

## 2. Hand over
Invoke that product's skill (`everlife-<id>`) and let it run: it does the preflight, the single image question (how many ·
direction with 🎲 Surprise me first and three inspirations · who's in them, with men / women / mix only for products made for both ·
form or strength if the product has several), the deal, the
prompts, both sizes, finishing, QA, the contact sheet, the logs. The designer's only other click is "Generate all N (≈ cost)".

## 3. Plain words, always
- Say what will happen before it happens, in one line ("I'll make 8 PT-141 ads in both sizes, about 16 credits; you'll see them
  all on one sheet in ~6 minutes").
- Show credits as a number, never a formula. Show results as a picture (the contact sheet), never as a file list.
- When something fails, say what you'll do about it, not what went wrong technically ("Two came back with text too small; I'm
  re-making those two, no extra cost beyond the batch").
- Finish with the folder opened on their screen (`open <folder>`; Windows: `explorer.exe`) and one line: what's in it, what's
  next ("Another 8 with new worlds?", "Variations of #3?"). Nothing is posted anywhere; review and Jeremy's sign-off still come first.
