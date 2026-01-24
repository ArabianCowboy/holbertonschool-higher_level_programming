#!/usr/bin/python3
"""
This module defines a Square class with size validation.
"""


class Square:
    """
    Represents a square defined by its size.

    The size is stored as a private attribute and validated on initialization.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (must be a non-negative integer).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
