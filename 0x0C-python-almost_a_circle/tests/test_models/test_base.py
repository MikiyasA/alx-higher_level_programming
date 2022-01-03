#!/usr/bin/python3
"""
Unittest for class base
"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """ The unittest class to test the outputs """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id_1(self):
        """ Tests the id is assigned correctly """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_2(self):
        """ Tests the id is assigned correctly """
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_id_3(self):
        """ Tests the id is assigned correctly """
        b = Base(86)
        self.assertEqual(b.id, 86)

    def test_id_4(self):
        """ Tests the id is assigned correctly """
        b = Base(94)
        self.assertEqual(b.id, 94)

    def test_id_5(self):
        """ Tests the id is assigned correctly """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
