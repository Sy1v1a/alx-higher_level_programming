#!/usr/bin/python3
"""defines a class Myint that is inherited from int"""


class MyInt(int):
    """Inverts ints operators == and !="""

    def __eq__(self, value):
        """Overrides operators behaviours"""
        return self.real != value

    def __ne__(self, value):
        """Overides operators behaviour"""
        return self.real == value
