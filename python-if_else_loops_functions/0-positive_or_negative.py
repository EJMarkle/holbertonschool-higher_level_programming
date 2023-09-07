#!/usr/bin/python3

import random
number = random.randint(-10, 10)

if number > 0:
    sign = "is positive"
elif number == 0:
    sign = "is zero"
elif number < 0:
    sign = "is negative"

print(f"{number} {sign}")
