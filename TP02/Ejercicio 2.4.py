def borrar_duplicados(l1,l2):
    '''Recibe dos listas y elimina en la primera lista los elementos que figuran repetidos respecto de la segunda lista.
        Pre: pasar como argumentos dos listas.
    Pos: imprime las dos listas originales, la lista con los elementos eliminados y la original modificada.
    '''
    print(f"Lista original sin modificaciones ->{l1}")
    print(f"Segunda lista ->{l2}")
    lista_elim =[]
    for elem in l1:
        if elem in l2:
            l1.remove(elem)
            lista_elim.append(elem)
    print(f"Lista de elementos elminados de la primera lista ->{lista_elim}")
    print(f"Lista de original con las eliminaciones ->{l1}")

# Ejemplos de listas para la impresión
lista1=[3,4,5,6,7,8]
lista2=[1,2,3,4,5,6]

borrar_duplicados(lista1,lista2)