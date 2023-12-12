#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using JSON representation

    Args:
        my_obj (string): The string to write into file
        filename (obj): Name of file to write
    """
    with open(filename, 'w', encoding='utf8') as myfile:
        json_object = json.dumps(my_obj)
        myfile.write(json_object)
