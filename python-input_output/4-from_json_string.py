#!/usr/bin/python3
""" a function that gets an object form json string """
import json


def from_json_string(my_str):
    """ returns object from json """
    return json.loads(my_str)
