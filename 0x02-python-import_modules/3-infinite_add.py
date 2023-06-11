#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lent = len(sys.argv)
    sum1 = 0
    if lent == 1:
        sum1 = 0
    else:
        for i in range(1, lent):
            sum1 += int(sys.argv[i])
    print("{:d}".format(sum1))
