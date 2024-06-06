import pytest

import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from atividade13_factorial import factorial

# ----- ROTINA DE TESTE -------

# Fatorial de números positivos.
# Fatorial de zero.
# Lidar com números negativos.
# Verificar se a função lida corretamente com valores pequenos.



def test_factorial_positive_numbers():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_negative_numbers():
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        factorial(-1)
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        factorial(-10)

def test_factorial_large_number():
    assert factorial(10) == 3628800
