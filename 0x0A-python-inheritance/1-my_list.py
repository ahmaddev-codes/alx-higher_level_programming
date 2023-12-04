#!/usr/bin/python3
"""
This module has a class MyList that inherits from list
"""


class MyList(list):
    """A class that inherits from list

    Args:
        list (class): Base class inherited from
    """

    def print_sorted(self):
        """
        Prints a sorted list in ascending order
        """

        if issubclass(MyList, list):
            print(sorted(self))
