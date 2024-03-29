#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific location in a list

    Args:
    @idx: The index of item to remove

    Returns:
    The list without the item at specified index
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    for i in range(len(my_list)):
        if i == idx:
            my_list.remove(my_list[i])

    return my_list
