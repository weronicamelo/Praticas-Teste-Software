def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def eh_par(numero):
    return numero % 2 == 0

def dividir(a, b):
    assert b != 0  
    return a / b

def resto_divisao(a, b):
    assert b != 0
    return a % b

def media_tres_numeros(a, b, c):
    return (a + b + c) / 3

def area_retangulo(base, altura):
    assert base > 0 and altura > 0
    return base * altura
