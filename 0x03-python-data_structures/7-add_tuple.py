#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples

    Args:
    @tuple_a: The first tuple
    @tuple_b: THe second tuple

    Returns:
    Result of the addition of two tuples
    """
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)

    result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return result


def check_tuple(_tuple=()):
    if len(_tuple) < 2:
        if len(_tuple) == 1:
            _tuple = (_tuple[0], 0)
        elif len(_tuple) == 0:
            _tuple = (0, 0)
    elif len(_tuple) > 2:
        _tuple = (_tuple[0], _tuple[1])

    return _tuple
