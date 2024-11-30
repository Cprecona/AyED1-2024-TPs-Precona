import sys
from typing import List

sys.setrecursionlimit(2000)


def mcd(x: int, y: int) -> int:
    """Halla el mínimo común divisor de dos números enteros
    no negativos.

    """
    if x == y:
        return x
    if x > y:
        return mcd(x - y, y)
    return mcd(x, y - x)


def hallar_MCD(lista: List, indice: int) -> int:
    """Utilizando la función anterior calcular el MCD de todos los elementos de una lista de
    números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
    utilizar iteraciones en ninguna etapa del proceso."""

    if indice == len(lista) - 1:
        return lista[indice]
    return mcd(lista[indice], hallar_MCD(lista, indice + 1))


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    hallar_MCD y le pasa la lista como parámetro.

    """
    resultado = hallar_MCD([14, 36, 12], 0)
    print(resultado)


if __name__ == "__main__":
    main()
