#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes exactly one funny line (<= 200 characters) to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.

Craft notes: round 1 worked through appliance revenge — the
smart speaker leaked a secret, so the toaster burns toast on purpose.
Round 2 worked through appliance gossip — the fridge started a
podcast about the human's midnight snacking. Round 3 leaves the
kitchen entirely and works through misread virtue: the smartwatch
praises the human for burning calories, but the "workout" was just
furiously deleting 3,000 unread emails. The sting is the last clause —
the health halo collapses into inbox rage, and the device's praise
is the joke. 111 characters, under the 200-char limit.
"""

import os

LINE = "My smartwatch congratulated me for burning 400 calories, but I was just furiously deleting 3,000 unread emails."


def main():
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"{LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
