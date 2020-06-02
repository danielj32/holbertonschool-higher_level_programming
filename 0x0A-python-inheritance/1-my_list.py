#!/usr/bin/python3
"""class MyList """


class MyList(list):
    """show the class Rectangule"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort) """
        print(sorted(self))
