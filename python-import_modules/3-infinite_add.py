#!/usr/bin/pytho3

if __name__ == "__main__":

    from sys import argv

    result = 0

    for argument in argv[1:]:
        result += int(argument)
    print(f"{result}")
