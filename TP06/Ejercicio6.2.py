import os


def dividir_archivo() -> None:
    """
    Escribir un programa que permita dividir un archivo de texto cualquiera en partes
    que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
    ingresa por teclado. Los nombres de los archivos generados deben respetar el
    nombre original con el agregado de un sufijo que indique de qué parte se trata.
    Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse después del delimitador del mismo.
    Mostrar un mensaje de error si el proceso no pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
    memoria.
    """
    tamanio_division = int(
        input("Ingrese el tamaño en el que debe dividirse el archivo: ")
    )
    tamanio_archivo = os.path.getsize("ventas.txt")
    cantidad_archivos = tamanio_archivo // tamanio_division + 1
    try:
        with open("ventas.txt", "rt", encoding="utf-8") as archivo:
            while True:
                linea = archivo.readline()
                if not linea:
                    break
                parte = 1
                for __ in range(cantidad_archivos):
                    nombre_parte = f"archivo_nuevo_{parte}.txt"
                    with open(nombre_parte, "wt", encoding="utf-8") as archivo_nuevo:
                        archivo_nuevo.write(linea)
                    parte += 1

    except FileNotFoundError as msg:
        print(f"Archivo no encontrado: {msg}")
    except:
        print("Error en los datos")
    else:
        print("\nDivisión realizada exitosamente")


def main() -> None:
    """Este es el programa principal. Solamente llama a la función dividir_archivo."""
    dividir_archivo()


if __name__ == "__main__":
    main()

# PROFE: EN ESTE CASO, ME DIVIDE EN LA CANTIDAD DE ARCHIVOS QUE YO LE INDICO, PERO SOBREESCRIBE SIEMPRE LA MISMA LÍNEA. NO PUDE SOLUCIONARLO.
