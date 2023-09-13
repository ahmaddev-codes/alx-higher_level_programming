#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix

    Args:
    @matrix: The matrix to compute its values

    Returns:
    The square of all values in the matrix
    """
    new_matrix = []

    for lists in matrix:
        inner_list = []
        for values in lists:
            inner_list.append(values ** 2)
        new_matrix.append(inner_list)

    return new_matrix
