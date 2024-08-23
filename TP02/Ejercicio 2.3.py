num =int(input("Ingrese un número: "))
lista = [i**2 for i in range(1,num+1)]
print(lista[-10:])