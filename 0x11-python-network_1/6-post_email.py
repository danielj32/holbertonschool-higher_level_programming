#!/usr/bin/python3
'''request'''
if __name__ == "__main__":
    import requests
    import sys

    dct = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=dct)
    print(req.text)
