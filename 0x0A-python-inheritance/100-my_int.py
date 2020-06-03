#!/usr/bin/python3
"""define a class Myint"""


class MyInt(int):
    """ change == and != """
    def __eq__(self, number):
        """ change != to =="""
        return int(self) != int(number)

    def __ne__(self, number):
        """ change == to != """
        return int(self) == int(number)
