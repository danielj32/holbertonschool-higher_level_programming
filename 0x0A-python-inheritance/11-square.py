#!/usr/bin/python3
"""define a class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size):
        """ Construct """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ Calculate area """
        return super().area()

    def __str__(self):
        """ print """
        return "[Square] {}/{}".format(self.__size, self.__size)
