import unittest
from unittest.mock import patch

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

    def test_subtraction(self):
        apr1 = Date(4, 18, 2014)
        apr2 = Date(4, 10, 2014)
        self.assertEqual(apr1 - apr2, 8)
        self.assertEqual(apr2 - apr1, -8)

        diffyear1 = Date(2, 2, 2006)
        diffyear2 = Date(9, 10, 2003)
        self.assertEqual(diffyear1 - diffyear2, 876)

        same = Date(1, 1, 1990)
        self.assertEqual(same - same, 0)

        diffmonth1 = Date(5, 2, 2020)
        diffmonth2 = Date(4, 30, 2020)
        self.assertEqual(diffmonth1 - diffmonth2, 2)

        leapyear1 = Date(3, 3, 2020)
        leapyear2 = Date(2, 27, 2020)
        self.assertEqual(leapyear1 - leapyear2, 5)

        unsupported = Date(1, 1, 1000)
        with self.assertRaises(TypeError):
            error = Date(unsupported) - 1

    def test_increment(self):
        normal = Date(1, 1, 2012)
        inc_normal = normal.increment()
        self.assertIs(inc_normal, normal)
        self.assertEqual(str(normal), "January 02, 2012")

        month1 = Date(4, 30, 2012)
        month1.increment()
        self.assertEqual(str(month1), "May 01, 2012")

        month2 = Date(1, 31, 2012)
        month2.increment()
        self.assertEqual(str(month2), "February 01, 2012")

        notleap = Date(2, 28, 2021)
        notleap.increment()
        self.assertEqual(str(notleap), "March 01, 2021")

        leap = Date(2, 28, 2020)
        leap.increment()
        self.assertEqual(str(leap), "February 29, 2020")
        leap.increment()
        self.assertEqual(str(leap), "March 01, 2020")

        year = Date(12, 31, 1990)
        year.increment()
        self.assertEqual(str(year), "January 01, 1991")

    def test_decrement(self):
        normal = Date(1, 2, 2012)
        dec_normal = normal.decrement()
        self.assertIs(dec_normal, normal)
        self.assertEqual(str(normal), "January 01, 2012")

        month1 = Date(5, 1, 2012)
        month1.decrement()
        self.assertEqual(str(month1), "April 30, 2012")

        notleap = Date(3, 1, 2021)
        notleap.decrement()
        self.assertEqual(str(notleap), "February 28, 2021")

        leap = Date(3, 1, 2020)
        leap.decrement()
        self.assertEqual(str(leap), "February 29, 2020")

        year = Date(1, 1, 1991)
        year.decrement()
        self.assertEqual(str(year), "December 31, 1990")

    def test_format(self):
        self.assertEqual(str(Date(4, 18, 2018)), "April 18, 2018")
        self.assertEqual(str(Date(2, 29, 2020)), "February 29, 2020")
        self.assertEqual(str(Date(1, 1, 1991)), "January 01, 1991")

    @patch("builtins.input", side_effect=["4", "18", "2018"])
    def test_input_valid(self, mock_input):
        result = Date.from_input()
        self.assertEqual((result.month, result.day, result.year), (4, 18, 2018))

    @patch("builtins.input", side_effect=["December", "1", "2020"])
    def test_input_nonnumeric(self, mock_input):
        with self.assertRaises(ValueError):
            result = Date.from_input()

    @patch("builtins.input", side_effect=["13", "1", "2020"])
    def test_input_month(self, mock_input):
        with self.assertRaises(ValueError):
            result = Date.from_input()

    @patch("builtins.input", side_effect=["12", "32", "2020"])
    def test_input_day(self, mock_input):
        with self.assertRaises(ValueError):
            result = Date.from_input()

    @patch("builtins.input", side_effect=["2", "29", "2021"])
    def test_input_leap(self, mock_input):
        with self.assertRaises(ValueError):
            result = Date.from_input()


if __name__ == "__main__":
    unittest.main()
