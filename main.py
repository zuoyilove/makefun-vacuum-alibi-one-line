#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes the robot vacuum's excuse for missing a spot to /output/entry.txt.
Deterministic: the same line every run, no input, no network.
"""

import os

LINE = (
    "I skipped that spot because my map says it is a lake. "
    "It is carpet. I stand by my map."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
