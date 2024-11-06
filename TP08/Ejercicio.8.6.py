from typing import List

def eliminar_repetidas() -> List:
    '''Elimina las palabras repetidas de una frase 
    sin importar los signos de puntuación. Luego
    devuelve las palabras ordenadas por su longitud.

    Pre: se ingresa la frase por teclado

    Post: devuelve una lista con las palabras ordenadas
    según su longitud
    '''
    while True:
        try:
            frase=input("Ingrese una frase con varias palabras: ")
            if not frase:
                raise ValueError("Ingrese una frase válida")
        except ValueError as mesaje:
            print(mesaje)
        else:
            palabras = [palabra.rstrip(".,?") for palabra in frase.split()]
            frase_sin_repetidas = list(set(palabras))
            frase_ordenadas = sorted(frase_sin_repetidas, key=len)
            return frase_ordenadas

def main() -> None:
    '''Este es el programa principal. 
    Llama a la función eliminar_repetidas e imprime
    la lista.

    Pre: recibe la frase ordenada sin repetidas.

    Post: no devuelve nada sino que imprime la frase
    '''
    frase_a_imprimir = eliminar_repetidas()
    print(frase_a_imprimir)

if __name__ == "__main__":
    main()