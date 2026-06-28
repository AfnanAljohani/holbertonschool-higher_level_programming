#!/usr/bin/python3
"""This module provides a function to find the max integer."""


def max_integer(list=[]):
    """Return the maximum integer in a list, or None if empty."""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
