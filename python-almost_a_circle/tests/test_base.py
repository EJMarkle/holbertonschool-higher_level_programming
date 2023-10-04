#!/usr/bin/python3
""" Test cases for Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for Base class """

    def test_id_incrementation(self):
        """ Test id incrementation """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_set(self):
        """ Test id is manually set """
        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_id_set_negative(self):
        """ Test id set with a negative value """
        b4 = Base(-10)
        self.assertEqual(b4.id, -10)

    def test_id_set_to_zero(self):
        """ Test id set to zero """
        b5 = Base(0)
        self.assertEqual(b5.id, 0)

    def test_id_set_string(self):
        """ Test id set to a string """
        b6 = Base("test")
        self.assertEqual(b6.id, "test")


if __name__ == '__main__':
    unittest.main()
