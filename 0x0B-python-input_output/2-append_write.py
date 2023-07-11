#!/usr/bin/python3
"""Append and write in file """


def append_write(filename="", text=""):
    """
    Append, write and return number of characters
    args:
        filename: name of file
        text: character to append
    Return:
        number of characters
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
