#!/usr/bin/python3
"""
A module that contains a function that returns the list of
attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available atrributes and methods of an object
    """
    return dir(obj)
