import pytest
from atividade04_sort_numbers import sort_numbers

def test_sort_numbers_with_unsorted_list():
    assert sort_numbers([3, 1, 2]) == [1, 2, 3]

def test_sort_numbers_with_mixed_list():
    assert sort_numbers([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_sort_numbers_with_empty_list():
    assert sort_numbers([]) == []