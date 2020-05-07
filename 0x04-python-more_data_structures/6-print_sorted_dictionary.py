#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
        sorted(a_dictionary.keys())
        for k in sorted(a_dictionary.keys()):
                print("{:s}: {}" .format(k, a_dictionary[k]))
