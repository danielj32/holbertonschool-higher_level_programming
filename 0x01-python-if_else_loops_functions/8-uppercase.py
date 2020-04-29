#!/usr/bin/python3
def islower(c):
        for k in range(len(str)):
                upper = str[k]
        if ord(str[k]) > 96 and ord(str[k]) < 123:
                upper = chr(ord(str[k]) - 32)
                print("{}".format(upper), end="")
print()
