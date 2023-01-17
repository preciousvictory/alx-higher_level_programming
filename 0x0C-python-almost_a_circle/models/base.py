#!/usr/bin/python3
"""
create the Base class
"""
import json


class Base:
    """
    the first class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method hat returns the JSON string representation of
        list_dictionaries
        If list_dictionaries is None or empty, return the string: "[]"
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         class methodthat writes the JSON string representation of
         list_objs to a file:
         The filename must be: <Class name>.json - example: Rectangle.json
        """
        filename = "{}.json".format(cls.__name__)
        text = []

        if list_objs is not None:
            for r in list_objs:
                r = r.to_dictionary()
                json_dict = json.loads(cls.to_json_string(r))
                text.append(json_dict)

        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(text, f)

    def from_json_string(json_string):
        """
        static method  that returns the list of the JSON string
        representation json_string:
        """
        con = []
        if json_string is None:
            return con

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method  that returns an instance with all attributes already set:
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            r2 = Rectangle(1, 1)
        elif cls is Square:
            r2 = Square(2)
        else:
            r2 = None

        r2.update(**dictionary)
        return(r2)
