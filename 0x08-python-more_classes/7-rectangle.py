#!/usr/bin/python3
"""
A module that implements a Ractangle class
"""


class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.

        Raises:
            TypeError: If width and height are not integers.
            ValueError: If width and height are less than 0.
        """
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __draw_rectangle(self):
        """Draws the shape of the rectangle."""
        shape_string = ""

        if self.__width == 0 or self.__height == 0:
            return shape_string

        for i in range(self.__height):
            if type(self.print_symbol) is list:
                self.print_symbol = str(self.print_symbol)
            shape_string += self.print_symbol * self.__width
            if i != self.__height - 1:
                shape_string += "\n"

        return shape_string

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return self.__draw_rectangle()

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a message when an instance of a rectangle
        is deleted
        """
        self.number_of_instances -= 1
        print("Bye rectangle...")
