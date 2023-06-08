#!/usr/bin/python3

"""a function to print last disit"""

def print_last_digit(number):
    last = abs(number) % 10
    print("{}".format(last), end='')
    return (last)
