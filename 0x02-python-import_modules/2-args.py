#!/usr/bin/python3
from sys import argv
ag = len(argv) - 1
if ag == 1:
    p = "argument:"
    if ag == 0:
        p = "arguments."
        if ag > 1:
            p = "arguments:"
            print("{} {}".format(ag, p))
if ag > 0:
    print("{}:".format(ag), end=' ')
    print("{}".join(argv[1:]))
