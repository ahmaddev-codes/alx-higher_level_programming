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
    array_length = len(my_list)

    if idx < 0:
        return my_list
    elif idx > array_length:
        return my_list
    else:
        for i in range(array_length):
            if i == idx:
                my_list[i] = element
