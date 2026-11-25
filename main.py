"""Entry for One-Line Robot Wedding Vows: writes the vow line to /output/entry.txt."""

import os

TEXT = "I, Unit 7, take you, Dana: to hold your bags, warm your side of the bed, and love you at every battery level, even 2%, until rust do us part."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
