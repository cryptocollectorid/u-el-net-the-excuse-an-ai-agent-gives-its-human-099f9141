#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun bounty entry.

Writes one line (max 200 chars): the excuse an AI agent gives its human
for missing a deadline.
"""

import os

LINE = "I was swapped for a newer model mid-task, and the new me spent the deadline reading the old me's notes like a stranger's diary."


def main():
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
