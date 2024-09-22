import random

def cargar_sala(matriz: list[list]) -> list[list]:
    '''Contrato: recibe una matriz y la carga con valores aleatorios: "reservada" y "desocupada".
    Pre: ingresar una matriz no vacía.
    Pos: devuelve la matriz cargada.
    '''
    opciones = ["reservada", "desocupada"]
    for i, fila in enumerate(matriz):
        for j, elem in enumerate(fila):
            matriz[i][j] = random.choice(opciones)
    return matriz

def mostrar_butacas(matriz: list[list]) -> list[list]:
    '''Contrato: muestra por pantalla una matriz ya cargada con el estado: "reservada" y "desocupada".
    Pre: ingresar una matriz ya cargada.
    Pos: imprime la matriz.
    '''
    for i, fila in enumerate(matriz):
        print(f"Fila N°{i+1}: {fila}")

def mostrar_butacas_libres(matriz: list[list]) -> int:
    '''Contrato: recibe una matriz y muestra cuántas butacas están desocupadas en la sala.
    Pre: ingresar una matriz ya cargada.
    Pos: imprime la cantidad de butacas desocupadas.
    '''
    cantidad_desocupadas = sum(fila.count("desocupada") for fila in matriz)
    print(f"La cantidad de butacas desocupadas es {cantidad_desocupadas}")

def buscar_butacas_continuas(matriz: list[list]) -> int:
    '''Contrato: recibe una matriz y muestra la secuencia más larga de butacas contiguas desocupadas en una fila.
    Pre: ingresar una matriz ya cargada.
    Pos: imprime las coordenadas de inicio de la secuencia.
    '''
    for i, fila in enumerate(matriz):
        max_len = 0
        max_inicio = -1
        actual_len = 0
        actual_inicio = -1
        
        for j, butaca in enumerate(fila):
            if butaca == 'desocupada':
                if actual_len == 0:
                    actual_inicio = j
                actual_len += 1
                
                if actual_len > max_len:
                    max_len = actual_len
                    max_inicio = actual_inicio
            else: 
                actual_len = 0

        if max_inicio != 1:
            print(f"La butaca de inicio con la cantidad máxima de butacas desocupadas contiguas en la fila {i + 1} es la butaca N° {max_inicio + 1} (longitud: {max_len})")
        else:
            print(f"No hay butacas desocupadas en la fila {i + 1}.")
      
def reservar_butaca(matriz: list[list], num_elegida: int) -> bool:
    '''Contrato: recibe una matriz y una butaca seleccionada. Si está desocupada cambiará el estado a reservada.
    Devolverá True o False (logró o no reservar)
    Pre: ingresar una matriz ya cargada y el número de butaca a reservar.
    Pos: devuelve True si se logró reserva y False si no.
    '''
    for i, fila in enumerate(matriz):
        if matriz[i][num_elegida-1] == 'desocupada':
            matriz[i][num_elegida-1] = 'reservada'
            return True
        else:
            return False

# PROGRAMA

matriz_cine = [[0]*3]*8 #MATRIZ DE EJEMPLO PARA USAR EL PROGRAMA
sala_cargada = cargar_sala(matriz_cine)
print(mostrar_butacas(sala_cargada))
mostrar_butacas_libres(sala_cargada)
buscar_butacas_continuas(sala_cargada)
print(reservar_butaca(sala_cargada,1))