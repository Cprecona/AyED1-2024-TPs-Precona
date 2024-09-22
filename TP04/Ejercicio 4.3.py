def obtener_claves_separadas(clave_unificada: str) -> str:
    '''Devuelve dos claves separadas a partir de una clave maestra, una con los dígitos 
    ubicados en posiciones impares y otra con los pares.

    Pre: ingresar una cadena de caracteres numéricos.

    Post: devuelve dos cadenas de caracteres numéricos.
    '''
    clave_1 = clave_unificada[::2]
    clave_2 = clave_unificada[1::2]

    return clave_1,clave_2

# PROGRAMA
clave_maestra = '18293'
claves = obtener_claves_separadas(clave_maestra)
clave_n_1 = claves[0]
clave_n_2 = claves[1]
print(f"La clave 1 es {clave_n_1} y la 2 es {clave_n_2}")