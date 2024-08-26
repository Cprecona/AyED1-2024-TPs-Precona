def calcular_gasto_viajes(cant):
    '''Calcula el gasto total en viajes de subte en función de la cantidad ingresada por el usuario.
    Pre: debe ingresarse un número entero mayor a cero.
    Pos: devuelve un flotante
    '''
    if 1 <= cant and cant <=20:
        gasto = 650 * cant
    else:
        if 21 <= cant and cant <=30:
            gasto = 650 * 20 + (cant - 20) * 650 * 0.80
        else:
            if 31 <= cant and cant <=40:
                gasto = 650 * 20 + 650 * 10 * 0.80 + (cant - 30) * 650 * 0.70
            else:
                if 41 <= cant:
                    gasto = 650 * 20 + 650 * 10 * 0.80 + 650 * 10 * 0.70 + (cant - 40) * 650 * 0.60
    return gasto

cant_viajes = int(input("Ingrese la cantidad de viajes del mes: "))

gasto_total = calcular_gasto_viajes(cant_viajes)

print("El gasto total del mes fue de $ ", gasto_total)
