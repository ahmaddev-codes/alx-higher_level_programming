#!/usr/bin/python3
"""
This module contains a class that inherits from a base class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        __init___: Initialized class on instantiation

        Args:
            width (int): width of the shape
            height (int): height of the class
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
