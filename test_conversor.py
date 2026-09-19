import pytest
from conversor import celsius_a_fahrenheit, kilometros_a_millas, pesos_a_dolares


@pytest.mark.unit
def test_celsius_a_fahrenheit():
    resultado = celsius_a_fahrenheit(0)
    assert resultado == 32


@pytest.mark.unit
def test_kilometros_a_millas():
    resultado = kilometros_a_millas(10)
    assert round(resultado, 2) == 6.21


@pytest.mark.parametrize("pesos, esperado", [
    (185, 10),
    (370, 20),
    (925, 50)
])
def test_pesos_a_dolares(pesos, esperado):
    resultado = pesos_a_dolares(pesos)
    assert round(resultado, 2) == esperado