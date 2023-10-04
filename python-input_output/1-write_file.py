#!/usr/bin/python3
""" defines a funtion that writes to files """


def write_file(filename="", text=""):
    """ writes input to file """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
