def crear_matriz() -> list[list]: 
    '''Contrato: crea una matriz a partir de dos números ingresados por teclado que representan la cantidad de filas y columnas.
    Pre: tiene que tener más de una fila y más de una columna.
    Pos: devuelve la matriz con los datos ingresados.
    '''
    cant_filas = int(input("Ingrese el número de filas, que debe ser un entero: "))
    cant_columnas = int(input("Ingrese el número de columnas, que debe ser un entero: "))
    matriz = []
    for i in range(cant_filas):
        fila = []   #crea tantas filas como cantidad de filas ingresadas por el usuario a medida que itera
        for j in range(cant_columnas):
            elem = int(input(f"Introduzca los números de la fila {i+1}: ")) #va ingresando los números de la fila en la que está iterando
            fila.append(elem) #se van cargando en la fila.
        matriz.append(fila) # agrega la fila a la matriz

    return matriz

def ordenar_matriz(matriz: list[list]) -> list[list]:
    '''Contrato: recibe una matriz y ordena sus filas en forma ascendente.
    Pre: la matriz no puede estar vacía.
    Pos: devuelve la matriz ordenada.
    '''
    for fila in matriz:
        fila.sort()
    
    return matriz

def intercambiar_filas_matriz(matriz: list[list], fil1: int, fil2: int) -> list[list]:
    '''Contrato: intercambia los datos de una fila respecto de otra en una matriz.
    Pre: se debe ingresar una matriz no vacía. Los números de filas a intercambiar deben existir, ser validos.
    Pos: devuelve la matriz modificada.
    '''
    aux = matriz[fil1]
    matriz[fil1] = matriz[fil2]
    matriz[fil2] = aux
    
    return matriz

def intercambiar_columnas_matriz(matriz: list[list], col1:int, col2:int) -> list[list]:
    '''Contrato: intercambia los datos de una columna respecto de otra en una matriz.
    Pre: se debe ingresar una matriz no vacía. Los números de columna a intercambiar deben existir, ser validos.
    Pos: devuelve la matriz modificada.
    '''
    for i, elem in enumerate(matriz):
        aux = matriz[i][col1]
        matriz[i][col1] = matriz[i][col2]
        matriz[i][col2] = aux
    
    return matriz
def transponer_matriz(matriz: list[list]) -> list[list]:
    '''Contrato: recibe una matriz y devuelve su traspuesta.
    Pre: se debe ingresar una matriz no vacía con la misma cantidad de filas que de columnas.
    Pos: devuelve la matriz modificada.
    '''
    matriz_traspuesta = [[fila[i] for columna in matriz] for i, fila in enumerate(matriz)]

    return matriz_traspuesta

def calcular_promedio_filas(matriz: list[list], num:int) -> float:
    '''Contrato: recibe una matriz y un número de fila y devuelve el promedio de esa fila.
    Pre: se debe ingresar una matriz no vacía. El número de fila debe existir y ser un entero.
    Pos: devuelve el promedio de la fila indicada que puede ser un flotante.
    '''
    numero_de_fila = num-1
    promedio_fila = sum(matriz[numero_de_fila]) / len(matriz[numero_de_fila])

    return promedio_fila

def calcular_porcentaje_impar(matriz: list[list], num:int) -> float:
    '''Contrato: recibe una matriz y un número de columna y devuelve el porcentaje de impares de la columna.
    Pre: se debe ingresar una matriz no vacía. El número de columna debe existir y ser un entero.
    Pos: devuelve el porcentaje de impares de la columna indicada que puede ser un flotante.
    '''
    numero_de_columna = num-1
    cantidad_de_impares = sum(1 for fila in matriz if fila[numero_de_columna] %2 !=0)
    porcentaje_impar = round(cantidad_de_impares / len(matriz) * 100,2)

    return porcentaje_impar

def comprueba_matriz_simetrica_diagonal_principal(matriz: list[list]) -> bool:
    '''Contrato: indica si una matriz es o no simétrica en su diagonal principal.
    Pre: debe ingresarse una matriz cuadrada.
    Pos: devuelve True si es simétrica y False si no lo es
    '''
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True

def comprueba_matriz_simetrica_diagonal_secundaria(matriz: list[list]) -> bool:
    '''Contrato: indica si una matriz es o no simétrica en su diagonal secundaria.
    Pre: debe ingresarse una matriz cuadrada.
    Pos: devuelve True si es simétrica y False si no lo es
    '''
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n-j-1][n-i-1]:
                return False

    return True

def comprobar_capicuas(matriz: list[list]) -> int:
    '''Contrato: los numeros de columnas que sean capicuas.
    Pre: debe ingresarse una matriz valida.
    Pos: devuelve la cantidad de columnas que sean capicua.
    '''
    n = len(matriz)
    m = len(matriz[0])
    resultados = 0

    for j in range(m):
        for i in range(n // 2):
            if matriz[i][j] == matriz[-i+1][j]:
                resultados += 1
                
    return resultados
# PROGRAMA ------------------------------------------------------------------------------------------------

matriz_prueba = crear_matriz()
print("MATRIZ DE PRUEBA ORIGINAL")
for fila in matriz_prueba:
    print(fila)

ordenar_matriz(matriz_prueba)
print("\nMATRIZ ORDENADA")
for fila in matriz_prueba:
    print(fila)

intercambiar_filas_matriz(matriz_prueba,1,2)
print("\nMATRIZ CON FILAS INTERCAMBIADAS")
for fila in matriz_prueba:
    print(fila)

intercambiar_columnas_matriz(matriz_prueba,1,2)
print("\nMATRIZ CON COLUMNAS INTERCAMBIADAS")
for fila in matriz_prueba:
    print(fila)

transponer_matriz(matriz_prueba)
print("\nMATRIZ TRANSPUESTA")
for fila in matriz_prueba: 
    print(fila)

promedio = calcular_promedio_filas(matriz_prueba,1)
print(f"El promedio de la fila es: {promedio}")

porcentaje_de_impares_columna = calcular_porcentaje_impar(matriz_prueba,1)
print(f"El porcentaje de impares en la columna es: {porcentaje_de_impares_columna} %")

simetria = comprueba_matriz_simetrica_diagonal_principal(matriz_prueba)
print(f"¿La matriz en simétrica por su diagonal principal: {simetria}")

simetria_secundaria = comprueba_matriz_simetrica_diagonal_secundaria(matriz_prueba)
print(f"¿La matriz en simétrica por su diagonal secundaria: {simetria_secundaria}")

columnas_capicua = comprobar_capicuas(matriz_prueba)
print(f"La cantidad de columnas capicua es {columnas_capicua}")