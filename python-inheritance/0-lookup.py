#!/usr/bin/python3

"""Define the lookup function"""


def lookup(obj):
    """Returns a lis object.
    
    Args:
        obj (obj): Object as argument\
        to return a list of his attributes and method.

    Returns:
        list (obj): Returns a list object.
    """
    return dir(obj)
