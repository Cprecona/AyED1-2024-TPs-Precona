import sys

sys.setrecursionlimit(2000)


def obtener_resto_restando(num1: int, num2: int) -> int:
    """Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas."""

    if num1 < num2:
        return num1

    return obtener_resto_restando(num1 - num2, num2)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    obtener_resto_restando y le pasa los números como parámetros.

    """
    resto = obtener_resto_restando(3253, 20)

    print(resto)


if __name__ == "__main__":
    main()
