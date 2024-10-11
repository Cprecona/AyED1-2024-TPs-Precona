def imprimir_numeros() -> None:
    """Genera números enteros entre el 1 y el 100000.
    En caso de que se interrumpa con CTRL-C debe preguntar
    al usuario confirmación para detenerse.

    Pre: la generación de números es automática.

    Post: no devuelve nada, sino que imprime los números
    """

    try:
        for numero in range(1, 100000):
            print(numero)
    except KeyboardInterrupt:
        confirmacion = input("¿Confirma interrupción? Y para sí y N para no: ")
        if confirmacion.upper() == "Y":
            print("Interrupción confirmada")
        else:
            imprimir_numeros()


# Programa

imprimir_numeros()
