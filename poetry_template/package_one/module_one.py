"""
    Application module.
"""
from typing import ClassVar

from poetry_template import settings
from poetry_template.package_two import module_two


def get_setting():
    return settings.filename


def add(x: int, y: int) -> int:
    """
    Add two numbers using a library.

    :param x: first whole number
    :param y: second whole number
    """
    return module_two.add_two_numbers(x, y)


def multiply(x: int, y: int) -> int:
    """
    Multiply two numbers using a library.

    :param x: first whole number
    :param y: second whole number
    """
    return module_two.multiply_two_numbers(x, y)


def raise_exception():
    """Raise an exception."""
    raise SystemExit(1)


class Calculator:
    class_field: ClassVar[str] = "class_value"
    instance_field: str

    def __init__(self, instance_value: str):
        self.instance_field = instance_value

    def multiply(self, a: int, b: int) -> int:
        return a * b
