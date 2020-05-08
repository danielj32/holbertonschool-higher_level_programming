#!/usr/bin/python3
def weight_average(my_list=[]):
        tot = 0
        d = 0
        if not my_list:
                return 0
        for y, z in my_list:
                tot += z
                d += y * z
        return d / tot
