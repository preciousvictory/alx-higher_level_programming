#!/usr/bin/python3
"""find_peak"""

def find_peak(list_):
    """a function that finds a peak in a list of unsorted integers."""
    l = len(list_)

    if l == 0:
        return None
    if l== 1:
        return list_[0]
    if l == 2:
        if list_[0] >= list_[1]:
            return list_[0]
        elif list_[1] >= list_[0]:
            return list_[1]

    peak = []
    for i in range(0, l):
        val = list_[i]
        if i > 0 and i < l - 1 and list_[i - 1] <= val and list_[i + 1] <= val:
            peak.append(val)
            print(val)

    return max(peak)
