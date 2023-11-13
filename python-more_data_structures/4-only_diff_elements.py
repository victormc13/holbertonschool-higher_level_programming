#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    new_set1 = list(set_1.difference(set_2))
    new_set2 = list(set_2.difference(set_1))

    set_3 = new_set1 + new_set2
    set_3.sort()

    return set_3
