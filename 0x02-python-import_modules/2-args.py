#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ag = len(argv) - 1
    if ag == 1:
        print("1 argument:")
    elif ag == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(ag))
        for i in range(ag):
            print("{}: {}".format(i + 1, argv[i + 1]))
