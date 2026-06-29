#!/usr/bin/python3
"""This module defines a function that prints a square."""


def print_square(size):
    """Print a square of size x size using the '#' character.

    size must be a non-negative integer, otherwise a TypeError or
    ValueError is raised.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
