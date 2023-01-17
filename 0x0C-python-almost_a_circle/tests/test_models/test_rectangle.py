#!/usr/bin/python3
from io import StringIO
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
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

    def test_str__(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        p = "[Rectangle] (12) 2/1 - 4/6\n"

        with patch('sys.stdout', new = StringIO()) as f_out:
            print(r1)
            self.assertEqual(f_out.getvalue(), p)


if __name__ == '__main__':
    unittest.main()
