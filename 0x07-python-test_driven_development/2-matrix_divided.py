#!/usr/bin/python3
def matrix_divided(matrix, div):
        matrix = [[]]
        if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
        if div == 0:
                raise ZeroDivisionError("division by zero")
        for row in matrix:
                for fills in row:
                        return fills
