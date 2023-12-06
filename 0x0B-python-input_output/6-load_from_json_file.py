#!/usr/bin/python3
import json


"""
This module contains a function that
creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename (object): Name of json file
    """
    with open(filename, encoding='utf8') as myfile:
        return json.load(myfile)
