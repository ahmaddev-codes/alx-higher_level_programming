#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order

    Args:
    @my_list: The list to traverse

    Return:
    The list with the elements in reverse order
    """
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
