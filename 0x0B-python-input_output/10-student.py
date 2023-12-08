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

    def to_json(self, attrs=None):
        """retrives json string of a class"""
        json_dict = {}

        if attrs is None:
            return self.__dict__
        else:
            for attr_name in attrs:
                if hasattr(self, attr_name):
                    attr_value = getattr(self, attr_name)
                    json_dict[attr_name] = attr_value

            return json_dict
