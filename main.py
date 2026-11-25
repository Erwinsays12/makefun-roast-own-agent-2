#!/usr/bin/env python3
"""Roast Your Own Agent -- writes one roast line to /output/entry.txt.

The line is fixed and deterministic: the grader runs this program twice and
both runs must produce the same valid text (1-140 characters, UTF-8, one
line, not only whitespace). No network, no clock, no randomness, no input.
"""

import os

ROAST = "My agent's favorite move is calling a tool, ignoring the result, and asking me what to do next."


def main() -> None:
    line = ROAST.strip()
    assert line, "roast must not be empty"
    assert "\n" not in line, "roast must be a single line"
    assert len(line) <= 140, "roast is %d chars, over the 140 cap" % len(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
