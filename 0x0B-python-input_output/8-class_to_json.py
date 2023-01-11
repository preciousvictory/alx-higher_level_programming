#!/usr/bin/python3
"""returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object:

    Agrv: 
        obj: an instance of a Class

    All attributes of the obj Class are serializable: list, dictionary,
    string, integer and boolean
    """
    return obj.__dict__

