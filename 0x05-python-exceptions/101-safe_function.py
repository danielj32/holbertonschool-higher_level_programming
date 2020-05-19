#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        func = fct(*args)
        return func
    except Exception as errare:
        sys.stderr.write("Exception: {}\n".format(errare))
        return None
