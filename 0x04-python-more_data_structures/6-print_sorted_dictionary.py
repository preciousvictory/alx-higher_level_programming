#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    d = sorted(a_dictionary)
    for key in d:
        print(f'{key}: {a_dictionary[key]}')
