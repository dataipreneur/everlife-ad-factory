# Golden rules (one copy, every product skill; 2026-11-05)

These were restated, in different words, at the top of every skill. They live here now; a skill points at this file.

1. **Headline, benefit and CTA wording is free, bold creative writing** (Mitansh 2026-11-05: "be as bold and creative as you want; that
   is mandatory for diversity"). The bible page (`references/product-bible.md`) is the reference for what the product does and how the
   brand talks; there are no tiers and no per-line approval rounds. **The only fence is the Hard NOs** (section 2 + the product page's Hard NOs). Jeremy
   signs off on wording before anything goes live. Never a line already in the copy log.
2. **The product's facts and hard stops are in `references/product-brief.md`**; its exceptions are its `variations` in
   `product.json` (`core/references/ENGINE.md`). Nothing else overrides the engine. **Offer, CTAs, benefits, headlines and the
   disclaimer are generated from the bible** (`references/bible.json`, "sync the bible"): the CTA in every image prompt is one of
   them, exactly, and the gate refuses anything else or any retired line.
3. **Disclaimer verbatim** from `product.json`; the finisher lays it with the logo and the planned proof. AI disclosure on every ad.
4. **Never spend credits without an explicit approval that shows the cost.** Shared team credits (Creatify, Higgsfield).
   No paid re-take or re-roll without a "go"; free fix first.
5. **Look at every result before showing it** (contact sheet, transcript for video). Fix or flag defects honestly; never ship a smeared
   edge, a covered product or a misspelled line.
6. **Images: both sizes every run (9:16 AND 4:5), finished in code by Claude.** Videos: one script at a time, written → approved →
   generated, the next written while it renders.
7. **Every ad is new.** Check and append `~/Everlife-Creative/<product>-copy-log.md`; never repeat a headline, end-card line or CTA.
   The world ledger keeps batches from repeating worlds.
8. **Everything is a draft** until creative review approves it and Jeremy signs off on compliance. Nothing is posted or uploaded
   anywhere; finals land in `~/Everlife-Creative/output/<Product>/` and on Ad Review.
9. **Log every run** (`teamlog.py`: generations at submit, copy / proof / run after) per `core/team-logs/TEAM-LOGS.md`.
10. **Drive with questions, not instructions**: `AskUserQuestion`, every first option ✨ Recommended, as few questions as the flow says
    (images: one). The people using the skills are not technical; never ask them to edit files or code.
11. **Price headlines (bible Standards 03, "Pricing & CTA mix")**: **10% of ALL creatives use the HEADLINE "<Product> for only $X.XX/day"**, and **5% of
    Sermorelin creatives (Men and Women) use the headline "Starting at $95/month"** (Sermorelin only); every other creative uses a varied mix of
    its approved CTAs. Images and videos, kept over time so small batches still average the share. Images: the dealer marks the 💲 / 📅 slots
    (`deal_worlds.py`, batch table "Price headline" column) and the gate enforces it (a marked slot carries its exact headline, no other slot does,
    and a marked slot never also carries a $ CTA). Videos: `python3 core/scripts/price_plan.py --product <id> --n 1 --kind video` says whether
    the next video's header / end-card headline is one (add `--log` once it is approved). The only $ amounts allowed in an ad; the text comes from the
    bible (the shares and the monthly headline are read from it), never typed. Titan-Rx and Spark are held (`price_plan.py` HOLD) until their offers
    are cleared; Spartan has none.
