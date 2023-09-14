#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == () or  my_list == 0:
        return 0

    return sum([mul(x[0], x[1]) for x in my_list]) / sum(x[1] for x in my_list)


def mul(x, y):
    return x * y
