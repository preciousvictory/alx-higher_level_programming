#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
import sys


def print_status():
    """
    Printing the status of the request
    """
    count = 0
    status_code = {"200" : 0, "301" : 0, "400" : 0, "401" : 0, "403" : 0,\
            "404" : 0, "405" : 0, "500" : 0}
    size = 0

    for l in sys.stdin:
        line = l.split()
        
        try:
            status = line[-2]
            size += int(line[-1])
            status_code[status] += 1
        except:
            continue

        if count == 9:
            print("File size: {}".format(size))
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print(key, ":", value)
            count = 0  
        count += 1

    if count < 9:
        print("File size: {}".format(size))
        for key, value in sorted(status_code.item()):
            if value != 0:
                print(key, ":", value)

if __name__ == "__main__":
    print_status()
