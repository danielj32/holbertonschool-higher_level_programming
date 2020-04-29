#!/usr/bin/python3
def fizzbuzz():

        fizz = 1
        for fizz in range(100):
                if fizz % 3 == 0 and fizz % 5 == 0:
                        print("Fizz", end='')

                elif fizz % 5 == 0 and fizz % 3 != 0:
                        print("Buzz", end='')

                elif fizz % 3 == 0 and fizz % 5 == 0:
                        print("FizzBuzz", end='')

                else:
                        print("{:d}".format(fizz), end="")

                if fizz != 100:
                        print(" ", end="")
