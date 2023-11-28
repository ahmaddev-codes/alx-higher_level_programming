#!/usr/bin/python3
"""This module has a function that prints
    My name is <first name> <last name>

    For the module to execute perfectly well,
    the following condition has to be met:
    * first name must be a string,
    * otherwise a TypeError with the exception first name
    must be a string is raised
    * last name must be a string,
    * otherwise a TypeError with the exception last name
    must be a string is raised
"""

def say_my_name(first_name, last_name=""):
    """returns a string containing the first
        and the last name

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: If the first_name or last_name is an integer

    Returns:
        A string of characters with first_name and last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
