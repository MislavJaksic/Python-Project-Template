from poetry_template.package_two import module_two


class TestClassForModuleTwo:
    def test_add_two_numbers(self):
        assert module_two.add_two_numbers(1, 5) == 6

    def test_multiply_two_numbers(self):
        assert module_two.multiply_two_numbers(2, 4) == 8
