from abc import ABC, abstractmethod

class BasicShape(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._area = 0.0

    @property
    def name(self) -> str:
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
        return self._area

    @abstractmethod
    def calc_area(self) -> None:
        raise NotImplementedError
