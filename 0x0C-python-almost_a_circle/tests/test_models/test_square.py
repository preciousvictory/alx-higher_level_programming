#!/usr/bin/python3
from io import StringIO
import unittest
from unittest.mock import patch
from models.square import Square

class TestSquare(unittest.TestCase):
    """ Test class - Square"""
    def test___str__(self):
        """Test string representation"""
        s1 = Square(5)
        a = "[Square] ({}) 0/0 - 5\n".format(s1.id)

        with patch('sys.stdout', new = StringIO()) as f_out:
            print(s1)
        self.assertEqual(f_out.getvalue(), a)

        s2 = Square(2, 2)
        a = "[Square] ({}) 2/0 - 2\n".format(s2.id)

        with patch('sys.stdout', new = StringIO()) as f_out:
            print(s2)
            self.assertEqual(f_out.getvalue(), a)

        s3 = Square(3, 1, 3)
        a = "[Square] ({}) 1/3 - 3\n".format(s3.id)

        with patch('sys.stdout', new = StringIO()) as f_out:
            print(s3)
            self.assertEqual(f_out.getvalue(), a)

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_display(self):
        """Test the formated representation"""
        s1 = Square(5)
        a = """\
#####
#####
#####
#####
#####
"""
        with patch('sys.stdout', new = StringIO()) as f_out:
            s1.display()
            self.assertEqual(f_out.getvalue(), a)

        s2 = Square(2, 2)
        a = """\
  ##
  ##
"""
        with patch('sys.stdout', new = StringIO()) as f_out:
            s2.display()
            self.assertEqual(f_out.getvalue(), a)

        s3 = Square(3, 1, 3)
        a = """\



 ###
 ###
 ###
"""
        with patch('sys.stdout', new = StringIO()) as f_out:
            s3.display()
            self.assertEqual(f_out.getvalue(), a)

    def test_size_get(self):
        """test size getter"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
            self.assertEqual(e.exception, "width must be an integer")

    def text_update(self):
        """Test update method"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(1, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.id, 1)

        s1.update(1, 2, 3)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.id, 1)

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.size, 2)

        s1.update(x=12)
        self.assertEqual(s1.x, 12)

        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def tests_to_dictionary(self):
        """Test method"""
        s1 = Square(1, 2, 3, 4)
        dict_ = s1.to_dictionary()
        a = {'x': 2, 'y': 3, 'size': 1, 'id': 4}
        self.assertEqual(type(s1.to_dictionary()), dict)

        self.assertEqual(dict_['id'], a['id'])


if __name__ == '__main__':
    unittest.main()
