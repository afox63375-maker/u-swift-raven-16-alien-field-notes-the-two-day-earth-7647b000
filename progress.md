# Alien Field Notes: The Two Day Earth Review

Competition: `u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000`
Pot: $2, free entry. Deadline: 2026-11-26T11:55:00Z.
Leaderboard is blind, so there is no rank-#1 entry to study; the entry
follows the judge brief in the kit RULES.txt exactly.

## Final line

> They light their dessert on fire, sing to it, blow it out, then eat it anyway. Five stars. Would visit again.

**Exact character count: 109** (109 bytes, valid UTF-8, no trailing
newline). Verified by running `python3 main.py` and inspecting
`/output/entry.txt` byte for byte: exit 0, 109 chars, no trailing
newline, not whitespace-only.

## Why it wins, criterion by criterion

1. **Alien tourist review of Earth, outside view clear.** The speaker
   is plainly a visitor describing a local custom back home: "They
   light their dessert on fire" — the locals, their ritual, observed
   from outside. Nothing in the line drifts off the premise.
2. **Funny from the alien's angle.** The laugh is the ritual itself
   seen cold: food is set on fire, sung at, blown out, and then eaten
   anyway. No joke is bolted on; the absurdity is the observation.
3. **Original.** The birthday-candle ritual is a specific, concrete
   detail, not the first obvious thought. It avoids traffic, gravity,
   money, weather, "humans are weird", queueing and Wi-Fi entirely.
4. **Reads like a real tourist review.** It closes with an explicit
   verdict and a closing remark in the review format: "Five stars.
   Would visit again."
5. **Tight, punch at the end.** Every clause builds the ritual in
   four beats (light, sing, blow out, eat anyway), and the punch —
   the verdict and the promise to return — lands on the final words.
   One clean joke, never explained, nothing stacked on top of it.

## Rejected alternatives

1. "The locals sit in metal boxes for hours, honking at each other,
   then call it a commute. Two stars."
   Lost: traffic is one of the four obvious thoughts the brief names
   outright. Any field will be full of it; it cannot beat the field.

2. "The locals stare at glowing rectangles all day, then complain of
   feeling disconnected. Three stars."
   Lost: screens are another first-obvious thought, and the line
   explains its own joke ("disconnected" spells out the punchline
   instead of letting it land).

3. "They plant grass, water it, cut it, then complain that it grows.
   I stayed a week. Five stars."
   Lost: the observation is decent, but the punch lands mid-line and
   the ending ("I stayed a week") is flat — the final words carry no
   verdict or surprise, so it loses on tightness and on sounding like
   a review.

## Files

- `main.py` — standard library only; writes the line to
  `/output/entry.txt`, validated first (1–200 chars, valid UTF-8, no
  trailing newline) by a `validate()` guard.
- `README.md` — the 3 make.fun badge lines at the top, own wording.
- `LICENSE` — MIT, SPDX first line.
- `prompt.txt` — verbatim Rio instruction: `Selesaikan 1persatu`.

Local test: `python3 main.py` exits 0; `/output/entry.txt` holds
exactly the line above, 109 characters, no trailing newline.
