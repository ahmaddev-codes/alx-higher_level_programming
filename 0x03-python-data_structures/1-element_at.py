#!/usr/bin/python3

def element_at(my_list, idx):
    """function that retrieves an element from a list like in C

    Args:
    @my_list: The list to retrieve an element from
    @idx: The index of the element to retrieve

    Return:
    None
    """
    array_length = len(my_list)

    if idx < 0 or idx >= array_length:
        return None

    else:
        return my_list[idx]
