from typing import Tuple


def verificar_fichas_domino(ficha1: Tuple[int], ficha2: Tuple[int]) -> bool:
    """Verifica si dos fichas de dominó encajan o no. Las fichas de dominó
    se pasan como parámetros en tuplas. Los números del dominó son
    enteros del 1 al 6.

    Pre: las fichas se pasan como tuplas compuestas de enteros.

    Post: devuelve True si encajan y False si no.
    """

    try:
        numeros = [ficha1[0], ficha1[1], ficha2[0], ficha2[1]]
        for numero in numeros:
            if numero < 1 or numero > 6:
                raise AssertionError("Las tuplas no tienen números válidos del 1 al 6")
    except AssertionError as mesaje:
        print(mesaje)
    else:
        conjunto = set(ficha1 + ficha2)
        if len(conjunto) in [1, 3]:
            return True
        else:
            return False


def main() -> None:
    """Este es el programa principal

    Pre: pasa como parámentros las tuplas.

    Post: imprime el resultado de la función verificar_fichas_domino. No devuelve nada.
    """
    resultado = verificar_fichas_domino((3, 4), (5, 4))
    print(resultado)


if __name__ == "__main__":
    main()
