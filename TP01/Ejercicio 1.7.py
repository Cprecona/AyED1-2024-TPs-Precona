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

DIA = int(input("Ingrese un dia: "))
MES = int(input("Ingrese un mes: "))
ANIO = int(input("Ingrese un año: "))

cantDiasSuma = int(input("Ingrese la cantidad de días a sumar: "))
for i in range (cantDiasSuma):
    diaSiguiente = dia_siguiente(DIA,MES,ANIO)
    DIA = diaSiguiente[0]
    MES = diaSiguiente[1]
    ANIO = diaSiguiente[2]

print("La fecha resultante es: ", diaSiguiente[0], "/", diaSiguiente[1], "/", diaSiguiente[2])

# Programa para calcular la cantidad de días existentes entre dos fechas / Se usará año comercial de 360 días y meses de 30 días

DIA1 = int(input("Ingrese un dia: "))
MES1 = int(input("Ingrese un mes: "))
ANIO1 = int(input("Ingrese un año: "))

DIA2 = int(input("Ingrese otro dia: "))
MES2 = int(input("Ingrese otro mes: "))
ANIO2 = int(input("Ingrese otro año: "))

fecha1 = dia_siguiente(DIA1, MES1, ANIO1)
fecha2 = dia_siguiente(DIA2, MES2, ANIO2)

diferenciaAnios = (fecha1[2] - fecha2[2]) * 360
diferenciaMeses = (fecha1[1] - fecha2[1]) * 30
diferenciaDias = fecha1[0] - fecha2[0]

print("La cantidad de días transcurridos entre las dos fechas es ", diferenciaAnios + diferenciaMeses + diferenciaDias)
