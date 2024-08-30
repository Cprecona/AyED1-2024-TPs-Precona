from random import randint

lista = list(range(randint(1,100))) #creación de una lista con números al azar entre 1 y 100

lista_impares = filter(lambda x: x%2 !=0, lista) #filtrado de los números impares de la lista anterior

print(lista)
print(list(lista_impares))