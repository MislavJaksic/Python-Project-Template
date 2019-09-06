import sys
import pytest

from tests import context
from big_package.package_one import module_one


class TestClassForModuleOne(object):
    def test_add(self):
        assert module_one.add(1, 5) == 6

    def test_raise_exception(self):
        with pytest.raises(SystemExit):
            module_one.raise_exception()


def test_need_temporary_directory(tmpdir):
    text_file = tmpdir.mkdir("sub_dir").join("file.txt")
    text_file.write("hello world")
    text_file.write("world, hello")

    assert text_file.read() == "world, hello"
    assert len(tmpdir.listdir()) == 1


@pytest.fixture(scope="function")
def basic_array():
    # setup
    yield [x for x in range(5)]

    # teardown


@pytest.fixture(scope="module")
def complex_array():
    yield [x for x in range(5)]


def test_manipulate_array(basic_array):
    assert len(basic_array) == 5
