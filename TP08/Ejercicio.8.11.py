from typing import Dict


def contar_vocales(palabra: str) -> Dict:
    """Recibe una palabra y cuenta cuántas vocales tiene.
    Identifica la cantidad de cada una. Devuelve un diccionario
    con los resultados.

    Pre: la palabra debe ser un string.

    Post: devuelve un diccionario con los resultados.
    """
    vocales = ("a", "e", "i", "o", "u")

    diccionario_vocales = {}

    for letra in vocales:
        cantidad = palabra.count(letra)
        diccionario_vocales[letra] = cantidad

    return diccionario_vocales


def main(frase: str) -> None:
    """Este es el programa principal. Lee una frase, separa las palabras
    y pasa cada palabra como parámetro a la función contar_vocales.
    Imprime las palabras y la cantidad de vocales halladas.

    Pre: la frase debe una cadena de caracteres.

    Post: no devuelve nada.
    """

    palabras = frase.split()
    for palabra in palabras:
        print(palabra)
        print(contar_vocales(palabra))


if __name__ == "__main__":
    main("Jubilado de todo")
