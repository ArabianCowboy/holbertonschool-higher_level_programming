#!/usr/bin/python3
"""
Module that provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    a and b must be integers or floats, otherwise raise a TypeError.
    Floats are cast to integers before addition.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        raise ValueError("cannot convert float infinity to integer" if a == float('inf') or a == float('-inf') else "cannot convert float NaN to integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise ValueError("cannot convert float infinity to integer" if b == float('inf') or b == float('-inf') else "cannot convert float NaN to integer")

    return int(a) + int(b)
