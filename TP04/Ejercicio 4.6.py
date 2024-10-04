def extraer_subcadena_rebanadas(cadena: str,pos: int, cant: int) -> str:
    '''Recibe una cadena de caracteres y extrae de la misma
    una subcadena cuya posición y cantidad de caracteres deseada
    es pasada como parámetro. Devuelve la cadena como retorno.

    Pre: la cadena debe ser un string. La posición y cantidad se pasan
    como parámetros y deben ser enteros.

    Post: retorna una subcadena como string.
    '''
    subcadena = cadena[pos:pos+cant:]

    return subcadena

def extraer_iterando_(cadena: str,pos: int, cant: int) -> str:
    '''Recibe una cadena de caracteres y extrae de la misma
    una subcadena cuya posición y cantidad de caracteres deseada
    es pasada como parámetro. Devuelve la cadena como retorno.

    Pre: la cadena debe ser un string. La posición y cantidad se pasan
    como parámetros y deben ser enteros.

    Post: retorna una subcadena como string.
    '''
    posicion_inicio = pos
    subcadena_iterando = ""
    while len(subcadena_iterando) < cant:
        for posicion, caracter in enumerate(cadena):
            if posicion >= posicion_inicio:
                subcadena_iterando += caracter

    return subcadena

# PROGRAMA

# Extracción subcadena utilizando rebanadas

cadena_original = "El número de teléfono es 4356-7890"
subcadena_1 = extraer_subcadena_rebanadas(cadena_original,25,9)
print(subcadena_1)

# Extracción subcadena sin utilizar rebanadas

cadena_original = "El número de teléfono es 4356-7890"
subcadena_2 = extraer_iterando_(cadena_original,25,9)
print(subcadena_2)