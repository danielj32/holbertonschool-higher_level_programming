#!/usr/bin/python3
'''request and display header'''
if __name__ == "__main__":
    import requests
    import sys

    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
