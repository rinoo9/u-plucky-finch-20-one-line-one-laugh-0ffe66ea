#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes exactly one funny line (<= 200 characters) to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.
"""

import os

LINE = "My smart speaker leaked my secret, so now my toaster burns my toast on purpose."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
