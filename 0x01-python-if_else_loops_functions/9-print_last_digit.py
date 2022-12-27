#!/usr/bin/python3
def print_last_digit(number):
    l = number % 10
    print('{}'.format(l), end="")
    return l
