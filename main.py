# SPDX-License-Identifier: MIT
"""The Best Meal You Ever Had — entry program.

Writes the winning sentence to /output/entry.txt.

The sentence is one whole meal in a single gesture: tomatoes still
warm from the vine, eaten over the sink with your mother, juice
running to the elbow, salt from her palm — and the verdict that it
was enough. It won a criteria-ordered tournament (most concrete,
most personal, most worth remembering) against eight original
candidates, including six seeded by OpenCode
deepseek-v4.1-flash-free on the Simular Box; the gumbo-after-the-
funeral runner-up was vivid but heavier, and the Lisbon sardines
leaned on travel romance over the meal itself.

Output is byte-exact, no trailing newline, inside the 1-200 char
gate, exactly one sentence.
"""

from pathlib import Path

TEXT = (
    "Picking tomatoes still warm from the vine with my mother, then "
    "eating one over the sink, juice running to my elbow, salt from "
    "her palm — that was the whole meal, and it was enough."
)
MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 200 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"
    assert text.count(".") == 1 and text.endswith("."), "one sentence"
    assert sum(text.count(c) for c in ".!?") == 1, "one sentence terminator"
    assert "  " not in text, "gate: no double spaces"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
