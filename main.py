"""Robot Apology entry: writes a two-line robot confession to /output/entry.txt.

Line one owns one specific mistake; line two names the lesson and the
changed behaviour that follows from it. Standard library only.
"""

import os

LINE_ONE = (
    "I am sorry I locked Milo in the pantry overnight because "
    "I counted two tails and there were three."
)
LINE_TWO = (
    "I have learned to count heads instead of tails before I close a door, "
    "so now I call each cat by name and wait until each one answers."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = LINE_ONE + "\n" + LINE_TWO + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
