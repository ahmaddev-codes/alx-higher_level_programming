#!/usr/bin/python3
"""This module contains a function that prints a pascal triangle"""


def pascal_triangle(n):
    """prints a pascal triangle

    Args:
        n (int): number of rows
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
