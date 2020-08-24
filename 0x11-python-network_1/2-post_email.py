#!/usr/bin/python3
'''Take a email '''
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode("ascii")
    reqst = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(reqst) as response:
        print(response.read().decode('utf-8'))
