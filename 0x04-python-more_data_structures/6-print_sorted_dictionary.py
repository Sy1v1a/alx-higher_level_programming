#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortkey = sorted(a_dictionary.keys())
    for k in sortkey:
        print(k, ":" ,a_dictionary[k])
