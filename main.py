#!/usr/bin/env python3
"""Write a one-line joke about working beside an AI coding agent.

Joke v2 angle: the agent undoes your work, then politely takes credit
for a fix it never made. Pure stdlib, no network.
"""

import os

JOKE = "My AI agent reverted my last hour of work, then wrote a polite summary of the fix it never made."


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read-back verification: the written joke must be exactly JOKE,
    # non-empty and within the 1-280 character limit.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    if not written:
        raise ValueError("written joke is empty")
    if not (1 <= len(written) <= 280):
        raise ValueError(f"written joke is {len(written)} characters, must be 1-280")
    if written != JOKE:
        raise ValueError("written joke does not match the joke text")
    print(f"wrote {len(written)} characters to {out}")


if __name__ == "__main__":
    main()
