# The Mood question: same for every product skill (Mitansh, 2026-11-02)

"These mood should be having all 15 options which the GDrive had, for all the product skills, and 1st should still be Surprise me,
which does random every time."

`AskUserQuestion` shows at most 4 options, so the Mood question is always:

1. **"🎲 Surprise me (Recommended)"**: a random style for every ad, different every batch. Description: "Picks a different one of the
   15 Drive styles for each ad, never the same set twice in a row."
2. **"📚 Pick from the 15 styles"**: opens the picker below.
3. **This product's own favourite mood** (the skill's existing first non-random mood, e.g. "✨ Ultra premium, product only").
4. **This product's second mood** (the skill's existing next mood). Any other mood the skill used to list stays reachable via "Other".

> **⛔ 💪 HARDCORE SHIRTLESS IS ALWAYS A VISIBLE OPTION (Mitansh, 2026-11-02: "WHy the fuck did Sermorelin skill didnt show
> "HARDCORE SHIRTLESS" Option man!???"):** for any product in `core/references/hardcore-men.json` whose audience includes men, the
> Mood question is: 1 **"💪 Hardcore shirtless (Recommended)"** (every men's slot HARDCORE per `hardcore-men.md`, H3–H11 refs,
> styles still drawn at random) · 2 "🎲 Surprise me" (random styles, 40% HARDCORE) · 3 "📚 Pick from the 15 styles" · 4 the
> product's own favourite mood. Never bury hardcore inside another option's description.

## 🎲 Surprise me
Run `python3 -I <skill-dir>/core/scripts/pick_styles.py --product <product id> --n <how many>` (add `--allow S12` only when the
product's `reviews.md` has screened reviews). It draws N different styles at random, skips styles used in this product's last two batches
(`~/Everlife-Creative/style-ledger.jsonl`), and prints one line per slot: code, name, board path. Use those as the slot
frameworks, Read each board before writing that slot's prompt, and show the style code in the batch table. After generating,
`pick_styles.py --log --product <id> --codes S02,S09,…` records the batch.
**Hardcore men (Jeremy, 2026-11-02):** always pass `--audience men|women|both`. For the products in
`core/references/hardcore-men.json` the picker tags 40% of the men's slots `HARDCORE`; write those slots per
`core/references/hardcore-men.md` (shirtless 40–45, flawless muscular condition, hard gym light) whatever the style is.

## 📚 Pick from the 15 styles: ONE AskUserQuestion, 4 questions, multiSelect, every option with its one-line look
- **Text-led:** Bold Headlines · Crossed Out Words · Reasons Why · Benefit Stacks
- **Compare:** Myth vs. Fact · Us vs. Them · What's Inside · Search
- **Phone & social:** Notes / Reminders · AMA (Ask Me Anything) · News · Phone Screen (forum post; never a call screen)
- **Out loud:** Testimonial (say "needs screened reviews" in its description when the product has none) · Whiteboard / Billboard · We're Sorry
The user may tick any number across the four. Fewer styles than ads → repeat with a different palette and product angle; more
styles than ads → take a random subset. Show "👀 boards" on request by Reading `boards/<code>_<slug>.jpg`.

## What the mood still controls
The style decides the LAYOUT. Palette, light and type still vary per ad under the skill's §2b rules and the product's colour rules
(women's creative: pinks, tans, beige; product colour may lead elsewhere). Every gate in `STYLES.md`, the product bible and the
global rules applies to every style.
