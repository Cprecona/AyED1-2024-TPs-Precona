import sys
from typing import List

sys.setrecursionlimit(2000)


def ordenar_con_recursion(lista: List, indice: int) -> List:
    """Realizar la implementación recursiva del método de selección para ordenar una lista
    de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
    posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las
    funciones min() ni max() de Python."""

    if indice == len(lista) - 1:
        return lista
    if lista[indice] > lista[indice + 1]:
        lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]

    return ordenar_con_recursion(lista, indice + 1)


def repetir_ordenamiento(lista: List, vuelta: int) -> List:

    if vuelta == 1:
        return lista
    return repetir_ordenamiento(ordenar_con_recursion(lista, vuelta - 1), vuelta - 1)


def main() -> None:
    """Este es el programa principal. Solamente llama a la funcion
    ordenar_con_recursion y le pasa los números como parámetros.
    El indice será el 0, que sabemos que es el número más pequeño.
    Luego se llama a la funcion repetir_ordenamiento, que dará una
    cantidad de vueltas equivalente al largo de la lista (se pasa como parámetro)
    La idea es que se emule el ordenamiento por burbujeo, que necesita
    ir comparando e intercambiando los elementos adyacentes de la lista,
    pero lo tiene que hacer una cantidad de veces igual al largo
    de la lista para que quede ordenado.

    """
    lista_ordenada_1 = ordenar_con_recursion([2, 8, 6, 7, 4], 0)
    lista_ordenada_final = repetir_ordenamiento(lista_ordenada_1, 5)

    print(lista_ordenada_final)


if __name__ == "__main__":
    main()

""" Profe: creo que me salió, fui ensayando varias cosas, porque al principio
no me quedaba bien ordenado porque sólo hacía una pasada (usaba solamente la primera
función). Luego se me ocurrió usar una segunda función recursiva para que 
tome la anterior y la pase la cantidad de veces según el largo de la lista (como el burbujeo).
Tampoco funcionaba. Fui cambiando el return, hasta que salió (no sé del todo como, jaja, lo hizo mi cerebro)"""
