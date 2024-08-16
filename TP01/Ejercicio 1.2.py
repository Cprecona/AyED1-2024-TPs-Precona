def valida_fecha(dia, mes, anio):
    if 12>=mes>0:
        if mes == 2:
            if anio%4==0 and (anio%100!=0 or anio%400==0):
                if 29>=dia>0:
                    resultado = True
                else:
                    resultado = False
            else:
                if 28>=dia>0:
                    resultado = True
                else:
                    resultado = False
        else:
            if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                if 31>=dia>0:
                    resultado = True
                else:
                    resultado = False
            else:
                if 30>=dia>0:
                    resultado = True
                else:
                    resultado = False
    else:
        resultado = False
    return resultado


INPUTDIA = int(input("Ingrese el dia: "))
INPUTMES = int(input("Ingrese el mes: "))
INPUTANIO = int(input("Ingrese el año: "))

RESULTADO = valida_fecha(INPUTDIA, INPUTMES, INPUTANIO)

print(RESULTADO)
