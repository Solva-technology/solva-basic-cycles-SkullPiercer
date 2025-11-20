import pytest
import main

# Тесты для sum_list_elements()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4], 10),
    ([-1, -2, -3], -6),
    ([10, 0, -5], 5),
    ([], 0),
])
def test_sum_list_elements(input_list, expected):
    assert main.sum_list_elements(input_list) == expected

# Тесты для find_max_element()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 9, 3, 5], 9),
    ([-10, -1, -5], -1),
    ([5, 5, 5], 5),
    ([1], 1),
    ([], None),
])
def test_find_max_element(input_list, expected):
    assert main.find_max_element(input_list) == expected

# Тесты для count_even_numbers()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4, 5, 6], 3),
    ([2, 4, 6, 8], 4),
    ([1, 3, 5, 7], 0),
    ([], 0),
    ([0, 2, -4], 3),
])
def test_count_even_numbers(input_list, expected):
    assert main.count_even_numbers(input_list) == expected

# Тесты для create_string_from_list()
@pytest.mark.parametrize("input_list, expected", [
    (["hello", " ", "world"], "hello world"),
    (["py", "th", "on"], "python"),
    (["a"], "a"),
    ([], ""),
])
def test_create_string_from_list(input_list, expected):
    assert main.create_string_from_list(input_list) == expected

# Тесты для sum_until_negative()
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 5, -1, 3, 4], 8),
    ([-1, 2, 3], 0),
    ([1, 2, 3], 6),
    ([], 0),
    ([1, 2, 0, 5, -5], 8),
])
def test_sum_until_negative(input_list, expected):
    assert main.sum_until_negative(input_list) == expected
