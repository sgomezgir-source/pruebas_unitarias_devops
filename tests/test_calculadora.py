import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, promedio, maximo, minimo,
    calcular_area_rectangulo, calcular_perimetro_rectangulo
)

def test_sumar_positivos():

    a, b = 7, 5

    resultado = sumar(a, b)

    assert resultado == 12

def test_restar_numeros():

    a, b = 10, 4

    resultado = restar(a, b)

    assert resultado == 6

def test_multiplicar_numeros():

    a, b = 6, 7

    resultado = multiplicar(a, b)

    assert resultado == 42

def test_dividir_numeros_validos():

    a, b = 10, 2

    resultado = dividir(a, b)

    assert resultado == 5.0

def test_dividir_por_cero_lanza_error():

    a, b = 10, 0

    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(a, b)

def test_potencia_enteros():

    base, exponente = 2, 3

    resultado = potencia(base, exponente)

    assert resultado == 8

def test_raiz_cuadrada_positiva():

    numero = 16

    resultado = raiz_cuadrada(numero)

    assert resultado == 4.0

def test_raiz_cuadrada_negativa_lanza_error():
    """Revela BUG 1 de calculadora: no lanza ValueError con números negativos."""

    numero = -9

    with pytest.raises(ValueError, match="No se puede calcular la raíz cuadrada de un número negativo"):
        raiz_cuadrada(numero)

def test_promedio_lista_valida():

    lista = [10, 20, 30]

    resultado = promedio(lista)

    assert resultado == 20.0

def test_promedio_lista_vacia_lanza_error():

    lista = []

    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        promedio(lista)

def test_maximo_lista_valida():

    lista = [3, 15, 7, 2]

    resultado = maximo(lista)

    assert resultado == 15

def test_maximo_lista_vacia_lanza_error():

    lista = []

    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        maximo(lista)

def test_minimo_lista_positivos():
    """Revela BUG 2 de calculadora: min_val inicia en 0 en vez de lista[0]."""

    lista = [5, 8, 12, 3]

    resultado = minimo(lista)

    assert resultado == 3

def test_minimo_lista_con_negativos():

    lista = [4, -2, 9, -7]

    resultado = minimo(lista)

    assert resultado == -7

def test_minimo_lista_vacia_lanza_error():

    lista = []

    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        minimo(lista)

def test_calcular_area_rectangulo_valido():

    base, altura = 5, 4

    resultado = calcular_area_rectangulo(base, altura)

    assert resultado == 20

def test_calcular_area_rectangulo_negativo_lanza_error():
    
    base, altura = -5, 4

    with pytest.raises(ValueError, match="La base y altura deben ser positivas"):
        calcular_area_rectangulo(base, altura)

def test_calcular_perimetro_rectangulo_valido():
    
    base, altura = 5, 4
    
    resultado = calcular_perimetro_rectangulo(base, altura)
    
    assert resultado == 18

def test_calcular_perimetro_rectangulo_negativo_lanza_error():

    base, altura = 5, -4

    with pytest.raises(ValueError, match="La base y altura deben ser positivas"):
        calcular_perimetro_rectangulo(base, altura)