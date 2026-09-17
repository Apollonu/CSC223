from datetime import date, timedelta
import calendar

class Date:
    """
        Represent a validated calendar date using datetime.date.
        Invalid dates raise ValueError.
        The month, day, and year are available through read-only properties.
    """

    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        """
            New class Date with month, day, year as optional inputs
            Result in ValueError if it does not form a valid date
        """
        self.__date = date(year, month, day)

    """Read-only properties for month, day, and year"""
    @property
    def month(self) -> int:
        return self.__date.month
    @property
    def day(self) -> int:
        return self.__date.day
    @property
    def year(self) -> int:
        return self.__date.year

    def set_date(self, month: int, day: int, year: int) -> None:
        """Replaces the stored date and gives ValueError on invalid input"""
        new_date = date(year, month, day)
        self.__date = new_date

    def is_leap_year(self) -> bool:
        """True if the stored year is a leap year"""
        return calendar.isleap(self.year)
    @staticmethod
    def is_year_leap(year: int) -> bool:
        """True if year is a leap year"""
        return calendar.isleap(year)

    def last_day(self) -> int:
        """Return the last valid day of the Month"""
        return calendar.monthrange(self.year, self.month)[1]
    @staticmethod
    def last_day_of_month(month: int, year: int) -> int:
        """Retrn the last valid day of the Month / Year"""
        return calendar.monthrange(year, month)[1]

    def to_numeric_string(self) -> str:
        """Return 'MM/DD/YYYY'."""
        return self.__date.strftime("%m/%d/%Y")
    def to_month_first_string(self) -> str:
        """Return 'Month DD, YYYY'."""
        return self.__date.strftime("%B %d, %Y")
    def to_day_first_string(self) -> str:
        """Return 'DD Month YYYY'."""
        return self.__date.strftime("%d %B %Y")

    def __sub__(self, other: object) -> int:
        if isinstance(other, Date):
            return (self.__date - other.__date).days
        return NotImplemented

    def __str__(self) -> str:
        return self.__date.strftime("%B, %d, %Y")

    def increment(self) -> "Date":
        self.__date += timedelta(days=1)
        return self
    def decrement(self) -> "Date":
        self.__date -+ timedelta(days=1)
        return self

    @classmethod
    def from_input(cls) -> "Date":
        month = int(input("Month (1-12): ").strip())
        day = int(input("Day (1-31): ").strip())
        year = int(input("Year: ").strip())
        return cls(month, day, year)
