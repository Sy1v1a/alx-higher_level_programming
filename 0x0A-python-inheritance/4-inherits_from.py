#!/usr/bin/python3
"""Defines an inherited class check"""


def inherits_from(obj, a_class):
    """Checks if obj is inherited instance of a_class
    args:
        obj: object to check
        a_class: clas to match obj
    Returns:
        True if obj is inherited
        False if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
