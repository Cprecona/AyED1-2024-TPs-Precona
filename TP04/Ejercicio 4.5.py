def filtrar_palabras_ciclos(frase: str,num_caracteres: int) -> str:
    '''Recibe una frase y un número N y devuelve una frase que contenga sólo las palabras que tengan
        el número de caracteres N o más.
    
    Pre: la frase debe ser un string y el número un entero positivo.

    Post: devuelve un string.
    '''
    palabras = frase.split()
    palabra_filtrada = []
    for palabra in palabras:
        if len(palabra) >= num_caracteres:
            palabra_filtrada.append(palabra)
    cadena = " ".join(palabra_filtrada)

    return cadena

def filtrar_palabras_lista_comprensión(frase: str,num_caracteres: int) -> str:
    '''Recibe una frase y un número N y devuelve una frase que contenga sólo las palabras que tengan
        el número de caracteres N o más.
    
    Pre: la frase debe ser un string y el número un entero positivo.

    Post: devuelve un string.
    '''
    palabras_filtradas = [palabra for palabra in frase.split() if len(palabra) >= num_caracteres]
    frase_nueva = " ".join(palabras_filtradas)

    return frase_nueva

def filtrar_palabras_filter(frase: str,num_caracteres: int) -> str:
    '''Recibe una frase y un número N y devuelve una frase que contenga sólo las palabras que tengan
        el número de caracteres N o más.
    
    Pre: la frase debe ser un string y el número un entero positivo.

    Post: devuelve un string.
    '''
    palabras_filtradas = list(filter(lambda palabra: len(palabra) >= num_caracteres,frase.split()))
    frase_nueva = " ".join(palabras_filtradas)

    return frase_nueva

# PROGRAMA

frase_prueba = "El camino del guerrero es la resolución sin la sombra de la duda."
frase_filtrada = filtrar_palabras_ciclos(frase_prueba,4)
print(frase_filtrada)

frase_filtrada2 = filtrar_palabras_lista_comprensión(frase_prueba,4)
print(frase_filtrada2)

frase_filtrada3 = filtrar_palabras_filter(frase_prueba,4)
print(frase_filtrada3)