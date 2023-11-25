#!/usr/bin/python3

"""Define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance,
    or if the object is an instance of a class that
    inherited from, the specified class.
    Args:
        obj (obj): Object to be checked.
        a_class (class): Class specified.

    Returns:
        bool: True if object is an instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
