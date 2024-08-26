def dia_siguiente(dia, mes, anio):
    ''' Recibe una fecha y devuelve el día siguiente al ingresado en días, meses y años
    
    Pre: dia, mes y anio son números enteros mayores a cero.
    
    Post: devuelve dia2, mes2 y anio2 como una lista.

    '''
    if dia == 31 and mes == 12:
        dia2 = 1
        mes2 = 1
        anio2 = anio + 1
    else:
        if mes == 2:
            if anio%4==0 and (anio%100!=0 or anio%400==0):
                if dia == 29:
                    dia2 = 1
                    mes2 = mes + 1
                    anio2 = anio
                else:
                    dia = dia + 1
                    mes2 = mes
                    anio2 = anio
        else:
            if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                if dia == 31:
                    dia2 = 1
                    mes2 = mes + 1
                    anio2 = anio
                else:
                    dia2 = dia + 1
                    mes2 = mes
                    anio2 = anio
            else:
                if dia == 30:
                    dia2 = 1
                    mes2 = mes + 1
                    anio2 = anio
                else:
                    dia2 = dia + 1
                    mes2 = mes
                    anio2 = anio
    return [dia2, mes2, anio2]


# Programa para sumar n días a la fecha

input_dia = int(input("Ingrese un dia: "))
input_mes = int(input("Ingrese un mes: "))
input_anio = int(input("Ingrese un año: "))

cant_dias_suma = int(input("Ingrese la cantidad de días a sumar: "))
for i in range (cant_dias_suma):
    nuevo_dia = dia_siguiente(input_dia,input_mes,input_anio)
    input_dia = nuevo_dia[0]
    input_mes = nuevo_dia[1]
    input_anio = nuevo_dia[2]

print(f"La fecha resultante es: {nuevo_dia[0]} / {nuevo_dia[1]} / {nuevo_dia[2]}")

# Programa para calcular la cantidad de días existentes entre dos fechas / Se usará año comercial de 360 días y meses de 30 días

inp_dia1 = int(input("Ingrese un dia: "))
input_mes1 = int(input("Ingrese un mes: "))
input_anio1 = int(input("Ingrese un año: "))

input_dia2 = int(input("Ingrese otro dia: "))
input_mes2 = int(input("Ingrese otro mes: "))
input_anio2 = int(input("Ingrese otro año: "))

fecha1 = dia_siguiente(inp_dia1,input_mes1,input_anio1)
fecha2 = dia_siguiente(input_dia2,input_mes2,input_anio2)

diferencia_anios = (fecha1[2] - fecha2[2]) * 360
diferencia_meses = (fecha1[1] - fecha2[1]) * 30
diferencia_dias = fecha1[0] - fecha2[0]

print(f"La cantidad de días transcurridos entre las dos fechas es {diferencia_anios + diferencia_meses + diferencia_dias}")