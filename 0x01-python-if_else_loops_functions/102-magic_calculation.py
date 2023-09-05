#!/usr/bin/python3
import dis

# magic_calculation - Calculate values and show it in the preprocessor
# @a: first value
# @b: second value
# @c: third value


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c


dis.dis(magic_calculation)
