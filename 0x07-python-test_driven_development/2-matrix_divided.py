#!/usr/bin/python3
def matrix_divided(matrix, div):
        if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
        if div == 0:
                raise ZeroDivisionError("division by zero")
        if type(matrix) is not list or len(matrix) == 0:
                raise TypeError("matrix must be a matrix (list of lists) \
                         of integers/floats")
        n_matrix = matrix.copy()
        first = []
        second = []

        for ct in n_matrix[0]:
                first.append(round(ct/div, 2))
        for ct2 in n_matrix[1]:
                second.append(round(ct2 / div, 2))
        n_matrix = [first, second]
        return n_matrix
