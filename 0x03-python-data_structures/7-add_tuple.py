#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        if len(tuple_a) is 0 or len(tuple_a) is 1:
                tuple_a = (0, 0)

        if len(tuple_b) is 0:
                tuple_b = (0, 0)
        elif len(tuple_b) is 1:
                tuple_b = (tuple_b[0], 0)
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
