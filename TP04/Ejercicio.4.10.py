def reemplazar_apariciones_palabras(
    frase: str, palabra_a_reemplazar: str, palabra_nueva: str
) -> str:
    """Recibe una cadena y reemplaza todas apariciones de una palabra
    por otra.

    Pre: la cadena y palabras son strings y se pasan como argumento.

    Post: devuelve un string con la cadena nueva. Imprime la cantidad
    de reemplazos realizados, que es un entero.

    """
    palabras = list(frase.split())
    for i, palabra in enumerate(palabras):
        if palabra == palabra_a_reemplazar:
            palabras[i] = palabra_nueva
    cadena_nueva = " ".join(palabras)
    cantidad_de_reemplazos = cadena_nueva.count(palabra_nueva)
    print(f"La cantidad de reemplazos fue de {cantidad_de_reemplazos}")

    return cadena_nueva


# PROGRAMA

cadena_original = "El gato estaba jugando con la bolsa y la bolsa atrapó al gato"
cadena_modificada = reemplazar_apariciones_palabras(cadena_original, "gato", "perro")
print(cadena_modificada)
