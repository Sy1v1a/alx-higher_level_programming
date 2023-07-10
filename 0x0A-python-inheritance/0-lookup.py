#!/usr/bin/python3
"""Defines a lookup function"""


def lookup(obj):
    """Return list of available attributes and methods"""
    return (dir(obj))
