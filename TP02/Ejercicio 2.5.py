def comprueba_orden_lista(lista):
    '''Comprueba si los datos de una lista están ordenados en forma ascendente.
    Pre: ingresar una lista compuesta por números.
    Pos: devuelve True si está ordenada o False si está desordenada
    '''
    elemento_anterior = lista[0]
    for elem in lista:
        if elem >= elemento_anterior:
            elemento_anterior = elem
            resultado = True
        else:
            resultado = False
    return resultado

lista1=[1,2,3,4]
print(comprueba_orden_lista(lista1))