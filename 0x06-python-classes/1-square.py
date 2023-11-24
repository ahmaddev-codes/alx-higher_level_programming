#!/usr/bin/python3
"""Square class

    A square class that initializes size
    as a private property
"""


class Square:

    def __init__(self, size):
        """__init__

        The __init__ method initializes the size value
        of the square.

        Attributes:
            size (int): The size of the square.

        """
        self.__size = size
