def calcular_max_estricto(n1, n2, n3):
    '''Devuelve el número máximo de los ingresado siempre que sea único.
    Pre: deben ingresarse números enteros positivos.
    Pos: devuelve el máximo siempre que sea único. De lo contrario, emite una sentencia informativa.
    '''
    if n1 < n2:
        if n2 < n3:
            nummax = n3
        else:
            if n2 == n3:
                nummax = -1
            else:
                nummax = n2
    else:
        if n1 < n3:
            nummax = n3
        else:
            if n1 == n2:
                nummax = -1
            else:
                nummax = n1

    return nummax

num1 = int(input("Ingrese un numero entero positivo: "))
num2 = int(input("Ingrese un numero entero positivo: "))
num3 = int(input("Ingrese un numero entero positivo: "))

num_maximo = calcular_max_estricto(num1,num2,num3)

if num_maximo == -1:
    print ("No existe un maximo estricto")
else:
    print ("El numero maximo es: ", num_maximo)
