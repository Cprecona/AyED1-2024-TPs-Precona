def generar_tabla() -> None:
    """Pide un número entero a un usuario y genera la tabla
    de multiplicar de ese número del 1 al 12. Muestra la tabla generada.

    Pre: el número es ingresado por el usuario.

    Post: no devuelve nada sino que imprime la tabla.
    """
    try:
        numero_ingresado = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Ingrese un número válido")
    else:
        tabla = {numero: numero * numero_ingresado for numero in range(1, 13)}
        for numero, producto in tabla.items():
            print(f"{numero_ingresado} x {numero} = {producto} ")


def main() -> None:
    """Este es el programa principal. Solamente llama a la función."""
    generar_tabla()


if __name__ == "__main__":
    main()
