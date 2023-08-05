#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if not a_dictionary:
        return None

    big = list(a_dictionary.values())[0]     
    for value in a_dictionary.values():
        if value > big:
            big = value
    key = [i for i in a_dictionary if a_dictionary[i] == big]
    return key[0]
