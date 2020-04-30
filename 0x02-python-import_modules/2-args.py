#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
        print("0 arguments.")
if len(sys.argv) == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(sys.argv[1]))
else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for count in range(1, len(sys.argv)):
                print("{}: {}".format(count,  sys.argv[count]))
