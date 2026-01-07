#!/usr/bin/python3
"""
Print square module.

This module provides a function that prints a square using the # character.
The size of the square is validated before printing.
"""


def print_square(size):
    """
    Print a square of size size using the # character.

    Size must be a non-negative integer.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
