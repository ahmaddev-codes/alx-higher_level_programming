#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:

:x
        text (string): The text to write into the file

    Return:
        Number of characters written
    """
    with open(filename, mode="w", encoding="utf8") as myFile:
        return myFile.write(text)
