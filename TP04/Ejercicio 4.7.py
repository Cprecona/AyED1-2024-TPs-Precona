def eliminar_subcadena_rebanadas(cadena: str,pos: int, cant: int) -> str:
    '''Recibe una cadena de caracteres y elimina de la misma
    una subcadena cuya posición y cantidad de caracteres deseada
    es pasada como parámetro. Devuelve la cadena original sin esa subcadena como retorno.

    Pre: la cadena debe ser un string. La posición y cantidad se pasan
    como parámetros y deben ser enteros.

    Post: retorna una cadena sin la subcadena como string.
    '''
    subcadena = cadena[:pos:] + cadena[pos+cant::]

    return subcadena

def eliminar_iterando(cadena: str,pos: int, cant: int) -> str:
    '''Recibe una cadena de caracteres y elimina de la misma
    una subcadena cuya posición y cantidad de caracteres deseada
    es pasada como parámetro. Devuelve la cadena como retorno.

    Pre: la cadena debe ser un string. La posición y cantidad se pasan
    como parámetros y deben ser enteros.

    Post: retorna una cadena sin la subcadena como string.
    '''
    posicion_inicio = pos
    subcadena_iterando = ""
    for posicion, caracter in enumerate(cadena):
        if posicion <= posicion_inicio or posicion >= posicion_inicio+cant:
            subcadena_iterando += caracter

    return subcadena


# PROGRAMA

# Eliminación subcadena utilizando rebanadas

cadena_original = "El número de teléfono es 4356-7890 y ya lo agendé"
subcadena = eliminar_subcadena_rebanadas(cadena_original,25,9)
print(subcadena)

# Eliminación subcadena sin utilizar rebanadas

cadena_original = "El número de teléfono es 4356-7890 y ya lo agendé"
subcadena_2 = eliminar_iterando(cadena_original,25,9)
print(subcadena_2)