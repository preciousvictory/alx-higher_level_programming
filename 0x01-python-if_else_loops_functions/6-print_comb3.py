#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i != j and i < j:
            print('{}{}'.format(i, j), end="")
            if i + j == 17 and j == 9:
                print("")
            else:
                print(', ', end="")
