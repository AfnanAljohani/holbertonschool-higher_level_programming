#!/usr/bin/python3
"""Module that defines a function to insert text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string."""
    lines = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
