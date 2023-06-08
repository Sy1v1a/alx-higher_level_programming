#!/usr/bin/python3
import sys
ag = sys.argv[1:]
sum1 = 0
for i in ag:
    sum1 += int(i)
    print("{}".format(sum1))
