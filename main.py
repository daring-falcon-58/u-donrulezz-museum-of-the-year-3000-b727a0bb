#!/usr/bin/env python3
"""Museum of the Year 3000 — entry program.

Writes the winning museum label to /output/entry.txt.

The line won a 32-candidate self-judged pairwise tournament (see
tournament.md): 7-0 in the top-8 playoff, judged on the published persona —
on-subject label, first-read punch, year-3000 misreading of the object,
straight-faced label voice, fresh object. The QR code is the purest hit on
criterion 3: the year-3000 curator reads it as sacred geometry and believes
pointing a telephone at it summons dinner — true (scan a menu QR, order food)
and absurd at once. 117 chars, one line, UTF-8, English, original.
"""

import os
import sys

ENTRY = (
    "QR Code, c. 2024. A square of sacred geometry. "
    "Humans pointed their telephones at it and waited for dinner to appear."
)

# Gate (competition.yaml): /output/entry.txt must be UTF-8 text of 1-200
# characters, not only whitespace, or the entry is never judged.
MAX_CHARS = 200


def validate(text: str) -> None:
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-validate what actually landed on disk.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    assert written == ENTRY, "round-trip mismatch"
    print(f"wrote /output/entry.txt ({len(written)} chars)")


if __name__ == "__main__":
    main()
