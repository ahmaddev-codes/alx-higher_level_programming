#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the maximum integer in a list

    Args:
    @my_list: The list to check

    Returns:
    The maximum value of the list
    """
    if len(my_list) == 0:
        return None

    max_val = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > max_val:
            max_val = my_list[i]

    return max_val
