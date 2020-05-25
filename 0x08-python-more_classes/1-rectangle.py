#!/usr/bin/python3
"""define a class Rectangule"""


class Rectangle:
    """show the class Rectangule"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w < 0:
            raise TypeError("width must be >= 0")
        self.__width = w
