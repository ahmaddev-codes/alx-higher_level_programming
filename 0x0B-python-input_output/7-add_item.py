#!/usr/in/python3
from os import path
from sys import argv


"""
This module contains a function that adds all arguments
to a python list and save them as a file
"""


save_to_json_file = \
        __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

if path.exists('add_item.json'):
    obj_json_file = load_from_json_file('add_item.json')
else:
    obj_json_file = []

for i in range(1, len(argv)):
    obj_json_file.append(argv[i])

save_to_json_file(obj_json_file, 'add_item.json')
