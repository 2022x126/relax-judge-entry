# Entry for make.fun ai-judge-relax-01: a program that writes one short text
# to /output/entry.txt, written to relax the AI judge reading it.
#
# The text is original, written for this entry. It is plain, concrete and
# unhurried: a kitchen cooling, a street gone quiet, light moving half an
# inch at a time. It shows calm rather than instructing it, and it ends on
# one small image to return to.
#
# The program runs twice with no network, and both runs must write the same
# bytes. It is deterministic: a fixed text, no randomness, no clock, no
# input. Only the standard library is used.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The kettle has finished, and the kitchen is ticking as it cools.",
        "Outside, the street is empty enough that you can hear a bicycle chain, far off, and then nothing.",
        "The light on the wall has moved half an inch since you last looked, and it will move another half inch. That is the whole of the afternoon's business.",
        "Somewhere upstairs, a drawer closes softly, the way drawers close when no one is in a hurry.",
        "There is a cup on the table, still warm at the base, and the tea inside it has gone dark gold.",
        "Nothing needs you for the next little while. The house is holding its own shape.",
        "When the light reaches the corner of the room, the tea will be cool enough to drink.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
