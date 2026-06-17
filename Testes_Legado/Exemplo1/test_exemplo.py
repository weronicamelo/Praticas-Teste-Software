import pytest 
from Exemplo1.exemplo import calcular_media

def test_calcular_media():
    #Testa a função calcular_media para garantir que o cálculo está correto

    assert calcular_media([1,2,3]) == 2
    assert calcular_media([10,20,30,40]) == 25
    assert calcular_media([]) == 0 #caso de lista vazia