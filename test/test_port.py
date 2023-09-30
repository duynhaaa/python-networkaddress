import pytest

from networkaddress.ip.port import PortNumber, MIN_VALUE, MAX_VALUE


@pytest.mark.parametrize("value", (MIN_VALUE, MAX_VALUE, MAX_VALUE / 2))
def test_init_valid(value: int) -> None:
    address = PortNumber(value)
    assert address._value == value
