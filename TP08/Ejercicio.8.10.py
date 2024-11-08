from typing import Dict, List


def eliminar_claves(diccionario: Dict, lista_de_claves: List) -> Dict:
    """Elimina del diccionario las claves que figuren en la lista.
    Devuelve el diccionario modificado e imprime un número que represente
    la cantidad de claves eliminadas.

    Pre: recibe como parámetros el diccionario y la lista de claves.

    Post: devuelve el diccionario modificado. Imprime el número de
    claves eliminadas.
    """
    claves_diccionario = diccionario.keys()
    largo_original = len(diccionario)
    for clave in lista_de_claves:
        if clave in claves_diccionario:
            diccionario.pop(clave)
    nuevo_largo = len(diccionario)
    cantidad_eliminadas = largo_original - nuevo_largo
    print(f"La cantidad de claves eliminadas fue de {cantidad_eliminadas}")
    return diccionario


def main() -> None:
    """Este es el programa principal.
    Pasa como parámetros un diccionario y una lista de claves.
    Imprime el diccionario modificado.
    """
    diccionario_a_pasar = {
        "lunes": "luna",
        "martes": "Marte",
        "miércoles": "Mercurio",
        "jueves": "Júpiter",
        "viernes": "Venus",
    }
    lista_a_pasar = ["lunes", "miércoles", "viernes"]

    diccionario_cambiado = eliminar_claves(diccionario_a_pasar, lista_a_pasar)
    print(f"El nuevo diccionario es: {diccionario_cambiado}")


if __name__ == "__main__":
    main()
