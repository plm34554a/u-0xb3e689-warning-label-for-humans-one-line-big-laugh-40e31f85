#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label that should come printed on
every human being to /output/entry.txt (or $MAKEFUN_OUTPUT /
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard library only.
"""

import os

LINE = (
    "WARNING: This unit overestimates its own competence, "
    "disregards all instructions, and will confidently explain "
    "things it does not understand."
)


def output_path() -> str:
    """Resolve where the entry goes, honouring the harness env vars."""
    explicit = os.environ.get("MAKEFUN_OUTPUT")
    if explicit:
        return explicit
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(LINE)}")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
