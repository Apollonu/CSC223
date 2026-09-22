import unittest
from ..parked_car import ParkedCar
from ..parking_ticket import ParkingTicket
from ..police_officer import PoliceOfficer

class TestParkingTicket(unittest.TestCase):
    def prep(self):
        self.car = ParkedCar("Mazda", "RX-7", "Blue", "ABC-123", 0)
        self.officer = PoliceOfficer("Sgt. Guy", "12345")

    def test_information(self):
        ticket = ParkingTicket(self.car, self.officer, 20)
        self.assertEqual(ticket.car_make, "Mazda")
        self.assertEqual(ticket.car_model, "RX-7")
        self.assertEqual(ticket.car_color, "Blue")
        self.assertEqual(ticket.car_plate, "ABC-123")
        self.assertEqual(ticket.officer_name, "Sgt. Guy")
        self.assertEqual(ticket.officer_badge, "12345")

    def test_overtime_values(self):
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, "5")
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, -1)

        ticket1 = ParkingTicket(self.car, self.officer, 1)
        self.assertEqual(ticket1, 25)

        ticket60 = ParkingTicket(self.car, self.officer, 60)
        self.assertEqual(ticket60, 25)

        ticket61 = ParkingTicket(self.car, self.officer, 61)
        self.assertEqual(ticket61, 35)

        ticket120 = ParkingTicket(self.car, self.officer, 120)
        self.assertEqual(ticket120, 35)

        ticket121 = ParkingTicket(self.car, self.officer, 121)
        self.assertEqual(ticket121, 45)

    def test_ticket(self):
        ticket = ParkingTicket(self.car, self.officer, 40)
        report = ticket.ticket()
        self.assertIn("Sgt. Guy", report)
        self.assertIn("12345", report)
        self.assertIn("Mazda", report)
        self.assertIn("RX-7", report)
        self.assertIn("Blue", report)
        self.assertIn("ABC-123", report)
        self.assertIn("Illegal Minutes: 40", report)
        self.assertIn("Total Fine: $25", report)

if __name__ == "__main__":
    unittest.main()
