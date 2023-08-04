#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list"""
    sum_ = 0
    num = []
    for i in my_list:
        if i not in num:
            sum_ += i
        num.append(i)
    return sum_
