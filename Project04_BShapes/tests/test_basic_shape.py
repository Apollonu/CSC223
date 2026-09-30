import unittest
from basic_shape import BasicShape
from circle import Circle

class TestBasicShape(unittest.TestCase):
    def test_instantiate_type(self):
        with self.assertRaises(TypeError):
            BasicShape("abstract")

    def test_validation_empty(self):
        c = Circle(0, 0, 1)
        with self.assertRaises(ValueError):
            c.name = ""

    def test_read_only(self):
        c = Circle(0, 0, 1)
        with self.assertRaises(AttributeError):
            c.area = 10

if __name__ == "__main__":
    unittest.main()
