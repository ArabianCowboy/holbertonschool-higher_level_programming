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

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip())
