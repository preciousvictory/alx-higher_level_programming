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
        if type(attrs) == list and \
                all(type(in_list) == str for in_list in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """method reload_from_json
        that replaces all attributes of the Student instance:
        """
        for key, value in json.items():
            if key == 'first_name':
                self.first_name = value
            if key == 'last_name':
                self.last_name = value
            if key == 'age':
                self.age = value
