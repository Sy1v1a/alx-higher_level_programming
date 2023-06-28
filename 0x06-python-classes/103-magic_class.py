#!/usr/bin/python3
"""define a magic class """
import math

class MagicClass:
    """Magic clas of a circle"""
    def __init__(self, radius=0):
        """init a Magicclass

        Arg:
        radius (int or float) of MC
        """
        self.__radius = 0
    if type(radius) is not int and type(radius) is not float:
        raise TypeError("radius must be a number")
    self.__radius = radius

    def area(self):
        """Return area of MC"""
        return (self.__radius ** 2 math.pi)
    def circumference(self):
        """Return cir.. of MC"""
        return (2 * math.pi * self.__radius)
