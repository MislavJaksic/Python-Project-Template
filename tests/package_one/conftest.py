# For the fixtures to be found in other files, the file must be called conftest.py!

import pytest


@pytest.fixture(scope="package")
def package_level():
    yield 1


@pytest.fixture(scope="session")
def session_level():
    yield 1
