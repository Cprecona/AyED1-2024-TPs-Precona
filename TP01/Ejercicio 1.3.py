def gasto_viajes(cant):
    if 1 <= cant <=20:
        gasto = 650 * cant
    else:
        if 21 <= cant <=30:
            gasto = 650 * 20 + (cant - 20) * 650 * 0.80
        else:
            if 31 <= cant <=40:
                gasto = 650 * 20 + 650 * 10 * 0.80 + (cant - 30) * 650 * 0.70
            else:
                if 41 <= cant:
                    gasto = 650 * 20 + 650 * 10 * 0.80 + 650 * 10 * 0.70 + (cant - 40) * 650 * 0.60
    return gasto

cantViajes = int(input("Ingrese la cantidad de viajes del mes: "))

GASTOTOTAL = gasto_viajes(cantViajes)

print("El gasto total del mes fue de $ ", GASTOTOTAL)
