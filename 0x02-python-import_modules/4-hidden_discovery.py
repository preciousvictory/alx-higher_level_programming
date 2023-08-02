#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    list_ = []
    for name in names:
        if not name.startswith("__"):
            list_.append(name)
    sort = sorted(list_)
    for i in sort:
        print(i)
