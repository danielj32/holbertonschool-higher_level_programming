#!/usr/bin/python3
''' send a request to url '''
if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            li = str(res.read().decode('utf-8'))
            print(li)
    except urllib.error.HTTPError as error:
            print("Error code: {}".format(error.code))
