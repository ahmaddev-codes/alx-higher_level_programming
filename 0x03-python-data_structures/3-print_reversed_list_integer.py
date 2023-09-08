#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order

    Args:
    @my_list: The list to traverse

    Return:
    The list with the elements in reverse order
    """
    array_length = len(my_list)

    for i in range(array_length - 1, -1, -1):
        print(my_list[i])
