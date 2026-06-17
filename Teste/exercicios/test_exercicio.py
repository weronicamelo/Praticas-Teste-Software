from exercicio1 import *

def test_somar():
    assert somar(4, 8) == 12

def test_subtrair():
    assert subtrair(5, 2) == 3

def test_multiplicar():
    assert multiplicar(5, 5) == 25

def test_eh_par():
    assert eh_par(8) is True
    assert eh_par(3) is False

def test_dividir():
    assert dividir(7, 2) == 3.5

def test_resto_divisao():
    assert resto_divisao(10, 3) == 1

def test_media_tres_numeros():
    assert media_tres_numeros(3, 6, 9) == 6

def test_area_retangulo():
    assert area_retangulo(5, 4) == 20