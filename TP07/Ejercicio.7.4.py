import sys

sys.setrecursionlimit(2000)


def multiplicar_sumando(num1: int, num2: int) -> int:
    """Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas."""

    if num2 == 0:
        return 0

    return num1 + multiplicar_sumando(num1, num2 - 1)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    multiplicar_sumando y le pasa los números como parámetros.

    """
    suma = multiplicar_sumando(4, 3)

    print(suma)


if __name__ == "__main__":
    main()
