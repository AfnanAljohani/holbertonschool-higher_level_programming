#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """Class for geometry operations"""

    def area(self):
        """Raises an Exception

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer

        Args:
            name (str): The name of the parameter
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
