#!/usr/bin/python3
import sys
if __name__ == "__main__":
        if len(sys.argv) == 1:
                print(0)
        elif len(sys.argv) == 2:
                print(sys.argv[1])
        else:
                sum = 0
                for j in range(1, len(sys.argv)):
                        ad = int(sys.argv[j])
                        sum = sum + ad
                print(sum)
