class ParkedCar:
    """Attributes are stored internally and accessed through verified properties"""
    @staticmethod
    def req_str(name: str, value: str) -> str:
        """Validates that it is not empty or incorrect value"""
        if not isinstance(value, str):
            raise TypeError(f"{name} must be a string")
        if not value:
            raise ValueError(f"{name} cannot be empty")
        return value
    @staticmethod
    def req_int(name: str, value: int) -> int:
        """Validates that the value is a non-negative int"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} cannot be negative")
        return value

    def __init__(
        self,
        make: str,
        model: str,
        color: str,
        plate: str,
        time: int
    ):
        """The constructor assigns values to the public properties for logic reuse"""
        self.make = make
        self.model = model
        self.color = color
        self.plate = plate
        self.time = time

    """Vehicle make"""
    @property
    def make(self) -> str:
        return self._make
    @make.setter
    def make(self, value: str):
        self._make = self.req_str("make", value)

    """Vehicle model"""
    @property
    def model(self) -> str:
        return self._model
    @model.setter
    def model(self, value: str):
        self._model = self.req_str("model", value)

    """Vehicle color"""
    @property
    def color(self) -> str:
        return self._color
    @color.setter
    def color(self, value: str):
        self._color = self.req_str("color", value)

    """Vehicle plate"""
    @property
    def plate(self) -> str:
        return self._plate
    @plate.setter
    def plate(self, value: str):
        self._plate = self.req_str("plate", value)

    """Vehicle time parked"""
    @property
    def time(self) -> int:
        return self._time
    @time.setter
    def time(self, value: int):
        self._time = self.req_int("time", value)
