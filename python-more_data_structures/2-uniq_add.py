#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqint = set()
    cnt = 0

    for num in my_list:
        if num not in uniqint:
            uniqint.add(num)
            cnt += num
    return cnt
