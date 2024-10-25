from typing import Tuple


def verificar_ortogonal(vector1: Tuple[int, float], vector2: Tuple[int, float]) -> bool:
    """Recibe dos vectores y verifica si son ortogonales.

    Pre: los vectores se reciben como parámetros y deben ser
    tuplas. Tienen que contener dos números reales cada uno.

    Post: devuelve True si son ortogonales y False si no lo son
    """
    try:
        if len(vector1) != 2 or len(vector2) != 2:
            raise AssertionError("Los vectores no tienen dos números cada uno")
    except AssertionError as mesage:
        print(mesage)
        return False
    else:
        producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        if producto_escalar == 0:
            return True
        else:
            return False


def main() -> None:
    """Este es el programa principal. Pasa los vectores a la función
    verificar_ortogonal. Imprime el resultado.

    Pre: los parámetros tienen que tener dos números reales cada uno.

    Post: imprime el resultado.
    """
    try:
        resultado = verificar_ortogonal((2, 3), (-3, 2))
    except NameError:
        print("Datos inválidos")
    else:
        print(resultado)


if __name__ == "__main__":
    main()
