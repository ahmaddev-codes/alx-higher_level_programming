#!/usr/bin/python3
"""
This module contains a function that writes
a string to a text file and returns the number
of characters written
"""


def read_file(filename=""):
    """
    Reads a text file and print it to stdout

    Args:
        filename (string): name of file to read

    Return:
        Nothing
    """
    with open("my_file_0.txt") as myFile:
        print(myFile.read())
