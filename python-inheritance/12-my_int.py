#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """MyInt class that inherits from int with inverted == and != operators

    This is a rebel integer where the == and != operators are swapped.
    """

    def __eq__(self, other):
        """Return the inverted equality comparison"""
        return int(self) != other

    def __ne__(self, other):
        """Return the inverted inequality comparison"""
        return int(self) == other
