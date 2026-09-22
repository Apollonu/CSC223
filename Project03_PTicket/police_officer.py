from parking_ticket import ParkingTicket

class PoliceOfficer:
    """
        Inspects a parked car, and if a ticket should be given
        If so it will use the officers information and cars information to issue one
    """
    @staticmethod
    def req_str(name: str, value: str) -> str:
        """Validates a string value"""
        if not isinstance(value, str):
            raise TypeError(f"{name} must be a string")
        if not value:
            raise ValueError(f"{name} cannot be empty")
        return value

    def __init__(self, name: str, badge: str):
        """Creates a officer with the supplied information"""
        self.name = name
        self.badge = badge

    """Defines name"""
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        self._name = self.req_str("name", value)

    """Defines badge"""
    @property
    def badge(self) -> str:
        return self._badge
    @badge.setter
    def badge(self, value: str):
        self._badge = self.req_str("badge", value)

    def inspection(self, car, meter):
        """Inspects a parked car with a meter and checks if a ticket needs to be issued"""
        if not hasattr(car, "time"):
            raise TypeError("car must have 'time'")
        if not hasattr(meter, "time"):
            raise TypeError("meter must have 'time'")

        overtime = car.time - meter.time
        if overtime <= 0:
            return None

        return ParkingTicket(car, self, overtime)
