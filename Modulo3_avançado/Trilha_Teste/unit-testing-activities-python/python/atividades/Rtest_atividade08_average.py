import pytest

import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from atividade08_average import calculate_average

#  -------- ROTEIRO DE TESTE --------
# Lista não vazia: Testa se a função calcula corretamente a média de uma lista de números.
# Lista vazia: Testa se a função lança uma exceção ao receber uma lista vazia.
# Lista com um único elemento: Testa se a função lida corretamente com uma lista contendo apenas um número.




def test_calculate_average_with_numbers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([10, 20, 30, 40, 50]) == 30.0
    assert calculate_average([1.5, 2.5, 3.5, 4.5]) == 3.0

def test_calculate_average_with_single_number():
    assert calculate_average([5]) == 5.0
    assert calculate_average([10]) == 10.0

def test_calculate_average_with_empty_list():
    with pytest.raises(ValueError, match="The list of numbers cannot be empty"):
        calculate_average([])
