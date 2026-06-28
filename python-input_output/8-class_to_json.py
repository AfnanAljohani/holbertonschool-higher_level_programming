#!/usr/bin/python3
"""Module that defines a function to convert a class to a JSON dict."""


def class_to_json(obj):
    """Return the dictionary description for JSON of an object."""
    return obj.__dict__
