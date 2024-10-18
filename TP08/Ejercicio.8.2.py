from typing import Tuple


def devolver_fecha_extendida(fecha: Tuple) -> None:
    """Recibe una fecha y la convierte en formato extendido.
    Si el año se pasa como dos dígitos, se toma como año de
    corte el 30. Si el año es superior a 30 se considerará del
    siglo pasado, y sino, del presente.

    Pre: la fecha se pasa como tupla.

    Post: no devuelve nada.
    """

    meses = {
        "1": "enero",
        "2": "febrero",
        "3": "marzo",
        "4": "abril",
        "5": "mayo",
        "6": "junio",
        "7": "julio",
        "8": "agosto",
        "9": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre",
    }
    anio_de_corte = 30
    dia = str(fecha[0])
    mes_numero = str(fecha[1])
    mes_palabra = meses.get(mes_numero)
    anio = fecha[2]
    if anio > 100:
        anio2 = str(anio)
    else:
        if anio > anio_de_corte:
            anio2 = "19" + str(anio)
        else:
            anio2 = "20" + str(anio)

    print(f"{dia} de {mes_palabra} de {anio2}")


# PROGRAMA

devolver_fecha_extendida((1, 4, 31))
