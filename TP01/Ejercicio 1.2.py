def validar_fecha(dia, mes, anio):
    '''Informa si la fecha ingresada es válida o no.
    Pre: deben ingresarse números enteros positivos mayores a cero para el caso de días y años.
    Pos: devuelve True si es válida y False si no lo es.
    '''
    if 12>=mes:
        if mes == 2:
            if anio%4==0 and (anio%100!=0 or anio%400==0):
                if 29>=dia:
                    resultado = True
                else:
                    resultado = False
            else:
                if 28>=dia:
                    resultado = True
                else:
                    resultado = False
        else:
            if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                if 31>=dia:
                    resultado = True
                else:
                    resultado = False
            else:
                if 30>=dia:
                    resultado = True
                else:
                    resultado = False
    else:
        resultado = False
    return resultado


input_dia = int(input("Ingrese el dia: "))
input_mes = int(input("Ingrese el mes: "))
input_anio = int(input("Ingrese el año: "))

resultado = validar_fecha(input_dia, input_mes, input_anio)

print(resultado)
