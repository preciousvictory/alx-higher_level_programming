#!/usr/bin/python3
"""
inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
     a function that inserts a line of text to a file, after each line
     containing a specific string (see example):
    """
    with open(filename, 'r+', encoding="utf-") as f:
        n = 0
        file_ = f.readlines()
        position = []
        for line in file_:
            i = 0
            for l in line:
                if l == search_string[0]:
                    if line[i:i + len(search_string)] == search_string[0:len(search_string)]:
                        position.append(n)
                i += 1
            n += 1

        for p in position:
            s = position.index(p)
            for i in range(len(file_)):
                if i == p:
                    file_.insert(i + s + 1, new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(file_)
