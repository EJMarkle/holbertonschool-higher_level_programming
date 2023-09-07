#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

lastdig = abs(number) % 10

if number < 0:
    lastdig = -lastdig

if lastdig > 5:
    case = "and is greater than 5"
elif lastdig == 0:
    case = "and is 0"
else:
    case = "and is less than 6 but not 0"

print(f"Last digit of {number} is {lastdig} {case}")
