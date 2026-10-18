import pytest
from src.validador import (
    validar_email, validar_telefono, validar_edad,
    validar_password, validar_url, validar_fecha, validar_cedula
)

def test_validar_email_casos():

    email_valido = "usuario@unal.edu.co"

    assert validar_email(email_valido) is True
    assert validar_email("") is False
    assert validar_email("sin_arroba.com") is False
    assert validar_email("doble@@arroba.com") is False
    assert validar_email("@sindominio.com") is False
    assert validar_email("usuario@sinpunto") is False

def test_validar_telefono_casos():

    tel_valido = "300-123 4567"

    assert validar_telefono(tel_valido) is True
    assert validar_telefono("") is False
    assert validar_telefono("3001234abc") is False
    assert validar_telefono("12345") is False

def test_validar_edad_casos():

    edad_valida = 25

    assert validar_edad(edad_valida) is True
    assert validar_edad("25") is False
    assert validar_edad(-1) is False
    assert validar_edad(130) is False

def test_validar_password_casos():

    pwd_valida = "Segura123"

    assert validar_password(pwd_valida) is True
    assert validar_password("") is False
    assert validar_password("Corta1") is False
    assert validar_password("sinmayuscula123") is False
    assert validar_password("SINMINUSCULA123") is False
    assert validar_password("SinNumeros") is False

def test_validar_url_casos():

    url_valida = "https://unal.edu.co"

    assert validar_url(url_valida) is True
    assert validar_url("") is False
    assert validar_url("ftp://invalida") is False

def test_validar_fecha_febrero_invalido():
    """Revela BUG 1 de validador: acepta 31 de febrero porque no valida días según el mes."""

    dia, mes, anio = 31, 2, 2026

    resultado = validar_fecha(dia, mes, anio)

    assert resultado is False

def test_validar_fecha_casos_generales():

    assert validar_fecha(15, 10, 2026) is True
    assert validar_fecha(29, 2, 2024) is True   # Año bisiesto
    assert validar_fecha(29, 2, 2025) is False  # Año no bisiesto
    assert validar_fecha("15", 10, 2026) is False
    assert validar_fecha(15, 13, 2026) is False
    assert validar_fecha(0, 10, 2026) is False
    assert validar_fecha(15, 10, 1800) is False

def test_validar_cedula_casos():

    cedula_valida = "1053800000"

    assert validar_cedula(cedula_valida) is True
    assert validar_cedula("") is False
    assert validar_cedula("12345abc") is False
    assert validar_cedula("12345") is False