import pytest

def soma_dobro(numeros):
    return sum(x * 2 for x in numeros)

@pytest.fixture
def lista_numeros():
    return [1, 2, 3]

def test_soma_dobro(lista_numeros):
    assert soma_dobro(lista_numeros) == 12

def test_soma_dobro_lista_vazia():
    assert soma_dobro([]) == 0