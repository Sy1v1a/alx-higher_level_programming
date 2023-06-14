#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return (0)
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        digit = 0
        result = 0
        for i in roman_string[::-1]:
            val = roman[i]
            if val >= digit:
                result += val
            else:
                result -= val
                digit = val
        return (result)
