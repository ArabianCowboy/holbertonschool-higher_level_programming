#!/usr/bin/python3
"""
Module that squares all values of a matrix
"""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with squared values."""
    return [[x ** 2 for x in row] for row in matrix]
