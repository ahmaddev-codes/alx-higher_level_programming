#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description with simple data structure (list, dictionary, string,
integer and boolean)
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure

    Args:
        obj (object): Object to convert
    """
    json_dict = {}

    for attr_name in dir(obj):
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)

            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value

    return json_dict
