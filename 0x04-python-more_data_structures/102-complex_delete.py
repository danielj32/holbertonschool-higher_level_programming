#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        for n_key in list(a_dictionary.keys()):
                if value == a_dictionary[n_key]:
                        del a_dictionary[n_key]
        return a_dictionary
