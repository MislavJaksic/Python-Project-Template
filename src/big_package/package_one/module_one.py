"""
    Application module.
"""
from big_package.package_two import module_two


def add(x, y):
    """Add two numbers using a library.
    """
    return module_two.add_two_numbers(x, y)


def multiply(x, y):
    """Multiply two numbers using a library.
    """
    return module_two.multiply_two_numbers(x, y)


def raise_exception():
    """Raise an exception.
    """
    raise SystemExit(1)
