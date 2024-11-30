import sys
from typing import List

sys.setrecursionlimit(2000)


def devolver_minimo(matriz: List[List], fila: int, columna: int, minimo: int) -> int:
    """Desarrollar una función que devuelva el mínimo elemento de una matriz de M x N."""

    if columna == len(matriz[0]):
        fila += 1
        columna = 0

    if fila == len(matriz):
        return minimo

    if matriz[fila][columna] < minimo:
        minimo = matriz[fila][columna]

    return devolver_minimo(matriz, fila, columna + 1, minimo)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    devolver_minimo y le pasa la matriz como parámetro.

    """
    suma = devolver_minimo([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0, 1000000)
    print(suma)


if __name__ == "__main__":
    main()

# Profe: para que funcione, le puse como mínimo un número muy grande. Sé que esto no la hace universal, pero es lo que se me ocurrió.
