#!/usr/bin/python3
from io import StringIO
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class - Base"""

    def test_id(self):
        """Test id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b3.id - 2)

        b5 = Base(12)
        self.assertEqual(b5.id, 12)

    def test_instance(self):
        """tests to check instance"""
        r1 = Base()
        self.assertTrue(isinstance(r1, Base))

    def test_attribute(self):
        """Test if it has all required attributes"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_to_json_string(self):
        """Test method
        returns the JSON string representation of list_dictionaries
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        a = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        json_dictionary = Base.to_json_string([dictionary])

        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        """test method sate_to_file"""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(type(f.read()), str)

        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_from_json_string(self):
        """Test from_json_string"""
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

        list_input = [
                {'id': 89, 'width': 10, 'height': 4}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

        list_input = [
                {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
                {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        """Test create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        """Test load_from_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertIsNot(list_rectangles_input[0], list_rectangles_output[0])
        self.assertIsNot(list_rectangles_input[1], list_rectangles_output[1])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertIsNot(list_rectangles_input[0], list_rectangles_output[0])
        self.assertIsNot(list_rectangles_input[1], list_rectangles_output[1])


if __name__ == '__main__':
    unittest.main()
