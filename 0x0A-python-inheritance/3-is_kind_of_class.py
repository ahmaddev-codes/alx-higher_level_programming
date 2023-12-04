#!/usr/bin/python3
"""
This modules contains a function that checks that an object instance
of a class inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class;
    otherwise False

    Args:
        obj(obj): subclass
        a_class(obj): base class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
