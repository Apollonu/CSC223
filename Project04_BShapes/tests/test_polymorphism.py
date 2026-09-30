import unittest
import math

from circle import Circle
from rectangle import Rectangle
from square import Square
from basic_shape import BasicShape

class TestPolymorphism(unittest.TestCase):
    def setUp(self):
        self.shapes = [
            Circle(0, 0, 1),
            Rectangle(3, 2),
            Square(7)
        ]

    def test_basicshape(self):
        for i in self.shapes:
            self.assertIsInstance(i, BasicShape)

    def test_access(self):
        for i in self.shapes:
            self.assertTrue(hasattr(i, "name"))
            self.assertTrue(hasattr(i, "area"))

    def test_polymorphism(self):
        expected = [
            math.pi * 1 ** 2,
            3 * 2,
            7 * 7
        ]
        for i, e in zip(self.shapes, expected):
            self.assertAlmostEqual(i.area, e)

    def test_without_checks(self):
        total = 0.0
        for shape in self.shapes:
            total += shape.area
        self.assertAlmostEqual(total, math.pi * 5 + 16)

if __name__ == "__main__":
    unittest.main()
