import unittest
from binary_expression_tree import BinaryExpressionTree

class TestBinaryExpressionTree(unittest.TestCase):
    def test_addition(self):
        tree = BinaryExpressionTree("4 6 +")
        self.assertAlmostEqual(tree.evaluate(), 10.0)
        self.assertEqual(tree.infix(), "(4 + 6)")

    def test_mixed_oper(self):
        tree = BinaryExpressionTree("6 4 + 10 *")
        self.assertAlmostEqual(tree.evaluate(), 100.0)
        self.assertEqual(tree.infix(), "((6 + 4) * 10)")

    def test_nocomm_order(self):
        tree = BinaryExpressionTree("2 2 / 6 +")
        self.assertAlmostEqual(tree.evaluate(), 7.0)
        self.assertEqual(tree.infix(), "((2 / 2) + 6)")

    def test_decimal_negative(self):
        tree = BinaryExpressionTree("-4 2.2 *")
        self.assertAlmostEqual(tree.evaluate(), -8.8)

    def test_postfix_match(self):
        expr = "6 4 2 * * 2 /"
        tree = BinaryExpressionTree(expr)
        self.assertEqual(tree.postfix(), expr)

    def test_too_few(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree("4 -")

    def test_too_many(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree("8 6 4 /")

    def test_unsupported(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree("6 4 ? *")

    def test_empty(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree("")

    def test_div_zero(self):
        tree = BinaryExpressionTree("7 0 /")
        with self.assertRaises(ZeroDivisionError):
            tree.evaluate()

if __name__ == "__main__":
    unittest.main()
