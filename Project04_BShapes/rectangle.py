from basic_shape import BasicShape

class Rectangle(BasicShape):
    """
        Implements area calculation for a rectangle
        Inherits from BasicShape and automatically triggers recalculation on size change
    """
    def __init__(
        self,
        length: float,
        width: float,
        name: str = "Rectangle"
    ) -> None:
        """Initializes a Rectangle object"""
        super().__init__(name)
        self._length = None
        self._width = None
        self.length = length
        self.width = width

    @property
    def length(self) -> float:
        """Reutns the rectangle's length as a float, validates it is a number and positive"""
        return self._length
    @length.setter
    def length(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("length must be a number")
        if value <= 0:
            raise ValueError("length must be positive")
        self._length = float(value)
        if self._width is not None:
            self.calc_area()

    @property
    def width(self) -> float:
        """Reutns the rectangle's width as a float, validates it is a number and positive"""
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be a number")
        if value <= 0:
            raise ValueError("width must be positive")
        self._width = float(value)
        if self._length is not None:
            self.calc_area()

    def calc_area(self) -> None:
        self._area = self._length * self._width
