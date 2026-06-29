#!/usr/bin/python3
"""This module defines a text indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'.

    text must be a string, otherwise a TypeError is raised. Spaces at the
    start and end of each printed line are removed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
