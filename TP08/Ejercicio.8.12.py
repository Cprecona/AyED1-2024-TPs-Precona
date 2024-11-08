from typing import Dict


def crear_diccionario_productos() -> Dict:
    """Crea un diccionario a partir de entradas de productos de libería
    y sus precios.

    Pre: los productos y precios se ingresan por teclado.

    Post: devuelve el diccionario creado.
    """
    diccionario_precios = {}
    while True:
        producto = input("Ingrese el nombre del producto y -1 para terminar: ")
        try:
            if producto == str(-1):
                break
            precio = float(input("Ingrese el precio del producto: "))
            diccionario_precios[producto] = precio
        except:
            print("Ingrese un dato válido")

    return diccionario_precios


def incrementar_precios(diccionario: Dict, incremento: int) -> Dict:
    """Incrementa los precios en un % pasado como parámetro.

    Pre: el diccionario se pasa como parámetro, así como el incremento.

    Post: devuelve el diccionario pasado.
    """
    for clave, valor in diccionario.items():
        diccionario[clave] = round(valor * (1 + incremento / 100))

    return diccionario


def main() -> None:
    """Este es el programa principal. Llama a la función
    crear_diccionario_productos para crear el diccionario
    con los datos ingresados por teclado.
    Además llama a la función incrementar_precios para que los aumente.
    E informa el ítem más costoso de los vendidos.
    """
    diccionario = crear_diccionario_productos()
    print(diccionario)
    diccionario_incrementado = incrementar_precios(diccionario, 15)
    print(diccionario_incrementado)
    precio_maximo = max(diccionario_incrementado.values())
    artículo_precio_maximo = [
        clave
        for clave, valor in diccionario_incrementado.items()
        if valor == precio_maximo
    ]
    print(f"El artículo más costoso es {artículo_precio_maximo[0]}")


if __name__ == "__main__":
    main()
