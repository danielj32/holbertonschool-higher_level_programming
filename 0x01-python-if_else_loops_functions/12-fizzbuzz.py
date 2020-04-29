#!/usr/bin/python3
def fizzbuzz():
    for fitz in range(1, 101):
        if fitz % 3 == 0:
            print("Fizz", end="")
        if fitz % 5 == 0:
            print("Buzz", end="")
        if fitz % 3 > 0 and fitz % 5 > 0:
            print("{:d}".format(fitz), end="")
        print(" ", end="")
