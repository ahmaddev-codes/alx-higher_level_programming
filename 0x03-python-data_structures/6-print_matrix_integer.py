#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
    @matrix: The matrix to print

    Return:
    Printed matrix
    """
    if matrix:
        for elems in matrix:
            i = 1
            length = len(elems)

            for elem in elems:
                if i == length:
                    print('{:d}'.format(elem), end='')
                else:
                    print('{:d}'.format(elem), end=' ')
                i += 1

            print()
