#!/usr/bin/python3
""" Test cases for Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class """

    def test_attributes(self):
        """ Test Rectangle attributes """
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_negative_width(self):
        """ Test Rectangle with negative width """
        with self.assertRaises(ValueError):
            r2 = Rectangle(-2, 3)

    def test_negative_height(self):
        """ Test Rectangle with negative height """
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, -3)

    def test_width_setter(self):
        """ Test Rectangle width setter """
        r4 = Rectangle(2, 3)
        r4.width = 5
        self.assertEqual(r4.width, 5)

    def test_height_setter(self):
        """ Test Rectangle height setter """
        r5 = Rectangle(2, 3)
        r5.height = 6
        self.assertEqual(r5.height, 6)

    def test_width_setter_negative(self):
        """ Test Rectangle width setter with negative value """
        r6 = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r6.width = -4

    def test_height_setter_negative(self):
        """ Test Rectangle height setter with negative value """
        r7 = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r7.height = -5

    def test_str(self):
        """ Test Rectangle __str__ method """
        r8 = Rectangle(3, 5, 1, 2, 7)
        self.assertEqual(str(r8), "[Rectangle] (7) 1/2 - 3/5")


if __name__ == '__main__':
    unittest.main()
