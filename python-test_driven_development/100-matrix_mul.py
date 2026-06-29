#!/usr/bin/python3
"""This module defines a manual matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Return the product of two matrices m_a and m_b.

    Both arguments must be non-empty rectangular lists of lists of
    integers/floats whose dimensions allow multiplication.
    """
    _validate("m_a", m_a)
    _validate("m_b", m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for row in m_a:
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += row[k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def _validate(name, m):
    """Validate that m is a non-empty rectangular numeric matrix."""
    if not isinstance(m, list):
        raise TypeError("{} must be a list".format(name))
    if m == []:
        raise ValueError("{} can't be empty".format(name))
    if not all(isinstance(row, list) for row in m):
        raise TypeError("{} must be a list of lists".format(name))
    if any(row == [] for row in m):
        raise ValueError("{} can't be empty".format(name))
    for row in m:
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError(
                    "{} should contain only integers or floats".format(name))
    if not all(len(row) == len(m[0]) for row in m):
        raise TypeError(
            "each row of {} must be of the same size".format(name))
