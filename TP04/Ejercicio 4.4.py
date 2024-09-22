def convertir_a_romanos(numero: int) -> str:
    '''Convierte a números romanos un número entero entre 0 y 3999.

    Pre: recibe un número entero entre 0 y 3999.

    Post: devuelve una cadena de caracteres.
    '''
    
    if numero/1000 != 0:
        cantidad_M = numero//1000
        M = 'M'
        diferencia = numero-1000*cantidad_M 
    if diferencia/ 500 != 0:
        cantidad_D = diferencia//500
        D = 'D'
        diferencia = diferencia - 500* cantidad_D
    if diferencia / 100 != 0:
        cantidad_C = diferencia//100
        C = 'C'
        diferencia = diferencia - 100* cantidad_C
    if diferencia / 50 != 0:
        cantidad_L = diferencia//50
        L = 'L'
        diferencia = diferencia - 50* cantidad_L
    if diferencia / 10 != 0:
        cantidad_X = diferencia//10
        X = 'X'
        diferencia = diferencia - 10* cantidad_X
    if diferencia / 5 != 0:
        cantidad_V = diferencia//5
        V = 'V'
        diferencia = diferencia - 5* cantidad_V
    if diferencia / 1 != 0:
        cantidad_I = diferencia//1
        I = 'I'

    return M*cantidad_M,D*cantidad_D,C*cantidad_C,L*cantidad_L,X*cantidad_X,V*cantidad_V,I*cantidad_I

#
tupla_romano = convertir_a_romanos(2024)
print(''.join(tupla_romano))