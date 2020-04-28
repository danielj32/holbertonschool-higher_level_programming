#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
ldigit = 10
rest = number % ldigit

if number < 0:
    rest -= 10
print("Last digit of {:d} is {:d} ".format(number, rest), end='')

if rest > 5:
    print(" and is greater than 5")

elif rest == 0:
    print("and is 0")

else:
    print("and is less than 6 and not 0")
