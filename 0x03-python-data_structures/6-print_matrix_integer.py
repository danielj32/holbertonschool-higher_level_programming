#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i in range(len(matrix)):
            for l in range(len(matrix[i])):
                if l < len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][l]), end=" ")
                else:
                    print("{:d}".format(matrix[i][l]), end="")
        print("")
