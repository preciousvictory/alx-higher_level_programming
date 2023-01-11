#!/usr/bin/python3
''' a class Student that defines a student
'''


class Student:
    """ My class
    """
    def __init__(self, first_name, last_name, age):
        '''method __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''method to_json
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved.
            Otherwise, all attributes must be retrieved
        '''
        if type(attrs) == list and all(type(in_list) == str for in_list in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

        return self.__dict_
    _
