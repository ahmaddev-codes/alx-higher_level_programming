#!/usr/bin/python3
"""
A module that contains a Square class
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple \
                        of 2 positive integer")
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        result = ""
        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            result += ' ' * self.__position[0] + '#' * self.__size + "\n"

        return result
