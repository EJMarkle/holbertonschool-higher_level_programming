#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

absnum = abs(number)

lastdig = absnum % 10

if lastdig > 5:
    case = "and is greater than 5"
elif lastdig == 0:
    case = "and is 0"
elif lastdig < 6 and !=0:
    case = "and is less than 6 but not 0"

print(f"Last digit of {number} is {lastdig} {case}")
