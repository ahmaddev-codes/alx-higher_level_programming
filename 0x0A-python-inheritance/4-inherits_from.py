#!/usr/bin/python3
"""
This module contains a function that checks if an instance
of a class inherits from a class
"""


def inherits_from(obj, a_class):
    """
    Checks if an instance of a class inherited
    directly or indirectly from a specified class

    Args:
        obj(obj): sub class
        a_class(class): base class

    Return:
        True: if it inherits from a class
        False: otherwise
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True
    
    return False
