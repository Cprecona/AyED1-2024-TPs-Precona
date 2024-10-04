def devolver_subcadena(cadena: str, cant: int) -> str:
    '''Recibe una cadena de caracteres y deuvelve una subcadena de N cantidad 
    de caracteres que se pasan como parámetros.

    Pre: la cadena debe ser un string. La cantidad y la cantidad
    se pasan como parámetros.

    Post: retorna un string.
    '''
    subcadena = cadena[-cant::]

    return subcadena

# PROGRAMA

cadena_original = "El número de teléfono es 4356-7890 y ya lo agendé."
subcadena_1 = devolver_subcadena(cadena_original,10)
print(subcadena_1)