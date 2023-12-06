#!/usr/bin/python3
"""
This module contains a function that apppends
a string at the end of text file
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Args:
        filename (object): The file to append into
        text (string): The text to append

    Return:
        The number of characters
    """
    with open(filename, 'a', encoding='utf8') as myfile:
        return myfile.write(text)
