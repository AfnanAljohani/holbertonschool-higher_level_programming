#!/usr/bin/python3
"""Module that defines a Student class with attribute filtering."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dict representation, optionally filtered by attrs."""
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
