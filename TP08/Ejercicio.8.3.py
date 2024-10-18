from typing import Tuple


def devolver_desarmado(cadena: str) -> Tuple[str, ...]:
    """Recibe una dirección de correo electrónico la divide
    en sus partes componentes. Devuelve las partes en una tupla.

    Pre: el correo electrónico debe ser un string.

    Post: la tupla que devuelve estará compuesta de strings.
    """
    partes1 = cadena.split("@")
    nombre = partes1[0]
    partes2 = partes1[1].split(".")

    return (nombre,) + tuple(partes2)


# Programa

partes_del_correo = devolver_desarmado("cprecona@uade.edu.ar")

print(partes_del_correo)
