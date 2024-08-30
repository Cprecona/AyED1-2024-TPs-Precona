def registar_socio():
    '''Registra los socios que ingresaron al club en un día determinado.
    Pre: el número de socio debe ser un entero de 5 dígitos. Para salir ingresar 0. 
    Pos: devuelve una lista con los socios que ingresaron ese día.
    '''
    ingresos = []
    socio = int(input("Ingrese el número de socio y 0 para terminar: "))
    while socio !=0:
        ingresos.append(socio)
        socio = int(input("Ingrese el número de socio y 0 para terminar: "))
    return ingresos

def listar_entradas(lista):
    '''Informa, para cada socio, la cantidad de veces que ingresó.
    Pre: ingresar una lista de ingresos.
    Pos: imprime por pantalla un listado.
    '''
    lista_de_socios = []
    print("N° DE SOCIO - CANTIDAD DE INGRESOS")
    for elem in lista:        
        if lista_de_socios.count(elem) == 0:
            lista_de_socios.append(elem)
            print(f"   {elem}               {lista.count(elem)}")


# Programa para listar los socios y la cantidad de veces que ingresó al club

listado_ingresos=registar_socio()
listar_entradas(listado_ingresos)

# Programa para eliminar los registros de un socio, imprimir el listado antes y después e informar cuántos registros se eliminaron.

socio_baja = int(input("Ingrese el número de socio que se dio de baja: "))
print("LISTADO DE SOCIOS ANTES DE LA ELIMINACIÓN")
listar_entradas(listado_ingresos)
cant_registros_eliminados = listado_ingresos.count(socio_baja)
listado_ingresos = [elem for elem in listado_ingresos if elem!=socio_baja]
listar_entradas(listado_ingresos)
print(f"La cantidad de registros eliminados es {cant_registros_eliminados}")
