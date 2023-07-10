#!/usr/bin/python3
"""defines a class Myint that is inherited from int"""


class MyInt(int):
    """Inverts ints operators == and !="""

    def __eq__(self, other):
        """Overrides operators behaviours"""
        self.real != other

    def __ne__(self, other):
        """Overides operators behaviour"""
        return self.real == other
