import sys

sys.setrecursionlimit(2000)


def contar_digitos(num: int) -> int:
    """Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
    utilizar cadenas de caracteres.
    """

    if num == 0:
        return 0
    else:
        return 1 + contar_digitos(num // 10)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    contar_digitos y le pasa el número como parámetro.

    """
    cantidad_digitos = contar_digitos(2488)
    print(cantidad_digitos)


if __name__ == "__main__":
    main()
