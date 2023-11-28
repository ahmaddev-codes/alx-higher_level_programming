#!/usr/bin/python3
"""This module prints a squarr with the character # in
    the specified number of ways

    For the program to run successfully, the follwing
    conditions must be met:
    * size is the size length of the square
    * size must be an integer, otherwise raise a TypeError
    exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    * if size is a float and is less than 0, raise a TypeError
    exception with the message size must be an integer
"""
def print_square(size):
    """prints s square with the character #

    Args:
        size (int): The size of the square to print

    Raises:
        TypeError: if size is < 0 or size is a float

    Returns:
        Nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
