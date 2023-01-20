#!/usr/bin/python3
from io import StringIO
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class - Rectangle"""

    def setUp(self):
        """Imports module, instantiates class"""
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_validation(self):
        """Test if exception are raised"""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
            self.assertEqual(e.exception, "height must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle("2", 10)
            self.assertEqual(e.exception, "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 3, "2")
            self.assertEqual(e.exception, "y must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, "3", -1)
            self.assertEqual(e.exception, "x must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
            self.assertEqual(e.exception, "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 10)
            self.assertEqual(e.exception, "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, -1)
            self.assertEqual(e.exception, "height must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
            self.assertEqual(e.exception, "height must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
            self.assertEqual(e.exception, "y must be >= 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -13, 2)
            self.assertEqual(e.exception, "x must be >= 0")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
            self.assertEqual(e.exception, "width must be > 0")

        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2)
            r.x = {}
            self.assertEqual(e.exception, "x must be an integer")

    def test_area(self):
        """Test area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 2, -13, 2)
            self.assertEqual(r.area(), "x must be >= 0")

    def test_display(self):
        """Test display() method
        checks if the function prints correctly to stdout"""
        r = Rectangle(4, 6)
        a = """\
####
####
####
####
####
####
"""

        with patch('sys.stdout', new = StringIO()) as f_out:
            r.display()
        self.assertEqual(f_out.getvalue(), a)

        r1 = Rectangle(2, 2)
        a = """\
##
##
"""
        with patch('sys.stdout', new = StringIO()) as f_out:
            r1.display()
            self.assertEqual(f_out.getvalue(), a)

        r2 = Rectangle(2, 3, 2, 2)
        a= """\


  ##
  ##
  ##
"""
        with patch('sys.stdout', new = StringIO()) as f_out:
            r2.display()
            self.assertEqual(f_out.getvalue(), a)

        r3 = Rectangle(3, 2, 1, 0)
        a =  """\
 ###
 ###
"""
        with patch('sys.stdout', new = StringIO()) as f_out:
            r3.display()
            self.assertEqual(f_out.getvalue(), a)

    def test___str__(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        p = "[Rectangle] (12) 2/1 - 4/6\n"

        with patch('sys.stdout', new = StringIO()) as f_out:
            print(r1)
            self.assertEqual(f_out.getvalue(), p)

    def test_update(self):
        """Test the update method"""
        r1 = Rectangle(10, 10, 10, 10)
        
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(9, 2)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)

    def test_to_dictionary(self):
        """Test method"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)

        a = {'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, a);

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)

        self.assertIsNot(r1, r2)


if __name__ == '__main__':
    unittest.main()
