#!/usr/bin/python3

"""Call the json module"""
import json

"""Defines save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """Returns an object represented by a JSON string.

    Args:
        my_obj (obj): Object to parse to JSON.
        filename (file): File to put the parsed object.
    """
    json.dump(my_obj, filename)
