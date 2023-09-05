#!/usr/bin/python3

# uppercase(str) - Prints a string in uppercase
# @str: string to transform to uppercase
def uppercase(str):
    result = ""
    for char in str:
        # check if the charater is lowercase
        if "a" <= char <= "z":
            # convert to uppercase with ASCII manipulation
            upper_char = chr(ord(char) - ord("a") + ord("A"))
            result += upper_char
        else:
            upper_char = chr(ord(char))
            result += upper_char

    print("{}".format(result), end="\n")
