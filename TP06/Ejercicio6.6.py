from random import randint
from tabulate import tabulate
from typing import List


def validar_coherencia_fechas() -> int:
    """Solicita al usuario una fecha de entrada y una fecha de salida.
    Valida si la fecha de salida es mayor a la de entrada. En ese caso,
    devuelve ambas fechas. Sino muestra un mensaje de error.

    Pre: se solicita al usuario ambas fechas con formato AAAAMMDD.

    Post: devuelve una tupla con las dos fechas válidas.
    """
    while True:
        try:
            fecha_entrada = int(input("Ingrese la entrada con el formato AAAAMMMDD: "))
            fecha_salida = int(input("Ingrese la salida con el formato AAAAMMMDD: "))
            if fecha_entrada < fecha_salida:
                return fecha_entrada, fecha_salida
            else:
                print(
                    "Fecha de entrada mayor a la fecha de salida. Ingrese fechas válidas"
                )
        except ValueError:
            print("Ingrese una fecha válida")


def cargar_check_in() -> None:
    """Carga los datos de check-in de clientes en un hotel. Graba los datos en un archivo
    CSV.

    Pre: los datos se ingresan por teclado.
    El DNI no puede repetirse y tiene que ser un número entero.
    Las fechas tienen que tener el formato AAAAMMDD y la de salida no puede ser mayor
    a la de entrada.
    El apellido y nombre serán strings y el número de ocupantes un entero.

    Post: se genera un archivo csv.
    """

    try:
        with open("huespedes.csv", "wt", encoding="utf-8") as archivo_huespedes:
            while True:
                try:
                    dni = int(input("Ingrese el DNI del huesped: "))
                    if dni == -1:
                        break
                except ValueError:
                    print("Ingrese un DNI válido")
                    continue
                with open("huespedes.csv", "rt", encoding="utf-8") as archivo_lectura:
                    lineas = archivo_lectura.readlines()
                    for linea in lineas:
                        campos = linea.strip().split(",")
                        if str(dni) == campos[0]:
                            print("El DNI ya existe")
                            break
                    else:
                        apellido_y_nombre = input(
                            "Ingrese el apellido y nombre del huesped: "
                        )
                        fechas = validar_coherencia_fechas()
                        fecha_de_entrada = fechas[0]
                        fecha_de_salida = fechas[1]
                        cant_ocupantes = int(
                            input("Ingrese la cantidad de ocupantes: ")
                        )
                        linea = ",".join(
                            [
                                str(dni),
                                apellido_y_nombre,
                                str(fecha_de_entrada),
                                str(fecha_de_salida),
                                str(cant_ocupantes),
                            ]
                        )
                        archivo_huespedes.write(f"{linea}\n")
    except FileNotFoundError as msg:
        print(f"El archivo no fue encontrado: {msg}")
    except:
        print("Error en los datos")
    else:
        print("El archivo fue creado exitosamente\n")


def asignar_piso_habitación() -> List[List]:
    """Asigna en forma aleatoria un número de piso entre el 1 y el 10 y un número de
    habitación entre el 1 y el 6. Esos números no pueden repetirse, es decir,
    no debe haber un check in en el archivo que ya los tenga asignados.

    Pre: Los números se generarán de forma automática.

    Post: agregará el dato de piso y habitación al resto de los datos de los pasajeros
    y los guardará en una matriz.
    """

    matriz_check_in = []
    pisos_asignados = set()
    try:
        with open("huespedes.csv", "rt", encoding="utf-8") as archivo_huespedes:
            lineas = archivo_huespedes.readlines()
            for linea in lineas:
                if linea.strip():
                    fila = linea.strip().split(",")
                    while True:
                        piso = randint(1, 10)
                        habitacion = randint(1, 6)
                        if (piso, habitacion) not in pisos_asignados:
                            pisos_asignados.add((piso, habitacion))
                            break
                    fila.append(piso)
                    fila.append(habitacion)
                    matriz_check_in.append(fila)
    except FileNotFoundError as msg:
        print(f"El archivo no fue encontrado: {msg}")
    except:
        print("Error en los datos")
    else:
        print("El archivo fue leido exitosamente\n")
        return matriz_check_in


def main() -> None:
    """Este es el programa principal. Llama a las funciones
    de cargar_check_in y asignar_piso_habitación. De esta forma
    obtiene una matriz con las habitaciones ocupadas.


    """
    cargar_check_in()
    matriz_habitaciones = asignar_piso_habitación()

    # Impresión del listado
    print("LISTADO DE HABITACIONES OCUPADAS")
    headers = ["DNI", "NOMBRE", "INGRESO", "EGRESO", "OCUPANTES", "PISO", "HAB"]
    for check_in in matriz_habitaciones:
        if check_in[0] != 0:
            print(tabulate(matriz_habitaciones, headers=headers, tablefmt="grid"))

    # Impresión piso con mayor cantidad de habitaciones ocupadas
    pisos = [fila[5] for fila in matriz_habitaciones]
    cantidad_pisos_repetidos = [pisos.count(i + 1) for i in range(1, 11)]
    maximo_piso = max(cantidad_pisos_repetidos)
    piso_max = cantidad_pisos_repetidos.index(maximo_piso)
    print(f"El piso en el que hay más habitaciones ocupadas es el N° {piso_max+1}\n")

    # IMPRESIÓN CANTIDAD DE HABITACIONES VACÍAS
    cant_vacias = 60 - len(matriz_habitaciones)
    print(f"La cantidad de habitaciones vacías es {cant_vacias}\n")

    # Impresión piso con mayor cantidad de ocupantes
    ocupantes_por_piso = []

    for i in range(1, 11):
        total_piso = 0
        for fila in matriz_habitaciones:
            if int(fila[5]) == i + 1:
                total_piso += int(fila[4])
        ocupantes_por_piso.append(total_piso)

    maximo_piso_ocupantes = max(ocupantes_por_piso)
    piso_max_oc = ocupantes_por_piso.index(maximo_piso_ocupantes)
    print(f"El piso en el que hay más cantidad de ocupantes es el N° {piso_max_oc+1}\n")

    # Impresión de la próxima habitación a desocuparse
    fecha_egreso = list(
        map(int, [fila[3] for fila in matriz_habitaciones if fila[3] != 0])
    )
    if not fecha_egreso:
        print("Todas las habitaciones están desocupadas\n")
    else:
        fecha_menor = min(fecha_egreso)
        habitacion_a_desocuparse = None
        piso_a_desocuparse = None
        for fila in matriz_habitaciones:
            if fila[3] == fecha_menor:
                habitacion_a_desocuparse = fila[6]
                piso_a_desocuparse = fila[5]

        if habitacion_a_desocuparse is not None:
            print(
                f"La próxima habitación en desocuparse es la N° {habitacion_a_desocuparse} del piso N° {piso_a_desocuparse}\n "
            )
        else:
            print("Todas las habitaciones están desocupadas\n")

    # Imprimir matriz ordenada por cantidad de días de alojamiento

    fecha_ingreso = list(
        map(int, [fila[2] for fila in matriz_habitaciones if fila[2] != 0])
    )
    cantidad_dias_alojamiento = [
        egreso - ingreso for ingreso, egreso in zip(fecha_ingreso, fecha_egreso)
    ]
    for i, fila in enumerate(matriz_habitaciones):
        fila.append(cantidad_dias_alojamiento[i])
    matriz_ordenada = sorted(matriz_habitaciones, key=lambda fila: fila[7])
    headers = [
        "DNI",
        "NOMBRE",
        "INGRESO",
        "EGRESO",
        "OCUPANTES",
        "PISO",
        "HAB",
        "DIAS ALOJAMIENTO",
    ]
    print("LISTADO DE HABITACIONES OCUPADAS ORDENADAS POR APELLIDO")
    for fila in matriz_ordenada:
        if fila[0] != "0":
            print(tabulate(matriz_habitaciones, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
