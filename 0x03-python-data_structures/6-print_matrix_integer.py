#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for ct in range(len(matrix)):
            for o in range(len(matrix[ct])):
                if o < len(matrix[ct]) - 1:
                    print("{:d}".format(matrix[ct][o]), end=' ')
                else:
                    print("{:d}".format(matrix[ct][o]), end='')
        print("")
