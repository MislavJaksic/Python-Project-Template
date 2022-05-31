# pytest only exposes fixtures in a file called conftest.py!

import pytest


@pytest.fixture(scope="package")
def package_level():
    yield 1


@pytest.fixture(scope="session")
def session_level():
    yield 1
