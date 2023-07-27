#!/usr/bin/python3
def no_c(my_string):
    """a function that removes all characters c and C from a string."""
    my_list = list(my_string)

    for i in range(len(my_list) - 2):
        if my_list[i] == 'c':
            my_list.pop(i)

        if my_list[i] == 'C':
            my_list.pop(i)

    new_str = ""
    for i in my_list:
        new_str += i
    return new_str
