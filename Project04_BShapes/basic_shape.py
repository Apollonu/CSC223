from abc import ABC, abstractmethod

class BasicShape(ABC):
    """
        Defines the interface for all given shapes
        Subclasses use a calc_area() to give area calculations
    """
    def __init__(self, name: str) -> None:
        """Initializes a BasicShape"""
        self.name = name
        self._area = 0.0

    @property
    def name(self) -> str:
        """Returns the shape's name, validates it is a string and not empty"""
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value.strip():
            raise ValueError("name can't be empty")
        self._name = value

    @property
    def area(self) -> float:
        """Returns a read-only area value"""
        return self._area

    @abstractmethod
    def calc_area(self) -> None:
        raise NotImplementedError
