import sys
import os 
import pytest
from math import isclose

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from atividade06_point import Point  


#  -------- ROTEIRO DE TESTE --------

# Verificar se a distância entre dois pontos é calculada corretamente.
# Verificar se a exceção é levantada quando o argumento não é uma instância de Point.

def test_distance_to():
    # Teste para a distância entre dois pontos
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert isclose(p1.distance_to(p2), 5.0, rel_tol=1e-9)
    
    p3 = Point(1, 1)
    p4 = Point(4, 5)
    assert isclose(p3.distance_to(p4), 5.0, rel_tol=1e-9)
    
    # Teste para a distância de um ponto a ele mesmo
    assert isclose(p1.distance_to(p1), 0.0, rel_tol=1e-9)

def test_distance_to_invalid_argument():
    # Teste para verificar se a exceção é levantada com argumento inválido
    p1 = Point(0, 0)
    with pytest.raises(ValueError, match="Argument must be a Point"):
        p1.distance_to((1, 1))  # Passando uma tupla em vez de um objeto Point

if __name__ == "__main__":
    pytest.main()
