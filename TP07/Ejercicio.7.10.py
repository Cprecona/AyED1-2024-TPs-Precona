import sys
from typing import List

sys.setrecursionlimit(2000)


def sumar_matriz(matriz: List[List], fila: int, columna: int, suma: int) -> int:
    """Escribir una función que sume todos los elementos de una matriz de M x N y devuelva el resultado. No usar la función sum()."""

    if columna == len(matriz[0]):
        fila += 1
        columna = 0

    if fila == len(matriz):
        return suma

    suma += matriz[fila][columna]
    return sumar_matriz(matriz, fila, columna + 1, suma)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    sumar_matriz y le pasa la matriz como parámetro.

    """
    suma = sumar_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0, 0)
    print(suma)


if __name__ == "__main__":
    main()
