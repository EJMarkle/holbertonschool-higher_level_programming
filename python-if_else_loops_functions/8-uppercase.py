#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_ascii = ord(char) - 32
            result += chr(upper_ascii)
        else:
            result += char
    print(result)
