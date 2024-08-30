#Creación e impresión de una lista de números múltiplos de 7 que no sean múltiplos de 5, en un rango de datos ingresado por teclado


A = int(input("Ingrese el primer número del rango: "))
B = int(input("Ingrese el último número del rango: "))

multiplos_7_no_multiplos_5 = [x for x in range(A,B+1) if x%7 == 0 and x%5 !=0] # creación de una lista por comprensión de números impares entre 100 y 200.

print(multiplos_7_no_multiplos_5)
