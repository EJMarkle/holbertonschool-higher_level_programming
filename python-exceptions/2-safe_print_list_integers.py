#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    i = 0
    try:
        while cnt < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                cnt += 1
            i += 1
        print()
        return cnt
    except IndexError:
        print()
        return cnt
