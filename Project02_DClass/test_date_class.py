import unittest
from date_class import Date

class TestDate(unittest.TestCase):
    pass

    def test_default_constructor(self):
        cls = Date()

        self.assertEqual(cls.month, 1)
        self.assertEqual(cls.day, 1)
        self.assertEqual(cls.year, 1900)
        self.assertEqual(cls.to_numeric_string(), "01/01/1900")
    def test_valid_constructor(self):
        cls1 = Date(2, 2, 2022)

        self.assertEqual(cls1.month, 2)
        self.assertEqual(cls1.day, 2)
        self.assertEqual(cls1.year, 2022)

        cls2 = Date(2, 29, 2020)

        self.assertTrue(cls2.is_leap_year())
        self.assertEqual(cls2.day, 29)

    def test_invalid_constructors(self):
        with self.assertRaises(ValueError):
            Date(0, 2, 2022)
        with self.assertRaises(ValueError):
            Date(13, 2, 2022)

        with self.assertRaises(ValueError):
            Date(2, 0, 2022)

        with self.assertRaises(ValueError):
            Date(4, 31, 2022)

        with self.assertRaises(ValueError):
            Date(2, 29, 2022)

    def test_read_only(self):
        cls = Date()

        with self.assertRaises(AttributeError):
            cls.month = 2
        with self.assertRaises(AttributeError):
            cls.day = 2
        with self.assertRaises(AttributeError):
            cls.year = 2022

    def test_set_date(self):
        cls1 = Date()

        cls1.set_date(9, 9, 1999)
        self.assertEqual(cls1.month, 9)
        self.assertEqual(cls1.day, 9)
        self.assertEqual(cls1.year, 1999)

        cls2 = Date(1, 1, 100)
        with self.assertRaises(ValueError):
            cls2.set_date(2, 30, 300)
        self.assertEqual(cls2.month, 1)
        self.assertEqual(cls2.day, 1)
        self.assertEqual(cls2.year, 100)

    def test_leap_year(self):
        self.assertTrue(Date(1, 1, 2024).is_leap_year())
        self.assertFalse(Date(1, 1, 2023).is_leap_year())

        self.assertTrue(Date.is_year_leap(2000))
        self.assertTrue(Date.is_year_leap(2024))
        self.assertFalse(Date.is_year_leap(1900))
        self.assertFalse(Date.is_year_leap(2023))

    def test_last_day(self):
        self.assertEqual(Date(1, 1, 2022).last_day(), 31)
        self.assertEqual(Date(4, 1, 2022).last_day(), 30)
        self.assertEqual(Date(2, 1, 2020).last_day(), 29)
        self.assertEqual(Date(2, 1, 2022).last_day(), 28)

        self.assertEqual(Date().last_day_of_month(1, 2022), 31)
        self.assertEqual(Date().last_day_of_month(4, 2022), 30)
        self.assertEqual(Date().last_day_of_month(2, 2020), 29)
        self.assertEqual(Date().last_day_of_month(2, 2022), 28)

    def test_string(self):
        self.assertEqual(Date(1, 1, 1000).to_numeric_string(), "01/01/1000")

        self.assertEqual(Date(12, 12, 1212).to_month_first_string(), "December 12, 1212")

        self.assertEqual(Date(1, 1, 1111).to_day_first_string(), "01 January 1111")

if __name__ == "__main__":
    unittest.main()
