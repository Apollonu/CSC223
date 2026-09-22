class ParkingMeter:
    """A parking meter that tracks the time purchased"""
    def __init__(self, time: int):
        self.time = time

    """Validates the purchased minuates and sets its value"""
    @property
    def time(self) -> int:
        return self._time
    @time.setter
    def time(self, value: int):
        if not isinstance(value, int):
            raise TypeError("time must be an integer")
        if value < 0:
            raise ValueError("time cannot be negative")
        self._time = value
