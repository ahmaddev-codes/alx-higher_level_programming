#!/usr/bin/python3


def check_tuple(tuple_a=(), tuple_b=()):
    """checks if tuple_a and tuple_b meet the condition for addition

    Args:
    @tuple_a: The first tuple
    @tuple_b: THe second tuple

    Returns:
    The new implemented tuple
    """
    # Check tuple_a
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        elif len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)

    elif len(tuple_a) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])

    #check tuple_b
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        elif len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)

    elif len(tuple_a) > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    return (tuple_a, tuple_b)

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples

    Args:
    @tuple_a: The first tuple
    @tuple_b: THe second tuple

    Returns:
    Addition of the with two tuples
    """
    new_tuple = check_tuple(tuple_a, tuple_b)
    result = ((new_tuple[0][0] + new_tuple[1][0]), \
            (new_tuple[0][1] + new_tuple[1][1]))
    return result
