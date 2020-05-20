#!/usr/bin/python3
"""show the class square"""


class Square:
    """Representsa class Square"""
    def __init__(self, size=0):
        if size < 0:
            raise TypeError("size must be an integer")
        elif type(size) is not int:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
