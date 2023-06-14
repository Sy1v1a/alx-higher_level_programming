#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = a_dictionary.copy()
    lk = list(newdict.keys())

    for key in lk:
        newdict[key] *= 2
    return (newdict)
