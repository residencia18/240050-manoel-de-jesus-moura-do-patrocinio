import pytest
from atividade03_find_max import find_max

def test_find_max_with_positive_numbers():
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_max_with_negative_numbers():
    assert find_max([-1, -2, -3, -4, -5]) == -1

def test_find_max_with_empty_list():
    assert find_max([]) == None