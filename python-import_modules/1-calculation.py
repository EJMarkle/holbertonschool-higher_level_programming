#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5

addResult = add(a, b)
subResult = sub(a, b)
mulResult = mul(a, b)
divResult = div(a, b)

print("{:d} + {:d} = {:d}".format(a, b, addResult))
print("{:d} - {:d} = {:d}".format(a, b, subResult))
print("{:d} * {:d} = {:d}".format(a, b, mulResult))
print("{:d} / {:d} = {:d}".format(a, b, divResult))
