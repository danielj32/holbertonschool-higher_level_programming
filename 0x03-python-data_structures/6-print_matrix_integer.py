#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	ct = 0
	for l in matrix:
		for k in l:
			if ct == len(l) - 1:
				print("{:d}".format(k), end="")
			else:
				print("{:d}".format(k), end=" ")
	ct += 1
	print('')
