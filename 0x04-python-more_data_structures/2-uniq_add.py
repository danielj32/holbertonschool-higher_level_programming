#!/usr/bin/python3
def uniq_add(my_list=[]):
        cpy_list = set(my_list)
        result = 0
        for i in cpy_list:
                result = result + i
        return result
