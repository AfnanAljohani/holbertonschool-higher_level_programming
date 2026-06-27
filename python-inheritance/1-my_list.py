#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """Class that inherits from list and adds a print_sorted method"""

    def print_sorted(self):
        """Print the list in sorted order

        Prints the list sorted in ascending order
        Does not modify the original list
        """
        print(sorted(self))
