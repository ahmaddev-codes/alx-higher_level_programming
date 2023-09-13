#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys

    Args:
    @a_dictionary: The dictionary to print

    Returns:
    A dictionary with ordered keys
    """
    sorted_dictionary = sorted(a_dictionary.items())

    for key, value in sorted_dictionary:
        print('{0}: {1}'.format(key, value))
