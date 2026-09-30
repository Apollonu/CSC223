import unittest
import math
from ..circle import Circle

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c = Circle(0, 0, 2)

    def test_area(self):
        expect = math.pi * 2 ** 2
        self.assertAlmostEqual(self.c.area, expect)

    def test_validation_type(self):
        with self.assertRaises(TypeError):
            self.c.radius = "large"

    def test_validation_zero(self):
        with self.assertRaises(ValueError):
            self.c.radius = o

    def test_validation_negative(self):
        with self.assertRaises(ValueError):
            self.c.radius = -5

    def test_recalculation_area(self):
        orig = self.c.area
        self.c.x = 10
        self.c.y = -4
        self.assertEqual(original, self.c.area)

    def test_custom_name(self):
        self.assertEqual(self.c.name, "Circle")
        custom = Circle(0, 0, 1, name = "MyCircle")
        self.assertEqual(custom.name, "MyCircle")

if __name__ == "__main__":
    unittest.main()
