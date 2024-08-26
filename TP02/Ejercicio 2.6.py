def normalizar_lista(lista):
    '''Recibe una lista de números enteros y los normaliza, de manera que sumen 1.
    Pre: la lista debe conformarse por números enteros.
    Pos: devuelve la lista normalizada redondeada en dos dígitos decimales.
    '''
    suma_lista=sum(lista)
    for i, elem in enumerate(lista):
        lista[i] = round(elem/suma_lista,2)

    return lista

lista_prueba = [1,1,2,2]
print(normalizar_lista(lista_prueba))