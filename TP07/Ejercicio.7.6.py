import sys

sys.setrecursionlimit(2000)


def imprimir_valores_ackerman(m: int, n: int) -> None:
    """La función de Ackermann A(m,n) se define de la siguiente forma:
    n+1 si m = 0
    A(m-1,1) si n = 0
    A(m-1,A(m,n-1)) de otro modo
    Imprimir un cuadro con los valores que adopta la función para valores de m entre 0
    y 3 y de n entre 0 y 7."""

    if m == 0:
        return n + 1
    if n == 0:
        return imprimir_valores_ackerman(m - 1, 1)
    if m != 0 and n != 0:
        return imprimir_valores_ackerman(m - 1, (imprimir_valores_ackerman(m, n - 1)))


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    imprimir_valores_ackerman y le pasa los números como parámetros.

    """
    for m in range(0, 4):
        for n in range(0, 8):
            print(f"{imprimir_valores_ackerman(m, n):>4} | ", end=" ")
        print()


if __name__ == "__main__":
    main()
