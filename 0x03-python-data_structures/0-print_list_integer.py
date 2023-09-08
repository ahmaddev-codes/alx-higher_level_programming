#!/usr/bin/python3
"""Function that prints all integers of a list.
print_list_integer - Prints all integers of a list.
@my_list: List of integers.
"""


def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
