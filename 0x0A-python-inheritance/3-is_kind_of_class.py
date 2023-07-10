#!/usr/bin/python3
"""Defines a class and inherited class check"""


def is_kind_of_class(obj, a_class):
    """Check if obj is instance of a_class
    args:
        obj: object to check
        a_class: class to match obj
    Returns:
    True if obj and a_class is same kind
    False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
