#!/usr/bin/python3
""" reads and prints a file """


def read_file(filename=""):
    """ prints the contents of a given file """
    try:
        file = open(filename, "r", encoding="utf-8")
        for line in file:
            print(line, end="")
        file.close()
    except FileNotFoundError:
        pass
