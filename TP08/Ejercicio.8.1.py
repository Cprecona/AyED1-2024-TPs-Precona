from typing import Tuple


def validar_fecha(fecha: Tuple) -> bool:
    """Informa si la fecha ingresada es válida o no.

    Pre: deben ingresarse una tupla con números enteros positivos mayores a cero para el caso de días y años.

    Post: devuelve True si es válida y False si no lo es.
    """
    resultado = False
    if (
        12 >= fecha[1]
        and fecha[1] == 2
        and fecha[2] % 4 == 0
        and (fecha[2] % 100 != 0 or fecha[2] % 400 == 0)
    ):
        if 29 >= fecha[0]:
            resultado = True
        else:
            if 28 >= fecha[0]:
                resultado = True
    if (
        fecha[1] == 1
        or fecha[1] == 3
        or fecha[1] == 5
        or fecha[1] == 7
        or fecha[1] == 8
        or fecha[1] == 10
        or fecha[1] == 12
    ):
        if 31 >= fecha[0]:
            resultado = True
        else:
            if 30 >= fecha[0]:
                resultado = True

    return resultado


def dia_siguiente(fecha: Tuple) -> Tuple:
    """Recibe una fecha y devuelve el día siguiente al ingresado en días, meses y años

    Pre: dia, mes y anio son números enteros mayores a cero.

    Post: devuelve dia2, mes2 y anio2 como una tupla.

    """
    dia2, mes2, anio2 = fecha

    if dia2 == 31 and mes2 == 12:
        dia2 = 1
        mes2 = 1
        anio2 += 1
    else:
        if mes2 == 2:
            if anio2 % 4 == 0 and (anio2 % 100 != 0 or anio2 % 400 == 0):
                if dia2 == 29:
                    dia2 = 1
                    mes2 += 1
                else:
                    dia2 += 1
            else:
                if dia2 == 28:
                    dia2 = 1
                    mes2 += 1
                else:
                    dia2 += 1
        else:
            if mes2 in [1, 3, 5, 7, 8, 10, 12]:
                if dia2 == 31:
                    dia2 = 1
                    mes2 += 1
                else:
                    dia2 += 1
            else:
                if dia2 == 30:
                    dia2 = 1
                    mes2 += 1
                else:
                    dia2 += 1
    return dia2, mes2, anio2


def validar_horario(hora: Tuple) -> bool:
    """Recibe una tupla con dos datos: hora y minutos.
    Valida si es correcto.

    Pre: la hora es una tupla con dos números enteros.

    Post: devuelve True si es correcto y False si es falso.
    """
    horas = hora[0]
    minutos = hora[1]
    resultado = (
        True
        if (horas <= 23 and minutos <= 60 and horas >= 0 and minutos >= 0)
        else False
    )

    return resultado


def calcular_diferencia_horario(horarios: Tuple) -> Tuple:
    """Recibe una tupla con dos horarios y calcula la diferencia.

    Pre: la tupla contiene dos tuplas con el horario de inicio y
    el de fin.

    Post: devuelve una tupla con la diferencia en horas y minutos.

    """
    horas1 = horarios[0][0]
    minutos1 = horarios[0][1]
    horas2 = horarios[1][0]
    minutos2 = horarios[1][1]

    validacion_1 = validar_horario((horas1, minutos1))
    validacion_2 = validar_horario((horas2, minutos2))

    dif_min = 0
    dif_horas = 0

    if validacion_1 is False or validacion_2 is False:
        print("Ingresar un horario válido")
    else:
        if minutos1 < minutos2:
            dif_min = minutos1 + 60 - minutos2
            if (horas1 - 1) < horas2:
                dif_horas = horas2 - (horas1 - 1)
            else:
                dif_horas = (horas1 - 1) - horas2
        else:
            dif_min = minutos1 - minutos2
            if horas1 < horas2:
                dif_horas = horas2 - horas1
            else:
                dif_horas = horas1 - horas2

    return dif_horas, dif_min


# Programa para verificar una fecha

resultado_validacion = validar_fecha((29, 2, 2023))
if resultado_validacion:
    print("La fecha es válida")
else:
    print("La fecha es inválida")

# Programa para sumar n días a la fecha

fecha_original = (28, 2, 2023)
cant_dias_suma = int(input("Ingrese la cantidad de días a sumar: "))
for i in range(cant_dias_suma):
    fecha_original = dia_siguiente((fecha_original))
print(f"La nueva fecha es {fecha_original[0]}/{fecha_original[1]}/{fecha_original[2]}")

# Programa para devolver si un horario es válido

validez = validar_horario((28, 10))
if validez:
    print("El horario es válido")
else:
    print("El horario es inválido")

# Programa para mostrar la diferencia entre dos horarios

diferencia = calcular_diferencia_horario(((20, 10), (10, 30)))
print(f"La diferencia es de {diferencia[0]} horas y {diferencia[1]} minutos")
