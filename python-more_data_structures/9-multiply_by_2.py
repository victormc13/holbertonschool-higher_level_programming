#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dict = dict(map(lambda kv: (kv[0], kv[1] * 2), a_dictionary.items()))

    return (new_dict)
