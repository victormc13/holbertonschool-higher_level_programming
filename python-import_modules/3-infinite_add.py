#!/usr/bin/pytho3

if __name__ == "__main__":

    from sys import argv

    result = 0

    for argument in range(1, len(argv)):
        result += int(argv[argument])
    print(result)
