#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list"""
    idx = 0
    new_list = my_list[0:]
    for i in new_list:
        if search == i:
            new_list[idx] = replace
        idx +=1
    return new_list
