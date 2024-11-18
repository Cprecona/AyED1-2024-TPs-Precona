def grabar_rango_alturas() -> None:
    """Graba en un archivo las alturas de los atletas de distintas
    disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
    línea distinta. Ejemplo:
    <Deporte 1>
    <altura del atleta 1>
    <altura del atleta 2>
    < . . . >
    <Deporte 2>
    <altura del atleta 1>
    <altura del atleta 2>
    < . . . >

    Pre: los datos se ingresan por teclado.
    Post: no devuelve nada.
    """
    try:
        with open("alturas.txt", "wt", encoding="utf-8") as archivo_alturas:
            while True:
                nombre_deporte = input("Ingrese el nombre del deporte: ")
                archivo_alturas.write(f"{nombre_deporte}\n")
                while True:
                    try:
                        altura = input(
                            f"Ingrese la altura del atleta del deporte {nombre_deporte}, -1 para cambiar de deporte y -2 para terminar: "
                        )
                        if altura == "-2":
                            return
                        elif altura == "-1":
                            break
                        altura = float(altura)
                        if altura < -3 or altura > 200:
                            raise ValueError("Ingrese un valor correcto de altura")
                        archivo_alturas.write(f"{altura}\n")
                    except ValueError as msg:
                        print(msg)
    except FileNotFoundError as msg:
        print(f"Archivo no encontrado: {msg}")
    except:
        print("Error en los datos")
    else:
        print("\nArchivo generado exitosamente")


def grabar_promedio() -> None:
    """Graba en un archivo los promedios de las alturas de los atletas,
    leyendo los datos del archivo generado en el paso anterior. La disciplina y el
    promedio deben grabarse en líneas diferentes. Ejemplo:
    <Deporte 1>
    <Promedio de alturas deporte 1>
    <Deporte 2>
    <Promedio de alturas deporte 2>
    < . . . >
    Pre: el archivo de alturas tiene que existir.
    Post: no devuelve nada sino que crea el archivo.
    """
    try:
        with open("alturas.txt", "rt", encoding="utf-8") as archivo_de_alturas:
            lineas = archivo_de_alturas.readlines()
            deportes = []
            alturas_por_deporte = []
            acumulado_alturas = []

            for linea in lineas:
                linea = linea.strip()
                try:
                    altura = float(linea)
                    acumulado_alturas.append(altura)
                except ValueError:
                    if acumulado_alturas:
                        alturas_por_deporte.append(acumulado_alturas)
                        acumulado_alturas = []
                    deportes.append(linea)

            if acumulado_alturas:
                alturas_por_deporte.append(acumulado_alturas)

            with open("promedios.txt", "at", encoding="utf-8") as archivo_promedios:

                for i, deporte in enumerate(deportes):
                    alturas_deporte = alturas_por_deporte[i]
                    promedio = sum(alturas_deporte) / len(alturas_deporte)
                    archivo_promedios.write(deporte + "\n")
                    archivo_promedios.write(f"{promedio}\n")

    except FileNotFoundError as msg:
        print(f"Archivo no encontrado: {msg}")
    except:
        print("Error en los datos")
    else:
        print("\nArchivo generado exitosamente")


def mostrar_mas_altos() -> None:
    """Muestra por pantalla las disciplinas deportivas cuyos atletas
    superan la estatura promedio general. Obtener los datos del segundo archivo.

    Pre: el archivo de promedios tiene que existir.
    Post: no devuelve nada sino que muestra por pantalla los más altos.
    """

    try:
        with open("promedios.txt", "rt", encoding="utf-8") as archivo_promedios:
            lineas_de_promedios = archivo_promedios.readlines()
            lineas_de_promedios = [linea.strip() for linea in lineas_de_promedios]
            nombres_deportes = lineas_de_promedios[::2]
            promedios = list(map(float, lineas_de_promedios[1::2]))
        with open("alturas.txt", "rt", encoding="utf-8") as archivo_alturas:
            lineas_de_alturas = archivo_alturas.readlines()
            alturas_solas = []
            for linea in lineas_de_alturas:
                linea = linea.strip()
                try:
                    altura = float(linea)
                    alturas_solas.append(altura)
                except ValueError:
                    pass
        promedio_general = sum(alturas_solas) / len(alturas_solas)
        for i, promedio in enumerate(promedios):
            if promedio > promedio_general:
                print(
                    f"Disciplina que supera el promedio en altura: {nombres_deportes[i]}"
                )
    except FileNotFoundError as msg:
        print(f"Archivo no encontrado: {msg}")
    except:
        print("Error en los datos")


def main() -> None:
    """Este es el programa principal. Llama a las funciones
    previamente creadas.
    """
    grabar_rango_alturas()
    grabar_promedio()
    mostrar_mas_altos()


if __name__ == "__main__":
    main()
