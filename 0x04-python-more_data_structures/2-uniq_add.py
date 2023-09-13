#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)

    Args:
    @my_list: The list to add all the unique integers

    Returns:
    The addition of all the unique elements
    """
    sum_all = 0
    uniq_vals = set(my_list)

    for data in uniq_vals:
        sum_all += data

    return sum_all
