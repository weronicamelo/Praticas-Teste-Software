import pytest

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

@pytest.mark.parametrize("n, esperado", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120)
])
def test_fatorial(n, esperado):
    assert fatorial(n) == esperado


def test_fatorial_negativo():
    try:
        fatorial(-1)
    except RecursionError:
        return  
    assert False, "Esperava RecursionError para número negativo"