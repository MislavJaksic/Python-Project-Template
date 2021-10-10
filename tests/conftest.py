# For the fixtures to be found in other files, the file must be called conftest.py!

import pytest

from poetry_template.package_one import module_one
from poetry_template.package_two import module_two


@pytest.fixture(scope="package")
def package_level():
    yield 1


@pytest.fixture(scope="session")
def session_level():
    yield 1


class MockAdd:  # used for mocking complex objects
    @staticmethod
    def ten():
        return 10


@pytest.fixture
def mock_add(monkeypatch):
    def mock(*args, **kwargs):
        return MockAdd().ten()

    monkeypatch.setattr(module_two, "add_two_numbers", mock)


class MockCalculator:  # used for mocking complex objects
    @staticmethod
    def multiply(a, b):
        return 99


@pytest.fixture
def mock_calculator(monkeypatch):
    def mock(*args, **kwargs):
        return MockCalculator()

    monkeypatch.setattr(module_one, "Calculator", mock)
