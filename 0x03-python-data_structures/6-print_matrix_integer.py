#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i in range(len(matrix)):
            for o in range(len(matrix[i])):
                if o == len(matrix[o]) - 1:
                    print("{:d}".format(matrix[i][o]), end='')
                else:
                    print("{:d}".format(matrix[i][o]), end=' ')
        print()
