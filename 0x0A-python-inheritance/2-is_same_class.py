#!/usr/bin/python3
"""Defines a class check"""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a class
    arg:
        obj: the object to check
        a_class: the class to match
    Returns:
        True if obj is same as a_class
        False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
