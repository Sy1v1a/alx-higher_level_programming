#!/usr/bin/python3
"""Defines a class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary rep of a simple data structure."""
    return obj.__dict__
