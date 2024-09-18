import random

'''Contrato: genera una matriz de una cantidad de filas y columnas ingresadas por el usuario.
Luego carga la matriz con números al azar únicos, en un rango de 0 al cuadrado de la cantidad de filas.
Pre: ingresar un número entero de filas y de columnas.
Pos: imprime la matriz generada.
'''
cant_filas = int(input("Ingrese el número de filas, que debe ser un entero: "))
cant_columnas = int(input("Ingrese el número de columnas, que debe ser un entero: "))
matriz = []
for i in range(cant_filas):
    for j in range(cant_columnas):
        numeros = range(0,9999)
        no_repetidos = random.sample(numeros,cant_filas**2)
        matriz.append(no_repetidos)

for fila in matriz:
    print(fila)