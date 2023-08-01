#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first = None
        lenght = 0
    else:
        first = sentence[0]
        lenght = len(sentence)
    return (lenght, first)
