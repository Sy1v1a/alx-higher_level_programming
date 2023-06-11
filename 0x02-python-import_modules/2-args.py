#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ag = len(sys.argv) - 1
    if ag == 0:
        print("0 arguments.")
    elif ag == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ag))
        for i in range(ag):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
