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
def test_classifica_crianca():
    assert classifica_idade(6) == 'crianca'
    assert classifica_idade(11) == 'crianca'


@pytest.mark.adolescente
def test_classifica_adolescente():
    assert classifica_idade(13) == 'adolescente'
    assert classifica_idade(19) == 'adolescente'


@pytest.mark.adulto
def test_classifica_adulto():
    assert classifica_idade(20) == 'adulto'
    assert classifica_idade(45) == 'adulto'
    assert classifica_idade(59) == 'adulto'


@pytest.mark.idoso
def test_classifica_idoso():
    assert classifica_idade(60) == 'idoso'
    assert classifica_idade(78) == 'idoso'