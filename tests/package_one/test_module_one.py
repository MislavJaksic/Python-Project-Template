from poetry_template.package_one.module_one import add
from tests import context

import pytest

from poetry_template.package_one import module_one

@pytest.fixture(scope="function")
def basic_array():
    # setup
    yield [x for x in range(5)]
    # teardown


@pytest.fixture(scope="module")
def complex_array():
    yield [x for x in range(5)]

def test_get_setting():
    assert module_one.get_setting() == "text.txt"

@pytest.fixture(scope="function")
def calculator():
    # setup
    calculator = module_one.Calculator("instance_value")
    yield calculator
    # teardown

class TestClassForModuleOne:
    def test_add(self):
        assert module_one.add(1, 5) == 6

    def test_raise_exception(self):
        with pytest.raises(SystemExit):
            module_one.raise_exception()


def test_temporary_directory_file(tmp_path):
    dir = tmp_path / "sub_dir"
    dir.mkdir()
    dir_file = dir / "file.txt"
    dir_file.write_text("hello world")  # instantiates the file
    dir_file.write_text("world, hello")

    assert len(list(tmp_path.iterdir())) == 1
    assert dir_file.exists() == True

    assert dir_file.read_text() == "world, hello"





def test_manipulate_array(basic_array):
    assert len(basic_array) == 5





class TestCalculator:
    # def __init__(self): # Forbidden by pytest! Use fixtures instead
    #     self.calculator = module_one.Calculator("instance_value")

    def test_multiply(self, calculator):
        assert calculator.multiply(1, 2) == 2



class TestAddMock:
    def test_add_mock(self, mock_add):
        result = add(1, 1)
        assert result == 10
