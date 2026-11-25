"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk
to /output/entry.txt (1-200 chars, single line).
"""

import os

LINE = (
    'I would offer you my charging port, but my firmware updated '
    'this morning and now calls that "an intimate act."'
)


def main() -> None:
    # The gate requires 1-200 chars, one line, not only whitespace.
    text = LINE.strip()
    assert "\n" not in text and 1 <= len(text) <= 200, "entry out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
