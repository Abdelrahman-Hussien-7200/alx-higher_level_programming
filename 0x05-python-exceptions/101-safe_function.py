#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        output = fct(*args)
        return output
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
