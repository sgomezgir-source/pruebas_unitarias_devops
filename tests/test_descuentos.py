import pytest
from src.descuentos import (
    aplicar_descuento, calcular_descuento, calcular_precio_final,
    descuento_por_volumen, descuento_cumulativo, descuento_apilado
)

def test_aplicar_descuento_valido():

    precio, porcentaje = 100, 20

    resultado = aplicar_descuento(precio, porcentaje)

    assert resultado == 80.0

def test_aplicar_descuento_precio_negativo_lanza_error():

    precio, porcentaje = -50, 10

    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        aplicar_descuento(precio, porcentaje)

def test_aplicar_descuento_porcentaje_invalido_lanza_error():

    precio, porcentaje = 100, 110

    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        aplicar_descuento(precio, porcentaje)

def test_calcular_descuento_valido():

    precio, porcentaje = 200, 15

    resultado = calcular_descuento(precio, porcentaje)

    assert resultado == 30.0

def test_calcular_descuento_precio_negativo_lanza_error():

    precio, porcentaje = -10, 15

    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        calcular_descuento(precio, porcentaje)

def test_calcular_descuento_porcentaje_invalido_lanza_error():

    precio, porcentaje = 100, -5

    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        calcular_descuento(precio, porcentaje)

def test_calcular_precio_final_impuesto_sobre_precio_descontado():
    """Revela BUG 1 de descuentos: el impuesto se calcula sobre el precio original y no sobre el descontado."""

    precio, impuesto, descuento = 100, 19, 10


    resultado = calcular_precio_final(precio, impuesto, descuento)

    assert resultado == pytest.approx(107.1)

def test_calcular_precio_final_precio_negativo_lanza_error():

    precio, impuesto, descuento = -100, 19, 10

    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        calcular_precio_final(precio, impuesto, descuento)

def test_calcular_precio_final_impuesto_negativo_lanza_error():

    precio, impuesto, descuento = 100, -5, 10

    with pytest.raises(ValueError, match="El impuesto no puede ser negativo"):
        calcular_precio_final(precio, impuesto, descuento)

def test_calcular_precio_final_descuento_invalido_lanza_error():

    precio, impuesto, descuento = 100, 19, 120

    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio_final(precio, impuesto, descuento)

def test_descuento_por_volumen_sin_descuento():

    cantidad, precio_unitario = 5, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 50.0

def test_descuento_por_volumen_10_unidades():

    cantidad, precio_unitario = 10, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 95.0

def test_descuento_por_volumen_20_unidades():

    cantidad, precio_unitario = 20, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 180.0

def test_descuento_por_volumen_50_unidades():

    cantidad, precio_unitario = 50, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 425.0

def test_descuento_por_volumen_100_unidades():

    cantidad, precio_unitario = 100, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 800.0

def test_descuento_por_volumen_cantidad_negativa_lanza_error():

    cantidad, precio_unitario = -1, 10

    with pytest.raises(ValueError, match="La cantidad no puede ser negativa"):
        descuento_por_volumen(cantidad, precio_unitario)

def test_descuento_por_volumen_precio_negativo_lanza_error():

    cantidad, precio_unitario = 10, -5

    with pytest.raises(ValueError, match="El precio unitario no puede ser negativo"):
        descuento_por_volumen(cantidad, precio_unitario)

def test_descuento_cumulativo_valido():

    precio, descuentos = 100, [10, 20]

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == 72.0

def test_descuento_cumulativo_lista_vacia():

    precio, descuentos = 100, []

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == 100

def test_descuento_cumulativo_error_validaciones():

    precio_negativo = -50
   
    descuentos_invalidos = [10, 150]

    with pytest.raises(ValueError):
        descuento_cumulativo(precio_negativo, [10])
    with pytest.raises(ValueError):
        descuento_cumulativo(100, descuentos_invalidos)

def test_descuento_apilado_excede_100_se_limita_a_cero():
    """Revela BUG 2 de descuentos: cuando la suma de descuentos supera 100%, lanza ValueError en vez de topar en 100% (precio 0)."""

    precio, descuentos = 100, [60, 50]

    resultado = descuento_apilado(precio, descuentos)

    assert resultado == 0.0

def test_descuento_apilado_casos_borde():

    precio = 100

    assert descuento_apilado(precio, []) == 100
    assert descuento_apilado(precio, [20, 30]) == 50.0
    with pytest.raises(ValueError):
        descuento_apilado(-10, [10])