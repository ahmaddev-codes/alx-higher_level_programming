#!/usr/bin/python3

# print_last_digit - prints last digit
#
# @number: number to print its last digit
def print_last_digit(number):
    if number < 0:
        number = - number

    last_digit = number % 10
    print("{}".format(last_digit), end="")

    return last_digit
