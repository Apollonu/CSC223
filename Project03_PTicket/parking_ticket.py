class ParkingTicket:
    """
        Implements all data needed to give a citation for an illegally parked car
        Stores the vehicle information and officer information as well as illegal parked time
        Afterwards it is formatted into a report via ticket
    """
    def __init__(self, car, officer, overtime: int):
        """Stores a copy of the car data and information for officer identification"""
        if not isinstance(overtime, int):
            raise TypeError("overtime must be an integer")
        if overtime < 0:
            raise ValueError("overtime cannot be negative")

        self.car_make = car.make
        self.car_model = car.model
        self.car_color = car.color
        self.car_plate = car.plate

        self.overtime = overtime
        self.fine = self._fine(overtime)

        self.officer_name = officer.name
        self.officer_badge = officer.badge

    @staticmethod
    def _fine(overtime: int) -> int:
        """
            Calculates the fine based off of time over paid minutes
            $25 for any part of the first hour
            every extra hour it is $10
            returns the collective fine value
        """
        fine = 25
        if overtime > 60:
            extra_overtime = overtime - 60
            extra_hours = (extra_overtime + 59) // 60
            fine += extra_hours * 10
        return fine

    def ticket(self) -> str:
        """
            Returns a formatted multi-line ticket
            Includes information of the vehicle, officer, total fine, and time parked
        """
        return "\n".join([
            f"Ticketing Officer: {self.officer_name} (Badge Number:{self.officer_badge})",
            f"Car: (Make) {self.car_make}, (Model) {self.car_model}, (Color) {self.car_color}",
            f"License Plate: {self.car_plate}",
            f"Illegal Minutes: {self.overtime}",
            f"Total Fine: ${self.fine}"
        ])
