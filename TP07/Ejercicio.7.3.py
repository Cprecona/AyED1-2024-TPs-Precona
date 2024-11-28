import sys

sys.setrecursionlimit(2000)


def sumar_naturales(n: int) -> int:
    """Escribir una función que devuelva la suma de los N primeros números naturales."""

    if n == 0:
        return 0
    return n + sumar_naturales(n - 1)


suma = sumar_naturales(10)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    sumar_naturales y le pasa el número como parámetro.

    """

    print(suma)


if __name__ == "__main__":
    main()
