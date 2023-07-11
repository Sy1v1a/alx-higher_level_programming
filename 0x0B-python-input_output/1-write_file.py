#!/usr/bin/python3
"""Writes a file"""


def write_file(filename="", text=""):
    """A funct to write in a file
    args:
        filename: name of file
        text: char to write in file
    Return:
        length of text
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
