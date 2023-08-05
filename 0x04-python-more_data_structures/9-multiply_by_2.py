#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    a_dict = {}
    for key, value in a_dictionary.items():
        a_dict.update({key: (value * 2)})
    return a_dict
