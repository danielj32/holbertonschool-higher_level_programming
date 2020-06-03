#!/usr/bin/python3
"""define a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """show the class Rectangle"""
    def __init__(self, width, height):
        """ Construct """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
