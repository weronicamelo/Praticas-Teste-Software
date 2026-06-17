import pytest

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120),
])

def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado

def test_fatorial_negativo():
    with pytest.raises(Exception):
        fatorial(-1)