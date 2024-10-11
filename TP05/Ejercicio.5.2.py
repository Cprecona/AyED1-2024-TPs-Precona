def sumar_cadenas(cadena1: str, cadena2: str) -> float:
    """Suma los números reales contenidos en dos cadenas de caracteres
    que se pasan como parámetros.

    Pre: las cadenas deben contener números reales.

    Post: devuelve la suma como número real.
    """
    try:
        suma = float(cadena1) + float(cadena2)

    except ValueError:
        return -1

    else:
        return suma


# Programa

cadenas_sumadas = sumar_cadenas("e5", "40")
print(cadenas_sumadas)
