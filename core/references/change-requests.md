# Change requests log: who asked for what

Priestley, 2026-11-02: "Keep a record of changes he tells us to do, so that we know it was told to us by him."
One row per request, newest first: who asked, how it reached us, their words (verbatim where we have them), what changed, where.
Add a row in the same PR as the change. Bible edits still come only from the live bible (`bible-sync.md`); a request that changes
claims or disclaimers still needs Jeremy.

| Date | Asked by (via) | Request | What changed | Branch / PR |
|---|---|---|---|---|
| 2026-11-02 | Mitansh (NAD+ session) | No incoming-call screens, no Accept / Decline buttons, ever. | New Hard NO in `style-library/STYLES.md`; S15 forum post only, S09 no AirDrop card. | PR #24 |
| 2026-11-02 | Mitansh (PT-141 batch 11) | "Why the hell are these things blurry on the edges! Who told you to do that!" · "make sure to do it always" · "show me first!" | `reposition_916.py` banned; `mirror_fit_916.py` first for any raw that runs into the footer; show every result before any re-roll. | PR #24 |
| 2026-11-02 | Mitansh (after PT-141 batches 8–10) | "It still feels like we're lacking a lot of variety… This batch is still feeling pretty flat and similar." Make the Drive style folder "a reference for all the product skills… in the core". | 15-style library in the core; "Surprise me" first in every skill's Mood question. | PR #24 |
| 2026-11-02 | Justin (forwarded by Mitansh) | "The disclaimer size is not fixed [in the ending of videos, for all the skills]. It always has to be 2 lines fixed." | Video endings (`full_layout.py`, `premium_finish.py`) use the shared standard: 18 px Inter Medium, exactly 2 lines, at the bottom. | `trust-callouts` |
| 2026-11-02 | Justin (forwarded by Mitansh) | "This banner here will always be the same size on every creative. And then the disclaimer is always the same size, ideally formatted to 2 lines and nested at bottom. Those 2 elements I really want to standardize." | New `core/tools/standard_footer.py`: trust row 990 px wide and the disclaimer at 18 px / 2 lines on every 1080-wide creative; used by `finish_batch.py`, `finish_modern.py`, `full_layout.py`, `premium_finish.py`. | `trust-callouts` |
| 2026-11-02 | Justin (bible v3, Standards 01 + 02 · 06; forwarded by Mitansh) | "Trust callouts (Trustpilot, doctor-prescribed, free shipping from pharmacy) go on 60% of graphics, not every one. 'Over 100,000 happy customers' goes on 40%." Reason: graphics "looking a little too cluttered". | Bible synced to 1793650290-a4dd; `finish_batch.py --proof trust/count` + `--proof-plan N`; one proof element per image ad; rules, gates and 11 skills' `image-batch.md`. | `trust-callouts` |
