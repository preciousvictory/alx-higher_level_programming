#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
