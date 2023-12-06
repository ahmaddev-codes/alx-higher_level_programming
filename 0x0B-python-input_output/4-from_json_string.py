#!/usr/bin/python3
import json


"""
This module contains a function that returns an object
represented by a JSON string
"""


def from_json_string(my_str):
    """returns an object represented by a JSON string

    Args:
        my_str (object): The string
    """
    return json.loads(my_str)
