def grabar_datos_longitud_fija() -> None:
    """Lee los datos de un  txt y los guarda en un csv. Los datos
    de ese txt se caracterizan por tener una longitud fija
    con un espacio de separación entre ellos.

    Pre: el arhivo debe existir previamente.
    Post: crea un archivo csv.
    """
    try:
        with open("archivo1.txt", "rt", encoding="utf-8") as archivo_1:
            with open("archivo1.csv", "at", encoding="utf-8") as archivo_1_csv:
                while True:
                    linea = archivo_1.readline()
                    linea = linea.strip()
                    if not linea:
                        break
                    campo1 = linea[:16]
                    campo2 = linea[16:25]
                    campo3 = linea[25:58]
                    linea = ",".join([campo1, campo2, campo3])
                    archivo_1_csv.write(f"{linea} \n")
    except FileNotFoundError as msg:
        print(f"El archivo no fue encontrado: {msg}")
    except:
        print("Error en los datos")
    else:
        print("El archivo fue creado exitosamente\n")


def grabar_datos_con_dos_digitos() -> None:
    """Lee los datos de un  txt y los guarda en un csv. Los datos
    de ese txt se caracterizan por que los dos campos previos
    a cada uno de ellos indican su longitud.
    Pre: el arhivo debe existir previamente.
    Post: crea un archivo csv.
    """
    try:
        with open("archivo2.txt", "rt", encoding="utf-8") as archivo_2:
            with open("archivo2.csv", "at", encoding="utf-8") as archivo_2_csv:
                while True:
                    linea = archivo_2.readline()
                    linea = linea.strip()
                    if not linea:
                        break
                    largo1 = int(linea[:2])
                    campo1 = linea[2 : largo1 + 2]
                    largo2 = int(linea[largo1 + 2 : largo1 + 4])
                    campo2 = linea[largo1 + 4 : largo1 + 4 + largo2]
                    largo3 = int(linea[largo1 + 4 + largo2 : largo1 + 6 + largo2])
                    campo3 = linea[largo1 + 6 + largo2 : largo1 + 6 + largo2 + largo3]
                    linea = ",".join([campo1, campo2, campo3])
                    archivo_2_csv.write(f"{linea} \n")
    except FileNotFoundError as msg:
        print(f"El archivo no fue encontrado: {msg}")
    except:
        print("Error en los datos")
    else:
        print("El archivo fue creado exitosamente\n")


def main() -> None:
    """Este es el programa principal. Solamente llama a las funciones."""
    grabar_datos_longitud_fija()
    grabar_datos_con_dos_digitos()


if __name__ == "__main__":
    main()
