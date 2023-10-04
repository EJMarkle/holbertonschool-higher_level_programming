#!/usr/bin/python3
""" Test cases for Square class """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for Square class """

    def test_attributes(self):
        """ Test Square attributes """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_negative_size(self):
        """ Test Square with negative size """
        with self.assertRaises(ValueError):
            s2 = Square(-2)

    def test_size_setter(self):
        """ Test Square size setter """
        s3 = Square(3)
        s3.size = 7
        self.assertEqual(s3.size, 7)

    def test_size_setter_negative(self):
        """ Test Square size setter with negative value """
        s4 = Square(4)
        with self.assertRaises(ValueError):
            s4.size = -5

    def test_str(self):
        """ Test Square __str__ method """
        s5 = Square(2, 3, 4, 10)
        self.assertEqual(str(s5), "[Square] (10) 3/4 - 2")


if __name__ == '__main__':
    unittest.main()
