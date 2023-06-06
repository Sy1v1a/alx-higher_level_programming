#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
str1 = "last digit of " + str(number) + "is " + str(ld)
if ld > 5:
    str1 += " and is greater than 5"
elif ld == 0:
    str1 += " and is 0"
elif ld < 6 and ld != 0:
    str1 += " and is less than 6 and not 0"
    print(str1)
