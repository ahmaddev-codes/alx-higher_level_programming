#!/usr/bin/python3
"""
This module checks if it can add some attributes to a class
"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible."""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
