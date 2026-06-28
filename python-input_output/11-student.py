#!/usr/bin/python3
"""Module that defines a Student class with reload capability."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dict representation, optionally filtered by attrs."""
        if (isinstance(attrs, list) and
                all(isinstance(e, str) for e in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
