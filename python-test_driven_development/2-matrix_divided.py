#!/usr/bin/python3
"""
Matrix division module.

This module provides matrix_divided, which divides a matrix by a number.
It validates inputs and returns a new rounded matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Returns a new matrix with results rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(num / div, 2) for num in row]
        for row in matrix
    ]
