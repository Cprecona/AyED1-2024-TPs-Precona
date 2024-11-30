import sys
from typing import List

sys.setrecursionlimit(2000)


def imprimir_matriz(matriz: List[List], vueltas: int) -> None:
    """Realizar una función recursiva para imprimir una matriz de M x N con el formato
    apropiado."""

    if vueltas == len(matriz):
        return None
    print(matriz[vueltas])
    return imprimir_matriz(matriz, vueltas + 1)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    imprimir_matriz y le pasa la matriz como parámetro.

    """
    imprimir_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0)


if __name__ == "__main__":
    main()
