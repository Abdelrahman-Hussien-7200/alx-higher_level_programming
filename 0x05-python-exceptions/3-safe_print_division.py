#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Result = a / b
    except (ZeroDivisionError, FloatingPointError):
        Result = None
    finally:
        print("Inside result: {}".format(Result))
    return Result
