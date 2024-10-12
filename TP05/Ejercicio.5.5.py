from math import sqrt

# Programa raíz cuadrada

"""Solicita un número al usuario y calcula su raíz cuadrada.
Si se ingresa un número negativo informa un mensaje de error.

Pre: el usuario debe ingresar un número positivo.

Post: imprime la raíz cuadrada
"""

while True:
    try:
        numero_conocer_raiz = float(input("Ingrese un número positivo: "))
        assert numero_conocer_raiz > 0, "Debe ingresar un número positivo"
    except AssertionError as mensaje:
        print(mensaje)
    except:
        print("Dato inválido, debe ingresar un número positivo")
    else:
        print(
            f"La raíz cuadrada de {numero_conocer_raiz} es {sqrt(numero_conocer_raiz)}"
        )
