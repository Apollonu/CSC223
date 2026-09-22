import unittest
from ..parked_car import ParkedCar

class TestParkedCar(unittest.TestCase):
    def test_construction(self):
        car = ParkedCar("Honda", "NSX", "Red", "ABC-123", 33)
        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "NSX")
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.plate, "ABC-123")
        self.assertEqual(car.time, 33)

    def test_reassignment(self):
        car = ParkedCar("Ford", "F-250", "Turquoise", "FELON", 524)
        car.make = "Chevrolet"
        car.model = "Corvette C5 Z06"
        car.color = "Yellow"
        car.plate = "FVU-656"
        car.time = "36"
        self.assertEqual(car.make, "Chevrolet")
        self.assertEqual(car.model, "Corvette C5 Z06")
        self.assertEqual(car.color, "Yellow")
        self.assertEqual(car.plate, "FVU-656")
        self.assertEqual(car.time, 36)

    def test_invalids(self):
        with self.assertRaises(ValueError):
            ParkedCar("", "RX-7", "Blue", "ABC-123", 30)
        with self.assertRaises(ValueError):
            ParkedCar("Mazda", "", "Blue", "ABC-123", 30)
        with self.assertRaises(ValueError):
            ParkedCar("Mazda", "RX-7", "", "ABC-123", 30)
        with self.assertRaises(ValueError):
            ParkedCar("Mazda", "RX-7", "Blue", "", 30)

        with self.assertRaises(ValueError):
            ParkedCar("Mazda", "RX-7", "Blue", "ABC-123", 0)
        with self.assertRaises(ValueError):
            ParkedCar("Mazda", "RX-7", "Blue", "ABC-123", -1)
        with self.assertRaises(ValueError):
            ParkedCar("Mazda", "RX-7", "Blue", "ABC-123", 33.33)

if __name__ == "__main__":
    unittest.main()
