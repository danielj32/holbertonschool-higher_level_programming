#!/usr/bin/python3
''' send a request to url and display '''

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
