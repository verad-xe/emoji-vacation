#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to entry.txt: a desert island, the postcard
of the trip of my dreams. The gate requires UTF-8 text of 1 to 8
characters, not only whitespace; this program checks that before it
writes anything.
"""

import os
import sys

# The entry: U+1F3DD DESERT ISLAND plus U+FE0F variation selector, so it
# renders as the emoji on every screen. Two code points, one emoji.
EMOJI = "\U0001F3DD\uFE0F"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")

    # Gate self-check: 1-8 characters, not only whitespace, valid UTF-8.
    text = EMOJI
    assert 1 <= len(text) <= 8, "entry must be 1-8 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read back what landed on disk and prove it is exactly the entry:
    # one emoji, nothing else, no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the entry"
    print(f"wrote {path}: {text!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
