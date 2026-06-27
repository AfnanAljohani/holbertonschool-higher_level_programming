#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherits from a_class

    Args:
        obj: The object to check
        a_class: The class to check inheritance from

    Returns:
        True if obj is an instance of a class that inherits from a_class
        (but not an instance of a_class directly)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
