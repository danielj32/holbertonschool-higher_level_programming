#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    ldigit = number % -10
else:
    ldigit = number % 10
if ldigit > 5:
    print("Last digit of {0:d} is {1:d}".format(number, ldigit), end=' ')
    print("and is greater than 5")
elif ldigit == 0:
    print("Last digit of {0:d} is {1:d} and is 0".format(number, ldigit))
elif ldigit < 6 and ldigit != 0:
    print("Last digit of {0:d} is {1:d}".format(number, ldigit), end=' ')
    print("and is less than 6 and not 0")
