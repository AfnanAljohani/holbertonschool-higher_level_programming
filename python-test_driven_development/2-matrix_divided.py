#!/usr/bin/python3
"""This module defines a matrix division function."""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements of matrix divided by div.

    matrix must be a list of lists of integers/floats with equal row sizes,
    and div must be a non-zero number. Results are rounded to 2 decimals.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(err)
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError(err)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(e / div, 2) for e in row] for row in matrix]
