#!/usr/bin/python3
""" Read a file """


def read_file(filename=""):
    """ read a text file in UTF8 """
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end='')
