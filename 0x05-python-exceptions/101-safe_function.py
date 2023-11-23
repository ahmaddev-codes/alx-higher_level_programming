#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)

    except ZeroDivisionError as zd:
        sys.stderr.write("Exception: " + str(zd) + "\n")
        return None
    except IndexError as ie:
        sys.stderr.write("Exception: " + str(ie) + "\n")
        return None
