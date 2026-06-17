import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b


def test_dividir_normal():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)