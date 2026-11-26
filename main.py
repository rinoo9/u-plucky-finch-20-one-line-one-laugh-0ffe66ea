#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes exactly one funny line (<= 200 characters) to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.

Craft notes: the first line worked through appliance revenge — the
smart speaker leaked a secret, so the toaster burns toast on purpose.
The new line works through appliance gossip instead: the fridge started
a podcast about the human's midnight snacking, and the sting is the
last clause — it already has more listeners than the human's band.
The appliances are not just rebelling, they are building an audience
out of the human's shame, and the human's own creative work loses to
a fridge. 103 characters, under the 200-char limit.
"""

import os

LINE = "My fridge started a podcast about my midnight snacking, and it already has more listeners than my band."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
