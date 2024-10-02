from random import randint
from typing import Dict
from typing import List

''' ANALISIS 
HOTEL CON 10 PISOS
6 HABITACIONES POR PISO
DATOS DEL HUESPED:
DNI (NUMERO ENTERO)
APELLIDO Y NOMBRE
FECHA DE INGRESO (DDMMAAAA)
FECHA DE EGRESO (DDMMAAAA)
CANTIDAD DE OCUPANTES

TAREAS:
1) REGISTRAR EL INGRESO HASTA QUE SE INGRESE UN DNI IGUAL A -1
LOS DNI NO PUEDEN REPETIRSE
LA FECHA DE SALIDA DEBE SER MEJOR A LA DE ENTRADA
PISO Y HABITACION RANDOM - NO PUEDEN REPETIRSE

2) SALIDAS
PISO CON MAYOR CANTIDAD DE HABITACIONES
CANTIDAD DE HABITACIONES VACÍAS
PISO CON MAYOR CANTIDAD DE PERSONAS
MOSTRAR CUÁL SERÁ LA PRÓXIMA HABITACIÓN EN DESOCUPARSE. LA FECHA ACTUAL SE INGRESA POR TECLADO
LISTADO DE HUÉSPEDES REGISTRADOS POR APELLIDO.

SE PUEDE HACER UNA MATRIZ. CADA FILA SERÁ UN CHECK IN.

'''
def validar_DNI_duplicado(matriz: List[List], mensaje: str) -> int:
    '''Valida si un DNI ingresado ya se encuentra en la matriz.

    Pre: pasar como parámentro una matriz ya creada con los check-in y
    el mensaje para el input del DNI. Si el DNI está duplicado mostrará un mensaje 
    de error hasta que se ingrese uno correcto.

    Post: devuelve el DNI si no está duplicado.
    '''
    while True:
        try:
            dni = int(input(mensaje))
            if dni == -1:
                return dni
            for fila in matriz:
                if dni == fila[0]:
                    print("El DNI ya existe")
                    break
            else:
                return dni
        except ValueError:
            print("Por favor ingresar un número válido")


def validar_coherencia_fechas() -> int:
    '''Solicita al usuario una fecha de entrada y una fecha de salida. 
    Valida si la fecha de salida es mayor a la de entrada. En ese caso,
    devuelve ambas fechas. Sino muestra un mensaje de error.

    Pre: se solicita al usuario ambas fechas con formato AAAAMMDD.

    Post: devuelve una tupla con las dos fechas válidas.
    '''
    while True:
        fecha_entrada = int(input("Ingrese la entrada con el formato AAAAMMMDD: "))
        fecha_salida = int(input("Ingrese la salida con el formato AAAAMMMDD: "))
        if fecha_entrada < fecha_salida:
            return fecha_entrada,fecha_salida 
        else:
            print("Fecha de entrada mayor a la fecha de salida. Ingrese fechas válidas")

def asignar_piso_habitación(matriz: List[List]) -> int:
    '''Asigna en forma aleatoria un número de piso entre el 1 y el 10 y un número de 
    habitación entre el 1 y el 6. Esos números no pueden repetirse, es decir,
    no debe haber un check in en la matriz que ya los tenga asignados.

    Pre: debe ingresarse como parámetro la matriz de ckeck-in. Los números 
    se generarán de forma automática.

    Post: devolverá una tupla con piso y habitación.
    '''
    while True:
        piso = randint(1,10)
        habitación = randint(1,6)
        for check_in in matriz:
            if piso != check_in[5] and habitación != check_in[6]:
                return piso,habitación


def cargar_check_in() -> List[List]:
    '''Carga los datos de check-in de clientes en un hotel. Devuelve una matriz con todos
    los check-in y sus datos.

    Pre: los datos, excepto el número de piso y habitación, se ingresan por teclado. 
    El DNI no puede repetirse y tiene que ser un número entero. 
    Las fechas tienen que tener el formato AAAAMMDD y la de salida no puede ser mayor
    a la de entrada.
    El apellido y nombre serán strings y el número de ocupantes un entero.

    Post: se genera una matriz cuyas filas serán los check-in.
    '''
    matriz_chech_in = [[0]*7 for _ in range(60)]
    dni = validar_DNI_duplicado(matriz_chech_in,"Ingrese el DNI del huesped: ")
    fila_index = 0
    while dni != -1:
        fila = []
        fila.append(dni)
        apellido_y_nombre = input("Ingrese el apellido y nombre del huesped: ")
        fila.append(apellido_y_nombre)
        fechas = validar_coherencia_fechas()
        fecha_de_entrada = fechas[0]
        fecha_de_salida = fechas[1]
        fila.append(fecha_de_entrada)
        fila.append(fecha_de_salida)
        cant_ocupantes = int(input("Ingrese la cantidad de ocupantes: "))
        fila.append(cant_ocupantes)
        piso_habitacion = asignar_piso_habitación(matriz_chech_in)
        fila.append(piso_habitacion[0])
        fila.append(piso_habitacion[1])
        matriz_chech_in[fila_index] = fila
        fila_index +=1
        dni = validar_DNI_duplicado(matriz_chech_in,"Ingrese el DNI del huesped: ")
    return matriz_chech_in

# PROGRAMA

matriz_habitaciones = cargar_check_in()
print("LISTADO DE HABITACIONES OCUPADAS")
print("DNI\t\tNOMBRE\t\tINGRESO\t\tEGRESO\tOC\tPISO\tHAB")
for check_in in matriz_habitaciones:
    if check_in[0] != 0:
        print("\t".join(map(str,check_in)))
    

# Impresión piso con mayor cantidad de habitaciones ocupadas
pisos =[fila[5] for fila in matriz_habitaciones]
cantidad_pisos_repetidos = [pisos.count(i+1) for i in range(1,11)]
maximo_piso = max(cantidad_pisos_repetidos)
piso_max = cantidad_pisos_repetidos.index(maximo_piso)
print(f"El piso en el que hay más habitaciones ocupadas es el N° {piso_max+1}")

# IMPRESIÓN CANTIDAD DE HABITACIONES VACÍAS
habitaciones = [fila[6] for fila in matriz_habitaciones]
cant_vacias = habitaciones.count(0)
print(f"La cantidad de habitaciones vacías es {cant_vacias}")

# Impresión piso con mayor cantidad de ocupantes
ocupantes_por_piso =[]

for i in range(1,11):
    total_piso = 0
    for fila in matriz_habitaciones:
        if fila[5] == i+1:
            total_piso += fila[4]
    ocupantes_por_piso.append(total_piso)

maximo_piso_ocupantes = max(ocupantes_por_piso)
piso_max_oc = ocupantes_por_piso.index(maximo_piso_ocupantes)
print(f"El piso en el que hay más cantidad de ocupantes es el N° {piso_max_oc+1}")
    
# Impresión de la próxima habitación a desocuparse
fecha_egreso =[fila[3] for fila in matriz_habitaciones if fila[3] != 0]
if not fecha_egreso:
    print("Todas las habitaciones están desocupadas")
else:
    fecha_menor = min(fecha_egreso)
    habitacion_a_desocuparse = None
    piso_a_desocuparse = None
for fila in matriz_habitaciones:
    if fila [3] == fecha_menor:
        habitacion_a_desocuparse = fila[6]
        piso_a_desocuparse = fila[5]

if habitacion_a_desocuparse is not None:
    print(f"La próxima habitación en desocuparse es la N° {habitacion_a_desocuparse} del piso N° {piso_a_desocuparse} ")
else:
    print("Todas las habitaciones están desocupadas")


# Imprimir matriz ordenada por apellido

matriz_convertida = [[str(elemento) for elemento in fila] for fila in matriz_habitaciones]
matriz_ordenada = sorted(matriz_convertida, key=lambda fila: fila[1])
print("LISTADO DE HABITACIONES OCUPADAS ORDENADAS POR APELLIDO")
print("DNI\t\tNOMBRE\t\tINGRESO\t\tEGRESO\tOC\tPISO\tHAB")
for fila in matriz_ordenada:
    if fila[0] != '0':
        print("\t".join(map(str,fila)))