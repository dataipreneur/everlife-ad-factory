# Category 5 — Contrast & Comparison

Library folders: Comparison · Side-by-Side · Versus fighting · No More Needles (boards 2, 4, 5, 6).
What the library shows: "Switch Ambien for Restora-Z" two-bottle tables with ✓/✗ columns (Restora examples); "Ditch Ambien for Restora" review-style; split-face light/dark portraits; monster battles (Godzilla vs Kong), pill-vs-pill boxing; needles vs tablet.
Why it works: contrast makes the choice obvious in one glance. It is also the riskiest category for compliance, so read every guardrail.

---

## 5A — Restora-Z vs Ambien  🔒 GATED
- **Rule (bible):** comparisons run one direction only (switching from Ambien to Restora); use ONLY the approved Ambien claims ("Warns of next-day impairment", "Next-day drowsiness reported", "Morning grogginess", "Risk of complex sleep behaviors") or the cleared alternate sentences, and **Ambien's actual pill must be shown**.
- **Gate:** before offering 5A, check for `<skill>/assets/ambien_pill.png` (a real photo of the Ambien tablet supplied by the team). If it's missing, say: "Ambien comparisons need a real Ambien pill image on file (compliance rule). Want to drop one in, or pick another style?" Never generate an Ambien pill.
- **Layout:** `--layout compare` with `"compare_pills": ["<skill>/assets/rz_capsule.png", "<skill>/assets/ambien_pill.png"]` (both pills shown above their columns, which satisfies the "actual pill" rule), `compare_left` (Restora-Z column = bible benefits: "Non-narcotic", "Non-addictive", "3-in-1 sleep formula", "Doctor prescribed") and `compare_right` (Ambien column = approved Ambien claims only), `compare_titles` ["Restora-Z", "Ambien"].
- **Headline options (bible):** *A Non-Narcotic Alternative to Ambien* · *Still Groggy After Ambien? Meet Restora* · *Ambien Feeling Less Effective? Explore Restora.* · *Beyond Ambien: A 3-in-1 Sleep Formula* · *Ambien Not Working Like It Used To?* · *Ready for an Alternative to Ambien?*
- **Never:** "better than", "safer than", side effects not on the approved list, pill sharing.

## 5B — "Before another sleep fix" checklist
- **Looks like (library statics in the PMG Restora folder + Comparison):** a hand holding the bottle over a cosy bed, a ❌ ❌ ✅ list above it.
- **Copy:** ❌ items are generic categories, never brands ("Another gummy", "Random sleep hacks", "Counting sheep"); the ✅ item is "Restora-Z: 3-in-1, doctor prescribed".
- **Layout:** `--layout checklist` with `checklist` = [["x","Another gummy"],["x","Random sleep hacks"],["check","Restora-Z — 3-in-1, doctor prescribed"]].
- **Video version:** Seedance or Marketing Studio: a hand sweeps clutter off the nightstand (unlabelled props) and places the bottle; the checklist ticks in finishing (one caption per beat).

## 5C — Night / morning split
- **Looks like (Side-by-Side):** the same person or same room in two halves: left cool blue 3 a.m. (awake, restless), right warm sunrise (rested, coffee), the bottle bridging the seam.
- **Guardrail:** **not a body before/after.** Same clothes, same person, the difference is the *light and the activity*, never body shape, face "aging" or skin. If unsure, use the room only (no person) or two different moments of the day.
- **Layout:** `--layout split` (left = pain point, right = benefit) or plain `standard`.
- **Video:** a wipe transition from night to morning on a locked frame (Seedance).

## 5D — Versus battle
- **Looks like (Versus fighting):** an epic, playful battle: a giant "3 A.M. Thoughts" storm-cloud creature vs the glowing Restora-Z capsule hero; boxing-ring style "Night vs Rest" with a referee sheep.
- **Engine:** Seedance (3D / cinematic).
- **Guardrails:** the opponent is a *problem* (restlessness, racing thoughts), never a competitor product or brand; no violence against people; the capsule "wins" by calming, not by knock-out gore.
- **Finishing:** `house`.
- **Starter:** "Main event: Racing Thoughts vs Restora-Z": an announcer VO, the cloud monster shrinks to a puff under the capsule's glow, then the bedroom goes quiet.
