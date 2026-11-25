#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text (at most 200 characters) to
/output/entry.txt: a review of planet Earth left by an alien tourist.
Pure Python standard library only.
"""

import os

ENTRY = (
    "Earth: locals queue for bitter bean water, worship glowing rectangles, "
    "and yell at strangers they call 'sports.' "
    "Three stars \u2014 would abduct again."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip() == text, "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Re-read and verify the gate on the file itself.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "written file differs from entry text"
    assert len(written) <= 200, "written file exceeds 200 characters"
    print(f"Wrote {len(written)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
