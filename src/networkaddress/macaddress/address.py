"""The address object."""

__all__ = ["Address"]

from enum import StrEnum
from typing import Any, ClassVar, Final, Self, Union

# https://en.wikipedia.org/wiki/Endianness#Networking
# https://stackoverflow.com/questions/17398882/network-byte-order-on-mac-address

MIN_VALUE: Final = int("0" * 12, base=16)
MAX_VALUE: Final = int("f" * 12, base=16)


class Address:

    __slots__ = ("_value",)

    def __init__(self, value: Union[int, bytes, str]) -> None:
        """

        :param value:
        """
        if isinstance(value, str):
            pass

        elif isinstance(value, bytes):
            pass

        assert isinstance(value, int)
        self._value = value

    def __index__(self) -> int:
        return self._value

    def __hash__(self) -> int:
        return hash((type(self), self._value))

    def __str__(self) -> str:
        return format(self._value, "0>12x")

    def __repr__(self) -> str:
        return "{module_name}.{class_name}(value={value})".format(
            module_name=self.__class__.__module__,
            class_name=self.__class__.__name__,
            value=
        )

    def __eq__(self, other: Any) -> bool:
        result = NotImplemented
        if isinstance(other, Address):
            result = self._value == other._value
        elif isinstance(other, Union[str, bytes]):
            try:
                result = self._value == Address(other)._value
            except ValueError:
                pass
        elif isinstance(other, Union[int, float, complex]):
            result = self._value == other
        return result

    def __lt__(self, other: Any) -> bool:
        result = NotImplemented
        if isinstance(other, Address):
            result = self._value < other._value
        elif isinstance(other, Union[str, bytes]):
            try:
                result = self._value < Address(other)._value
            except ValueError:
                pass
        elif isinstance(other, Union[int, float, complex]):
            result = self._value < other
        return result

    def __le__(self, other: Any) -> bool:
        result = NotImplemented
        if isinstance(other, Address):
            result = self._value <= other._value
        elif isinstance(other, Union[str, bytes]):
            try:
                result = self._value <= Address(other)._value
            except ValueError:
                pass
        elif isinstance(other, Union[int, float, complex]):
            result = self._value <= other
        return result

    def __gt__(self, other: Any) -> bool:
        result = NotImplemented
        if isinstance(other, Address):
            result = self._value > other._value
        elif isinstance(other, Union[str, bytes]):
            try:
                result = self._value > Address(other)._value
            except ValueError:
                pass
        elif isinstance(other, Union[int, float, complex]):
            result = self._value > other
        return result

    def __ge__(self, other: Any) -> bool:
        result = NotImplemented
        if isinstance(other, Address):
            result = self._value >= other._value
        elif isinstance(other, Union[str, bytes]):
            try:
                result = self._value >= Address(other)._value
            except ValueError:
                pass
        elif isinstance(other, Union[int, float, complex]):
            result = self._value >= other
        return result


