import random

def carga_lista(n:int):
    '''Carga una lista de N números aleatorios del 1 al 100.
    Pre: cargar un número entero N que será la cantidad de números de la lista.
    Pos: devuelve la lista con números del 1 al 100 (enteros)
    '''
    lista=[random.randint(1,100) for _ in range(n)]
    return lista

def comprueba_repetido(lista):
    '''Recibe una lista y devuelve True si tiene algún elemento repetido.
    Pre: informar una lista.
    Pos: devuelve True si tiene algún elemento repetido.
    '''
    for elem in lista:
        if lista.count(elem) > 1:
            return True

def devuelve_unicos(lista):
    '''Recibe una lista y devuelve una nueva lista con los elementos que no se repiten.
    Pre: informar una lista.
    Pos: devuelve una lista nueva que solamente incluye los elementos no repetidos.
    '''
    lista2=[]
    for elem in lista:
        if lista.count(elem) == 1:
            lista2.append(elem)
    return lista2


N = int(input("Ingrese la cantidad de números que desea para la lista: "))
lista1 = carga_lista(N)
print(lista1)
print(comprueba_repetido(lista1))
print(devuelve_unicos(lista1))
       