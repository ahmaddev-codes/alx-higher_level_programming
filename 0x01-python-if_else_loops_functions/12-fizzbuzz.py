#!/usr/bin/python3

# fizzbuzz - A function that prints fizz for multiple of 3,
# prints buzz for multiples of 5 and
# and fizzbuzz for multiples of both 3 and 5
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
