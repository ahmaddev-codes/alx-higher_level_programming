#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = -number % 10
    last_digit = -last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} "
            f"and is greater than 5", end="\n")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} "
            f"and is 0", end="\n")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} "
            f"and is less than 6 and not 0", end="\n")
