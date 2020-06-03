#!/usr/bin/python3
"""define a class BaseGeometry"""


class BaseGeometry:
    """show the class BaseGeometry"""
    def area(self):
        """show the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ area integer validation """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
