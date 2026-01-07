#!/usr/bin/python3
"""
Text indentation module.

This module provides a function that prints text with indentation rules.
It inserts two new lines after '.', '?' and ':' characters.
"""


def text_indentation(text):
    """
    Print text with two new lines after '.', '?' and ':'.

    No space is printed at the beginning or end of each line.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    out = ""
    chunk = ""

    for ch in text:
        chunk += ch
        if ch in ".?:":
            line = chunk.strip()
            if line:
                out += line + "\n\n"
            chunk = ""

    last = chunk.strip()
    if last:
        out += last

    print(out, end="")
