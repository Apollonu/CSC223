class ParkedCar:
    @staticmethod
    def req_str(name: str, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{name} must be a string")
        if not value:
            raise ValueError(f"{name} cannot be empty")
        return value
    @staticmethod
    def req_int(name: str, value: int) -> int:
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
        self.make = make
        self.model = model
        self.color = color
        self.plate = plate
        self.time = time

    @property
    def make(self) -> str:
        return self._make
    @make.setter
    def make(self, value: str):
        self._make = self.req_str("make", value)

    @property
    def model(self) -> str:
        return self._model
    @model.setter
    def model(self, value: str):
        self._model = self.req_str("model", value)

    @property
    def color(self) -> str:
        return self._color
    @color.setter
    def color(self, value: str):
        self._color = self.req_str("color", value)

    @property
    def plate(self) -> str:
        return self._plate
    @plate.setter
    def plate(self, value: str):
        self._plate = self.req_str("plate", value)

    @property
    def time(self) -> int:
        return self._time
    @time.setter
    def time(self, value: int):
        self._time = self.req_int("time", value)
