#!/usr/bin/python3
for n in range(0, 100):
        i = n % 10
        j = n / 10

        if j < i and j != i and n != 89:
                print("{:02d}, ".format(n), end="")

        if n == 89:
                print("{:d}".format(n))
