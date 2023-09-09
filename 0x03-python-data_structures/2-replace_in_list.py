#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position (like in C)

    Args:
    @my_list: The list to change element from
    @idx: The index in the list to change its element
    @element: The element to put in the index instead

    Return:
    The mutated list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
