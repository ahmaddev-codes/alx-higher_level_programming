#!/usr/bin/python3


def no_c(my_string):
    """Removes all characters c and C from a string

    Args:
    @my_string: String to remove characters from

    Return:
    The new string without letters
    """
    new_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_string += i
    return new_string
