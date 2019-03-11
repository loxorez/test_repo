import unittest
import random
from Homework3 import is_year_leap, is_triangle_exist, triangle_type


class TestYear(unittest.TestCase):

    def test_is_year_leap(self):
        self.assertIsNotNone(is_year_leap(random.randint(1, 2000)))
        self.assertEqual(is_year_leap(2020), True)
        self.assertTrue(is_year_leap(2016))
        self.assertNotEqual(is_year_leap(2019), True)
        self.assertFalse(is_year_leap(2018))
        with self.assertRaises(TypeError):
            is_year_leap('String instead int')
        with self.assertRaises(TypeError):
            is_year_leap()


class TestTriangles(unittest.TestCase):

    def test_is_triangle_exists(self):
        self.assertIsNotNone(is_triangle_exist(*[random.randint(1, 100) for i in range(3)]))
        self.assertEqual(is_triangle_exist(7, 8, 12), True)
        self.assertTrue(is_triangle_exist(5, 5, 5))
        self.assertEqual(is_triangle_exist(10, 2, 4), False)
        self.assertFalse(is_triangle_exist(1, 15, 5))
        with self.assertRaises(TypeError):
            is_triangle_exist('4', 6, 2)
        with self.assertRaises(TypeError):
            is_triangle_exist()

    def test_triangle_type(self):
        self.assertIsNotNone(triangle_type(8, 5, 7))
        self.assertEqual(triangle_type(5, 5, 5), 'Equilateral triangle')
        self.assertEqual(triangle_type(8, 8, 12), 'Isosceles triangle')
        self.assertEqual(triangle_type(71, 81, 63), 'Versatile triangle')
        self.assertEqual(triangle_type(56, 1, 94), 'Not a triangle')
        with self.assertRaises(TypeError):
            triangle_type('7', 14, 27)
        with self.assertRaises(TypeError):
            triangle_type()

