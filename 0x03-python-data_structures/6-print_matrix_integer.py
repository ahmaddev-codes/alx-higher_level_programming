#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
    @matrix: The matrix to print

    Return:
    Printed matrix
    """
    for row in matrix:
        for elem in row:
            print("{:d}".format(elem), end=" ")
        print()
