#!/usr/bin/python3
"""Define a square class"""


class Square:
    """
    Represents a Square class
    """
    def __init__(self, size=0):
        """
        Insitializes a new Square

        :param size (int): its the size of the square, and the Default is 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size