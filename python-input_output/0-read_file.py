#!/usr/bin/python3
""" reads and prints a file """


def read_file(filename=""):
    """ prints the contents of a given file """
    if filename != "":
        with open(filename, encoding="utf-8") as cur_file:
            print(cur_file.read(), end="")
