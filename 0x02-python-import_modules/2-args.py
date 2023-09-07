#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    argument_vector = sys.argv
    argument_count = len(argument_vector) - 1

    if argument_count > 1:
        print(argument_count, "arguments:")
        for i in range(1, argument_count + 1):
            print("{}: {}".format(i, argument_vector[i]))

    elif argument_count == 1:
        print(argument_count, "argument:")
        for i in range(1, argument_count + 1):
            print("{}: {}".format(i, argument_vector[i]))

    elif argument_count == 0:
        print(argument_count, "argument.")
