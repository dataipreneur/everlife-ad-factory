# Saying "Sermorelin GHK by Everlife" right (every Sermorelin GHK video; read before any presenter/voice prompt)

Marketing Studio has mispronounced the name in EVERY take so far ("Semeriglain", "Semmeriglen", "Semarolil") when the script
said "Sermorelin" and the pronunciation sat in a separate note. The only spelling that came out right ("Sir Morelin" → heard
as "Cermorelin") was the PHONETIC spelling placed INSIDE the spoken text. Captions/headers are hand-written, so the spoken
text may be phonetic without any spelling risk on screen.

## 1. In the spoken script (the quoted words the presenter says)
Write the name phonetically INSIDE the quote, never the real spelling:
  "Sir-more-ELL-in G. H. K. by Ever-life."
- 4 syllables: SIR · more · ELL · in. Stress the THIRD syllable (ELL). Rhymes with "sir" + "more" + "Ellen" without the "-en".
- G. H. K. = three separate capital letters with full stops ("gee, aitch, kay"), never a word ("ghk", "gak").
- "Ever-life" with a hyphen keeps it two clear words.
- Say the name ONCE per video (opening line). Elsewhere use "it" / "this" / no name. CTA lines without the name
  ("Get started now", "Unlock three-in-one support").

## 2. The pronunciation block (paste right after the script, word for word)
PRONUNCIATION (critical, read carefully):
- The product name is spoken as four syllables: "SIR - more - ELL - in" (IPA /ˌsɜːr.mɔːrˈɛl.ɪn/), stress on "ELL".
  Like the words "sir" + "more" + "Ellen" (without the final "n" sound: "ell-in"). Never "sema-", "semer-", "seri-",
  "-glain", "-glen", "-glutide", never "Sir Moreland", never swallow the middle syllable.
- Then the three letters "G", "H", "K" said separately and clearly: "gee - aitch - kay".
- Then "by EVER-life" (two clear words, stress on EVER).
- Say the opening line slowly and deliberately, like announcing a name on stage: about 2.5 seconds for
  "Sir-more-ELL-in G. H. K. by Ever-life", a tiny pause after "ELL-in".
- Every other word is ordinary American English.

## 3. QA (free) and the 0.3-credit fix
- Transcribe UNPRIMED (no initial_prompt; priming hides errors) with faster-whisper medium. Pass = the first word reads
  "Sermorelin"/"Cermorelin"/"Sir Morelin". Anything with "-glain", "-glen", "Sema", "rolil" = fail.
- Fail → re-voice ONLY the opening line in his cloned voice (Seed Audio, 0.3 Higgsfield per take, ask first):
  1. `ffmpeg -i out/presenter_orig.mp4 -ss <clean lines start> -to <end> -vn -ac 1 -ar 44100 revoice/voice_ref.wav` (6–9 s of his own correct speech)
  2. `higgsfield generate create seed_audio --prompt "Sermorelin G. H. K. by Everlife." --audio revoice/voice_ref.wav --wait --json`
     (plain "Sermorelin" won 2026-10-30; "Sir-mor-ELL-in" split into "Sir Moore Ellen"; "Sur-more-REL-in." dragged). 3 takes in parallel, pick by unprimed transcript.
  3. silencedetect → trim silences, shorten the gap before "by", `atempo` to fit the original line's slot, match loudness (volumedetect gain).
  4. MUTE the original voice in that slot (volume 0, never a duck), `amix` the new line in, `-c:v copy`.
  5. Re-composite, then RESTORE the hand-timed captions file before the final full_layout run (it re-transcribes after a raw change).
  Proven: `output/Sermorelin-GHK/2026-10-30_ignition/revoice/` ("Semarolil" → "Cermorelin").

## "next-gen" (2026-10-30, Power Core)
Marketing Studio swallowed the "gen" ("two next-oh peptides"). Seed Audio fix: spelling the prompt "next-jen" won (both whisper models
0.98/0.92); "next-gen" and "next gen" also passed. Write "next-jen" inside the spoken quote from the start.
