import pytest
from atividade01_add import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_and_positive():
    assert add(-1, 1) == 0

def test_add_negative_numbers():
    assert add(-1, -1) == -2
