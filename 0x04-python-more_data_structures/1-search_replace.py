#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list

    Args:
    @my_list: The initial list
    @search: The element to replace in the list
    @replace: The new element

    Returns:
    The new modified list
    """
    new_list = []
    for data in my_list:
        if data == search:
            data = replace
        new_list.append(data)

    return new_list
