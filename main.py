#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line office joke (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

Python 3 standard library only. No network. Deterministic: the same
line is written on every run.
"""

import os
import sys

# The selected line, chosen from eight candidates: a team-building
# escape room where the team escapes, the manager does not, and the
# last clause lands the laugh as a deadpan morale report.
ENTRY = (
    "Our team-building day was an escape room: we got out in nine "
    "minutes, the manager is still locked in there, and morale has "
    "never been higher."
)

MAX_CHARS = 200


def main() -> int:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(ENTRY), MAX_CHARS)
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")

    out_target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = (
        out_target
        if out_target.endswith(".txt")
        else os.path.join(out_target, "entry.txt")
    )
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Verify the gate on what was actually written: byte-identical to
    # the selected line, and the line itself inside 1-200 characters.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        raise ValueError("written entry does not match the selected line")
    if not 1 <= len(written.rstrip("\n")) <= MAX_CHARS:
        raise ValueError("written entry fails the 1-200 character gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
