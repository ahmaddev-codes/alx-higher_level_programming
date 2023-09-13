#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set

    Args:
    @set_1: The first set to compare
    @set_2: The second set to compare

    Returns:
    A set of all elements present in only one set
    """
    return set_1 ^ set_2
