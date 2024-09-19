from random import randint

def crear_matriz() -> list[list]:
    '''Contrato: crea una matriz con números al azar para una n cantidad de fábricas (filas) ingresada por el usuario, para
    una semana (7 columnas). La cantidad generada al azar por día no puede ser mayor a 150, y puede ser igual a cero.
    Pre: ingresar un número entero para la cantidad de fábricas.
    Pos: devuelve la matriz construida
    '''
    cant_filas = int(input("Ingrese el número de fábricas, que debe ser un entero: "))
    matriz = []
    for i in range(cant_filas):
        fila = []
        for j in range(6):
            produccion = randint(0,150)
            fila.append(produccion)
        matriz.append(fila)
    return matriz


cantidad_bicicletas = crear_matriz()


for i, fabrica in enumerate(cantidad_bicicletas):
    print(f"La cantidad de bicicletas fabricadas en la fábrica {i+1} es {sum(fabrica)}")


# PROGRAMA PARA DETERMINAR LA FÁBRICA EN LA QUE SE PRODUJO MÁS EN UN DÍA DETERMINADO
dia = int(input("Ingrese el número de día a consultar, siendo 0 para lunes, 1 para martes, y así sucesivamente hasta el sábado: "))
dias_semana = ('lunes','martes','miércoles','jueves','viernes','sábado')
mayor_fabricacion = 0
fabrica_mayor_fabricacion = 0
for i, fabrica in enumerate(cantidad_bicicletas):
   if mayor_fabricacion < fabrica[dia]:
        mayor_fabricacion == fabrica[dia]
        fabrica_mayor_fabricacion = i
print(f"La fabrica en la que se fabricó más en el día {dias_semana[dia]} es la fabrica N° {fabrica_mayor_fabricacion}")

# PROGRAMA PARA DETERMINAR EL DIA MÁS PRODUCTIVO CONSIDERANDO TODAS LAS FÁBRICAS COMBINADAS
mayor_fabricacion_por_dia = -1
dia_mayor_fabricacion = -1
for i, dia in enumerate(dias_semana):
    total_dia = sum(fabrica[i] for fabrica in cantidad_bicicletas)
    if mayor_fabricacion_por_dia < total_dia:
        mayor_fabricacion_por_dia == total_dia
        dia_mayor_fabricacion = i
print(f"El día más productivo fue el {dias_semana[i]}")

# PROGRAMA PARA QUE IMPRIMA LA MENOR CANTIDAD PRODUCIDA EN CADA FÁBRICA
menor_cantidad_fabrica = [min(fabrica) for fabrica in cantidad_bicicletas]
for i, fabrica in enumerate(cantidad_bicicletas):
    print(f"La menor cantidad de producción en la fábrica {i+1} fue de {menor_cantidad_fabrica[i]} unidades")
