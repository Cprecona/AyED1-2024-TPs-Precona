def eliminar_con_remove() -> None:
    """Solicita valores al usuario y luego los
    elimina de un conjunto de números enteros previamente
    fijados del 0 al 9. Muestra el conjunto
    luego de cada eliminación. Finaliza el proceso
    al ingresar -1.

    Pre: los valores se ingresan por teclado. Finaliza
    cuando se ingresa -1.

    Post: no devuelve nada sino que muestra el conjunto
    luego de cada eliminación.
    """

    conjunto = set(range(0, 10))
    while True:
        entrada = input("Ingrese un número entero y -1 para terminar: ")
        try:
            numero = int(entrada)
        except ValueError:
            print("Ingrese un número entero válido")
        else:
            if numero == -1:
                break

            if numero not in conjunto:
                conjunto.add(numero)
                conjunto.remove(numero)
            print(conjunto)


def main() -> None:
    """Esta en la función principal. Llama
    a la función eliminar_con_remove. No devuelve nada.
    """
    eliminar_con_remove()


if __name__ == "__main__":
    main()
