# Actividad Integradora - Conversor de Unidades

Este proyecto consiste en un conversor de unidades realizado en Python. 
Permite realizar conversiones de temperatura, distancia y moneda.

## Requerimientos

| ID | Tipo | Requerimiento |
|---|---|---|
| RF01 | Funcional | El sistema permite convertir grados Celsius a Fahrenheit. |
| RF02 | Funcional | El sistema permite convertir grados Fahrenheit a Celsius. |
| RF03 | Funcional | El sistema permite convertir kilómetros a millas y viceversa. |
| RF04 | Funcional | El sistema permite convertir pesos mexicanos a dólares y viceversa. |
| RNF01 | No funcional | El sistema muestra los resultados con una precisión de dos decimales. |
| RNF02 | No funcional | El programa puede ejecutarse desde la terminal utilizando Python. |

## Casos de prueba

### CP01 - Conversión de Celsius a Fahrenheit

- Descripción: Verificar la conversión de Celsius a Fahrenheit.
- Requerimiento relacionado: RF01
- Entrada: 0 °C
- Resultado esperado: 32 °F
- Resultado obtenido: 32 °F

### CP02 - Conversión de kilómetros a millas

- Descripción: Verificar la conversión de kilómetros a millas.
- Requerimiento relacionado: RF03
- Entrada: 10 km
- Resultado esperado: 6.21 millas
- Resultado obtenido: 6.21 millas

### CP03 - Conversión de pesos a dólares

- Descripción: Verificar la conversión de pesos mexicanos a dólares utilizando una tasa fija de 18.50.
- Requerimiento relacionado: RF04
- Entradas: 185, 370 y 925 pesos
- Resultados esperados: 10, 20 y 50 dólares
- Resultados obtenidos: 10, 20 y 50 dólares

## Pruebas con pytest

Para ejecutar las pruebas se utiliza:

python -m pytest -v

## Evidencia de ejecución

Las pruebas fueron ejecutadas desde la terminal utilizando pytest.

Resultado obtenido:

5 passed in 0.05s

Todas las pruebas se ejecutaron correctamente.