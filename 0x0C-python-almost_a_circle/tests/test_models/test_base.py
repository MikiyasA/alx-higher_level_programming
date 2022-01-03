#!/usr/bin/python3
"""
Unittest for class base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ The unittest class to test the outputs """

    def test_id_1(self):
        """ Tests the id is assigned correctly """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_2(self):
        """ Tests the id is assigned correctly """
        b = Base()
        self.assertEqual(b.id, 2)

    def test_id_3(self):
        """ Tests the id is assigned correctly """
        b = Base()
        self.assertEqual(b.id, 3)

    def test_id_4(self):
        """ Tests the id is assigned correctly """
        b = Base(86)
        self.assertEqual(b.id, 86)

    def test_id_5(self):
        """ Tests the id is assigned correctly """
        b = Base(94)
        self.assertEqual(b.id, 94)

    def test_id_6(self):
        """ Tests the id is assigned correctly """
        b = Base()
        self.assertEqual(b.id, 4)
