#!/usr/bin/python3

def uniq_add(my_list=[]):

    my_list = set(my_list)
    result = 0

    for element in my_list:
        result += element

    return (result)
