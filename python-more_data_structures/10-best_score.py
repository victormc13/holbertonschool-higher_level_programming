#!/usr/bin/python3

from functools import reduce


def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    def best_value(k1, k2):
        if a_dictionary[k1] > a_dictionary[k2]:
            return k1
        else:
            return k2

    best_key = reduce(best_value, a_dictionary.keys())

    return (best_key)
