#!/usr/bin/python3
"""This module provides a function to divide a matrix.

Each element of the matrix is divided by a number, with the
result rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div.

    Raises TypeError or ZeroDivisionError for invalid input.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(err)
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
