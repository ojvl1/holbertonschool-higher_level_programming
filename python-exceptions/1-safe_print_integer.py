#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is not int:
            print("{:d}".format(value))
            return True
    except (ValueError, TypeError):
        return False
