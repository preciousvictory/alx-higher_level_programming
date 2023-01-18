#!/usr/bin/python3
import os
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test class - Base"""
    def test_instance(self):
        """tests to check instance"""
        r1 = Base()
        self.assertTrue(isinstance(r1, Base))

    def test_attribute(self):
        """Test if it has all required attributes"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_id(self):
        """Test id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)
        self.assertEqual(b2.id, 2)

        c = 0
        for i in range(5):
            Base()
            c += 1

        b4 = Base()
        self.assertEqual(b4.id, 3 + c + 1)

        b5 = Base(12)
        self.assertEqual(b5.id, 12)


if __name__ == '__main__':
    unittest.main()
