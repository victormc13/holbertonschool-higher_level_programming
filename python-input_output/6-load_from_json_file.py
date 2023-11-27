#!/usr/bin/python3

"""Call the json module"""
import json

"""Defines load_from_json_file function"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (file): File in JSON representation.
    """
    json.loads(filename)
