#!/usr/bin/python3
""" defines a function to append to file """


def append_write(filename="", text=""):
    """ appends text to specified file """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
