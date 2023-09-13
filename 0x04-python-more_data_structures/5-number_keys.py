#!/usr/bin/python3

def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary

    Args:
    @a_dictionary: The dictionary to read

    Returns:
    The keys in a dictionary
    """
    count = 0

    for i in a_dictionary:
        count = count + 1

    return count
