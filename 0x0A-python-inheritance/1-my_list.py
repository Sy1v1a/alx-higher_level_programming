#!/usr/bin/python3
"""Defines an iherited list"""


class MyList(list):
    """Prints the list but sorted"""

    def print_sorted(self):
        """Print list in sorted ascending order"""
        print(sorted(self))
