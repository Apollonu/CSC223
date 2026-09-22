import unittest
from ..police_officer import PoliceOfficer
from ..parked_car import ParkedCar
from ..parking_meter import ParkingMeter
from ..parking_ticket import ParkingTicket

class TestPoliceOfficer(unittest.TestCase):
    def prep(self):
        self.officer = PoliceOfficer("Sgt. Guy", "12345")

    def test_no_ticket(self):
        car = ParkedCar("Toyota", "Tundra", "Gray", "123-123", 35)
        meter = ParkingMeter(30)
        self.assertIsNone(self.officer.inspection(car, meter))
    def test_exact_ticket(self):
        car = ParkedCar("Toyota", "Tundra", "Gray", "123-123", 60)
        meter = ParkingMeter(60)
        self.assertIsNone(self.officer.inspection(car, meter))

    def test_ticket(self):
        car = ParkedCar("Toyota", "Tundra", "Gray", "123-123", "65")
        meter = ParkingMeter(60)
        inspection = self.officer.inspection(car, meter)

        self.assertIsInstance(inspection, ParkingTicket)
        self.assertEqual(inspection.overtime, 5)

        self.assertEqual(inspection.car_make, "Toyota")
        self.assertEqual(inspection.car_model, "Tundra")
        self.assertEqual(inspection.car_color, "Gray")
        self.assertEqual(inspection.car_plate, "123-123")
        self.assertEqual(inspection.officer_name, "Sgt. Guy")
        self.assertEqual(inspection.officer_badge, "12345")

if __name__ == "__main__":
    unittest.main()
