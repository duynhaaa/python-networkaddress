"""MAC address."""

__all__ = [

]

import re
from typing import Final, Union

MIN_VALUE: Final = int("0" * 12, base=16)
MAX_VALUE: Final = int("f" * 12, base=16)

DOT_NOTATION_DELIMITER: Final = "."
DOT_NOTATION_REGEX_PATTERN: Final = re.compile(r"^[0-9a-f]{4}(\.[0-9a-f]{4}){2}$", re.I)
IEEE_NOTATION_DELIMITER: Final = "-"
IEEE_NOTATION_REGEX_PATTERN: Final = re.compile(r"^[0-9a-f]{2}(-[0-9a-f]{2}){5}$", re.I)
IETF_NOTATION_DELIMITER: Final = ":"
IETF_NOTATION_REGEX_PATTERN: Final = re.compile(r"^[0-9a-f]{{2}}({}[0-9a-f]{{2}}){{5}}$", re.I)


class Address:

    __slots__ = ("_value",)

    def __init__(self, value: Union[str, bytes, int]) -> None:
        """

        :param value:
        """
        if isinstance(value, str):
            value = _str_to_int(value)
        self._value = value

    def to_hex_string(self, with_prefix: bool = True, with_padding: bool = False) -> str:
        """Return the hexadecimal representation of the MAC address."""
        hex_str = format(self._value, "x" if not with_padding else "0>12x")
        return ("0x" if with_prefix else "") + hex_str

    def to_dot_notation(self) -> str:
        """Return the dot-notation string representation of the MAC address."""

    def to_ieee_notation(self) -> str:
        """Return the IEEE notation string representation of the MAC address."""

    def to_ietf_notation(self) -> str:
        """Return the IETF notation string representation of the MAC address."""


class AddressValueError(ValueError):
    """Raised when a MAC address is invalid."""


def _str_to_int(value: str) -> int:
    """

    :param value:
    :return:
    """


def _hex_to_int(value: str) -> int:
    """

    :param value:
    :return:
    """


def _dot_to_int(value: str) -> int:
    """

    :param value:
    :return:
    """


def _ieee_to_int(value: str) -> int:
    """

    :param value:
    :return:
    """


def parse_ietf_notation_string(value: str) -> Address:
    """

    :param value:
    :return:
    """
