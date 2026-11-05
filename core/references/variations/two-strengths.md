# Variation: two-strengths (products sold in more than one strength)

Products: Sermorelin GHK (500 mcg · 1000 mcg), Sermorelin (500 mcg · 1000 mcg). `product.json` → `strengths` lists each with its
bottle render and label; `renders.bottle` is the default.

- **The image question gains one item: Strength** — "Either (Recommended): the strength is never mentioned, default bottle" /
  "500 mcg" / "1000 mcg". One strength per ad; "Either" ads never state a number.
- The prompt attaches **that strength's bottle render** (`strengths.<id>.bottle`); the label on the render is the only place the
  strength appears unless the copy names it on purpose.
- **"Double Strength"** is wording for the 1000 mcg bottle only (Sermorelin GHK 1000, Sermorelin 1000): on screen with the 1000 mcg
  bottle in frame, never on a 500 mcg or "Either" ad (Mitansh 2026-10-30, flagged for Jeremy's sign-off like all wording).
- Renders gate: if the chosen strength's bottle file is missing from `assets/`, stop before generating and say which file is needed.
- Videos: unchanged (their own setup still asks the strength).
