import random

def cargar_lista():
    ''' Genera una lista de una cantidad aleatoria de datos de dos dígitos. Los números de la lista también
    son aleatorios y tienen 4 dígitos.    
    '''
    cantidad_elementos = random.randint(10,99)
    lista=[random.randint(1000,9999) for _ in range(cantidad_elementos)]

    return lista

def calcular_producto_lista(lista):
    '''Devuelve el producto de todos los elementos de una lista
    Pre: debe hacerse referencia a una lista.
    Pos: devuelve como resultado un número entero o flotante.    
    '''
    resultado = 1
    for i in lista:
        resultado = i*resultado
    return resultado

def eliminar_item(lista,val_elim):
    '''Elimina todas las repeticiones del elemento que se ingrese dentro de una lista.
    Pre: debe ingresase una lista y un elemento.
    Pos: no devuelve nada, solamente elimina los elementos.    
    '''
    for i in lista:
        if i == val_elim:
            lista.remove(val_elim)
    return lista

def comprobar_capicua(lista):
    '''Comprueba si una lista es capicua.
    Pre: debe cargarse una lista.
    Pos: devuelve True si es capicua y False si no lo es.
    '''
    medio = len(lista)//2
    for i in range(medio):
        if i == -(i+1):
            return True
        else:
            return False


lista1 = cargar_lista()
print(lista1)
producto = calcular_producto_lista(lista1)
print(producto)
lista_con_eliminaciones = eliminar_item(lista1,2057)
print(lista_con_eliminaciones)
capicua = comprobar_capicua(lista1)
print(f"¿La lista es capicua? -> {capicua}")
