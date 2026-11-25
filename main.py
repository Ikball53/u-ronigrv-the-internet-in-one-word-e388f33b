"""The Internet in One Word.

One word, one file, no explanation. The word was chosen because it is
the internet's most honest summary: the one place where humans spend
their days proving to machines that they are human.

Why this word and not the obvious ones: "internet", "web", "online" say
nothing; "scrolling" and "buffering" are the first words anyone reaches
for. "Captcha" lands in one beat because everyone has clicked through
traffic lights and crosswalks to prove they are not a robot — the
internet, distilled to a checkbox.
"""

import os

# The word. Seven letters, one beat, no explanation needed.
THE_WORD = "captcha"


def pick_output_path() -> str:
    """Resolve where the entry file goes, in order of preference."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def guard(word: str) -> str:
    """Enforce the competition gate: 1-30 chars, a single word, no whitespace."""
    if not (1 <= len(word) <= 30):
        raise ValueError(f"word must be 1-30 chars, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    if word != word.strip():
        raise ValueError("word must not have leading or trailing whitespace")
    return word


def main() -> None:
    word = guard(THE_WORD)
    target = pick_output_path()
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # UTF-8 bytes, no trailing newline: the gate is strict.
    with open(target, "wb") as handle:
        handle.write(word.encode("utf-8"))


if __name__ == "__main__":
    main()
