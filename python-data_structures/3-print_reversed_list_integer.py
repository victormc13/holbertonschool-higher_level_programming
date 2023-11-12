#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if my_list == None:
        return []
    reversed_list = my_list[::-1]
    for element in reversed_list:
        print("{:d}".format(element))
