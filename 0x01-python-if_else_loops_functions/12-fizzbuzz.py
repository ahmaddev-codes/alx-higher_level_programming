#!/usr/bin/python3

# fizzbuzz - A function that prints fizz for multiple of 3,
# prints buzz for multiples of 5 and
# and fizzbuzz for multiples of both 3 and 5
def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 == 0):
            print("Fizz ", end="")
        elif (number % 5 == 0):
            print("Buzz ", end="")
        elif (number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz", end="")
        else:
            print("{} ".format(number), end="")
