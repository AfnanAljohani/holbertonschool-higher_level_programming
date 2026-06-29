#!/usr/bin/python3
"""This module defines a function that prints a full name."""


def say_my_name(first_name, last_name=""):
    """Print "My name is <first_name> <last_name>".

    first_name and last_name must be strings, otherwise a TypeError is raised.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
