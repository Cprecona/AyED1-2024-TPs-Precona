def borrar_duplicados(l1,l2):
    '''Recibe dos listas y elimina en la primera lista los elementos que figuran repetidos respecto de la segunda lista.
    Pre: pasar como argumentos dos listas.
    Pos: devuelve la primera lista modificada.
    '''
    for elem in l1:
        if elem in l2:
            l1.remove(elem)
    return l1

lista1=[3,4,5,6,7,8]
lista2=[1,2,3,4,5,6]

print(borrar_duplicados(lista1,lista2))