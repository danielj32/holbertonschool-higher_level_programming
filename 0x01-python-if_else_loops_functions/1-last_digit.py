#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = 10
rest = number % ldigit
if rest > 5:
    print("Last digit of {:d} is {:d}".format(number, rest), end=' ')
    print(" and is greater than 5")
if rest == 0:
    print("Last digit of {:d} is {:d}  and is 0".format(number, rest))
elif rest < 6:
    print("Last digit of {:d} is {:d} ".format(number, rest), end=' ')
    print("and is less than 6 and not 0")
