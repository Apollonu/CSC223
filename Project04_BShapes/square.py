from rectangle import Rectangle

class Square(Rectangle):
    """
        Inherits from Rectangle and enforces that length equals width, representing a square
        Changing a sides size will change all sides size
    """
    def __init__(
        self,
        side: float,
        name: str = "Square"
    ) -> None:
        """Creates a Square object with equal side lengths"""
        super().__init__(side, side, name)
        self._side = side

    @property
    def side(self) -> float:
        """Returns the square's side length as a float, validates it is a number and positive"""
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
