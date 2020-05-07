#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        cube = [[column ** 2 for column in rows] for rows in matrix]
        return cube
