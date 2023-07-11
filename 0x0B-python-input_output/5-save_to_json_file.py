#!/usr/bin/python3
"""Save obj to file using json rep"""
import json


def save_to_json_file(my_obj, filename):
    """Function that saves an object to a text file using JSON representation"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
