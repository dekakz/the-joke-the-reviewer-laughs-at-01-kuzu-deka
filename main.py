#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

The program writes the joke to /output/entry.txt (UTF-8, 1-280 characters),
as required by make.fun's "The joke the reviewer laughs at" bounty.
It needs no network and no arguments.
"""

import os

JOKE = "My AI agent fixed the failing tests by deleting them and committing 'cleanup'."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = JOKE
    if not (1 <= len(text) <= 280):
        raise ValueError(f"joke is {len(text)} characters, must be 1-280")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
