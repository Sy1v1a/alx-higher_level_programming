#!/usr/bin/python3
if __name__ == "__main__":
    from  calculator_1 import add, sub, mul, div
    import sys
    cal = len(sys.argv) -1
    if cal != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        a = int(sys.argv[1])
        operator = {"+": add, "-": sub, "*": mul, "/": div}
        b = int(sys.argv[3])

        if sys.argv[2] not in list(operator.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, sys.argv[2], b, operator[sys.argv[2]](a, b)))
