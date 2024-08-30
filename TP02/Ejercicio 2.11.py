def registrar_consulta():
    '''Permite registrar las consultas de los pacientes, generando dos listados, uno de consultas por urgencia y otro de consultas por turno.
    La carga termina cuando se ingresa -1-
    Pre: el número de afiliado debe ser entero positivo de cuatro dígitos. El motivo será 0 si es por urgencia y 1 si es por turno.
    Pos: devuelve dos listas, una de los atendidos por urgencia y otra de los atendidos por turno.
    '''
    lista_urgencia = []
    lista_turno = []
    num_af = int(input("Ingrese el número de afiliado y -1 para terminar: "))
    while num_af !=-1:
        motivo = int(input("Ingrese 0 si es por urgencias y 1 si es por turno: "))
        if motivo == 0:
            lista_urgencia.append(num_af)
        else: 
            lista_turno.append(num_af)
        num_af = int(input("Ingrese el número de afiliado y -1 para terminar: "))
    return lista_urgencia, lista_turno

def informar_motivos_consulta(urgencia, turno):
    '''Recibe dos listas, una con el listado de pacientes por urgencias y otra con el de pacientes por turnos, además del número de afiliado. Devuelve la cantidad de veces
    que cada paciente se atendió por cada motivo, hasta que se ingrese -1 como número de afiliado.
    Pre: ingresar las dos listas como argumentos. Cuanto se pida el ingreso del número de afiliado, ingresar un número entero de 4 dígitos y -1 para salir.
    Pos: informa por pantalla las cantidades de veces que se atendió por cada motivo.
    '''
    afiliado = int(input("Ingrese el número de afiliado para informar cantidad de consultas y -1 para terminar: "))
    while afiliado !=-1:
        cantidad_urgencia = urgencia.count(afiliado)
        cantidad_turno = turno.count(afiliado)
        print(f"Los motivos del consulta del afiliado N° {afiliado} son: {cantidad_urgencia} veces para urgencias y {cantidad_turno} veces para turnos")
        afiliado = int(input("Ingrese el número de afiliado para informar cantidad de consultas y -1 para terminar: "))

# Programa ##########################################

listas_de_consultas = registrar_consulta() # llama a la función de consulta

# desempaquetado
listado_urgencias = listas_de_consultas[0]
listado_turnos = listas_de_consultas[1]

# impresión de listas
print(f"Pacientes atendidos por urgencias -> {listado_urgencias}")
print(f"Pacientes atendidos por turnos -> {listado_turnos}")

# llama a la función de búsqueda de cantidad de consultas por afiliado
informar_motivos_consulta(listado_urgencias,listado_turnos)