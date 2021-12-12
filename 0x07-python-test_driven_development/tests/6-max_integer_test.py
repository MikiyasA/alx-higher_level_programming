#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ The unittest class to test the outputs """

    def test_max(self):
        """ Test if max_integer is the maximum value in the list """
        self.assertEqual(max_integer([12, 13, 54, 98]), 98)

    def test_same_num(self):
        self.assertEqual(max_integer([12, 32, 32, 21]), 32)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([1.1, 2.3, 3.3]), 3.3)

    def test_onenum_inlist(self):
        self.assertEqual(max_integer([89]), 89)

    def test_zero_num(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_negetive_num(self):
        self.assertEqual(max_integer([-32, -53, -43]), -32)

    def test_max_at_beg(self):
        self.assertEqual(max_integer([100, 98, 89]), 100)
    def test_optd_num(self):
        self.assertEqual(max_integer([3 + 2, 5 - 1, 2 * 2]), 5)

    def test_large_list(self):
        self.assertEqual(max_integer([1, 21, 32, 43, 33, 53, 23, 64,
                                      23, 54, 65, 76, 45, 76, 95, 94,
                                      39, 56, 76, 78, 89, 79, 62, 60,
                                      10, 20, 30, 40, 50, 60, 70, 80,
                                      99, 88, 77, 66, 55, 44, 22, 11,
                                      123,342, 345, 456, 567, 678, 989,
                                      321, 432, 534, 654,756, 876, 987]), 989)
    def test_string_inlist(self):
        with self.assertRaises(TypeError):
            max_integer([10, '11'])

    def test_tuples_inlist(self):
        self.assertRaises(TypeError, max_integer, [10, (11, 12)])

    def test_only_num(self):
        self.assertRaises(TypeError, max_integer, 1)
