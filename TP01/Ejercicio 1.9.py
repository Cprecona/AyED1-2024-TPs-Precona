import random

def carga_lista(cant,lim1,lim2):
    '''Carga una lista con números enteros random de acuerdo a los argumentos pasados
    Pre: "cant" es la cantidad de elementos de la lista. Lim1 y Lim2 los límites del rango que se desea cargar.
    Post: devuelve una lista de números enteros.  
    
    '''
    lista = [random.randint(lim1,lim2) for _ in range(cant)]
    return lista

CANTNARANJAS = int(input("Ingrese la cantidad de naranjas: "))

LISTANARANJAS = carga_lista(CANTNARANJAS,150,350)

naranja300 = 0
naranjaJugo = 0
for i in LISTANARANJAS:
    if 200 <= i <=300:
        naranja300 += 1
    if i <=200 or i>=300:
        naranjaJugo += 1
CANTIDADCAJONES = naranja300//100

print(f"La cantidad de cajones de naranja que se pueden llenar es {CANTIDADCAJONES}.")
print(f"La cantidad de naranjas para jugo es {naranjaJugo}.")
print(f"La cantidad de naranjas que quedan fuera para un próximo envío es de {naranja300%100}.")
print(f"La cantidad de camiones necesarios es {CANTIDADCAJONES * 30 // (500 * 0.8)}.")
