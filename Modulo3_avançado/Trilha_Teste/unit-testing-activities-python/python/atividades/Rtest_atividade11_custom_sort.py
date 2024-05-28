import pytest

import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from atividade11_custom_sort import custom_sort

# ----- ROTINA DE TESTE -------

# Lista de números em ordem crescente.
# Lista de números em ordem decrescente.
# Lista de números com valores iguais.
# Lista vazia.
# Lista com um único elemento.
# Lista com números negativos e positivos.

def test_custom_sort_with_ascending_numbers():
    assert custom_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_custom_sort_with_descending_numbers():
    assert custom_sort([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]

def test_custom_sort_with_equal_numbers():
    assert custom_sort([2, 2, 2, 2]) == [2, 2, 2, 2]

def test_custom_sort_with_empty_list():
    assert custom_sort([]) == []

def test_custom_sort_with_single_element():
    assert custom_sort([1]) == [1]

def test_custom_sort_with_mixed_numbers():
    assert custom_sort([-1, 3, 0, -2, 2]) == [3, 2, 0, -1, -2]
