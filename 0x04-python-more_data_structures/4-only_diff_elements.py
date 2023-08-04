#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ returns a set of all elements present in only one set"""
    d = set_1.symmetric_difference(set_2)
    return d
