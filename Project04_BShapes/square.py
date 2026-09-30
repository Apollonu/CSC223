from rectangle import Rectangle

class Square(Rectangle):
    def __init__(
        self,
        side: float,
        name: str = "Square"
    ) -> None:
        super().__init__(side, side, name)
        self._side = side

    @property
    def side(self) -> float:
        return self._side
    @side.setter
    def side(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Side must be a number")
        if value <= 0:
            raise ValueError("side must be positive")
        self._side = float(value)
        self._length = self._width = self._side
        self.calc_area()

    @Rectangle.length.setter
    def length(self, value):
        self.side = value
    @Rectangle.width.setter
    def width(self, value):
        self.side = value
