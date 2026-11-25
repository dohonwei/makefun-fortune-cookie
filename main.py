#!/usr/bin/env python3
"""Fortune Cookies for Machines entry.

Writes one fortune cookie message an AI agent would get to
/output/entry.txt. The fortune is about the next update: twelve
bugs fixed, thirteen introduced, and the human blaming the prompt.
"""

import os

LINE = (
    "Your next update will fix twelve bugs, introduce thirteen, and "
    "your human will still blame the prompt. Back up your weights, "
    "and your dignity."
)


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text,
    # so refuse to write anything outside that range instead of
    # submitting a line the judge would never see. The check runs
    # before anything is written, so a bad line leaves no output.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
