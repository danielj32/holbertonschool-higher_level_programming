#!/usr/bin/python3
for n in range(122, 96, -1):
    setoff = 0
    if n % 2:
        setoff = 32
    print("{:s}".format(chr(n - setoff)), end="")
