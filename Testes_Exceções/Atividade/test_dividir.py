import pytest
from dividir import dividir

def test_divisao_normal():
    assert dividir(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError, match="Não é possível dividir por zero"):
        dividir(10, 0)