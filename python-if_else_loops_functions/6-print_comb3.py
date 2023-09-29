#!/usr/bin/python3

for i in range(10):
    for i2 in range(i + 1, 10):
        if i != i2:
            if i == 8 and i2 == 9:
                print("{:d}{:d}".format(i, i2))
            else:
                print("{:d}{:d}, ".format(i, i2), end="")
