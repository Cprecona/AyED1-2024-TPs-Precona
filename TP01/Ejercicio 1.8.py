def dia_de_la_semana(dia:int,mes: int,anio: int) -> int:
    '''Permite averiguar el día de la semana para una fecha determinada. 
    La fecha se suministra en forma de tres parámetros enteros y la función 
    devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. 
    
    '''

    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def main() -> None:
    '''Este es el programa principal. Llama a la función dias_de_la semana,
    previo pedir el mes año, para pasarle los parámetros.
    Luego a partir de eso se genera el calendario con formato tradicional.
    '''

    treinta = (4,6,9,11)
    treinta_y_uno = (1,3,5,7,8,10,12)

    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    dia = 1
    dia_sem_1 = dia_de_la_semana(dia,mes,anio)

    dias_a_imprimir = 0
    if mes in treinta:
        dias_a_imprimir = 30
    elif mes in treinta_y_uno:
        dias_a_imprimir = 31
    elif mes == 2:
        if anio%4==0 and (anio%100!=0 or anio%400==0):
            dias_a_imprimir = 29
        else:
            dias_a_imprimir = 28

    lista_dias = list(range(1,dias_a_imprimir+1))
    ceros = [0]*dia_sem_1
    lista_dias = ceros + lista_dias
    
    semanas = [lista_dias[i:i + 7] for i in range(0, len(lista_dias), 7)]

    print(f"*** CALENDARIO MES de {mes} de {anio}***")
    print("\nD | L | M | M | J | V | S ")
    for semana in semanas:
        print("  ".join(str(dia) for dia in semana))

if __name__ == "__main__":
    main()
