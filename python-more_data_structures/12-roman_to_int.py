#!/usr/bin/python3

def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0

    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    integer_value = 0
    prev_value = 0

    for symbol in reversed(roman_string):

        value = dic[symbol]

        if value < prev_value:
            integer_value -= value
        else:
            integer_value += value

        prev_value = value

    return integer_value
