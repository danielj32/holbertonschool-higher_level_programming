#!/usr/bin/python3
""" function number of lines"""


def number_of_lines(filename=""):
    """ return of number of lines text file """
    ct = 0

    with open(filename, 'r') as f:
        for i in f:
            ct += 1
    return ct
