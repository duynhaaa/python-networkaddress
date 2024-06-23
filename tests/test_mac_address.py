import pytest

from networkaddress import MACAddress, MIN_MAC_ADDRESS_VALUE, MAX_MAC_ADDRESS_VALUE


@pytest.mark.parametrize(
    ["input_value", "expected_value"],
    [
        pytest.param(MIN_MAC_ADDRESS_VALUE, int("0" * 12, base=16), id="min_value"),
        pytest.param(MAX_MAC_ADDRESS_VALUE, int("f" * 12, base=16), id="max_value"),
        pytest.param(5628, 5628, id="int_5628"),
        pytest.param("1234567890AB", int("1234567890AB", base=16), id="str_delim_none"),
        pytest.param("1234.5678.90AB", int("1234567890AB", base=16), id="str_delim_dot"),
        pytest.param("12:34:56:78:90:AB", int("1234567890AB", base=16), id="str_delim_colon"),
        pytest.param("12-34-56-78-90-AB", int("1234567890AB", base=16), id="str_delim_hyphen"),
    ]
)
def test_init(input_value, expected_value):
    assert MACAddress(input_value)._value == expected_value


