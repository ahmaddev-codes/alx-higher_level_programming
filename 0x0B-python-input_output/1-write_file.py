#!/usr/bin/python3
"""
This module contains a function that writes into a text file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename(object): The file to write into
        text (string): The text to write into the file

    Return:
        Number of characters written
    """
    with open(filename, mode="w", encoding="utf8") as myFile:
        return myFile.write(text)
