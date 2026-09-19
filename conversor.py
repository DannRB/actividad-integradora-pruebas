# Conversor de unidades

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def kilometros_a_millas(kilometros):
    return kilometros * 0.621371


def millas_a_kilometros(millas):
    return millas * 1.60934


def pesos_a_dolares(pesos):
    tipo_cambio = 18.50
    return pesos / tipo_cambio


def dolares_a_pesos(dolares):
    tipo_cambio = 18.50
    return dolares * tipo_cambio


def main():
    print("CONVERSOR DE UNIDADES")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilometros a Millas")
    print("4. Millas a Kilometros")
    print("5. Pesos Mexicanos a Dolares")
    print("6. Dolares a Pesos Mexicanos")

    opcion = input("Selecciona una opcion: ")
    valor = float(input("Ingresa el valor que quieres convertir: "))

    if opcion == "1":
        resultado = celsius_a_fahrenheit(valor)
    elif opcion == "2":
        resultado = fahrenheit_a_celsius(valor)
    elif opcion == "3":
        resultado = kilometros_a_millas(valor)
    elif opcion == "4":
        resultado = millas_a_kilometros(valor)
    elif opcion == "5":
        resultado = pesos_a_dolares(valor)
    elif opcion == "6":
        resultado = dolares_a_pesos(valor)
    else:
        resultado = None
        print("Opcion no valida")

    if resultado is not None:
        print("Resultado:", round(resultado, 2))


if __name__ == "__main__":
    main()