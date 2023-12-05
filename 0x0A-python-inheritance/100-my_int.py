#!/usr/bin/python3
"""
This module contains a class that inherits from int
"""


class MyInt(int):
    """A class that inherits from int"""
    def __eq__(self, other):
        """Override the == operator to invert its behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to invert its behavior."""
        return super().__eq__(other)
