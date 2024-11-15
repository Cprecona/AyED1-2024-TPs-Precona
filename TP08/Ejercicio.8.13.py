from typing import Dict, List


def buscar_clave(diccionario: Dict, valor: str) -> List:
    """Devuelve una lista de claves cuyo valor coincida con el pasado como parámetro.

    Pre: el diccionario y el valor se pasan como parámetros.

    Post: devuelve una lista.
    """
    lista_de_claves = [clave for clave, dato in diccionario.items() if dato == valor]
    return lista_de_claves


def main() -> None:
    """Este es el programa principal. Llama a la función
    buscar_clave y muestra la lista. No devuelve nada.
    """
    diccionario = {"lunes": "frío", "martes": "calor", "miércoles": "frío"}
    claves = buscar_clave(diccionario, "frío")
    print(claves)


if __name__ == "__main__":
    main()
