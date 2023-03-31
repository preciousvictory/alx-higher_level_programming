#!/usr/bin/python3
"""find_peak"""


def find_peak(list_):
    """a function that finds a peak in a list of unsorted integers."""
    len_ = len(list_)

    if len_ == 0:
        return None
    if len_ == 1:
        return list_[0]
    if len_ == 2:
        if list_[0] >= list_[1]:
            return list_[0]
        elif list_[1] >= list_[0]:
            return list_[1]

    peak = []
    for i in range(0, len_):
        val = list_[i]
        if i > 0 and i < len_ - 1 and list_[i - 1] <= val and list_[i + 1] <= val:
            peak.append(val)

    return max(peak)
