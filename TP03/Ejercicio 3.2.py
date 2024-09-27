def crear_matriz() -> list[list]: 
    '''Crea una matriz a partir de dos números ingresados por teclado que representan la cantidad de filas y columnas.
    
    Pre: tiene que tener más de una fila y más de una columna.
    
    Pos: devuelve la matriz con los datos ingresados.
    '''
    cant_filas = int(input("Ingrese el número de filas, que debe ser un entero: "))
    cant_columnas = int(input("Ingrese el número de columnas, que debe ser un entero: "))
    matriz = [[0]*cant_columnas for _ in range(cant_filas)]
    return matriz
    
def cargar_matriz_a(matriz: list[list]) -> list[list]:
    '''Recibe una matriz y la carga, en la diagonal principal (comenzando desde
    el elemento 1 de la fila 1), con números impares, comenzando por el 1.

    Pre: ingresar una matriz.

    Post: devuelve la matriz cargada.
    '''
    numero_impar = 1
    for i, fila in enumerate(matriz):
        matriz[i][i] = numero_impar
        numero_impar +=2
            
    return matriz

def cargar_matriz_b(matriz: list[list]) -> list[list]:
    '''Recibe una matriz y la carga, en la diagonal inversa (comenzando desde
    el último elemento de la fila 1, el anteúltimo de la 2 y así sucesivamente), 
    con números que surjan de multiplicar por 3 el número anterior,
    comenzando por el 1 en la última fila.

    Pre: ingresar una matriz.

    Post: devuelve la matriz cargada.
    '''
    n = len(matriz)
    numero_inicio = 3**(n-1)
    for i in range(n):
        matriz[i][n-1-i] = numero_inicio
        numero_inicio = numero_inicio // 3
            
    return matriz

def cargar_matriz_c(matriz: list[list]) -> list[list]:
    '''Recibe una matriz y la carga con números de la siguiente manera:
    En la primera fila, un número en la primera posición que es igual al len de la matriz.
    En las siguientes filas: len de la matriz menos número de fila, en las posiciones que 
    corresponden al número de fila (ejemplo, en la fila 2, si el len es 4, será 4-1: 3, 
    repetido en las posiciones 1 y 2 (fila 2)).

    Pre: ingresar una matriz.

    Post: devuelve la matriz cargada.
    '''
    n = len(matriz)
    matriz[0][0] = n
    for i in range(1,n):
        num_a_repetir = n - i
        for j in range(i+1):
            matriz[i][j] = num_a_repetir
            
    return matriz

def cargar_matriz_d(matriz: list[list]) -> list[list]:
    '''Recibe una matriz y la carga con números de la siguiente manera:
    en la primera fila el len multiplicado * 2 y en las siguientes
    la fila anterior / 2. 

    Pre: ingresar una matriz.

    Post: devuelve la matriz cargada.
    '''
    n = len(matriz)
    primer_numero = n*2
    matriz[0]= [primer_numero]*n
    for i in range(1,n):
        primer_numero //= 2
        for j in range(n):
            matriz[i][j] = primer_numero
            
    return matriz

def cargar_matriz_e(matriz: list[list]) -> list[list]:
    '''Recibe una matriz y la carga con números de la siguiente manera:
    Alterna 0 con números del 1 al doble del len de la matriz. 

    Pre: ingresar una matriz.

    Post: devuelve la matriz cargada.
    '''
    n = len(matriz)
    primer_numero = 1
    for i in range(n):
        for j in range(n):
            if i%2 == 0 and j%2 !=0:                
                matriz[i][j] = primer_numero
                primer_numero +=1
            else:
                if i%2 != 0 and j%2 ==0:                
                    matriz[i][j] = primer_numero
                    primer_numero +=1
            
    return matriz

def cargar_matriz_f(matriz: list[list]) -> list[list]:
    '''Recibe una matriz y la carga con números de la siguiente manera:
    En cada fila tiene la misma cantidad de números que i+1. Los números
    comienzan con 1 para la primera fila y se incrementan consecutivamente.

    Pre: ingresar una matriz.

    Post: devuelve la matriz cargada.
    '''
    n = len(matriz)
    primer_numero = 1
    for i in range(n):
        for j in range(i+1):
            matriz[i][-(j+1)] = primer_numero
            primer_numero +=1
           
    return matriz

# PROGRAMA

matriz_prueba = crear_matriz()
matriz_a = cargar_matriz_a(matriz_prueba)
for fila in matriz_a:
    print(fila)

matriz_prueba_2 = crear_matriz()
matriz_b = cargar_matriz_b(matriz_prueba_2)
for fila in matriz_b:
    print(fila)

matriz_prueba_3 = crear_matriz()
matriz_c = cargar_matriz_c(matriz_prueba_3)
for fila in matriz_c:
    print(fila)

matriz_prueba_4 = crear_matriz()
matriz_d = cargar_matriz_d(matriz_prueba_4)
for fila in matriz_d:
    print(fila)

matriz_prueba_5 = crear_matriz()
matriz_e = cargar_matriz_e(matriz_prueba_5)
for fila in matriz_e:
    print(fila)

matriz_prueba_6 = crear_matriz()
matriz_f = cargar_matriz_f(matriz_prueba_6)
for fila in matriz_f:
    print(fila)

# FALTA DESARROLLAR LAS ÚLTIMAS 2