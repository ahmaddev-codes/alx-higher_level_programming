#!/usr/bin/python3
"""
This module contains a Square class
"""


class Square:
    """Square Class
    A Square Class
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        The __init__ method initializes the size value of the square.

        Attributes:
            size (obj:'int', optional): The size of the square.
            position (obj:'int', optional): The position of the attributes.
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size
        The size setter method update the size value of the square.

        Attributes:
            value (:obj:`int`): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """position
        The position setter method update the size value of the square.

        Attributes:
            value (obj:`int`): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of two positive int
        """

        if self.__check_tuple(value) is False \
           or self.__check_indexes(value) is False \
           or self.__check_integers(value) is False \
           or self.__check_values(value) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def __check_tuple(self, position):
        if isinstance(type(position), tuple):
            return True
        return False

    def __check_indexes(self, position):
        if len(position) > 0:
            return True
        return False

    def __check_integers(self, position):
        if type(position[0]) is int and type(position[1]) is int:
            return True
        return False

    def __check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True
        return False

    def area(self):
        """Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
