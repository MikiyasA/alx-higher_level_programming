#!/usr/bin/python3

"""
usittest for class Rectangle

"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRect(unittest.TestCase):
    """ The unittest class to test the outputs """

    def setUp(self):
        """ The method invoked for each test """
        Base._Base__nb_objects = 0

    def test_rec_a1(self):
        """ The the attributs of rectangle """
        r = Rectangle(1, 3)
        self.assertEqual(r.width, 1)

    def test_rec_a2(self):
        """ The the attributs of rectangle """
        r = Rectangle(1, 3)
        self.assertEqual(r.height, 3)

    def test_rec_a3(self):
        """ The the attributs of rectangle """
        r = Rectangle(1, 3)
        self.assertEqual(r.x, 0)

    def test_rec_a4(self):
        """ The the attributs of rectangle """
        r = Rectangle(1, 3)
        self.assertEqual(r.y, 0)

    def test_rec_b1(self):
        """ The the attributs of rectangle """
        r = Rectangle(12, 19, 21, 27)
        self.assertEqual(r.width, 12)

    def test_rec_b2(self):
        """ The the attributs of rectangle """
        r = Rectangle(12, 19, 21, 27)
        self.assertEqual(r.height, 19)

    def test_rec_b3(self):
        """ The the attributs of rectangle """
        r = Rectangle(12, 19, 21, 27)
        self.assertEqual(r.x, 21)

    def test_rec_b4(self):
        """ The the attributs of rectangle """
        r = Rectangle(11, 19, 21, 27)
        self.assertEqual(r.y, 27)

    def test_id_rec_1(self):
        """ The the id using subclass Rectangle """
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)

    def test_id_rec_2(self):
        """ The the id using subclass Rectangle """
        r = Rectangle(10, 2, 0, 0, 21)
        self.assertEqual(r.id, 21)

    def test_id_rec_3(self):
        """ The the id using subclass Rectangle """
        r = Rectangle(10, 2, 0, 0, 999)
        self.assertEqual(r.id, 999)

    def test_id_rec_4(self):
        """ The the id using subclass Rectangle """
        r = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r.id, 1)

    def test_rec_w_int_1(self):
        """ Test the value of width is intger """
        self.assertRaises(TypeError, Rectangle, ('10', 2))

    def test_rec_w_int_2(self):
        """ Test the value of width is intger """
        self.assertRaises(TypeError, Rectangle, ((10), 2))

    def test_rec_w_int_3(self):
        """ Test the value of width is intger """
        self.assertRaises(TypeError, Rectangle, ('w', 2))

    def test_rec_w_int_4(self):
        """ Test the value of width is intger """
        self.assertRaises(TypeError, Rectangle, ([10], 2))

    def test_rec_w_int_5(self):
        """ Test the value of width is intger """
        self.assertRaises(TypeError, Rectangle, ("10", 2))

    def test_rec_h_int_1(self):
        """ Test the value of height is intger """
        self.assertRaises(TypeError, Rectangle, (2, '19'))

    def test_rec_h_int_2(self):
        """ Test the value of height is intger """
        self.assertRaises(TypeError, Rectangle, (2, (19)))

    def test_rec_h_int_3(self):
        """ Test the value of height is intger """
        self.assertRaises(TypeError, Rectangle, (2, 'g'))

    def test_rec_h_int_4(self):
        """ Test the value of height is intger """
        self.assertRaises(TypeError, Rectangle, (2, [19]))

    def test_rec_h_int_5(self):
        """ Test the value of height is intger """
        self.assertRaises(TypeError, Rectangle, (2, "19"))

    def test_rec_x_int_1(self):
        """ Test the value of x is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, '21'))

    def test_rec_x_int_2(self):
        """ Test the value of x is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, (21)))

    def test_rec_x_int_3(self):
        """ Test the value of x is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, 'x'))

    def test_rec_x_int_4(self):
        """ Test the value of x is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, [21]))

    def test_rec_x_int_5(self):
        """ Test the value of x is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, "21"))

    def test_rec_y_int_1(self):
        """ Test the value of y is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, 21, '27'))

    def test_rec_y_int_2(self):
        """ Test the value of y is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, 21, (27)))

    def test_rec_y_int_3(self):
        """ Test the value of y is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, 21, 'x'))

    def test_rec_y_int_4(self):
        """ Test the value of y is intger """
        self.assertRaises(TypeError, Rectangle, (2, 19, 21, [27]))

    def test_rec_y_int_5(self):
        """ Test the value of y is intger """
        self.assertRaises(TypeError, Rectangle, ('2', 19, 21, "27"))

    def test_rect_w_val_1(self):
        """ Test the value of width is > 0 """
        r = Rectangle(12, 19)
        self.assertEqual(r.width, 12)

    def test_rect_w_val_2(self):
        """ Test the value of width is > 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(-1, 19)

    def test_rect_w_val_3(self):
        """ Test the value of width is > 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(0, 19)

    def test_rect_w_val_4(self):
        """ Test the value of width is > 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(-111, 19)

    def test_rect_h_val_1(self):
        """ Test the value of height is > 0 """
        r = Rectangle(12, 19)
        self.assertEqual(r.height, 19)

    def test_rect_h_val_2(self):
        """ Test the value of height is > 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(12, 0)

    def test_rect_h_val_3(self):
        """ Test the value of height is > 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(12, -1)

    def test_rect_h_val_4(self):
        """ Test the value of height is > 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(12, -111)

    def test_rect_x_val_1(self):
        """ Test the value of x is >= 0 """
        r = Rectangle(12, 19, 21)
        self.assertEqual(r.x, 21)

    def test_rect_x_val_2(self):
        """ Test the value of x is >= 0 """
        r = Rectangle(12, 19, 0)
        self.assertEqual(r.x, 0)

    def test_rect_x_val_3(self):
        """ Test the value of x is >= 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(12, 19, -1)

    def test_rect_x_val_4(self):
        """ Test the value of x is >= 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(12, 19, -111)

    def test_rect_y_val_1(self):
        """ Test the value of y is >= 0 """
        r = Rectangle(12, 19, 21, 27)
        self.assertEqual(r.y, 27)

    def test_rect_y_val_2(self):
        """ Test the value of y is >= 0 """
        r = Rectangle(12, 19, 21, 0)
        self.assertEqual(r.y, 0)

    def test_rect_y_val_3(self):
        """ Test the value of y is >= 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(12, 19, 21, -1)

    def test_rect_y_val_4(self):
        """ Test the value of y is >= 0 """
        with self.assertRaises(ValueError):
            n = Rectangle(12, 19, 21, -111)

    def test_rect_area_1(self):
        """ Test the return value of method area """
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rect_area_2(self):
        """ Test the return value of method area """
        r = Rectangle(3, 7, 0)
        self.assertEqual(r.area(), 21)

    def test_rect_area_3(self):
        """ Test the return value of method area """
        r = Rectangle(3, 10, 1, 3)
        self.assertEqual(r.area(), 30)

    def test_rect_area_4(self):
        """ Test the return value of method area """
        with self.assertRaises(ValueError):
            r = Rectangle(3, 0)

    def test_rect_area_5(self):
        """ Test the return value of method area """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)

    def test_displ_1(self):
        """ Test string printed """
        r = Rectangle(3, 4)
        res = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.display()
            self.assertEqual(strout.getvalue(), res)

    def test_displ_2(self):
        """ Test string printed """
        r = Rectangle(2, 3)
        res = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.display()
            self.assertEqual(strout.getvalue(), res)

    def test_str_1(self):
        """ Test string printed """
        r = Rectangle(3, 5)
        res = "[Rectangle] (1) 0/0 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_2(self):
        """ Test string printed """
        r = Rectangle(3, 5, 7)
        res = "[Rectangle] (1) 7/0 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_3(self):
        """ Test string printed """
        r = Rectangle(3, 5, 7, 10)
        res = "[Rectangle] (1) 7/10 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_4(self):
        """ Test string printed """
        r = Rectangle(3, 5, 7, 10, 21)
        res = "[Rectangle] (21) 7/10 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_displ_a1(self):
        """ Test string printed """
        r = Rectangle(3, 4, 0, 0)
        res = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.display()
            self.assertEqual(strout.getvalue(), res)

    def test_displ_a2(self):
        """ Test string printed """
        r = Rectangle(3, 4, 3, 3)
        res = "\n\n\n   ###\n   ###\n   ###\n   ###\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.display()
            self.assertEqual(strout.getvalue(), res)

    def test_displ_a3(self):
        """ Test string printed """
        r = Rectangle(3, 4, 1, 3)
        res = "\n\n\n ###\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.display()
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_1(self):
        """ Test string printed with update method"""
        r = Rectangle(21, 22, 23, 24, 27)
        res = "[Rectangle] (27) 23/24 - 21/22\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_2(self):
        """ Test string printed with update method"""
        r = Rectangle(21, 22, 23, 24, 27)
        res = "[Rectangle] (19) 23/24 - 21/22\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(19)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_3(self):
        """ Test string printed with update method"""
        r = Rectangle(21, 22, 23, 24, 27)
        res = "[Rectangle] (19) 23/24 - 1/22\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(19, 1)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_4(self):
        """ Test string printed with update method"""
        r = Rectangle(21, 22, 23, 24, 27)
        res = "[Rectangle] (19) 23/24 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(19, 1, 2)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_5(self):
        """ Test string printed with update method"""
        r = Rectangle(21, 22, 23, 24, 27)
        res = "[Rectangle] (19) 3/24 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(19, 1, 2, 3)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_6(self):
        """ Test string printed with update method"""
        r = Rectangle(21, 22, 23, 24, 27)
        res = "[Rectangle] (19) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(19, 1, 2, 3, 4)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_k1(self):
        """ Test string printed with update method"""
        r = Rectangle(1, 2, 3, 4, 7)
        res = "[Rectangle] (7) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_k2(self):
        """ Test string printed with update method"""
        r = Rectangle(1, 2, 3, 4, 7)
        res = "[Rectangle] (19) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(id=19)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_k3(self):
        """ Test string printed with update method"""
        r = Rectangle(1, 2, 3, 4, 7)
        res = "[Rectangle] (19) 3/4 - 30/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(id=19, width=30)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_k4(self):
        """ Test string printed with update method"""
        r = Rectangle(1, 2, 3, 4, 7)
        res = "[Rectangle] (19) 3/4 - 30/32\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(id=19, width=30, height=32)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_k5(self):
        """ Test string printed with update method"""
        r = Rectangle(1, 2, 3, 4, 7)
        res = "[Rectangle] (19) 33/4 - 30/32\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(id=19, width=30, height=32, x=33)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_str_updt_k6(self):
        """ Test string printed with update method"""
        r = Rectangle(1, 2, 3, 4, 7)
        res = "[Rectangle] (19) 33/34 - 30/32\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            r.update(id=19, width=30, height=32, x=33, y=34)
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_dic_1(self):
        """ Test the output of methon to_dictionary """
        r = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r)
            self.assertEqual(strout.getvalue(), res)

    def test_dic_1(self):
        """ Test the ourput of method to_dictionart """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dic = r1.to_dictionary()
        r1.update(**r1_dic)
        res1 = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}\n"

        with patch('sys.stdout', new=StringIO()) as strout:
            print(r1_dic)
            self.assertEqual(strout.getvalue(), res1)

        res2 = "[Rectangle] (1) 1/9 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(r1)
            self.assertEqual(strout.getvalue(), res2)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
