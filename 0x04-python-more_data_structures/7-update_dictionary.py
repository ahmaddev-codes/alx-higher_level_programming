#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary

    Args:
    @a_dictionary: The dictionary to update
    @key: The keys in the dictionary
    @value: The vales in the dictionary

    Returns:
    The new implemented dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
