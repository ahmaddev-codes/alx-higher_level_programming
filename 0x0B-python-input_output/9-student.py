#!/usr/bin/python3
"""This module contains a class"""


class Student:
    """defines a class Student"""
    def __init__(self, first_name, last_name, age):
        """initializes the class

        Args:
            first_name (string): first name of student
            last_name (string): last name of student
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives json sting of a class"""
        json_dict = {}

        for attr_name in dir(self):
            if not attr_name.startswith("__"):
                attr_value = getattr(self, attr_name)

                if isinstance(attr_value, (list, dict, str, int)):
                    json_dict[attr_name] = attr_value

        return json_dict
