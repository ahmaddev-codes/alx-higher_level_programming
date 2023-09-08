#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    without modifying the original list

    Args:
    @my_list: The list to traverse
    @idx: The index to replace element
    @element: The element to put in the index location

    Return:
    The new list (copy of the original list) with the mutated index
    """
    array_length = len(my_list)

    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
