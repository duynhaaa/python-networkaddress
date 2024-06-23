""""""

__all__ = [
    "MIN_VALUE",
    "MAX_VALUE",
    "Address",
]

from string import hexdigits
from typing import Final, Union, Literal, Any, NewType

MIN_VALUE: Final = int("0" * 12, base=16)
MAX_VALUE: Final = int("f" * 12, base=16)

OCTET_SEPARATOR_DOT: Final = "."
OCTET_SEPARATOR_COLON: Final = ":"
OCTET_SEPARATOR_HYPHEN: Final = "-"
OCTET_SEPARATORS: Final = (
    OCTET_SEPARATOR_DOT,
    OCTET_SEPARATOR_COLON,
    OCTET_SEPARATOR_HYPHEN,
)


def validate_dot_notation(value: str) -> None:
    """
    Validate a MAC address's dot separated notation.

    :param value:
    :return:
    """
    octets = value.split(OCTET_SEPARATOR_DOT, maxsplit=3)
    if len(octets) != 3:
        raise ValueError("Expected 3")


def is_colon_notation(value: str) -> bool:
    """
    Check if a string is a colon separated notation of a MAC address.

    :param value:
    :return:
    """


def is_hyphen_notation(value: str) -> bool:
    """
    Check if a string is a hyphen separated notation of a MAC address.

    :param value:
    :return:
    """


class Address:
    __slots__ = ("_value",)

    def __init__(
        self,
        value: Union[str, bytes, int],
        endian: Literal["big", "small", None] = None
    ) -> None:
        """

        :param value:
        :param endian:
        """
        if isinstance(value, str):
            if OCTET_SEPARATOR_DOT in value:
                separator = OCTET_SEPARATOR_DOT
            value_int = int(value, base=16)

        elif isinstance(value, bytes):
            raise NotImplementedError

        else:
            value_int = value

        if not (MIN_VALUE <= value_int <= MAX_VALUE):
            raise InvalidMACAddressError(value)

        self._value = value_int

    def to_string(
            self,
            delimiter: Literal[":", "-", ".", None] = None,
            endian: Literal["big", "small"] = "big"
    ) -> str:
        """

        :param delimiter:
        :param endian:
        :return:
        """
        result = format(self._value, "0>12x")
        if delimiter == ".":
            result = delimiter.join(result[i:i + 4] for i in range(0, 12, 4))
        if delimiter == ":" or delimiter == "-":
            result = delimiter.join(result[i:i + 4] for i in range(0, 12, 2))
        return result

    def __str__(self) -> str:
        return self.to_string(delimiter=":")

    def __repr__(self) -> str:
        return "{module_name}.{class_name}(value={value})".format(
            module_name=type(self).__module__,
            class_name=self.__class__.__name__,
            value=self._value,
        )

    def __index__(self) -> int:
        return self._value

    def __hash__(self) -> int:
        return hash((type(self), self._value))



class InvalidMACAddressError(ValueError):
    """An error raised when a MAC address is invalid."""
