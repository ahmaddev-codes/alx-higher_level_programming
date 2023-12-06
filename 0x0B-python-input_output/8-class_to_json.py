#!/usr/bin/python3
import json


"""
This module contains a function that returns the dictionary
description with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj (object): Object to serialize
    """
    json_dict = {}

    for attr_name in dir(obj):
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)

            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value

    return json_dict
