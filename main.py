#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes one single sentence that could have replaced an entire
pointless meeting: the line that kills the meeting dead.
"""
import os

ENTRY = "This meeting could have been an email, but then nobody would have gotten to say 'let's circle back' out loud."
# One sentence, no setup: the line itself is the whole meeting, killed.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.write("\n")


if __name__ == "__main__":
    main()
