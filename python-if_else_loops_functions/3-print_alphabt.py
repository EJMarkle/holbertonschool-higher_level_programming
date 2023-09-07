#!/usr/bin/python3

i = 97
while i > 96 and i < 123:
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
    i = i + 1
print()
