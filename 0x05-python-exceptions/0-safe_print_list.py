#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for ct in my_list:
            if n < x:
                print("{}".format(ct), end="")
                n += 1
        print('')
        return n
    except SyntaxError:
        print("error solution")
