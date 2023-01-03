#!/usr/bin/python3


def safe_print_division(a, b):
    x = None
    try:
        x = int(a) / int(b)
        print("Inside result: {:d}".format(int(x)))
    except ZeroDivisionError:
        print("Inside result: None")
    return x
