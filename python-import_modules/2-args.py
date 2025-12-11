#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(count, "" if count == 1 else "s"))
        for i in range(count):
            print("{}: {}".format(i + 1, args[i]))
