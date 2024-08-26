def concatenar():
    '''Devuelve la concatenación de dos números enteros positivos.
    Pre: los números deben ser enteros positivos.
    Pos: devuelve la concatenación al tomarlos como strings por la manera de ingresarlos.
    '''
    num1 = input("Ingrese un numero: ")
    num2 = input("Ingrese otro numero: ")
    return num1 + num2


resultado = concatenar()
print(resultado)