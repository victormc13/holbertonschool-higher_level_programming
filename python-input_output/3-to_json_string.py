#!/usr/bin/python3

import json

"""Defines to_json_string function"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj (obj): Object to parse to JSON.

    Returns:
        JSON: JSON representation of the my_obj.
    """
    return (json.dumps(my_obj))
