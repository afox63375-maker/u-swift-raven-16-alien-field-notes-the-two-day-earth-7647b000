[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/afox63375-maker/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/afox63375-maker/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

# Alien Field Notes: The Two Day Earth Review

One line, written as a review of planet Earth by a visitor from
elsewhere. The tourist spent two days on Earth, watched the locals
celebrate a birthday, and filed this report.

## The entry

> They light their dessert on fire, sing to it, blow it out, then eat it anyway. Five stars. Would visit again.

## How it works

`main.py` uses only the Python standard library. Run it and it writes
exactly that one line to `/output/entry.txt` — plain UTF-8 text, no
trailing newline, well inside the 200-character limit. Before writing,
it validates the line against the gate: 1 to 200 characters, not only
whitespace, valid UTF-8, no trailing newline.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the review line.
- `prompt.txt` — the instruction this entry was built from.
- `LICENSE` — MIT.

Built for the [make.fun bounty](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000).
