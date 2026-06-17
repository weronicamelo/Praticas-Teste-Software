import pytest

def classifica_idade(idade):
    if idade < 13:
        return 'crianca'
    elif idade < 20:
        return 'adolescente'
    elif idade < 60:
        return 'adulto'
    else:
        return 'idoso'

@pytest.mark.crianca
def test_crianca():
    assert classifica_idade(10) == 'crianca'

@pytest.mark.adolescente
def test_adolescente():
    assert classifica_idade(20) == 'adolescente'

@pytest.mark.adulto
def test_adulto():
    assert classifica_idade(60) == 'adulto'

@pytest.mark.idoso
def test_idoso():
    assert classifica_idade(65) == 'idoso'
