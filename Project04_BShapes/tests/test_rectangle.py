import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(4, 3)

    def test_area(self):
        self.assertEqual(self.r.area, 12)

    def test_length_type(self):
        with self.assertRaises(TypeError):
            self.r.length = "long"

    def test_width_type(self):
        with self.assertRaises(TypeError):
            self.r.width = None

    def test_length_zero(self):
        with self.assertRaises(ValueError):
            self.r.length = 0

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            self.r.width = -1

    def test_length_change(self):
        self.r.length = 5
        self.assertEqual(self.r.area, 5 *4)

    def test_width_change(self):
        self.r.width = 7
        self.assertEqual(self.r.area, 4 * 7)

    def test_failed_assignment(self):
        or_length = self.r.length
        or_width = self.r.width
        or_area = self.r.area
        with self.assertRaises(ValueError):
            self.r.length = -1
        self.assertEqual(self.r.length, or_length)
        self.assertEqual(self.r.width, or_width)
        self.assertEqual(self.r.area, or_area)

if __name__ == "__main__":
    unittest.main()
