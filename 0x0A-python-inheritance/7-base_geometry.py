#!/usr/bin/python3
"""
This module contains an class BaseGeomtry
"""


class BaseGeometry:
    """A BaseGeometry class"""

    def area(self):
        """area of the shape

        Raises:
            Exception: a string
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates values passed

        Args:
            name (string): variable name
            value (int): value to store in it

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than or equal 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
