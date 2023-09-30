__all__ = ["MACAddress"]

import re
from typing import Any

MIN_VALUE = int("0" * 12, base=16)
MAX_VALUE = int("f" * 12, base=16)


DOT_NOTATION_DELIMITER = "."
DOT_NOTATION_REGEX = re.compile(r"^[0-9a-f]{4}(\.[0-9a-f]{4}){2}$", re.I)
IEEE_NOTATION_DELIMITER = "-"
IEEE_NOTATION_PATTERN = re.compile(r"^[0-9a-f]{2}(-[0-9a-f]{2}){5}$", re.I)
IETF_NOTATION_DELIMITER = ":"
IETF_NOTATION_PATTERN = re.compile(r"^[0-9a-f]{2}(:[0-9a-f]{2}){5}$", re.I)


class MACAddress:
    __slots__ = ("_value",)

    def __init__(self, value: int, /) -> None:
        if value < MIN_VALUE:
            raise ValueError(
                "%s (< %s) is not permitted as a MAC address"
                % (value, MIN_VALUE)
            )
        if value > MAX_VALUE:
            raise ValueError(
                "%s (> %s) is not permitted as a MAC address"
                % (value, MAX_VALUE)
            )
        self._value = value

    @classmethod
    def from_string(cls, value: str, /) -> "MACAddress":
        if DOT_NOTATION_REGEX.fullmatch(value):
            value = value.replace(DOT_NOTATION_DELIMITER, "")
        elif IEEE_NOTATION_PATTERN.fullmatch(value):
            value = value.replace(IEEE_NOTATION_DELIMITER, "")
        elif IETF_NOTATION_PATTERN.fullmatch(value):
            value = value.replace(IETF_NOTATION_DELIMITER, "")
        try:
            value_int = int(value, 16)
        except ValueError as exc:
            raise ValueError(f"'{value}' is not a valid MAC address") from exc
        return cls(value_int)

    def hex_string(self, *, prefix: bool = True, padded: bool = False) -> str:
        return ("0x" if prefix else "") + format(
            self._value, "x" if not padded else "0>12x"
        )

    def dot_notation(self) -> str:
        hex_string = self.hex_string(prefix=False, padded=True)
        octet_quadruplets = [
            hex_string[i : i + 4] for i in range(0, len(hex_string), 4)
        ]
        return DOT_NOTATION_DELIMITER.join(octet_quadruplets)

    def ieee_notation(self) -> str:
        hex_string = self.hex_string(prefix=False, padded=True)
        octet_pairs = [
            hex_string[i : i + 2] for i in range(0, len(hex_string), 2)
        ]
        return IEEE_NOTATION_DELIMITER.join(octet_pairs)

    def ietf_notation(self) -> str:
        hex_string = self.hex_string(prefix=False, padded=True)
        octet_pairs = [
            hex_string[i : i + 2] for i in range(0, len(hex_string), 2)
        ]
        return IETF_NOTATION_DELIMITER.join(octet_pairs)

    def __str__(self) -> str:
        return hex(self)

    def __repr__(self) -> str:
        return "%s.%s(%s)" % (
            self.__class__.__module__,
            self.__class__.__name__,
            self.ietf_notation(),
        )

    def __index__(self) -> int:
        return self._value

    def __hash__(self) -> int:
        return hash((type(self), self._value))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, MACAddress):
            return self._value == other._value
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, MACAddress):
            return self._value < other._value
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, MACAddress):
            return self._value <= other._value
        return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, MACAddress):
            return self._value > other._value
        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, MACAddress):
            return self._value >= other._value
        return NotImplemented
