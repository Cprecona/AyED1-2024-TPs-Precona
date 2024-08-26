from random import randint

def cargar_lista(cant,lim1,lim2):
    '''Carga una lista con números enteros random de acuerdo a los argumentos pasados
    Pre: "cant" es la cantidad de elementos de la lista. Lim1 y Lim2 los límites del rango que se desea cargar.
    Post: devuelve una lista de números enteros.  
    
    '''
    lista = [randint(lim1,lim2) for _ in range(cant)]
    return lista

cant_naranjas = int(input("Ingrese la cantidad de naranjas: "))

lista_naranjas = cargar_lista(cant_naranjas,150,350)

naranja_300 = 0
naranja_Jugo = 0
for i in lista_naranjas:
    if 200 <= i and i <=300:
        naranja_300 += 1
    if i <=200 or i>=300:
        naranja_Jugo += 1
cantidad_cajones = naranja_300//100

print(f"La cantidad de cajones de naranja que se pueden llenar es {cantidad_cajones}.")
print(f"La cantidad de naranjas para jugo es {naranja_Jugo}.")
print(f"La cantidad de naranjas que quedan fuera para un próximo envío es de {naranja_300%100}.")
print(f"La cantidad de camiones necesarios es {cantidad_cajones * 30 // (500 * 0.8)}.")
