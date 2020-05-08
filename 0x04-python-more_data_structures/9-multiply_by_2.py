#!/usr/bin/python3
def multiply_by_2(a_dictionary):
        n_dict = a_dictionary.copy()
        for i in a_dictionary:
                        n_dict[i] = n_dict[i] * 2
        if not a_dictionary:
                return a_dictionary
        return n_dict
