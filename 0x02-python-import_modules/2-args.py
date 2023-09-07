#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    argv = sys.argv
    argc = len(argv) - 1

    if argc > 1:
        print(argc, "arguments:")
        for i in range(1, argc + 1):
            print("{:d}: {}".format(i, argv[i]))

    elif argc == 1:
        print(argc, "argument:")
        for i in range(1, argc + 1):
            print("{:d}: {}".format(i, argv[i]))

    elif argc == 0:
        print(argc, "arguments.")
