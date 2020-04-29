#!/usr/bin/python3
def print_last_digit(number):
        ldigit = number % 10

        if number < 0:
                ldigit -= 10
        if ldigit < 0:
                ldigit *= -1
        print("{}".format(ldigit), end="")
        return (ldigit)
