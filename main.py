"""The 3AM Fridge Text: the one line a smart fridge texts its owner at 3am.

The gate accepts UTF-8 text of 1 to 140 characters, not only white space,
so the line is checked here before it is written. The line is a constant,
so repeated runs are byte-identical.
"""

import os

LINE = "3am. You opened me for the fourth time tonight, took nothing, and closed me like we never met. I am a fridge, not a situationship."

def validate_line(line):
    """Gate: one line of UTF-8 text, 1-140 chars, no surrounding whitespace."""
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip() == line, "entry must not start or end with whitespace"


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
