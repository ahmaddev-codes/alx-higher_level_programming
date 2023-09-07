#!/usr/bin/python3
from add_0 import add

if __name__=="__main__":
    """
    prints the addition of two numbers

    """
    a = 1
    b = 2

    print("{0} + {1} = {2}".format(a, b, add(a, b)), end="\n")
