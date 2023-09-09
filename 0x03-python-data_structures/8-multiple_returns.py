#!/usr/bin/python3

def multiple_returns(sentence):
    """Reads a string and retur a tuple with the length of the string
    and its first character

    Args:
    @sentence: The tuple to read

    Returns:
    A tuple with the length of the string and the fist character
    """
    if not sentence:
        return (0, None)

    return (len(sentence), sentence[0])
