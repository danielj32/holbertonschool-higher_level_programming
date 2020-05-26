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
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        r = ""
        if self.__width == 0 or self.__height == 0:
            return r
        for ct_1 in range(self.__height):
            for ct_2 in range(self.__width):
                r += '#'
            if (ct_1 < self.__height - 1):
                r += '\n'
        return r

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
