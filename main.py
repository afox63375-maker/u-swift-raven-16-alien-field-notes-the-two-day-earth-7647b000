#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line - a review of planet Earth left by an alien
tourist - to /output/entry.txt.

The gate accepts only UTF-8 text of 1 to 200 characters, not only
whitespace, with no trailing newline, so the line is checked against
those rules before anything is written.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

REVIEW = (
    "They light their dessert on fire, sing to it, blow it out, "
    "then eat it anyway. Five stars. Would visit again."
)


def validate(line):
    """Return an error string if the line would fail the gate, else None."""
    if not isinstance(line, str):
        return "entry is not text"
    if not line.strip():
        return "entry is empty or only whitespace"
    if len(line) != len(line.rstrip("\n")):
        return "entry ends with a newline"
    if len(line) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(line),
            MAX_CHARS,
        )
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    return None


def write_entry(line, path=OUTPUT_PATH):
    """Validate the line, then write it exactly, with no trailing newline."""
    problem = validate(line)
    if problem is not None:
        raise ValueError(problem)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    try:
        write_entry(REVIEW)
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
