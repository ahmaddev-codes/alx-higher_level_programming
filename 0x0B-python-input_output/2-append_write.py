#!/usr/bin/python3
def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a', encoding='utf8') as myfile:
        return myfile.write(text)
