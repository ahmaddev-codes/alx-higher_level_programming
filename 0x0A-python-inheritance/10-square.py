#!/usr/bin/python3
"""
This module contains a class that inherits from a base class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle"""

    def __init__(self, size):
        """
        __init___: Initialized class on instantiation

        Args:
            width (int): size of the square
        """
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """returns the area of the rectangle"""
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
