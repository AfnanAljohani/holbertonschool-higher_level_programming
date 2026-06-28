#!/usr/bin/python3
"""This module provides a function that prints a square.

The square is drawn using the '#' character.
"""


def print_square(size):
    """Print a square with the '#' character.

    Raises TypeError or ValueError for invalid size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
