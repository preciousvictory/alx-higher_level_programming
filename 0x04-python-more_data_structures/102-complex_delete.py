#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary."""
    k = []
    for key, val in a_dictionary.items():
        if val == value:
            k.append(key)
    for i in k:
        a_dictionary.pop(i)
    return a_dictionary
