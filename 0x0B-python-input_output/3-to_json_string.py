#!/usr/bin/python3
import json


"""
This module contains a function that returns the JSON
representation of an object
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object

    Args:
        my_obj (string): The object to stringify
    """
    return json.dumps(my_obj)
