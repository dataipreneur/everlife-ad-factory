#!/usr/bin/env python3
"""The global Hard NOs a line of copy can be checked for mechanically (CLAUDE.md gates §2-3; bible Global Hard NOs).

One copy, imported by teamlog.py (copy pre-screen), build_product_bibles.py (auto screening of bible lines) and
core/hooks/batch_hook.py (the copy gate on image prompts). Entries: (regex, why, video_only).

    from hard_nos import check
    check("Get Started Now") -> [("\\bget started now\\b", 'why…')]
"""
import re

BANNED = [
    (r"\bget started now\b", "\"Get Started Now\" is banned as a CTA (bible 2026-11-03): lead with the offer", False),
    (r"\b(i|i'm|i've|i'd|i'll|me|my|mine|myself)\b", "first person is a Hard NO (\"I tried\", \"my results\")", False),
    (r"\bneedles?\b|needle-free", "never mention needles, including \"needle-free\"", False),
    (r"\bGH\b", "spell out \"growth hormone\", never \"GH\"", False),
    (r"ghk-cu|copper peptide", "creative says \"GHK\", never \"GHK-Cu\" / \"copper peptide\" (H2 product name only)", False),
    (r"\b(melt\w*|burn\w*|ripped|shred\w*)\b", "no melt / burn / ripped / shred", False),
    (r"body[- ]?composition", "never the phrase \"body composition\" anywhere: rewrite it (\"supports lean muscle\"; bible 2026-11-04)", False),
    (r"\b(fat|skinny)\b", "no \"fat\" or \"skinny\" claims anywhere (bible 2026-11-04)", False),
    (r"\barousal|aroused|arousing\b", "never \"arousal\" or any form of it", False),
    (r"\ball[- ]natural\b", "never \"all natural\" for a sublingual", False),
    (r"\bclinically (studied|backed|proven)\b", "\"clinically studied/backed\" only for a named ingredient", False),
    (r"\b(cure|cures|treats?|prevents?)\b", "no disease claims (cure / treat / prevent)", False),
    (r"trustpilot rating", "Trustpilot reads exactly \"Trustpilot rated 4.9 Excellent\"", False),
    (r"\bbreaking news\b", "no \"Breaking News\" framing", False),
    (r"\bsave\s+\d+\s*%(?!\s+compared)", "the offer reads \"Save Up to N%\" (with \"Up to\"; the product's % from its bible page)", False),
    (r"\b(after|over|past|at|turning|under)\s+\d{2}\b|\b\d{2}\s*(\+|plus|years?|yrs?)\b|\b(twenty|thirty|forty|fifty|sixty|seventy)(-\w+)?\b",
     "no specific ages in video scripts or captions (team video rules, 2026-11-03)", True),
]
WARN = [
    (r"\bare you\b", "second-person health question with a pronoun? (pronoun-free questions are fine)"),
    (r"\bbuilds\b", "say \"supports\", never \"builds\""),
    (r"\bboosts?\b", "\"boost\" reads as an outcome claim: prefer \"supports\""),
    (r"\bguarantee", "no guaranteed outcomes"),
]


def check(text, video=False, extra=()):
    """→ [(pattern, why)] for every banned pattern the text hits. `extra` = product patterns [(regex, why)] (bible-screen.json)."""
    hits, low = [], text.lower()
    for pat, why, video_only in BANNED:
        if video_only and not video:
            continue
        if re.search(pat, text if pat == r"\bGH\b" else low):
            hits.append((pat, why))
    for pat, why in extra:
        try:
            if re.search(pat, low, re.I):
                hits.append((pat, why))
        except re.error:
            hits.append((pat, f"bad pattern in bible-screen.json: {pat}"))
    return hits


def warnings(text):
    return [(pat, why) for pat, why in WARN if re.search(pat, text.lower())]
