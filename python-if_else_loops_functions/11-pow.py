#!/usr/bin/python3

def pow(a, b):
    result = a ** b
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result
