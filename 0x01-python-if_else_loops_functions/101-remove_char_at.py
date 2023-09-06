#!/usr/bin/python3

"""
remove_char_at - A function to remove character at a particular index

@str: The string to read
@n: The index to remove from
"""


def remove_char_at(str, n):
    new_string = ""

    for i in range(len(str)):
        if i != n:
            new_string += str[i]

    return new_string
