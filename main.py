#!/usr/bin/env python3
"""One Word From Grandma — writes exactly one word to /output/entry.txt.

The word: grandma's first and last word at the table — a command and
a blessing in one syllable. It carries a whole kitchen of love and a
warning: sit down, you are too thin, there is more where that came from.
"""
import os

WORD = "Eat."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

if __name__ == "__main__":
    main()
