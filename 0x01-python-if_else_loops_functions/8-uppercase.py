#!/usr/bin/python3
def uppercase(str):
    for letters in str:
            upperc = chr(ord(letters) - 32) if ord(letters) >= 97 and ord(letters) <= 122 else letters
            print("{}".format(upperc), end='')
    print()
