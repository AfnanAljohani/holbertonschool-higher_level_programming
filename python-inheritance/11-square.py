#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle

    A square is a special case of rectangle where width equals height.

    Private attributes:
        __size: The size of the square (width and height)
    """

    def __init__(self, size):
        """Initialize a Square

        Args:
            size: The size of the square (must be a positive integer)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is not greater than 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """Return the representation of the square"""
        return f"Square({self.__size})"
