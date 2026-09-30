import unittest
from basic_shape import BasicShape

class TestBasicShape(unittest.TestCase):
    def test_instantiate(self):
        with self.assertRaises(TypeError):
            BasicShape("abstract")

    def test_validation_type(self):
        from basic_shapes.circle import Circle
        c = Circle(0, 0, 1)
        with self.assertRaises(TypeError):
            c.name = 123

    def test_validation_empty(self):
        from basic_shapes.circle import Circle
        c = Circle(0, 0, 1)
        with self.assertRaises(TypeError):
            c.name = 123
    def test_read_only(self):
        from basic_shapes.circle import Circle
        c = Circle(0, 0, 1)
        with self.assertRaises(AttributeError):
            c.area = 10

if __name__ == "__main__":
    unittest.main()
