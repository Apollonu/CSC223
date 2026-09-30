import math
from basic_shape import BasicShape

class Circle(BasicShape):
    """
        Implements area calculation and inherits from BasicShape
        Radius will automatically trigger recalculation
    """
    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        name: str = "Circle"
    ) -> None:
        """Initializes a Circle with position and radius"""
        super().__init__(name)
        self._x = x
        self._y = y
        self.radius = radius

    @property
    def x(self) -> float:
        """Returns the x-coordinate of the center, validates it is a number"""
        return self._x
    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = float(value)

    @property
    def y(self) -> float:
        """Returns the y-coordinate of the center, validates it is a number"""
        return self._y
    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = float(value)

    @property
    def radius(self) -> float:
        """Return's the circle's radius as a float, validates it is a number and positive"""
        return self._radius
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = float(value)
        self.calc_area()

    def calc_area(self) -> None:
        self._area = math.pi * self._radius ** 2
