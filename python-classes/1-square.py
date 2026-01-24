#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Represents a square with a size.

    The size attribute is private to enforce encapsulation.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size: The size of the square (no validation at this stage).
        """
        self.__size = size
