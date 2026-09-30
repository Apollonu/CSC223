import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s = Square(4)

    def test_invariant(self):
        self.assertEqual(self.s.side, 4)
        self.assertEqual(self.s.length, 4)
        self.assertEqual(self.s.width, 4)

    def test_area(self):
        self.assertEqual(self.s.area, 16)

    def test_setter_all(self):
        self.s.side = 7
        self.assertEqual(self.s.side, 7)
        self.assertEqual(self.s.length, 7)
        self.assertEqual(self.s.width, 7)
        self.assertEqual(self.s.area, 49)

    def test_length_setter_square(self):
        self.s.length = 2
        self.assertEqual(self.s.side, 2)
        self.assertEqual(self.s.width, 2)

    def test_width_setter_square(self):
        self.s.width= 3
        self.assertEqual(self.s.side, 3)
        self.assertEqual(self.s.width, 3)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            self.s.side = "large"

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            self.s.side = 0

    def test_failed_assignment(self):
        or_side = self.s.side
        or_area = self.s.area
        with self.assertRaises(ValueError):
            self.s.side = -1
        self.assertEqual(self.s.side, or_side)
        self.assertEqual(self.s.area, or_area)

if __name__ == "__main__":
    unittest.main()
