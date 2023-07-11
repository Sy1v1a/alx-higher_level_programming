#!/usr/bin/python3
"""Defines a funct that reads text file"""


def read_file(filename=""):
    """Read a text file
    args:
        filename: name of file to be read
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
