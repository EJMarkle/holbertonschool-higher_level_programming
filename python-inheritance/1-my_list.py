#!/usr/bin/python3
""" a class that will inherit from list """


class MyList(list):
    """ the class that holds the sorted printer """
    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
