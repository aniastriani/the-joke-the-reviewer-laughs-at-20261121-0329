"""Write one short joke about pair-programming with an AI coding agent.

The entry is a single line of plain text, saved as entry.txt inside the
output folder the harness provides. The text is fixed in this file so every
run produces exactly the same bytes.
"""

import os
import sys


JOKE = (
    "Working beside my AI coding agent means I never write bugs anymore "
    "\u2014 I just approve them, one 400-line diff at a time."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    text = JOKE.strip()
    encoded = text.encode("utf-8")
    if not 1 <= len(encoded) <= 280:
        print(f"entry must be 1-280 UTF-8 bytes, got {len(encoded)}", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    print(f"wrote {len(encoded)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
