__all__ = ["PortNumber"]

from typing import Any

MIN_VALUE = 0
MAX_VALUE = 65535


class PortNumber:
    __slots__ = ("_value",)

    def __init__(self, value: int, /) -> None:
        if value < MIN_VALUE:
            raise ValueError(
                "%s (< %s) is not permitted as a port number"
                % (value, MIN_VALUE)
            )
        if value > MAX_VALUE:
            raise ValueError(
                "%s (> %s) is not permitted as a port number"
                % (value, MAX_VALUE)
            )
        self._value = value

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return "%s.%s(%s)" % (
            self.__class__.__module__,
            self.__class__.__name__,
            self._value,
        )

    def __index__(self) -> int:
        return self._value

    def __hash__(self) -> int:
        return hash((type(self), self._value))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, PortNumber):
            return self._value == other._value
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, PortNumber):
            return self._value < other._value
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, PortNumber):
            return self._value <= other._value
        return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, PortNumber):
            return self._value > other._value
        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, PortNumber):
            return self._value >= other._value
        return NotImplemented
