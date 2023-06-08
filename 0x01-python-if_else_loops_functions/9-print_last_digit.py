#!/usr/bin/python3
# 9-print_last_digit.py

"""a function to print last disit"""

def print_last_digit(number):
    last = abs(number) % 10
    print("{}".format(last), end='')
    return (last)
