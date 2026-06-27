#!/usr/bin/python3
"""Module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry

    Private attributes:
        __width: The width of the rectangle
        __height: The height of the rectangle
    """

    def __init__(self, width, height):
        """Initialize a Rectangle

        Args:
            width: The width of the rectangle (must be a positive integer)
            height: The height of the rectangle (must be a positive integer)

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is not greater than 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Return the representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
