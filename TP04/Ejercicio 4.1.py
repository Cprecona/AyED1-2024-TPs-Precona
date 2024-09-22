def comprobar_capicua(cadena:str) -> bool:
    '''Comprueba si una cadena de caracteres es capicua.
    Pre: debe ingresarse un string
    Pos: devuelve True si es capicua y False si no lo es.
    '''
    medio = len(cadena)//2
    for i in range(medio):
        resultado = cadena[i] == cadena[-(i+1)]
    
    return resultado

# programa

print(comprobar_capicua('neuquen'))