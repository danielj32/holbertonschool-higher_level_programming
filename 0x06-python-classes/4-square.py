#!/usr/bin/python3
"""is the class square"""


class Square:
    """is the class square"""

    def __init__(self, size=0):
        """Init the class"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """manage error"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """define area"""
        return self.__size ** 2
