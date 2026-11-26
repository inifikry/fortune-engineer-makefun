#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes one fortune cookie message for a software engineer
(a single line, at most 120 characters) to /output/entry.txt.
"""

import os

ENTRY = "Your code will pass every test on the first run. The tests, unfortunately, test nothing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
