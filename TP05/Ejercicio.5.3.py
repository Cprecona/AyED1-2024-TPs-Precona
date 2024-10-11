def devolver_mes(mes_numero: int) -> str:
    """Recibe el número de un mes y devuelve su nombre.

    Pre: debe pasarse como parámetro el mes (número entero).

    Post: devuelve el nombre. Si el número de mes es inválido devuelve
    una cadena vacía.
    """
    nombre_meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    try:
        mes = nombre_meses[mes_numero - 1]
        assert (
            mes_numero <= 12 and mes_numero > 0 and mes_numero == int(mes_numero)
        ), "Debe ingresar un número válido"
    except:
        return ""
    else:
        return mes


# Programa

mes_a_obtener = devolver_mes(10)
print(mes_a_obtener)
