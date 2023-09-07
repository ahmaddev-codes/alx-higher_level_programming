#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc < 2:
        print("0")
    else:
        total = 0

        for i in range(1, argc + 1):
            total += int(argv[i])
        print(total)

