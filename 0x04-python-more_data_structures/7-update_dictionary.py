#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
        for n_key in a_dictionary:
                if n_key is key:
                        a_dictionary[n_key] = value
        a_dictionary.update({key: value})
        return a_dictionary
