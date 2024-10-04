def ordenar_palabras(cadena: str) -> str:
    '''Recibe una cadena de caracteres con palabras separadas
    por uno o más espacios y devolverla con las palabras ordenadas
    según su longitud dejando un espacio entre cada una.

    Pre: la cadena tiene que ser un string y las palabras tienen
    que estar separadas por uno o más espacios.

    Post: devuelve la cadena con las palabras ordenadas según
    su longitud en forma ascendente.
    '''

    palabra_filtrada = sorted(cadena.split(), key= len)
    cadena_ordenada = " ".join(palabra_filtrada)

    return cadena_ordenada

# PROGRAMA

cadena_original = "Aragorn Arwen Elros Elrond Durin Gandalf"
cadena_modificada = ordenar_palabras(cadena_original)
print(cadena_modificada)