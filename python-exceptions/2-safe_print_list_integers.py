#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    printed = 0

    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            printed += 1
        except (ValueError, TypeError, IndexError):
            if isinstance(my_list[element], int):
                raise
        finally:
            counter += 1

    print()
    return printed


