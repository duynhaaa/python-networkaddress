"""Notation."""

__all__ = []

from string import hexdigits
from typing import Final

# Octet separators
DOT_SEPARATOR: Final = "."
COLON_SEPARATOR: Final = ":"
HYPHEN_SEPARATOR: Final = "-"
OCTET_SEPARATORS: Final = (DOT_SEPARATOR, COLON_SEPARATOR, HYPHEN_SEPARATOR)


def validate_notation(value: str) -> None:
    """

    :param value:
    :return:
    """
    is_valid = False
    errors = []
    validators = [
        validate_hex_string,
        validate_dot_notation,
        validate_hyphen_notation,
        validate_colon_notation,
    ]

    for validate in validators:
        try:
            if not is_valid:
                validate(value)
        except ValueError as e:
            errors.append(e)
        else:
            is_valid = True

    if not is_valid:
        raise ExceptionGroup("Invalid MAC address", errors)


def validate_hex_string(value: str) -> None:
    """

    :param value:
    :return:
    """
    errors = []
    for i, c in enumerate(value):
        if c not in hexdigits:
            error = ValueError("")


def validate_dot_notation(value: str) -> None:
    """

    :param value:
    :return:
    """


def validate_colon_notation(value: str) -> None:
    """

    :param value:
    :return:
    """


def validate_hyphen_notation(value: str) -> None:
    """

    :param value:
    :return:
    """


def is_dot_notation(value: str) -> bool:
    """

    :param value:
    :return:
    """


def is_colon_notation(value: str) -> bool:
    """

    :param value:
    :return:
    """


def is_hyphen_notation(value: str) -> bool:
    """

    :param value:
    :return:
    """


def format_dot_notation(value: str) -> str:
    """

    :param value:
    :return:
    """


def format_colon_notation(value: str) -> str:
    """

    :param value:
    :return:
    """


def format_hyphen_notation(value: str) -> str:
    """

    :param value:
    :return:
    """
