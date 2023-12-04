#!/usr/bin/python3
"""
This module contains a class that checks if a subclass is exactly
an instance of a base class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of the specified class,
    otherwise False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
