#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is False:
        first = None
        lenght = 0
    first = sentence[0]
    lenght = len(sentence)
    return (lenght, first)
