import unittest
from parking_meter import ParkingMeter

class TestParkingMeter(unittest.TestCase):
    def test_construction(self):
        meter = ParkingMeter(40)
        self.assertEqual(meter.time, 40)

    def test_reassignment(self):
        meter = ParkingMeter(0)
        self.assertEqual(meter.time, 0)
        meter.time = 65
        self.assertEqual(meter.time, 65)

    def test_invalids(self):
        with self.assertRaises(ValueError):
            ParkingMeter(-5)
        with self.assertRaises(TypeError):
            ParkingMeter(5.5)
        with self.assertRaises(TypeError):
            ParkingMeter("5")

if __name__ == "__main__":
    unittest.main()
