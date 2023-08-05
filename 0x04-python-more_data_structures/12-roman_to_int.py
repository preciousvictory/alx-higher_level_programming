#!/usr/bin/python3
def roman_to_int(roman_string):
    """a function that converts a Roman numeral to an integer."""
    if type(roman_string) != str or roman_string is None:
        return 0
    all_roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        if roman_string[i] not in all_roman.keys():
            return 0

        if (i + 1) != len(roman_string):
            if all_roman.get(roman_string[i]) >= \
                            all_roman.get(roman_string[i + 1]):
                total += all_roman.get(roman_string[i])
            else:
                total -= all_roman.get(roman_string[i])
        else:
            total += all_roman.get(roman_string[i])
    return total
