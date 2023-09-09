#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list

    Args:
    @my_list: The list to find multiples from

    Returns:
    A new list with True or False if it is divisible by 2 or not
    """
    new_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
