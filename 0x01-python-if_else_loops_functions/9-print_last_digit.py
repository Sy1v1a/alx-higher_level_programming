#!/usr/bin/python3
#this is just to let you know that we needed 88 characters so this ...
def print_last_digit(number):
    last = number % 10
    print("{}".format(last), end='')
    return last
