def generar_diccionarios() -> None:
    '''Genera un diccionario donde las claves sean números
    entre 1 y 20 y los valores sean el cuadrado de las
    claves.

    Pre: no se ingresan datos por teclado.

    Post: no hay salida sino que imprime el diccionario creado.
    '''
    diccionario = {num:num**2 for num in range(1,21)}
    print(diccionario)

def main() -> None:
    '''Este es el programa principal.
    Solamente llama a la función.
    '''

    generar_diccionarios()

if __name__ == "__main__":
    main()