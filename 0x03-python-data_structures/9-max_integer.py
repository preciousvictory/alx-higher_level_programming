#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is False:
        return None
    big = 0
    for i in my_list:
        if i > big:
            big = i
    return big
