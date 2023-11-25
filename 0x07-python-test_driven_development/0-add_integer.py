#!/usr/bin/python3
def add_integer(a, b=98):
    """add_integer

    adds two integers

    Args:
        a (int or float): First integer
        b (int or float): Second integer
    Returns:
        The addition of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
