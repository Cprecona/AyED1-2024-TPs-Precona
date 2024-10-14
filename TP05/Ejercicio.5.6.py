from typing import List

def cargar_numeros() -> List:
    '''Permite cargar por teclado una serie de números y -1 para terminar.
    Guarda los números en una lista.

    Pre: los números deben ser enteros.

    Post: devuelve una lista con los números.
    '''
    lista_numeros =[]
    while True:
        try:
            numero_a_ingresar = int(input("Ingrese de a una vez números enteros y -1 para terminar: "))
        except ValueError:
            print("Ingrese un número entero")
        else:
            if numero_a_ingresar ==-1:
                break
            lista_numeros.append(numero_a_ingresar)
        
    return lista_numeros

def visualizar_posicion_numeros(lista_num: List) -> None:
    '''Permite que el usuario pueda ingresar
    algunos números y ver en qué posición están, usando el método "index".
    Si el número no pertence a la lista se imprimirá un mensaje de error
    y se solicitará otro. Al tercer error detectado se aborta el proceso.

    Pre: se deben ingresar como parámetro una lista de enteros.

    Post: los números cuya posición se consulta deben estar dentro de la lista.
    '''
    intentos_fallidos = 0
    while True:
        try:
            numero_a_buscar = int(input("Ingrese el número cuya posición en la lista quiere saber: "))
            posicion = lista_num.index(numero_a_buscar)
        except ValueError:
            intentos_fallidos += 1
            print("El número no está en la lista")
            if intentos_fallidos >= 3:
                print("Demasiados errores, saliendo del sistema...")
                break
        else:
            print(f"La posición del número {numero_a_buscar} es la N° {posicion+1}")
            break
            

# Programa para cargar y visualizar números

listado_de_numeros = cargar_numeros()
visualizar_posicion_numeros(listado_de_numeros)

