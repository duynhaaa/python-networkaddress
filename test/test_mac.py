# pylint: disable=protected-access
import re
from typing import Any

import pytest
from networkaddress.mac import MACAddress, MIN_VALUE, MAX_VALUE


@pytest.mark.parametrize("value", (MIN_VALUE, MAX_VALUE, MAX_VALUE / 2))
def test_init_valid(value: int) -> None:
    address = MACAddress(value)
    assert address._value == value


INVALID_MIN_ERROR_REGEX = re.compile(
    rf"(-?\d+) \(< {MIN_VALUE}\) is not permitted as a MAC address"
)


@pytest.mark.parametrize("value", (MIN_VALUE - 1, -MAX_VALUE))
def test_init_invalid_min(value: int) -> None:
    with pytest.raises(ValueError, match=INVALID_MIN_ERROR_REGEX) as exc_info:
        MACAddress(value)
    error_message = exc_info.value.args[0]
    assert isinstance(error_message, str)
    match = INVALID_MIN_ERROR_REGEX.fullmatch(error_message)
    assert match is not None and int(match.group(1)) == value


INVALID_MAX_ERROR_REGEX = re.compile(
    rf"(-?\d+) \(> {MAX_VALUE}\) is not permitted as a MAC address"
)


@pytest.mark.parametrize("value", (MAX_VALUE + 1, MAX_VALUE * 2))
def test_init_invalid_max(value: int) -> None:
    with pytest.raises(ValueError, match=INVALID_MAX_ERROR_REGEX) as exc_info:
        MACAddress(value)
    error_message = exc_info.value.args[0]
    assert isinstance(error_message, str)
    match = INVALID_MAX_ERROR_REGEX.fullmatch(error_message)
    assert match is not None and int(match.group(1)) == value


@pytest.mark.parametrize(
    ("value_str", "value_int"),
    (
        ("eaa29d9a2f9f", 257984149729183),
        ("0xeaa29d9a2f9f", 257984149729183),
        ("eaa2.9d9a.2f9f", 257984149729183),
        ("ea:a2:9d:9a:2f:9f", 257984149729183),
        ("ea-a2-9d-9a-2f-9f", 257984149729183),
    ),
)
def test_init_from_string(value_str: str, value_int: int) -> None:
    address = MACAddress.from_string(value_str)
    assert address._value == value_int


@pytest.mark.parametrize(
    ("value_int", "prefix", "padded", "value_str"),
    (
        (2644127647, False, False, "9d9a2f9f"),
        (2644127647, True, False, "0x9d9a2f9f"),
        (2644127647, False, True, "00009d9a2f9f"),
        (2644127647, True, True, "0x00009d9a2f9f"),
    ),
)
def test_to_hex_string(
    value_int: int, prefix: bool, padded: bool, value_str: str
) -> None:
    address = MACAddress(value_int)
    assert address.hex_string(prefix=prefix, padded=padded) == value_str


@pytest.mark.parametrize(
    ("value_int", "value_str"),
    (
        (2644127647, "0000.9d9a.2f9f"),
        (257984149729183, "eaa2.9d9a.2f9f"),
    ),
)
def test_to_dot_notation(value_int: int, value_str: str) -> None:
    address = MACAddress(value_int)
    assert address.dot_notation() == value_str


@pytest.mark.parametrize(
    ("value_int", "value_str"),
    (
        (2644127647, "00-00-9d-9a-2f-9f"),
        (257984149729183, "ea-a2-9d-9a-2f-9f"),
    ),
)
def test_to_ieee_notation(value_int: int, value_str: str) -> None:
    address = MACAddress(value_int)
    assert address.ieee_notation() == value_str


@pytest.mark.parametrize(
    ("value_int", "value_str"),
    (
        (2644127647, "00:00:9d:9a:2f:9f"),
        (257984149729183, "ea:a2:9d:9a:2f:9f"),
    ),
)
def test_to_ietf_notation(value_int: int, value_str: str) -> None:
    address = MACAddress(value_int)
    assert address.ietf_notation() == value_str


@pytest.mark.parametrize(
    ("value_int", "value_str"),
    (
        (2644127647, "0x9d9a2f9f"),
        (257984149729183, "0xeaa29d9a2f9f"),
    ),
)
def test_to_string(value_int: int, value_str: str) -> None:
    address = MACAddress(value_int)
    assert str(address) == value_str


def test_to_string_invalid() -> None:
    with pytest.raises(ValueError):
        MACAddress.from_string("12345Z")


REPR_REGEX = re.compile(
    r"([_\w]+\.)+MACAddress\([0-9a-f]{2}(:[0-9a-f]{2}){5}\)"
)


def test_repr() -> None:
    assert REPR_REGEX.fullmatch(repr(MACAddress(12345)))


def test_to_int() -> None:
    assert int(MACAddress(12345)) == 12345


def test_to_float() -> None:
    assert float(MACAddress(12345)) == 12345.0


@pytest.mark.parametrize(
    ("this", "other", "expected"),
    (
        (MACAddress(10), MACAddress(10), True),
        (MACAddress(10), MACAddress(9), False),
        (MACAddress(10), MACAddress(11), False),
        (MACAddress(10), 10, False),
        (MACAddress(10), 10.0, False),
    ),
)
def test_hash(this: MACAddress, other: Any, expected: bool) -> None:
    assert (hash(this) == hash(other)) is expected


@pytest.mark.parametrize(
    ("this", "other", "expected"),
    (
        (MACAddress(10), MACAddress(10), True),
        (MACAddress(10), MACAddress(9), False),
        (MACAddress(10), MACAddress(11), False),
        (MACAddress(10), 10, False),
        (MACAddress(10), 10.0, False),
    ),
)
def test_compare_eq(this: MACAddress, other: Any, expected: bool) -> None:
    assert (this == other) is expected


@pytest.mark.parametrize(
    ("this", "other", "expected"),
    (
        (MACAddress(10), MACAddress(10), False),
        (MACAddress(10), MACAddress(9), False),
        (MACAddress(10), MACAddress(11), True),
    ),
)
def test_compare_lt(this: MACAddress, other: Any, expected: bool) -> None:
    assert (this < other) is expected


@pytest.mark.parametrize(
    ("this", "other", "expected"),
    (
        (MACAddress(10), MACAddress(10), True),
        (MACAddress(10), MACAddress(9), False),
        (MACAddress(10), MACAddress(11), True),
    ),
)
def test_compare_le(this: MACAddress, other: Any, expected: bool) -> None:
    assert (this <= other) is expected


@pytest.mark.parametrize(
    ("this", "other", "expected"),
    (
        (MACAddress(10), MACAddress(10), False),
        (MACAddress(10), MACAddress(9), True),
        (MACAddress(10), MACAddress(11), False),
    ),
)
def test_compare_gt(this: MACAddress, other: Any, expected: bool) -> None:
    assert (this > other) is expected


@pytest.mark.parametrize(
    ("this", "other", "expected"),
    (
        (MACAddress(10), MACAddress(10), True),
        (MACAddress(10), MACAddress(9), True),
        (MACAddress(10), MACAddress(11), False),
    ),
)
def test_compare_ge(this: MACAddress, other: Any, expected: bool) -> None:
    assert (this >= other) is expected


@pytest.mark.parametrize("other", (10, 10.0))
def test_compare_lt_invalid(other: Any) -> None:
    with pytest.raises(TypeError):
        assert MACAddress(123) < other


@pytest.mark.parametrize("other", (10, 10.0))
def test_compare_le_invalid(other: Any) -> None:
    with pytest.raises(TypeError):
        assert MACAddress(123) <= other


@pytest.mark.parametrize("other", (10, 10.0))
def test_compare_gt_invalid(other: Any) -> None:
    with pytest.raises(TypeError):
        assert MACAddress(123) > other


@pytest.mark.parametrize("other", (10, 10.0))
def test_compare_ge_invalid(other: Any) -> None:
    with pytest.raises(TypeError):
        assert MACAddress(123) >= other
