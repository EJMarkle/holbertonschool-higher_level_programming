#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_val = 0

    for i in range(len(roman_string) - 1, -1, -1):
        value = roman_values.get(roman_string[i], 0)

        if value < prev_val:
            result -= value
        else:
            result += value
        prev_val = value
    return result
